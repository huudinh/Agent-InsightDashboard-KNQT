#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
doi-khuon-chatbox.py · đổi bản xuất AI Chatbox → khuôn hội thoại của id-B §2

    python tools/doi-khuon-chatbox.py data/hoi-thoai-khach-quoc-te.md du-lieu/hoi-thoai.md

Bản xuất của `GET /api/conversations` (trang ai-chatbox) có khuôn riêng:

    ## 1. Khách chưa nêu tên — 04/09/2026 16:57
    | **Mã hội thoại** | conv-... |
    | **Ngôn ngữ** | en |
    | **Kênh liên hệ** | WhatsApp |
    | **Số điện thoại** | +61480337514 |
    **Khách** · 04/09/2026 16:57
    > nội dung

Script này đổi sang khuôn `id.py doc` đọc được, và **suy `Nước:` từ mã quốc gia
của số điện thoại** — căn cứ chắc hơn mọi cách suy từ chữ (id-B §3 dòng 1).

★ BA ĐIỀU PHẢI BIẾT VỀ DỮ LIỆU NÀY — ⛔ đừng đọc báo cáo như báo cáo trực kênh:

① NGƯỜI TRẢ LỜI LÀ MỘT CON BOT, không phải nhân viên.
   → `NV:` ghi là `AI Chatbox`. Mọi điểm `N` là điểm của CÂU TRẢ LỜI CỦA BOT,
     ⛔ không phải điểm của một con người. Bốn rào an toàn của id-F §7 sinh ra
     để bảo vệ người — với bot thì đầu ra đi về NGƯỜI HUẤN LUYỆN BOT,
     ⛔ không đi vào sổ tay cá nhân.

② SLA CỦA BOT LUÔN ĐẠT. Bot trả lời trong cùng một phút, kể cả 3 giờ sáng.
   → Nhóm `N1` và tiêu chí `N7.4` ra gần 100% và ⛔ KHÔNG nói lên điều gì.
     Đọc `N3` · `N4` · `N7` (nội dung) thay vì `N1` (tốc độ).

③ ⛔ KHÔNG CÓ MỐC "NGOÀI GIỜ" THEO NGHĨA LỊCH TRỰC. Bot không có ca.
   Giờ khách nhắn vẫn đáng đọc — nó cho biết khách ở múi giờ nào — nhưng
   ô "ngoài giờ 8–17 ICT" ở đây là chỉ số về KHÁCH, không phải về lịch trực.
