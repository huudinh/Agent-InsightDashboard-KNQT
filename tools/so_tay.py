#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
so_tay.py · Agent-InsightDashboard-KNQT  (bản QUỐC TẾ)

Sinh SỔ TAY THỰC THI theo khuôn id-I:
  ST-CN · một bản cho mỗi nhân viên trực kênh   (1 trang)
  ST-TN · một bản cho trưởng nhóm               (cả nhóm)
  ST-ND · một bản cho người làm nội dung        (⛔ không có tên nhân viên)

Script điền phần ĐẾM ĐƯỢC và chừa chỗ `«agent điền: …»` cho phần ĐỌC HIỂU
— câu mẫu, insight, câu hỏi ngầm. ⛔ Script không nghĩ hộ.

★ Hai mục riêng của bản quốc tế, ⛔ KHÔNG được bỏ:
  ST-CN mục 6 · "VIỆC KHÔNG PHẢI CỦA BẠN" — những câu nhân viên chưa trả lời được
         là vì HỆ THỐNG CHƯA CẤP. Không nói rõ ra thì người giỏi sẽ TỰ NGHĨ RA
         MỘT CON SỐ — và đó đúng là cách cờ đỏ CĐ-5 xuất hiện (id-I §3).
  ST-TN mục 6 · "LỊCH TRỰC THEO MÚI GIỜ" — việc của LỊCH, không của người.

    python tools/so_tay.py --ky 19-25/10
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RA = os.path.join(GOC, "out")
THU_MUC = os.path.join(RA, "so-tay")
PHAC_HOA = os.path.join(RA, "chan-dung.json")


def nap_ten_cd():
    """Tên chân dung lấy từ bản phác họa của kỳ, ⛔ không có bộ mặc định nào."""
    ten = {"CD0": "chưa đủ dữ kiện để xếp"}
    if os.path.exists(PHAC_HOA):
        try:
            with open(PHAC_HOA, encoding="utf-8") as f:
                for c in (json.load(f).get("tep") or []):
                    if c.get("ma"):
                        ten[c["ma"]] = c.get("ten") or c["ma"]
        except ValueError:
            pass
    return ten

TEN_NHOM = {"N1": "Phản hồi & SLA", "N2": "Khai thác tình trạng & bối cảnh",
            "N3": "Trả lời đúng & minh bạch", "N4": "Xử lý rào cản",
            "N5": "Xin liên hệ & chốt", "N6": "Ngôn từ & thái độ",
            "N7": "★ Năng lực quốc tế"}

# ★ Bảy nhóm LỖI HỆ của bản quốc tế (id-F §7 rào ③). Tiêu chí nào chấm "—" nhiều
#   thì phần lớn thuộc một trong bảy nhóm này — và ⛔ KHÔNG được viết thành việc
#   của nhân viên.
LOI_HE = {
    "N7.6": ("chưa có SỐ NGÀY Ở LẠI theo từng dịch vụ", "Khoa Chuyên môn"),
    "N3.1": ("dịch vụ khách hỏi không có trong bảng giá công khai", "Vận hành"),
    "N3.5": ("chưa có số ngày ở lại để trả lời", "Khoa Chuyên môn"),
    "N7.3": ("chưa có người trực ngôn ngữ đó trong ca", "Vận hành"),
    "N7.4": ("lịch trực chưa phủ múi giờ đó", "Vận hành + Điều phối QT"),
    "N1.1": ("tin đến ngoài giờ 8–17 ICT — việc của lịch trực", "Vận hành"),
    "N2.3": ("chưa có privacy notice đạt GDPR cho khách EU/UK", "Pháp chế"),
}