"""

import argparse
import os
import re
import sys
import unicodedata
from collections import Counter

# Mã quốc gia → mã thị trường của id-L §9. ⛔ Không đặt mã ngoài schema đó:
# nước nào chưa có trong schema thì để TRỐNG và báo lại ở cuối, để người dùng
# quyết định bổ sung schema hay xếp vào TT-0.
MA_NUOC = [
    ("+84", "VN"), ("84", "VN"),
    ("+61", "AU"), ("61", "AU"),
    ("+64", "NZ"),
    ("+44", "UK"),
    ("+49", "DE"), ("+420", "CZ"),
    ("+971", "AE"), ("+966", "SA"), ("+965", "KW"), ("+974", "QA"),
    ("+855", "KH"), ("+856", "LA"), ("+95", "MM"), ("+62", "ID"),
    ("+63", "PH"), ("+60", "MY"), ("+65", "SG"), ("+66", "TH"), ("+91", "IN"),
    ("+81", "JP"), ("+82", "KR"), ("+886", "TW"), ("+852", "CN-HK"),
]
# Vùng +1 của Canada — phần còn lại của +1 coi là US.
# Nước có thật nhưng ⛔ KHÔNG có trong schema id-L §9. Gọi đúng tên, để TRỐNG mã,
# và báo lại ở cuối để người dùng quyết định: bổ sung schema hay để TT-0.
NGOAI_SCHEMA = [
    ("+7", "Nga"), ("+48", "Ba Lan"), ("+260", "Zambia"), ("+380", "Ukraine"),
    ("+90", "Thổ Nhĩ Kỳ"), ("+27", "Nam Phi"), ("+234", "Nigeria"),
    ("+20", "Ai Cập"), ("+33", "Pháp"), ("+39", "Ý"), ("+34", "Tây Ban Nha"),
    ("+31", "Hà Lan"), ("+46", "Thuỵ Điển"), ("+47", "Na Uy"), ("+45", "Đan Mạch"),
    ("+41", "Thuỵ Sĩ"), ("+43", "Áo"), ("+32", "Bỉ"), ("+353", "Ireland"),
    ("+972", "Israel"), ("+880", "Bangladesh"), ("+92", "Pakistan"),
    ("+94", "Sri Lanka"), ("+977", "Nepal"), ("+976", "Mông Cổ"),
    ("+86", "Trung Quốc"), ("+55", "Brazil"), ("+52", "Mexico"),
]
VUNG_CA = {"204", "226", "236", "249", "250", "289", "306", "343", "365", "387",
           "403", "416", "418", "428", "431", "437", "438", "450", "506", "514",
           "519", "548", "579", "581", "584", "587", "604", "613", "639", "647",
           "672", "705", "709", "742", "753", "778", "780", "782", "807", "819",
           "825", "867", "873", "902", "905"}

RE_BLOCK = re.compile(r'^##\s+(\d+)\.\s*(.+?)\s*$', re.M)
RE_META = re.compile(r'^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$', re.M)
RE_NOI = re.compile(r'^\*\*(Khách|Trợ lý AI)\*\*\s*·\s*(\d{2})/(\d{2})/(\d{4})\s+(\d{2}:\d{2})\s*$')
RE_TRICH = re.compile(r'^>\s?(.*)$')
RE_CHU_THICH = re.compile(r'^_?\s*(?:→|->|\[|Hệ thống)')


def suy_nuoc(sdt, ngon_ngu):
    """Suy mã thị trường từ số điện thoại. Trả về (ma, ghi_chu).

    ⚠ Hai cái bẫy của dữ liệu thật, cả hai đều dẫn tới GÁN SAI TẦNG — đúng cái
      lỗi im lặng mà id-L §2 cảnh báo:
      ① Số NANP khách gõ không có mã quốc gia: `2813894741` là số Mỹ (vùng 281),
         ⛔ không phải "+281".
      ② Nước có thật nhưng NGOÀI schema id-L §9 (RU · PL · ZM …): phải gọi đúng
         tên nước rồi để TRỐNG mã, ⛔ không nhét vào một tầng cho đủ bảng.
    """
    if not sdt:
        return "", ""
    s = re.sub(r'[^\d+]', '', sdt)

    def nanp(x):
        """x = 10 chữ số NANP → CA hay US theo mã vùng."""
        return "CA" if x[:3] in VUNG_CA else "US"

    if not s.startswith("+"):
        if len(s) == 10 and s[0] in "23456789":
            return nanp(s), ""                      # số Mỹ/Canada thiếu mã quốc gia
        if len(s) == 11 and s.startswith("1"):
            return nanp(s[1:]), ""
        if len(s) == 10 and s.startswith("0"):
            return ("", "số 10 chữ số bắt đầu bằng 0 — không rõ nước (có thể là số giả)")
        s = "+" + s
    if s.startswith("+1") and len(s) >= 12:
        return nanp(s[2:12]), ""
    for tien, ma in MA_NUOC:
        tien = tien if tien.startswith("+") else "+" + tien
        if s.startswith(tien):
            if ma == "VN":
                # ⚠ Số VN trên site quốc tế: khách nhắn EN thì là expat đang ở VN;
                #   nhắn tiếng Việt thì ⛔ KHÔNG đoán — để trống cho id-B §3 xử.
                return ("VN-EXPAT", "") if ngon_ngu == "EN" else ("", "số VN + tiếng Việt")
            return ma, ""
    for tien, ten in NGOAI_SCHEMA:
        if s.startswith(tien):
            return "", "%s (%s) — nước có thật nhưng NGOÀI schema id-L §9" % (ten, tien)
    return "", "mã quốc gia %s chưa tra được" % s[:4]


def doc_khoi(raw):
    moc = [(m.start(), m.group(1), m.group(2)) for m in RE_BLOCK.finditer(raw)]
    for i, (vt, so, ten) in enumerate(moc):
        het = moc[i + 1][0] if i + 1 < len(moc) else len(raw)
        yield so, ten, raw[vt:het]


def main():
    ap = argparse.ArgumentParser(description="Đổi bản xuất AI Chatbox → khuôn id-B §2")
    ap.add_argument("nguon")
    ap.add_argument("dich")
    args = ap.parse_args()

    with open(args.nguon, encoding="utf-8") as f:
        raw = f.read()

    ra = ["# Hội thoại khách quốc tế — đã đổi khuôn cho id.py",
          "",
          "> Nguồn: `%s` (bản xuất AI Chatbox)." % os.path.basename(args.nguon),
          "> ⚠ Người trả lời là **AI Chatbox**, ⛔ không phải nhân viên — xem đầu"
          " `tools/doi-khuon-chatbox.py`.",
          "> ⛔ File này chứa lời khách thật. ⛔ KHÔNG commit.",
          ""]
    dem_nuoc, dem_nn, dem_kenh, la = Counter(), Counter(), Counter(), []
    so_ht = bo = 0

    for so, ten, khoi in doc_khoi(raw):
        meta = {k.strip(): v.strip() for k, v in RE_META.findall(khoi)}
        if "Mã hội thoại" not in meta:
            continue
        nn = (meta.get("Ngôn ngữ") or "").strip().lower()
        nn = {"vi": "VI", "en": "EN"}.get(nn, "XX")
        sdt = meta.get("Số điện thoại", "")
        sdt = "" if sdt in ("--", "—", "") else sdt
        nuoc, ghi = suy_nuoc(sdt, nn)
        if ghi:
            la.append("HT-%03d · %s" % (int(so), ghi))
        kenh = (meta.get("Kênh liên hệ") or "").strip()
        kenh = "AI Chatbox" if kenh in ("--", "—", "") else kenh

        tin = []
        dong = khoi.splitlines()
        i = 0
        while i < len(dong):
            m = RE_NOI.match(dong[i].strip())
            if not m:
                i += 1
                continue
            ai, dd, mm, _yyyy, hhmm = m.groups()
            noi = []
            i += 1
            while i < len(dong):
                t = dong[i].rstrip()
                if RE_NOI.match(t.strip()) or t.startswith("## ") or t.strip() == "---":
                    break
                mt = RE_TRICH.match(t)
                if mt:
                    noi.append(mt.group(1).strip())
                i += 1
            # ⚠ Bản xuất chèn CHÚ THÍCH HỆ THỐNG vào giữa lời bot
            #   ("_→ Hệ thống ghi nhận số điện thoại tại bước này._"). Đó không
            #   phải chữ bot gõ cho khách — giữ lại thì câu tiếng Anh bị nhận
            #   thành tiếng Việt và đẻ ra một hàng "hệ thống — ngôn ngữ" giả.
            noi = [x for x in noi if x and not RE_CHU_THICH.match(x)]
            noi = " ".join(noi).strip()
            if noi:
                tin.append(("%s-%s %s" % (mm, dd, hhmm),
                            "KH" if ai == "Khách" else "NV AI Chatbox", noi))

        if len(tin) < 2:
            bo += 1
            continue

        so_ht += 1
        dem_nuoc[nuoc or "(chưa rõ)"] += 1
        dem_nn[nn] += 1
        dem_kenh[kenh] += 1

        cap = meta.get("Cập nhật cuối", "")
        ra += ['### <a id="ht-%d"></a>%d. Khách %d' % (so_ht, so_ht, so_ht),
               "",
               "_Cập nhật: %s · NV: AI Chatbox · SĐT: %s · ID: %s_"
               % (cap, "Có" if sdt else "Không", meta["Mã hội thoại"]),
               "_Kênh: %s · Nước: %s · Ngôn ngữ: %s_" % (kenh, nuoc, nn),
               ""]
        for tem, ai, noi in tin:
            ra.append("- `%s` **%s:** %s" % (tem, ai, noi))
        ra.append("")

    os.makedirs(os.path.dirname(os.path.abspath(args.dich)), exist_ok=True)
    with open(args.dich, "w", encoding="utf-8") as f:
        f.write("\n".join(ra))

    p = print
    p("")
    p("  Đã đổi khuôn %d hội thoại → %s" % (so_ht, args.dich))
    if bo:
        p("  ⚠ Bỏ %d hội thoại dưới 2 tin (id-B §6)." % bo)
    p("")
    p("  NƯỚC suy từ mã quốc gia của SĐT:")
    for k, v in dem_nuoc.most_common():
        p("    %-12s %3d" % (k, v))
    p("  NGÔN NGỮ : " + " · ".join("%s %d" % x for x in dem_nn.most_common()))
    p("  KÊNH     : " + " · ".join("%s %d" % x for x in dem_kenh.most_common()))
    if la:
        p("")
        p("  ⚠ %d hội thoại có mã quốc gia NGOÀI schema id-L §9 — cần người dùng"
          " quyết định bổ sung schema hay để TT-0:" % len(la))
        for x in la[:20]:
            p("     %s" % x)
    p("")
    p("  → Chạy: python tools/id.py doc %s --ky \"<kỳ>\"" % args.dich)
    p("")


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