# Việc mẫu theo nhóm yếu nhất — viết như HÀNH ĐỘNG, không phải phẩm chất (id-I §6).
VIEC = {
    "N1": ("Nhắn lại một câu hỏi về tình trạng khi khách im quá 30 phút (trong giờ)",
           ["EN: Still here for you — could you tell me which part you'd like to improve?",
            "VI: Em vẫn ở đây ạ. Chị gửi em tấm ảnh nghiêng, em nhờ bác sĩ xem giúp chị nhé."],
           ("Hello, welcome to Kangnam", "khách đã được chào rồi — câu này không mở được gì")),
    "N2": ("Hỏi MỘT câu về tình trạng trước khi gõ câu xin liên hệ",
           ["EN: Have you had any previous surgery in this area?",
            "EN: Which part would you like to improve — the bridge or the tip?"],
           ("May I have your phone number?", "gõ ngay khi chưa biết khách cần gì")),
    "N3": ("Nêu giá theo /price-list/ VÀ luôn kèm dòng phụ phí quốc tế 10%",
           ["EN: Rhinoplasty starts from 35,200,000 VND (about 1,353 USD). "
            "The price does not include the 10% international service charge.",
            "EN: Final cost is confirmed by the doctor after in-person examination."],
           ("Our doctor will tell you the price when you come",
            "né hẳn câu hỏi — ở bản quốc tế giá ĐÃ CÔNG KHAI nên đây là lỗi người")),
    "N4": ("Trả lời đúng RÀO khách đang lo — hỏi về chuyến đi thì ⛔ không trả lời bằng giá",
           ["EN: You're asking how long you need to stay. The surgeon confirms this at your "
            "assessment — I'll get you the typical range today and message you back.",
            "EN: Interpreter support continues after you fly home, through this same channel."],
           ("We have a special promotion this month",
            "khách lo rào XA mà trả lời bằng NGẠI (chi phí) — lệch rào, tiêu chí N4.2")),
    "N5": ("Hỏi khung giờ gọi KÈM MÚI GIỜ, và hẹn lịch có ghi rõ giờ Việt Nam",
           ["EN: What time works for you — and which time zone are you in?",
            "EN: Would 3pm Vietnam time (UTC+7) on Tuesday work? I'll hold the slot."],
           ("Let me know when you're free",
            "không có ngày giờ + múi giờ thì cuộc gọi đó đơn giản là không diễn ra")),
    "N6": ("Cắt đoạn dán dài, trả lời đúng điều khách vừa hỏi trước",
           ["EN: Short answer first: «…». I'll send the details after."],
           ("<khối giới thiệu công nghệ 500 chữ>", "khách chỉ hỏi một câu, đoạn dán không trả lời câu đó")),
    "N7": ("Câu đầu tiên sau lời chào: hỏi khách đang ở nước nào",
           ["EN: May I ask which country you're messaging from? It helps me give you the "
            "right schedule and travel information.",
            "EN: Only our surgeon and medical team will see your photos; they will not be "
            "used for marketing."],
           ("<không hỏi gì, trả lời luôn về giá>",
            "không biết khách ở đâu thì không biết họ cần gì — tiêu chí N7.1, và TT-0 phình lên")),
}

CHUNG_KHONG = [
    "⛔ Không dùng chữ *lifetime* hay nêu bất kỳ thời hạn bảo hành — viết "
    "«follow-up and warranty policy — see terms»",
    "⛔ Không tự nêu SỐ NGÀY khách phải ở lại Việt Nam, ⛔ không nói «you can fly on day X» "
    "— viết «the surgeon confirms this at your assessment»",
    "⛔ Không nêu giá mà bỏ dòng «the price does not include the 10% international service charge»",
    "⛔ Không nói *board certified*, ⛔ không gắn chức danh bác sĩ chưa đối chiếu",
    "⛔ Không trả lời câu bệnh nền — chuyển «this needs an in-person assessment by the surgeon»",
]
GHI_CHU_DIEM = ("> Điểm dùng để phân việc kèm cặp. "
                "Không phải căn cứ kỷ luật hay xếp hạng công khai.")

SO_VIEC = {"A": 1, "B": 1, "C": 2, "D": 1}


def ten_file(s):
    s = re.sub(r'[^\w\s-]', '', s, flags=re.U).strip()
    return re.sub(r'\s+', '-', s) or "khong-ro"


def nap():
    f = os.path.join(RA, "doc-hoi-thoai.json")
    if not os.path.exists(f):
        sys.exit("⛔ Chưa có out/doc-hoi-thoai.json. Chạy `id.py doc` trước.")
    with open(f, encoding="utf-8") as fh:
        D = json.load(fh)
    rows = []
    c = os.path.join(RA, "cham-hoi-thoai.csv")
    if os.path.exists(c):
        with open(c, encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh))
    return D, rows


def pct(a, b):
    return round(a / b * 100, 1) if b else None


def so_cn(nv, D, rows, ky):
    rs = [r for r in rows if r["nv"] == nv["ten"]]
    n = len(rs)
    loai = nv["loai"]
    yeu, manh = nv["yeu_nhat"], nv["manh_nhat"]
    # Việc được chọn theo nhóm MẤT NHIỀU ĐIỂM NHẤT, không phải nhóm dễ sửa nhất (id-I §2).
    cot = {g: [c for c in rs[0].keys() if c.startswith(g + ".")] for g in TEN_NHOM} if rs else {}
    xep = sorted([g for g in TEN_NHOM if _pct_nhom(rs, g, cot.get(g, [])) is not None],
                 key=lambda g: _pct_nhom(rs, g, cot.get(g, [])))
    chon = xep[:SO_VIEC.get(loai, 1)] or [yeu]
    cot_yeu = cot.get(yeu, [])

    TEN_CD = nap_ten_cd()
    cd_chinh = Counter(r["cd"] for r in rs if r["cd"]).most_common(1)
    o_chinh = Counter(o for r in rs for o in (r["ma_o"] or "").split()
                      if o.startswith("O-")).most_common(1)

    pct_yeu = _pct_nhom(rs, yeu, cot_yeu)
    khoi_yeu = next((g["pct_dat"] for g in D["nhan_vien"]["nhom"] if g["ma"] == yeu), None)
    cot_manh = [c for c in rs[0].keys() if c.startswith(manh + ".")] if rs else []

    L = []
    a = L.append
    a("# SỔ TAY THỰC THI · %s" % nv["ten"])
    a("Kỳ %s · %d hội thoại · %s/100 · loại **%s**"
      % (ky, n, nv["diem"] if nv["diem"] is not None else "—", loai))
    a("")
    a(GHI_CHU_DIEM)
    a("")
    a("## 1 · KỲ NÀY BẠN LÀM TỐT NHẤT ĐIỀU GÌ")
    a("**%s · %s** — %s%% đạt  *(cả khối: %s%%)*"
      % (manh, TEN_NHOM.get(manh, ""), _pct_nhom(rs, manh, cot_manh),
         next((g["pct_dat"] for g in D["nhan_vien"]["nhom"] if g["ma"] == manh), "—")))
    a("")
    a("«agent điền: một câu nguyên văn của chính người này làm tốt, kèm HT-nnn»")
    a("")
    a("## 2 · ★ %s VIỆC CỦA KỲ TỚI" % ({1: "MỘT", 2: "HAI"}.get(len(chon), str(len(chon)))))
    for i, g in enumerate(chon):
        viec, cau_dung, (cau_sai, ly_do) = VIEC.get(g, VIEC["N2"])
        p_g = _pct_nhom(rs, g, cot.get(g, []))
        khoi_g = next((x["pct_dat"] for x in D["nhan_vien"]["nhom"] if x["ma"] == g), None)
        a("")
        a("### %s. %s" % (i + 1, viec))
        a("")
        a("Vì sao: nhóm **%s · %s** đạt **%s%%** trên %d hội thoại áp dụng  *(cả khối %s%%)*."
          % (g, TEN_NHOM.get(g, ""), p_g, n, khoi_g))
        a("")
        bc = [r for r in rs if any(r.get(c) == "✗" for c in cot.get(g, []))][:2]
        if bc:
            a("Bằng chứng — hội thoại của chính bạn:")
            for r in bc:
                tr = [c for c in cot.get(g, []) if r.get(c) == "✗"]
                a("- `%s` · trượt %s · khách thuộc %s · %s"
                  % (r["ma"], ", ".join(tr),
                     ("%s %s" % (r["cd"], TEN_CD.get(r["cd"], ""))).strip()
                     if r["cd"] else "chân dung chưa phác họa",
                     r["vi_sao_roi"]))
            a("")
        a("Làm thế nào — câu dùng được ngay:")
        for c in cau_dung:
            a("- ✅ *%s*" % c)
        a("- ⛔ *%s* — %s" % (cau_sai, ly_do))
        a("")
        a("Đo thế nào ở kỳ sau: **%s** từ %s%% lên **%s%%**"
          % (g, p_g, min(100, round((p_g or 0) + 15))))
    a("")
    a("## 3 · KHÁCH CỦA BẠN LÀ AI")
    if cd_chinh:
        a("Chân dung gặp nhiều nhất: **%s · %s** — %d/%d hội thoại"
          % (cd_chinh[0][0], TEN_CD.get(cd_chinh[0][0], "—"), cd_chinh[0][1], n))
    else:
        a("⏳ Chân dung của kỳ **chưa được phác họa** — chờ CỔNG 0 (id-C §1). "
          "Phần này sẽ điền khi chạy lại sau khi duyệt.")
    if o_chinh:
        a("Họ đang sợ: **%s** — %d lần" % (o_chinh[0][0], o_chinh[0][1]))
    a("")
    a("Câu hỏi ngầm: «agent điền: dịch câu khách gõ thành điều khách thật sự muốn biết»")
    a("")
    a("Ba câu trả lời sẵn cho tệp này:")
    a("1. «agent điền»")
    a("2. «agent điền»")
    a("3. «agent điền»")
    a("")
    a("## 4 · ⛔ NĂM ĐIỀU TUYỆT ĐỐI KHÔNG — bản quốc tế")
    for x in CHUNG_KHONG:
        a("- %s" % x)
    if nv.get("co_do"):
        a("")
        a("🔴 **Kỳ này bạn có cờ đỏ:** %s" % " · ".join(nv["co_do"]))
        for c in D["nhan_vien"]["co_do"]:
            if c["nguoi"] == nv["ten"]:
                a("- `%s` · %s · trích: «%s»" % (c["ht"], c["ma"], c["trich"]))
        a("")
        a("⚠️ Cờ đỏ phải ngồi lại với trưởng nhóm trong 48 giờ.")
    a("")
    a("## 5 · KIỂM TRƯỚC KHI ĐÓNG MỖI HỘI THOẠI")
    a("- [ ] Đã biết khách đang ở **nước nào** chưa?")
    a("- [ ] Đã hỏi tình trạng **trước khi** xin liên hệ chưa?")
    a("- [ ] Nếu khách hỏi giá: đã nêu giá **kèm phụ phí 10%** chưa?")
    a("- [ ] Đã hỏi khung giờ gọi **kèm múi giờ** chưa?")
    a("- [ ] Đã hẹn lịch có **ngày + giờ + «giờ Việt Nam»** chưa?")
    a("- [ ] ★ Khách này đã đủ thông tin để **mở app hàng không và chọn ngày bay** chưa?")
    for g in chon:
        a("- [ ] %s" % VIEC.get(g, VIEC["N2"])[0])
    a("")
    # ★ Mục 6 — mục riêng của bản quốc tế, ⛔ KHÔNG được bỏ (id-I §3).
    a("## 6 · ★ VIỆC KHÔNG PHẢI CỦA BẠN")
    a("Những câu bạn chưa trả lời được trong kỳ này là vì **hệ thống chưa cấp**, "
      "⛔ không phải vì bạn làm sai. Chúng đã được đưa lên mục *việc hệ thống*:")
    co = False
    for tc, (ly_do, ai) in LOI_HE.items():
        n_kad = sum(1 for r in rs if r.get(tc) == "—")
        if n_kad >= max(2, n // 5):
            a("- `%s` — %s — **%s** — chặn %d hội thoại của bạn" % (tc, ly_do, ai, n_kad))
            co = True
    if not co:
        a("- Kỳ này không có ô nào đủ ngưỡng để ghi vào đây.")
    a("")
    a("⛔ Bạn **không** cần tự nghĩ ra câu trả lời cho những câu này. "
      "Tự nghĩ ra một con số về số ngày ở lại là **cờ đỏ `CĐ-5`** — và đó là rủi ro y khoa thật.")
    a("")
    return "\n".join(L)


def _pct_nhom(rs, ma, cot):
    dat = sum(1 for r in rs for c in cot if r.get(c) == "✓")
    chua = sum(1 for r in rs for c in cot if r.get(c) == "✗")
    return pct(dat, dat + chua)


def so_tn(D, rows, ky):
    V = D["nhan_vien"]
    pb = V["phan_bo"]
    nhom_xep = sorted([g for g in V["nhom"] if g["pct_dat"] is not None],
                      key=lambda g: g["pct_dat"])
    A = [c for c in V["ca_nhan"] if c["loai"] == "A"]
    D_ = [c for c in V["ca_nhan"] if c["loai"] == "D"]

    L = ["# SỔ TAY TRƯỞNG NHÓM · trực kênh quốc tế", "Kỳ %s" % ky, "", GHI_CHU_DIEM, "",
         "## 1 · PHÂN BỐ NHÓM",
         " · ".join("%s: %d" % (k, v) for k, v in sorted(pb.items())), "",
         "## 2 · BA TIÊU CHÍ YẾU NHẤT CỦA KHỐI",
         "*Đây là nội dung buổi đào tạo 15 phút kỳ tới.*", ""]
    for g in nhom_xep[:3]:
        tc = sorted([c for c in g["tieu_chi"] if c["pct_dat"] is not None],
                    key=lambda c: c["pct_dat"])[:1]
        for c in tc:
            L.append("- **%s · %s** — %s%% đạt, %d HT không áp dụng"
                     % (c["ma"], c["ten"], c["pct_dat"], c["khong_ap_dung"]))
    L += ["", "## 3 · AI KÈM AI"]
    if A and D_:
        for i, d in enumerate(D_):
            a = A[i % len(A)]
            L.append("- **%s** kèm **%s** — về nhóm %s" % (a["ten"], d["ten"], d["yeu_nhat"]))
    else:
        L.append("- ⚠ Kỳ này không có người loại A để kèm. Trưởng nhóm kèm trực tiếp %d người loại D."
                 % len(D_))
    L += ["", "## 4 · CỜ ĐỎ CẦN XỬ TRONG 48 GIỜ"]
    if V["co_do"]:
        for c in V["co_do"]:
            L.append("- `%s` · **%s** · %s · trích: «%s» → *«agent điền: xử thế nào»*"
                     % (c["ma"], c["nguoi"], c["ht"], c["trich"]))
        nang = sorted({c["ma"] for c in V["co_do"]} & {"CĐ-5", "CĐ-7", "CĐ-9"})
        if nang:
            L += ["",
                  "★ **%s** — những cờ này người ta cắm vào khi **đang cố giúp khách**, "
                  "nên phải nói với **cả nhóm**, ⛔ không chỉ với người cắm cờ "
                  "(`id-I §4`)." % " · ".join(nang)]
    else:
        L.append("- Không có cờ đỏ trong kỳ.")
    L += ["", "## 5 · VIỆC KHÔNG PHẢI CỦA NHÓM BẠN",
          "*Các ô chấm «—» do lỗi hệ thống — đã đẩy lên mục việc hệ thống của dashboard, "
          "⛔ không trừ điểm nhân viên.*", ""]
    for g in V["nhom"]:
        for c in g["tieu_chi"]:
            if c["khong_ap_dung"] >= max(3, len(rows) // 10):
                L.append("- `%s · %s` — %d HT không áp dụng" % (c["ma"], c["ten"], c["khong_ap_dung"]))
    # ★ Mục 6 — lịch trực theo múi giờ. Việc của LỊCH, ⛔ không của người (id-I §4).
    MG = (D.get("thi_truong") or {}).get("mui_gio") or {}
    L += ["", "## 6 · ★ LỊCH TRỰC THEO MÚI GIỜ"]
    if MG:
        L.append("- %s HT đến **ngoài giờ 8–17 ICT** (%s%% mẫu) · chờ trung bình **%s h** · "
                 "**%s HT mất quá 12h**"
                 % (MG.get("ngoai_gio"), MG.get("pct_ngoai_gio"),
                    MG.get("cho_tb_gio") if MG.get("cho_tb_gio") is not None else "—",
                    MG.get("mat_qua_12h")))
        for x in (MG.get("theo_tang") or []):
            if x.get("ngoai_gio"):
                L.append("  - `%s` — %d HT ngoài giờ · chờ TB %s h"
                         % (x["tt"], x["ngoai_gio"],
                            x["cho_tb_gio"] if x["cho_tb_gio"] is not None else "—"))
        L += ["", "⚠️ Đây là việc của **LỊCH TRỰC**, ⛔ không của người. "
                  "17:00 ICT = 20:00 Sydney · 10:00 London · 06:00 Los Angeles — "
                  "lead tầng C gửi tin lúc tối ở nước họ sẽ không có ai trả lời trong nhiều giờ "
                  "(`id-L §4`).",
              "→ *«agent điền: đề xuất ca trực cho múi giờ đang hở»*"]
    else:
        L.append("- ⚠ Kỳ này chưa có khối `thi_truong` — chạy lại `id.py doc`.")

    L += ["", "## 7 · BẢNG ĐIỂM CẢ NHÓM", "",
          "| Nhân viên | HT | Điểm | Loại | Nhóm yếu nhất | Nhóm mạnh nhất |",
          "|---|---:|---:|---|---|---|"]
    for c in V["ca_nhan"]:
        L.append("| %s | %d | %s | %s | %s | %s |"
                 % (c["ten"], c["ht"], c["diem"] if c["diem"] is not None else "—",
                    c["loai"], c["yeu_nhat"], c["manh_nhat"]))
    L += ["", "⛔ Bảng này ⛔ không phát ra ngoài nhóm, ⛔ không dán lên màn hình chung "
              "(rào an toàn ④ của `id-F §7`).", ""]
    return "\n".join(L)


def so_nd(D, ky):
    M = D.get("ma_tran") or {}
    # ⚠ out/doc-hoi-thoai.json không có khối ma_tran/r8 — hai khối đó nằm ở file kỳ
    #   của dashboard. Thiếu thì để chỗ trống, ⛔ không bịa trạng thái đã duyệt.
    L = ["# SỔ TAY NỘI DUNG QUỐC TẾ · kỳ %s" % ky, "",
         "⛔ Sổ này ⛔ không chứa tên nhân viên trực kênh nào.", "",
         "## 1 · Ô ĐƯỢC CHỌN"]
    if M.get("trang_thai") != "da_duyet":
        L.append("⏳ **Ma trận chưa được duyệt** — chưa chốt ô nào. Xem `id-G`.")
    else:
        L.append("«agent điền: bảng ô được chọn theo khuôn id-G §6»")
    L += ["", "## 2 · NGÂN HÀNG HOOK KỲ NÀY",
          "«agent điền: bảng hook theo khuôn id-H §4 — mỗi hook phải có **TẦNG · NGÔN NGỮ · "
          "RÀO · TRUY NGƯỢC**»",
          "⚠️ Kiểm lại: hook cho `TT-C` có bị gắn format bị chặn (`L04·L05·L06·L08`) không?", "",
          "## 3 · NỘI DUNG PHẢI DỪNG",
          "«agent điền: nội dung 🔴 KÉM + mã O/OQ thấp → bỏ hẳn»", "",
          "## 4 · Ô ĐANG PHÍ",
          "«agent điền: ô ③ của ma trận CD×S7 — nhiều nội dung, ít người hỏi»", ""]

    # ★ Mục 5 — ô chờ dữ kiện. ⛔ KHÔNG phải việc của Content (id-G §4).
    L += ["## 5 · ★ Ô CHỜ DỮ KIỆN — ⛔ KHÔNG NHẬN LÀM"]
    cc = (M.get("cho_cap") or []) or ((D.get("ket_luan") or {}).get("cho_cap") or [])
    if cc:
        for r in cc:
            L.append("- **%s** — %s — chặn %s HT — %s"
                     % (r.get("du_kien"), r.get("ai_cap"), r.get("so_ht"), r.get("chan_ma", "")))
    else:
        L.append("«agent điền: các dòng ⏸ của ma trận — dữ kiện trống · ai cấp · chặn bao nhiêu HT»")
    L += ["", "⛔ Đây **không** phải việc của Content. Đừng nhận, đừng viết tạm: không ai viết "
              "nổi một hook về «số ngày ở lại» khi chưa có con số (`id-G §4`).", ""]

    L += ["## 6 · ⛔ CỜ PHÁP CHẾ TRƯỚC KHI SẢN XUẤT — HAI TẦNG",
          "**Tầng ① luật Việt Nam**",
          "- ⛔ Chữ *lifetime* / mọi thời hạn bảo hành — chưa có T&C (`id-K §3①`)",
          "- ⛔ Số ngày ở lại / mốc được phép bay bằng số cứng (`id-K §6` `L10`)",
          "- ⛔ Nêu giá mà bỏ **phụ phí quốc tế 10%** (`id-K §3③`)",
          "- ⛔ *Board certified* / claim hội ở mức thương hiệu (`id-K §3②`)",
          "- ⛔ Chức danh / số năm bác sĩ chưa qua bốn cổng (`id-K §3④`)",
          "- ⛔ Nhắc 5 viện thẩm mỹ tỉnh cho khách quốc tế (`id-K §1`)",
          "",
          "**Tầng ② luật nước người xem** — rà theo từng `market` có mặt trong kỳ",
          "- 🔴 `TT-C` (AU · UK · EU · US · GCC): ⛔ testimonial kết quả lâm sàng, "
          "⛔ before–after mặc định không dùng (AHPRA · ASA · FTC — `id-K §4`)",
          "- 🔴 EU/UK: ⛔ thu dữ liệu khi chưa có privacy notice đạt GDPR (`L12`)",
          "- ⛔ Before–after cơ thể / ngôn từ cân nặng — mọi thị trường",
          "- ⛔ So sánh giá với quốc gia / cơ sở có tên",
          "",
          "**`R8` — đủ điều kiện KCB cho người nước ngoài:** %s"
          % ("✅ đã xác nhận" if ((D.get("r8") or {}).get("xac_nhan")) else
             "🔴 `[CHỜ CẤP — Pháp chế + Điều phối QT]`"),
          "",
          "⛔ Còn một dòng 🔴 ở **bất kỳ tầng nào**, hoặc `R8` chưa xác nhận → ⛔ không phát "
          "bản này (`id-K §9`).", ""]
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser(description="Sinh sổ tay thực thi theo khuôn id-I")
    p.add_argument("--ky", required=True)
    p.add_argument("--chi", help="chỉ sinh cho một nhân viên")
    args = p.parse_args()

    D, rows = nap()
    os.makedirs(THU_MUC, exist_ok=True)
    V = D["nhan_vien"]

    da = 0
    for nv in V["ca_nhan"]:
        if args.chi and nv["ten"] != args.chi:
            continue
        if nv["loai"] == "chưa đủ mẫu":
            continue
        fp = os.path.join(THU_MUC, "ST-CN_%s.md" % ten_file(nv["ten"]))
        with open(fp, "w", encoding="utf-8") as f:
            f.write(so_cn(nv, D, rows, args.ky))
        da += 1

    with open(os.path.join(THU_MUC, "ST-TN_truong-nhom.md"), "w", encoding="utf-8") as f:
        f.write(so_tn(D, rows, args.ky))
    with open(os.path.join(THU_MUC, "ST-ND_noi-dung.md"), "w", encoding="utf-8") as f:
        f.write(so_nd(D, args.ky))

    chua = V["phan_bo"].get("chưa đủ mẫu", 0)
    print("")
    print("  Đã sinh %d sổ tay cá nhân + 1 sổ trưởng nhóm + 1 sổ nội dung" % da)
    print("  Thư mục: out/so-tay/")
    if chua:
        print("  ⚠ %d người chưa đủ 10 hội thoại — ⛔ không phân loại, ⛔ không sinh sổ (id-F §6)" % chua)
    print("  ⚠ Còn «agent điền: …» ở phần đọc hiểu — agent phải viết trước khi phát.")
    print("  ⛔ Phát riêng từng người. ⛔ Không gửi vào nhóm chat chung.")
    print("")


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
