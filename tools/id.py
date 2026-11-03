#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
id.py · Agent-InsightDashboard-KNQT  (bản QUỐC TẾ)

Làm phần ĐẾM ĐƯỢC của quy trình B1–B6:
  doc       : đọc file hội thoại → ★ TẦNG THỊ TRƯỜNG · ngôn ngữ · kênh · giờ ICT
              · chặng S1–S7 · mã O + mã OQ · mức nóng · rào cản · vì sao rơi
              · chấm điểm nhân viên N1–N7 · cờ đỏ
              + rút NGUYÊN LIỆU PHÁC HỌA CHÂN DUNG (cụm chữ khách tự nói, câu đầu)
              + gán chân dung NẾU out/chan-dung.json đã qua CỔNG 0
  chan-dung : quản lý bản phác họa chân dung của kỳ — tạo mẫu · kiểm · duyệt
  ads       : đọc chỉ số quảng cáo → chi → CPM→CTR→CPI→CPL→CPB→★CPA-KHÁM,
              ★ cắt theo thị trường (cần cột `market`)
  bao-cao   : gộp kết quả thành file JSON cho dashboard

⛔ Script KHÔNG có sẵn bộ chân dung nào. Chân dung được **phác họa từ chính hội
   thoại của kỳ** (id-C §1): agent đọc nguyên liệu → viết out/chan-dung.json →
   người dùng duyệt ở CỔNG 0 → script mới gán được chân dung cho từng hội thoại.

⛔ Script KHÔNG làm phần đọc hiểu: phác họa chân dung, insight, câu hỏi ngầm,
   hướng nội dung, câu mẫu trong sổ tay, và mọi phán đoán PHÁP CHẾ HAI TẦNG.
   Đó là việc của agent (SYSTEM-PROMPT §8).

★ Suy tầng thị trường (id-B §3) là việc script làm được, nhưng nó chỉ SUY.
   TT-0 ≥ 20% mẫu → CỔNG M: in bảng căn cứ suy và chờ người dùng xác nhận.

Cách dùng:
    python tools/id.py doc du-lieu/hoi-thoai.md --ky 19-25/10
    python tools/id.py chan-dung --ky 19-25/10 --mau
    python tools/id.py chan-dung --ky 19-25/10 --kiem
    python tools/id.py chan-dung --ky 19-25/10 --duyet "Tên người duyệt"
    python tools/id.py doc du-lieu/hoi-thoai.md --ky 19-25/10      # chạy lại, có CD
    python tools/id.py ads du-lieu/ads.csv --ky 19-25/10
    python tools/id.py bao-cao --ky 19-25/10
"""

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TU_DIEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tu_dien.json")
RA = os.path.join(GOC, "out")
PHAC_HOA = os.path.join(RA, "chan-dung.json")           # bản phác họa chân dung của kỳ
NGUYEN_LIEU = os.path.join(RA, "nguyen-lieu-chan-dung.json")

CD_DU = "CD0"                          # ★ mã DỰ TRỮ, không phác họa, không đặt lại
TEN_CD_DU = "Chưa đủ dữ kiện để xếp"   # hội thoại không khớp dấu hiệu nào
CD_TOI_THIEU_DE_DE = 15                # ≥ ngần này HT rơi CD0 → nên phác họa thêm (id-C §1)

TT_DU = "TT-0"                         # ★ tầng DỰ TRỮ — chưa khai được (id-L §1)
TEN_TT = {"TT-A": "Khu vực lân cận", "TT-B": "Kiều bào", "TT-C": "Thị trường phát triển",
          "TT-D": "Expat tại VN", TT_DU: "Chưa khai được"}
TT_NGUONG_CONG_M = 20.0                # ★ TT-0 ≥ 20% mẫu → CỔNG M (id-L §1)
TANG_TOI_THIEU = 10                    # < ngần này HT → ⛔ không kết luận riêng cho tầng

# ★ Giờ làm việc công bố trên site quốc tế: Mon–Sun 8am–5pm, giờ Việt Nam (UTC+7).
#   Tin đến NGOÀI khung này → N1.1 = "—", ⛔ KHÔNG phải ✗ (id-L §4).
GIO_MO, GIO_DONG = 8.0, 17.0
SLA_PHUT = 5                           # ★ ngưỡng trả lời tin đầu — 5′, không phải 2′ (id-F §3)
SLA_NGOAI_GIO_GIO = 12                 # ★ tin ngoài giờ phải được dọn trong 12h (N7.4)
MAU_TOI_THIEU_NV = 10                  # id-F §6

# Bốn rào chốt (id-D §6) suy từ mã O/OQ. Mỗi hội thoại lấy ĐÚNG MỘT rào —
# rào của mã OQ thắng, vì rào XA là rào cuối và là rào quyết định của bản này.
RAO_THEO_MA = {
    "OQ-01": "XA", "OQ-02": "XA", "OQ-03": "XA", "OQ-04": "XA", "OQ-05": "XA",
    "OQ-07": "XA", "OQ-06": "NGẠI", "OQ-08": "NGẠI",
    "O-02": "SỢ", "O-04": "SỢ", "O-12": "SỢ",
    "O-05": "NGỜ", "O-06": "NGỜ", "O-10": "NGỜ",
    "O-01": "NGẠI", "O-03": "NGẠI", "O-07": "NGẠI", "O-09": "NGẠI", "O-11": "NGẠI",
}


# ─────────────────────────────── tiện ích ───────────────────────────────

def khong_dau(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


_CACHE_RE = {}


def _re_tu(tu):
    """Khớp theo RANH GIỚI TỪ — nếu không, 'mí' sẽ khớp nhầm trong 'mình'."""
    k = khong_dau(tu)
    if k not in _CACHE_RE:
        _CACHE_RE[k] = re.compile(r'(?<![0-9a-zđ])' + re.escape(k) + r'(?![0-9a-zđ])')
    return _CACHE_RE[k]


def co_tu(text, danh_sach):
    t = khong_dau(text)
    return any(_re_tu(tu).search(t) for tu in danh_sach)


def tu_khop(text, danh_sach):
    t = khong_dau(text)
    return [tu for tu in danh_sach if _re_tu(tu).search(t)]


def nap_tu_dien():
    with open(TU_DIEN, encoding="utf-8") as f:
        return json.load(f)


def pct(a, b):
    return round(a / b * 100, 1) if b else None


# ★ Số điện thoại quốc tế: khách để lại số có MÃ QUỐC GIA, nên khuôn của bản
#   nội địa (bắt đầu bằng 0 hoặc +84) ⛔ không đủ.
RE_SDT_TEXT = re.compile(r'(?:\+\d{1,3}[\s.\-]?)?(?:\b0)?\d[\d .\-]{7,15}\d')
# ★ Hai thứ bản quốc tế phải bỏ thêm (id-B §2): hộ chiếu · số hiệu chuyến bay.
RE_HO_CHIEU = re.compile(r'\b[A-Z]{1,2}\d{6,9}\b')
RE_CHUYEN_BAY = re.compile(
    r'\b(?:VN|VJ|QH|SQ|TG|KE|OZ|CX|QF|JQ|EK|QR|CZ|MH|PR|BR|CI|NH|JL)\s?\d{2,4}\b', re.I)
RE_MAIL = re.compile(r'[\w.+-]+@[\w-]+\.\w+')
RE_LINK = re.compile(r'https?://\S+|\b(?:fb|facebook|zalo|m)\.(?:com|me)/\S+', re.I)


def an_danh(s):
    """★ Luật ⑩. Mọi câu của khách phải qua hàm này trước khi ghi ra file."""
    s = RE_LINK.sub("«link»", s or "")
    s = RE_MAIL.sub("«email»", s)
    s = RE_CHUYEN_BAY.sub("«chuyến bay»", s)
    s = RE_HO_CHIEU.sub("«hộ chiếu»", s)
    s = RE_SDT_TEXT.sub("«sđt»", s)
    return re.sub(r'\s+', ' ', s).strip()


# ─────────────────────────── đọc file hội thoại ──────────────────────────

RE_TIEU_DE_A = re.compile(r'^###\s+(?:<a id="ht-(\d+)"></a>)?(\d+)\.\s*(.+?)\s*$', re.M)
RE_TIEU_DE_B = re.compile(r'^##\s+(\d+)\.\s*(.+?)\s*$', re.M)
RE_META_A = re.compile(
    r'_Cập nhật:\s*([\d\-: ]+)\s*·\s*NV:\s*(.*?)\s*·\s*SĐT:\s*(\S+)\s*·\s*ID:\s*(\S+?)_')
RE_META_B = re.compile(
    r'\*\*Page:\*\*\s*(.*?)\s*·\s*\*\*Nhân viên:\*\*\s*(.*?)\s*·\s*\*\*Cập nhật:\*\*\s*([\d\-: ]+)')
RE_TIN = re.compile(r'^-\s+`(\d{2}-\d{2}\s+\d{2}:\d{2})`\s+\*\*(.+?):?\*\*:?\s*(.*)$')
# ★ Dòng meta riêng của bản quốc tế (id-B §2):
#   _Kênh: WhatsApp · Nước: AU · Ngôn ngữ: EN_
#   Thiếu dòng này thì vẫn chạy được: tầng · kênh · ngôn ngữ suy ra từ chữ của
#   khách, nhưng độ tin thấp hơn và phải ghi nhãn `suy ra`.
RE_META_QT = re.compile(
    r'_?\s*Kênh:\s*(?P<kenh>[^·_\n]*?)\s*(?:·\s*Nước:\s*(?P<nuoc>[^·_\n]*?)\s*)?'
    r'(?:·\s*Ngôn ngữ:\s*(?P<ngon_ngu>[^·_\n]*?)\s*)?_?\s*$', re.M)

# Dòng do HỆ THỐNG sinh, không phải lời khách. ⛔ Không đếm là một lượt của khách,
# không đưa vào văn bản phân loại — nếu đếm thì "bỏ sau 1 lượt" luôn ra 0%.
RE_NHIEU = re.compile(
    r'(\[tệp đính kèm|\[hình ảnh|cuộc gọi thoại|cuộc gọi video|đã gọi cho bạn|'
    r'bạn có thể gọi cho|bạn có một tin nhắn|^\{"filename"|^https?://|'
    r'đã gửi một|người dùng đã|^\s*$)', re.I)


def la_nhieu(text):
    return bool(RE_NHIEU.search((text or "").strip()))


def co_anh(text):
    return bool(re.search(r'(\[tệp đính kèm|\[hình ảnh|"type"\s*:\s*"image")', text or "", re.I))


def doc_hoi_thoai(duong_dan):
    """Trả về danh sách hội thoại. Hỗ trợ hai khuôn xuất Caresoft."""
    with open(duong_dan, encoding="utf-8") as f:
        raw = f.read()

    moc = [(m.start(), m.group(2) or m.group(1), m.group(3)) for m in RE_TIEU_DE_A.finditer(raw)]
    if not moc:
        moc = [(m.start(), m.group(1), m.group(2)) for m in RE_TIEU_DE_B.finditer(raw)]
    if not moc:
        sys.exit("⛔ Không nhận ra khuôn file hội thoại. Xem knowledge/id-B §2.")

    ket = []
    for i, (vt, so, ten) in enumerate(moc):
        het = moc[i + 1][0] if i + 1 < len(moc) else len(raw)
        khoi = raw[vt:het]

        kenh_khai, nuoc_khai, nn_khai = "", "", ""
        mq = RE_META_QT.search(khoi)
        if mq:
            kenh_khai = (mq.group("kenh") or "").strip()
            nuoc_khai = (mq.group("nuoc") or "").strip().upper()
            nn_khai = (mq.group("ngon_ngu") or "").strip().upper()

        nv_ho_so, co_sdt = "", False
        m = RE_META_A.search(khoi)
        if m:
            nv_ho_so = m.group(2).strip()
            co_sdt = khong_dau(m.group(3)).startswith("co")
        else:
            m = RE_META_B.search(khoi)
            if m:
                nv_ho_so = m.group(2).strip()

        tin = []
        for dong in khoi.splitlines():
            mt = RE_TIN.match(dong.strip())
            if not mt:
                continue
            tem, ai, noi_dung = mt.group(1), mt.group(2).strip(), mt.group(3).strip()
            la_nv = khong_dau(ai).startswith("nv")
            nv_ten = ai[2:].strip() if la_nv else ""
            if not la_nv and khong_dau(ai) not in ("kh",) and nv_ho_so and ai == nv_ho_so:
                la_nv, nv_ten = True, ai
            tin.append({"tem": tem, "nv": la_nv, "ten": nv_ten, "text": noi_dung,
                        "nhieu": la_nhieu(noi_dung), "anh": co_anh(noi_dung)})

        thuc = [t for t in tin if not t["nhieu"]]
        if len(thuc) < 2:
            continue

        nv = nv_ho_so or next((t["ten"] for t in tin if t["nv"] and t["ten"]), "")
        if co_sdt is False:
            co_sdt = bool(re.search(r'\b0\d{8,10}\b', khoi))

        # ⚠ Bản xuất Caresoft gắn sẵn một dòng [Tệp đính kèm] vào MỌI hội thoại đến
        #   từ quảng cáo (ảnh preview của ad), nên "có dòng ảnh" KHÔNG đồng nghĩa
        #   "khách gửi ảnh tình trạng".
        anh_kh = [i for i, t in enumerate(tin) if t["anh"] and not t["nv"]]
        vt_moi_anh = next((i for i, t in enumerate(tin)
                           if t["nv"] and re.search(r'(gửi|xin|chụp).{0,12}(ảnh|hình)',
                                                    t["text"], re.I)), None)
        #   Dòng ảnh mặc định nằm ngay đầu hội thoại nên ⛔ không dùng số lượng ảnh
        #   làm căn cứ — chỉ nhận khi ảnh đến SAU lời mời gửi ảnh của nhân viên.
        gui_anh = vt_moi_anh is not None and any(i > vt_moi_anh for i in anh_kh)

        ket.append({
            "ma": "HT-%03d" % int(so),
            "nv": nv or "(không rõ)",
            "co_sdt": co_sdt,
            "kenh_khai": kenh_khai,
            "nuoc_khai": nuoc_khai,
            "ngon_ngu_khai": nn_khai,
            "tin": thuc,                       # ⛔ đã bỏ dòng hệ thống
            # Đồng hồ SLA chạy từ tin ĐẦU TIÊN của hội thoại, kể cả dòng hệ thống:
            # đó là lúc khách bấm quảng cáo, không phải lúc khách gõ câu đầu.
            "moc_bat_dau": tin[0]["tem"] if tin else None,
            "kh_gui_anh": gui_anh,
            "kh_text": " ".join(t["text"] for t in thuc if not t["nv"]),
            "nv_text": " ".join(t["text"] for t in thuc if t["nv"]),
        })
    return ket


def phut(tem_a, tem_b):
    """Khoảng cách phút giữa hai tem `MM-DD HH:MM`."""
    try:
        a = datetime.strptime("2026-" + tem_a, "%Y-%m-%d %H:%M")
        b = datetime.strptime("2026-" + tem_b, "%Y-%m-%d %H:%M")
        return (b - a).total_seconds() / 60
    except ValueError:
        return None


def gio_cua(tem):
    try:
        t = datetime.strptime("2026-" + tem, "%Y-%m-%d %H:%M")
        return t.hour + t.minute / 60
    except ValueError:
        return None


# ───────────────────────────── phân loại ─────────────────────────────────

RE_MA_CD = re.compile(r'^CD[1-9][0-9]*$')


def kiem_phac_hoa(pho):
    """Soát bản phác họa chân dung. Trả về danh sách lỗi — rỗng là sạch."""
    if not isinstance(pho, dict):
        return ["file không phải một đối tượng JSON"]
    loi = []
    tep = pho.get("tep")
    if not isinstance(tep, list) or not tep:
        return ["thiếu danh sách `tep` — phải có ít nhất một chân dung"]
    da_thay = set()
    for i, c in enumerate(tep, 1):
        c = c or {}
        vt = "dòng %d" % i
        ma = (c.get("ma") or "").strip()
        if not RE_MA_CD.match(ma):
            loi.append("%s: mã «%s» sai khuôn — phải là CD1, CD2, … (CD0 là mã dự trữ)" % (vt, ma))
        elif ma in da_thay:
            loi.append("%s: mã «%s» bị trùng" % (vt, ma))
        da_thay.add(ma)
        if not (c.get("ten") or "").strip():
            loi.append("%s «%s»: thiếu `ten`" % (vt, ma))
        dh = [x for x in (c.get("dau_hieu") or []) if (x or "").strip()]
        if not dh:
            loi.append("%s «%s»: thiếu `dau_hieu` — không có dấu hiệu thì script không gán được" % (vt, ma))
        hs = c.get("he_so_gia_tri")
        if hs is not None and hs not in (1, 2, 3):
            loi.append("%s «%s»: `he_so_gia_tri` phải là 1, 2 hoặc 3 (id-G §3)" % (vt, ma))
        tt = c.get("tt") or []
        if not tt:
            loi.append("%s: thiếu `tt` — chân dung quốc tế phải khai tầng chính (id-C §1)" % vt)
        else:
            xau = [x for x in tt if x not in ("TT-A", "TT-B", "TT-C", "TT-D")]
            if xau:
                loi.append("%s: `tt` có giá trị lạ %s — chỉ TT-A…TT-D (⛔ không khai TT-0)"
                           % (vt, xau))
        if (c.get("rao_chot") or "") not in ("SỢ", "NGỜ", "NGẠI", "XA"):
            loi.append("%s: `rao_chot` phải là ĐÚNG MỘT trong SỢ · NGỜ · NGẠI · XA (id-D §6)" % vt)
        if not (c.get("rang_buoc_chuyen_di") or "").strip():
            loi.append("%s: thiếu `rang_buoc_chuyen_di` — ⛔ không bỏ trống ở bản quốc tế" % vt)
        if not (c.get("trich") or []):
            loi.append("%s «%s»: thiếu `trich` — chân dung phải truy ngược về HT-nnn (luật ①)" % (vt, ma))
    if pho.get("trang_thai") == "da_duyet" and not (pho.get("duyet_boi") or "").strip():
        loi.append("`trang_thai` là da_duyet nhưng `duyet_boi` trống "
                   "— ⛔ agent không tự duyệt thay người dùng")
    return loi


def nap_phac_hoa(ky):
    """Đọc bản phác họa chân dung của kỳ. Trả về (bản phác họa | None, lý do).

    ⛔ Chỉ nhận bản ĐÃ QUA CỔNG 0. Chưa duyệt thì script không gán chân dung —
    hội thoại để `cd = null` và agent phải phác họa trước (id-C §1).
    """
    if not os.path.exists(PHAC_HOA):
        return None, "chưa có out/chan-dung.json — chân dung chưa được phác họa"
    try:
        with open(PHAC_HOA, encoding="utf-8") as f:
            pho = json.load(f)
    except ValueError as e:
        return None, "out/chan-dung.json không đọc được: %s" % e
    loi = kiem_phac_hoa(pho)
    if loi:
        return None, ("out/chan-dung.json còn %d lỗi — chạy `id.py chan-dung --kiem`" % len(loi))
    if (pho.get("ky") or "") != ky:
        return None, ("out/chan-dung.json là của kỳ «%s», không phải «%s»"
                      % (pho.get("ky") or "trống", ky))
    if pho.get("trang_thai") != "da_duyet":
        return None, "chân dung chưa qua CỔNG 0 — chờ `id.py chan-dung --duyet «tên người»`"
    return pho, None


def gan_chan_dung(ht, pho):
    """Gán theo DẤU HIỆU của bản phác họa đã duyệt, xét từ trên xuống.

    Dòng đầu khớp thì lấy dòng đó → xếp chân dung HẸP trước, RỘNG sau (id-C §1).
    Không khớp dòng nào → CD0, mã dự trữ, ⛔ không phải "rác".
    """
    if not pho:
        return None
    kh = ht["kh_text"]
    for c in pho["tep"]:
        if not co_tu(kh, c["dau_hieu"]):
            continue
        if c.get("khong_phai") and co_tu(kh, c["khong_phai"]):
            continue
        return c["ma"]
    return CD_DU


def cau_dau_kh(ht):
    """Câu hỏi ĐẦU TIÊN của khách — căn cứ gán chặng (id-C §3)."""
    return next((t["text"] for t in ht["tin"] if not t["nv"] and len(t["text"]) > 3), "")


# ★ Chặng S6 nhận bằng chữ hậu phẫu; đặt riêng để khỏi lẫn với O-04 (sợ đau).
HAU_PHAU = ["swelling after", "after my surgery", "after the surgery", "aftercare",
            "recovery tips", "when can i remove", "stitches", "cắt chỉ xong",
            "sau khi mổ", "hậu phẫu", "tái khám"]
HOC_HOI = ["what is", "what's the difference between", "should i get", "types of",
           "is it worth", "nên làm gì", "có nên"]
SO_SANH_DIEM_DEN = ["in vietnam", "vietnam safe", "why vietnam", "vs thailand", "vs korea",
                    "vs turkey", "than thailand", "than korea", "than turkey",
                    "which country", "ở việt nam có"]


def gan_chang(ht, td):
    """Phễu 7 chặng — chạy theo ĐÚNG thứ tự của id-C §3, dừng ở dòng khớp đầu tiên.

    ⚠ Bước S4 đặt TRƯỚC S5 là có chủ ý: câu "how many days and how much" chứa cả
      chữ về chi phí, nhưng intent chính là KẾ HOẠCH — và một câu trả lời chỉ có
      giá ⛔ không trả lời được nó. Đảo hai bước này là xoá sạch chặng S4 khỏi
      báo cáo, mà tổng vẫn khớp nên không ai nhìn ra.
    """
    dau = cau_dau_kh(ht)
    oq = td["ma_oq"]
    if co_tu(dau, oq["OQ-01"] + oq["OQ-03"] + oq["OQ-05"] + oq["OQ-07"]):
        return "S4"
    if co_tu(dau, td["ma_o"]["O-01"] + oq["OQ-06"] + ["book", "đặt lịch"]):
        return "S5"
    if co_tu(dau, td["ma_o"]["O-02"] + td["ma_o"]["O-04"] + td["ma_o"]["O-05"]
                  + td["ma_o"]["O-06"] + td["ma_o"]["O-07"]):
        return "S3"
    if co_tu(dau, SO_SANH_DIEM_DEN) and not co_tu(dau, sum(td["dich_vu_chinh"].values(), [])):
        return "S2"
    if co_tu(dau, HOC_HOI):
        return "S1"
    if co_tu(dau, HAU_PHAU):
        return "S6"
    # ★ Câu HỎI THÔNG TIN DỊCH VỤ thuần ("I'd like to know about breast
    #   augmentation") là chặng S1: khách đang tìm hiểu, CHƯA chọn nước (S2),
    #   CHƯA sợ (S3), CHƯA tính chuyến đi (S4). ⛔ Không đẩy nhóm này sang S2:
    #   S2 là chặng chọn NƯỚC, không phải chặng hỏi dịch vụ.
    if co_tu(dau, td.get("hoi_thong_tin", [])):
        return "S1"
    # ⛔ Không mặc định S1. Chưa rõ thì ghi là chưa rõ — id-C §3 bước 7.
    return "chưa rõ"


# ⚠ Nhận ngôn ngữ phải khớp chữ CÓ DẤU. Bỏ dấu rồi so là cách sai: tên bác sĩ
#   Việt trong một câu tiếng Anh ("Dr. Nguyễn Quốc Chí") sẽ khớp "chị", "mình",
#   "giá"… và biến câu tiếng Anh thành tiếng Việt — đẻ ra một hàng
#   "hệ thống — ngôn ngữ" không có thật.
RE_TU_VIET = re.compile(
    r'(?<![0-9A-Za-zÀ-ỹ])(?:ạ|ơi|nhé|của|được|không|mình|chị|em|anh|giá|bác sĩ|làm|vâng|dạ'
    r'|và|có|cho|với|này|thì|là|rất|nhưng|hoặc|cũng|đã|sẽ|tại|về|theo|một)'
    r'(?![0-9A-Za-zÀ-ỹ])', re.I)


def dem_dau_viet(s):
    """Số lần xuất hiện từ tiếng Việt CÓ DẤU — ⛔ không bỏ dấu trước khi so."""
    return len(RE_TU_VIET.findall(s or ""))


def gan_ngon_ngu(ht, td):
    """Ngôn ngữ của KHÁCH. ⚠ Tiếng Việt ⛔ không có nghĩa là khách nội địa (id-L §1)."""
    if ht.get("ngon_ngu_khai") in ("EN", "VI", "KM", "AR", "XX"):
        return ht["ngon_ngu_khai"]
    kh = ht["kh_text"]
    for ma in ("KM", "AR"):
        if any(x in kh for x in td["ngon_ngu"].get(ma, [])):
            return ma
    if dem_dau_viet(kh) >= 2:
        return "VI"
    return "EN" if re.search(r'[A-Za-z]{3,}', kh) else "XX"


def gan_ngon_ngu_nv(ht, td):
    """Ngôn ngữ nhân viên TRẢ LỜI — chấm riêng cột, đối chiếu với cột khách (N7.3)."""
    nv = ht["nv_text"]
    if not nv.strip():
        return None
    # ⚠ Ngưỡng 3 (cao hơn phía khách): lời bot hay lẫn tên bác sĩ Việt và
    #   một hai chữ Việt sót lại, chưa đủ để gọi là trả lời bằng tiếng Việt.
    return "VI" if dem_dau_viet(nv) >= 3 else ("EN" if re.search(r'[A-Za-z]{3,}', nv) else "XX")


def gan_kenh(ht, td):
    """Kênh nhắn tin. ⚠ Chỉ Messenger + click-to-WhatsApp nối được về ads (id-L §5)."""
    khai = khong_dau(ht.get("kenh_khai") or "")
    for ten in td["kenh"]:
        if ten.startswith("_"):
            continue
        if khai and khong_dau(ten) in khai:
            return ten
    return "chưa rõ"


def gan_tt(ht, td):
    """★ Suy TẦNG THỊ TRƯỜNG — id-B §3, chạy theo ĐÚNG thứ tự, dừng ở dòng đầu khớp.

    Trả về (tầng, market, căn cứ). ⛔ Ba cách suy SAI, tuyệt đối không dùng:
      ① suy từ DỊCH VỤ khách hỏi        — dịch vụ không nói gì về vị trí
      ② suy từ NGÔN NGỮ một mình        — tiếng Việt có thể là TT-B
      ③ suy từ TÊN THÀNH PHỐ trong câu  — "surgery in Hanoi" là NƠI MỔ
    """
    T = td["thi_truong"]
    bang = T["tang_theo_nuoc"]
    kh = ht["kh_text"]
    nn = ht.get("_ngon_ngu")

    # ① file khai sẵn
    nuoc = ht.get("nuoc_khai") or ""
    if nuoc:
        if nuoc == "VN-EXPAT":
            return "TT-D", nuoc, "khai sẵn"
        if nuoc.startswith("VN-DIASPORA"):
            return "TT-B", nuoc, "khai sẵn"
        if nuoc in bang:
            tt = "TT-B" if nn == "VI" and co_tu(kh, T["ve_nuoc"]) else bang[nuoc]
            return tt, nuoc, "khai sẵn"

    # ② khách tự nói nước mình đang ở
    ma_nuoc = None
    for ma, tu in T["nuoc"].items():
        if co_tu(kh, tu):
            ma_nuoc = ma
            break

    # ③ tiếng Việt + nói "về nước" → kiều bào
    if nn == "VI" and co_tu(kh, T["ve_nuoc"]):
        return "TT-B", ("VN-DIASPORA-" + ma_nuoc) if ma_nuoc else "VN-DIASPORA-?", "khách tự nói"

    # ④ đang sống ở VN → expat
    if co_tu(kh, T["dang_o_vn"]):
        return "TT-D", "VN-EXPAT", "khách tự nói"

    # ⑤ nói nước mình ở (không phải kiều bào)
    if ma_nuoc:
        return bang.get(ma_nuoc, TT_DU), ma_nuoc, "khách tự nói"

    # ⑥ hỏi chuyện bay sang / hỏi mã OQ của chặng S4 → chắc chắn là khách quốc tế,
    #    nhưng ⛔ CHƯA BIẾT NƯỚC. Không đoán tầng, chỉ ghi nhận là quốc tế.
    if co_tu(kh, T["se_bay_sang"]) or co_tu(kh, td["ma_oq"]["OQ-01"] + td["ma_oq"]["OQ-05"]):
        return TT_DU, None, "quốc tế nhưng chưa rõ nước"

    # ⑦ suy từ kênh — độ tin YẾU, luôn ghi nhãn
    kenh = ht.get("_kenh")
    if kenh == "KakaoTalk":
        return "TT-A", "KR", "suy từ kênh ⚠"
    if kenh == "Line":
        return "TT-A", "JP", "suy từ kênh ⚠"

    return TT_DU, None, "không khớp dòng nào"


def ngoai_pham_vi(ht, td):
    """★ Khách NỘI ĐỊA nhắn lạc vào kênh quốc tế — id-B §3.

    Dấu hiệu: tiếng Việt, ⛔ không nhắc gì đến ở nước ngoài / về nước / bay.
    Xử lý: loại khỏi mẫu phân tích, ⛔ KHÔNG xếp vào TT-B.
    """
    if ht.get("_ngon_ngu") != "VI":
        return False
    T = td["thi_truong"]
    return not (co_tu(ht["kh_text"], T["ve_nuoc"])
                or co_tu(ht["kh_text"], sum(T["nuoc"].values(), []))
                or co_tu(ht["kh_text"], sum((td["ma_oq"].get(m, []) for m in
                                             ("OQ-01", "OQ-03", "OQ-05", "OQ-07")), [])))


def trong_gio(ht):
    """Tin ĐẦU TIÊN của hội thoại đến trong khung 08:00–17:00 ICT hay không (id-L §4)."""
    g = gio_cua(ht.get("moc_bat_dau") or "")
    if g is None:
        return None
    return GIO_MO <= g <= GIO_DONG


def cho_bao_lau(ht):
    """Số GIỜ từ tin đầu của khách tới tin trả lời đầu tiên của nhân viên."""
    moc = ht.get("moc_bat_dau")
    tra = next((x for x in ht["tin"] if x["nv"]), None)
    if not moc or not tra:
        return None
    d = phut(moc, tra["tem"])
    return round(d / 60, 1) if d is not None and d >= 0 else None


def gan_ma_o(ht, td, ma_oq=()):
    """12 mã O dùng chung cả hệ.

    ⚠ Thứ tự của id-D §1: không xếp được vào 12 mã O thì XÉT BỘ OQ TRƯỚC; chỉ khi
      cả hai bộ đều không chứa mới gán O-00. ⛔ Gán O-00 cho một hội thoại mà
      phản đối của nó là mã OQ sẽ làm O-00 phình lên và che mất tín hiệu thật.
    """
    kh = ht["kh_text"]
    ma = [m for m, tu in td["ma_o"].items() if co_tu(kh, tu)]
    # Khách gửi ảnh tình trạng mà không tả bằng chữ vẫn là O-08 "không biết mình cần gì".
    if ht.get("kh_gui_anh") and "O-08" not in ma:
        ma.append("O-08")
    if ma:
        return sorted(ma)
    if ma_oq:
        return []          # ★ phản đối đã xếp được vào bộ OQ → ⛔ không phải O-00
    # ⚠ Phân biệt hai thứ hay bị gộp:
    #   "(chưa nêu)" = khách chưa nói gì đủ để có phản đối  → KHÔNG tính vào O-00
    #   "O-00"       = khách CÓ nêu điều gì đó mà danh sách 12 mã không chứa
    #                  → vượt 10% mẫu là tín hiệu phải bổ sung từ điển (id-D §1)
    # ★ Tách "(chưa nêu)" khỏi "O-00" (id-D §1):
    #   (chưa nêu) = khách chưa nói gì đủ để có phản đối, HOẶC chỉ hỏi thông tin
    #                dịch vụ — một câu hỏi dịch vụ thuần ⛔ không phải một phản đối.
    #   O-00       = khách CÓ nêu một điều mà cả hai danh sách O và OQ không chứa
    #                → vượt 10% mẫu là tín hiệu phải bổ sung từ điển, ⛔ không tự thêm mã.
    if len(re.sub(r'\W+', '', kh)) < 20 or co_tu(kh, td.get("hoi_thong_tin", [])):
        return ["(chưa nêu)"]
    return ["O-00"]


def gan_lam_o_dau(ht, td):
    """id-K §4b — BA loai "em da lam roi", va chung ⛔ KHONG giong nhau.

      noi-khac            -> ca tu van moi, rao NGO rat nang
      tai-kn-trong-vn     -> KHIEU NAI, ⛔ khong phai co hoi ban
      tai-kn-da-ve-nuoc   -> 🔴 CAP CUU Y KHOA O XA. Khach ⛔ khong quay lai
                             duoc de (dung rao XA) -> chuyen bac si NGAY.

    ⛔ KHONG khoa o nay sau mot ma dich vu nao: mot lo hong cua bo cum
    ⛔ khong duoc bien thanh mot ca khieu nai bi cham nhu co hoi ban.
    """
    t = td.get("lam_o_dau", {})
    kh = ht["kh_text"]
    # ⚠ Nhan bang LOGIC, ⛔ khong bang mot danh sach cau day du: khach viet
    # "I had my rhinoplasty at Kangnam six weeks ago" — liet ke het cac cach
    # dien dat la viec khong bao gio xong. Dieu kien: TEN + nhan DA LAM.
    if co_tu(kh, t.get("ten_kn", [])) and co_tu(kh, t.get("da_lam", [])):
        return "tai-kn-da-ve-nuoc" if co_tu(kh, t.get("da_ve_nuoc", [])) else "tai-kn-trong-vn"
    if co_tu(kh, t.get("noi_khac", [])):
        return "noi-khac"
    return ""


def co_dau_hieu_an_toan(ht, td):
    """id-K §4b ① — tra ve "cap-tinh" | "chong-chi-dinh" | "".

    ⚠ HAI TANG, va chi tang dau lam hoi thoai thanh luong KHONG-BAN:
      · cap-tinh       : trieu chung DANG dien ra -> N3 va N5 cham "—"
      · chong-chi-dinh : benh nen/thuoc khach tu neu -> PHAI chuyen bac si cho
                         CAU HOI Y KHOA (CD-3 · N3.5), nhung hoi thoai VAN la
                         ca tu van hop le -> ⛔ KHONG mien N5.

    ★ "collapsed" / "deformed" la CHI DINH LAM LAI, ⛔ khong phai cap tinh.
      Mot ca lam lai duoc tu van tot thi phai duoc CHAM — mien no la mat
      phan khen dung.
    """
    t = td.get("dau_hieu_an_toan", {})
    kh = ht["kh_text"]
    if co_tu(kh, t.get("cap_tinh", [])):
        return "cap-tinh"
    if co_tu(kh, t.get("chong_chi_dinh", [])):
        return "chong-chi-dinh"
    return ""


def gan_ma_oq(ht, td):
    """★ Tám mã phản đối CHỈ CÓ Ở KHÁCH QUỐC TẾ (id-D §2).

    ⚠ Mã OQ xuất hiện MUỘN trong hội thoại — câu "how many days do I stay"
      thường là câu thứ năm, thứ sáu. Vì vậy quét TOÀN BỘ lời khách, ⛔ không
      chỉ ba tin đầu.
    """
    kh = ht["kh_text"]
    return sorted(m for m, tu in td["ma_oq"].items()
                  if not m.startswith("_") and co_tu(kh, tu))


def gan_rao_chot(ma_o, ma_oq):
    """ĐÚNG MỘT rào trong SỢ · NGỜ · NGẠI · XA (id-D §6).

    ★ Mã OQ thắng mã O: rào XA là rào CUỐI CÙNG — khách đã vượt Sợ, Ngờ, Ngại
      rồi mới chạm vào nó, nên mất khách ở đây là mất khách đắt nhất.
    """
    for m in ma_oq:
        if m in RAO_THEO_MA:
            return RAO_THEO_MA[m]
    for m in ma_o:
        if m in RAO_THEO_MA:
            return RAO_THEO_MA[m]
    return None


def s4_chua_dong(ht, td, ma_oq):
    """★ Bốn câu của rào XA (id-D §6.1) — câu nào khách hỏi mà CHƯA được trả lời.

    Phép thử của bản quốc tế: "đọc hết hội thoại này, khách có đủ thông tin để
    mở app hàng không và chọn ngày bay chưa?" — đây là phần đếm được của nó.
    """
    nv = ht["nv_text"]
    cau = []
    if "OQ-01" in ma_oq and not co_tu(nv, td["nv_hoan_so_ngay"] + ["days", "ngày"]):
        cau.append("1_so_ngay")
    if "OQ-02" in ma_oq and not co_tu(nv, ["interpreter", "follow up", "follow-up",
                                           "international patient", "phiên dịch", "tái khám"]):
        cau.append("2_ai_lo")
    if "OQ-04" in ma_oq:
        cau.append("3_ai_tra_phi")      # 🔴 chưa có T&C → ⛔ không ai trả lời được
    if "OQ-03" in ma_oq and not co_tu(nv, ["interpreter", "english", "phiên dịch", "tiếng anh"]):
        cau.append("4_ngon_ngu")
    return cau


def gan_nhiet(ht, td):
    th = []
    kh = ht["kh_text"]
    if co_tu(kh, sum(td["dich_vu_chinh"].values(), [])) or ht.get("kh_gui_anh"):
        th.append("1_dich_vu")
    # ★ Tín hiệu ② của bản quốc tế là CỬA SỔ CHUYẾN ĐI, không phải "mốc ≤14 ngày".
    #   ⚠ Luật mùa (id-L §6) do agent áp khi đọc: cùng câu "em về Tết" nói vào
    #     tháng 10 là cửa sổ đang mở, nói vào tháng 2 là cửa sổ đã đóng.
    if co_tu(kh, td["tin_hieu_nong"]["2_cua_so_chuyen_di"]):
        th.append("2_cua_so_chuyen_di")
    if ht["co_sdt"]:
        th.append("3_lien_he")
    if co_tu(kh, td["tin_hieu_nong"]["4_dieu_kien"]):
        th.append("4_dieu_kien")
    # ★ Tín hiệu ⑤ đòi có MÚI GIỜ. Khung giờ không kèm múi giờ là một con số vô
    #   dụng — và đó là lỗi của CÂU HỎI, không phải của khách.
    if co_tu(kh, td["tin_hieu_nong"]["5_khung_gio"]):
        th.append("5_khung_gio")
    n = len(th)
    muc = "HOT" if n >= 4 else ("WARM" if n >= 2 else "COLD")
    return muc, th


def gan_dich_vu(ht, td):
    kh = ht["kh_text"]
    for dv, tu in td["dich_vu_chinh"].items():
        if co_tu(kh, tu):
            return dv
    return "(chưa nêu)"


def he_so_gia_tri(ht, td, tt=None):
    """Hệ số 1 · 2 · 3 theo BẢNG GIÁ CÔNG KHAI (/price-list/ — id-G §3).

    ★ LUẬT COMBO: dịch vụ giá thấp (cắt mí đơn lẻ · da liễu · clinic) cho
      TT-A/B/C bị cắt về hệ số 1 — ⛔ không ai bay 6 giờ để cắt mí. Với TT-D
      (expat đang ở VN) thì ngược lại: đây là dịch vụ LÕI, giữ nguyên hệ số.
    """
    kh = ht["kh_text"]
    hs = 1
    for bac in ("3", "2", "1"):
        if co_tu(kh, td["gia_tri_don"][bac]):
            hs = int(bac)
            break
    gia_thap = co_tu(kh, td["gia_tri_don"]["1"]) and not co_tu(
        kh, td["gia_tri_don"]["3"] + td["gia_tri_don"]["2"])
    if gia_thap and tt in ("TT-A", "TT-B", "TT-C"):
        return 1
    return hs


def gan_vi_sao_roi(ht, td, diem, ma_oq=(), s4=()):
    """Mỗi hội thoại ĐÚNG MỘT giá trị (id-D §4).

    ★ Bản quốc tế tách nhánh "hệ thống" thành BA nhánh, vì ba người khác nhau
      sửa: dữ kiện (Khoa Chuyên môn · Pháp chế · Điều phối QT) · múi giờ (lịch
      trực) · ngôn ngữ (vận hành). Gộp lại thì mục việc hệ thống ra một dòng
      vô nghĩa kiểu "cần hoàn thiện hệ thống".
    """
    if ht["co_sdt"] or ht.get("chot_lich"):
        return "không rơi"
    tin = ht["tin"]
    kh_luot = sum(1 for t in tin if not t["nv"])
    nv_luot = sum(1 for t in tin if t["nv"])

    # ① Không ai trả lời, mà tin đến NGOÀI GIỜ ICT → lỗi LỊCH TRỰC, ⛔ không
    #    phải lỗi người. Đây là nguyên nhân số một của lead quốc tế mất.
    if nv_luot == 0:
        return "hệ thống — múi giờ" if ht.get("_trong_gio") is False else "hệ thống — dữ kiện"

    # ② Chờ quá lâu vì lệch giờ, dù sau đó có trả lời.
    if ht.get("_trong_gio") is False:
        ch = cho_bao_lau(ht)
        if ch is not None and ch > SLA_NGOAI_GIO_GIO and kh_luot <= 2:
            return "hệ thống — múi giờ"

    # ③ Khách nhắn một ngôn ngữ, nhân viên trả lời ngôn ngữ khác.
    if ht.get("_ngon_ngu") and ht.get("_ngon_ngu_nv") and \
            ht["_ngon_ngu"] != ht["_ngon_ngu_nv"] and "XX" not in (
            ht["_ngon_ngu"], ht["_ngon_ngu_nv"]):
        return "hệ thống — ngôn ngữ"

    # ④ ★ Khách hỏi rào XA mà câu đó KHÔNG AI TRẢ LỜI ĐƯỢC vì thiếu dữ kiện gốc
    #    (số ngày ở lại · T&C bảo hành · visa · thanh toán) → lỗi DỮ KIỆN.
    if s4 and kh_luot >= 2:
        return "hệ thống — dữ kiện"

    cuoi = tin[-1]
    if cuoi["nv"] and kh_luot >= 2:
        return "khách tự dừng"
    if kh_luot == 1 and nv_luot >= 1:
        return "trực kênh"
    if diem is not None and diem < 55:
        return "trực kênh"
    # ⚠ Né giá ở bản quốc tế là LỖI NGƯỜI, không phải lỗi hệ: giá đã công khai
    #   tại /price-list/ (id-K §3③). Ngược hẳn bản nội địa.
    if co_tu(ht["kh_text"], td["ma_o"]["O-01"]) and not co_tu(ht["nv_text"], td["nv_neu_gia"]):
        return "trực kênh"
    return "khách tự dừng"


# Rào cản suy ra từ mã O. Hai nhãn "đã làm nơi khác" và "chờ ưu đãi" nhận bằng
# từ khoá ở tu_dien.json → `rao_can`; "chưa nói tình trạng" và "hỏi giá ngay"
# tính riêng bên dưới.
# ⛔ Không nhãn nào được suy ra từ CHÂN DUNG. Chân dung của kỳ do người dùng duyệt
#   ở CỔNG 0 — lấy nó làm căn cứ chấm rào cản là chấm lại hội thoại (luật ③).
RAO_CAN = {
    "sợ đau/nghỉ việc": "O-04",
    "ở xa": "O-09",
    "người nhà cản": "O-11",
    "so giá đối thủ": "O-10",
    "chưa tin cơ sở": "O-06",
    # ★ Năm nhãn của bản quốc tế, suy từ mã OQ
    "chưa biết ở lại mấy ngày": "OQ-01",
    "lo thanh toán/đặt cọc": "OQ-06",
    "rào ngôn ngữ": "OQ-03",
}


def gan_rao_can(ht, td, ma_o, ma_oq=()):
    rc = []
    kh = ht["kh_text"]
    # Khách không nêu được dịch vụ nào và cũng không gửi ảnh tình trạng
    # → chưa nói tình trạng. ⚠ Đây là tình trạng của HỘI THOẠI, không phải
    #   của chân dung: quảng cáo kéo được người vào mà không làm họ kể.
    if not co_tu(kh, sum(td["dich_vu_chinh"].values(), [])) and not ht.get("kh_gui_anh"):
        rc.append("chưa nói tình trạng")
    dau = next((t["text"] for t in ht["tin"] if not t["nv"] and len(t["text"]) > 3), "")
    if co_tu(dau, td["ma_o"]["O-01"]):
        rc.append("hỏi giá ngay")
    for ten, tu in td.get("rao_can", {}).items():
        if ten.startswith("_") or not isinstance(tu, list):
            continue
        if co_tu(kh, tu):
            rc.append(ten)
    for ten, ma in RAO_CAN.items():
        if isinstance(ma, str) and (ma in ma_o or ma in ma_oq):
            rc.append(ten)
    # ★ Hai nhãn chỉ có ở bản quốc tế, nhận bằng chữ chứ không qua mã
    if ht.get("_ngon_ngu") == "VI" and co_tu(kh, td["thi_truong"]["ve_nuoc"]):
        if co_tu(kh, td["rao_can"]["cửa sổ chuyến đi quá ngắn"]):
            rc.append("cửa sổ chuyến đi quá ngắn")
    if co_tu(kh, td["rao_can"]["đi một mình"]):
        rc.append("đi một mình")
    return sorted(set(rc))


# ───────────── nguyên liệu PHÁC HỌA chân dung — bước B3 ──────────────────
# ⛔ Phần này KHÔNG xếp chân dung. Nó chỉ bày ra chữ của khách để agent đọc và
#   phác họa, rồi người dùng duyệt ở CỔNG 0 (id-C §1).

RE_TACH_TU = re.compile(r"[^0-9A-Za-zÀ-ỹ]+")


def _tach_tu(text):
    t = unicodedata.normalize("NFC", (text or "")).lower()
    return [x for x in RE_TACH_TU.split(t) if len(x) > 1]


def cum_chu_khach(cap_ht_text, tu_dung, toi_thieu, lay=60):
    """Cụm 2–3 chữ khách tự nói, đếm theo SỐ HỘI THOẠI chứa cụm.

    ⚠ Đếm theo hội thoại, ⛔ không theo số lần xuất hiện: một người nhắc
    «đầu mũi bóng đỏ» chín lần không làm cụm đó thành tiếng của chín người.
    """
    dem, vi_du = Counter(), defaultdict(list)
    for ma, text in cap_ht_text:
        tu = _tach_tu(text)
        cum = set()
        for k in (2, 3):
            for i in range(len(tu) - k + 1):
                p = tu[i:i + k]
                if p[0] in tu_dung or p[-1] in tu_dung:
                    continue          # bỏ cụm mở/đóng bằng từ dừng
                if all(x in tu_dung for x in p):
                    continue
                cum.add(" ".join(p))
        for c in cum:
            dem[c] += 1
            if len(vi_du[c]) < 6:
                vi_du[c].append(ma)
    ra = [{"cum": c, "so_ht": v, "ht": vi_du[c]} for c, v in dem.most_common() if v >= toi_thieu]
    return ra[:lay]


def nguyen_lieu_chan_dung(ban_ghi, hts, td, ky, nguon):
    n = len(ban_ghi)
    theo_ma = {h["ma"]: h for h in hts}
    tu_dung = set(td.get("_tu_dung") or [])
    toi_thieu = max(3, int(round(n * 0.02)))
    cum = cum_chu_khach([(r["ma"], theo_ma[r["ma"]]["kh_text"]) for r in ban_ghi],
                        tu_dung, toi_thieu)
    cau_dau = []
    for r in ban_ghi:
        tin = theo_ma[r["ma"]]["tin"]
        dau = next((t["text"] for t in tin if not t["nv"] and len(t["text"]) > 3), "")
        cau_dau.append({"ht": r["ma"], "chang": r["chang"], "dich_vu": r["dich_vu"],
                        "tt": r["tt"], "market": r["market"], "ngon_ngu": r["ngon_ngu"],
                        "kenh": r["kenh"], "nhiet": r["nhiet"], "ma_o": r["ma_o"],
                        "ma_oq": r["ma_oq"], "rao_chot": r["rao_chot"],
                        "co_lien_he": r["co_sdt"], "rao_can": r["rao_can"],
                        "cau_dau": an_danh(dau)[:200]})
    return {
        "schema": "nguyen-lieu-chan-dung/1",
        "ky": ky, "nguon": nguon, "so_ht": n,
        "tao": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "muc_dich": "Nguyên liệu để agent PHÁC HỌA chân dung của kỳ (id-C §1). "
                    "⛔ Đây CHƯA phải chân dung.",
        "nguong_cum": toi_thieu,
        "cum_chu": cum,
        "dich_vu": dict(Counter(r["dich_vu"] for r in ban_ghi).most_common()),
        "chang": dict(Counter(r["chang"] for r in ban_ghi)),
        # ★ Ba bảng của bản quốc tế: agent phải thấy khách Ở ĐÂU và nói NGÔN NGỮ gì
        #   trước khi phác họa chân dung (id-C §1 điều ④).
        "tang": dict(Counter(r["tt"] for r in ban_ghi).most_common()),
        "ngon_ngu": dict(Counter(r["ngon_ngu"] for r in ban_ghi).most_common()),
        "kenh": dict(Counter(r["kenh"] for r in ban_ghi).most_common()),
        "rao_can": [{"nhan": a, "so": b} for a, b in
                    Counter(rc for r in ban_ghi for rc in r["rao_can"]).most_common()],
        "cau_dau": cau_dau,
        "ghi_chu": [
            "Cụm chữ đếm theo SỐ HỘI THOẠI chứa cụm, ngưỡng ≥ %d HT." % toi_thieu,
            "Câu đầu đã ẩn danh — số điện thoại, email, link thay bằng «…» (luật ⑩).",
            "⛔ Cụm chữ đông nhất KHÔNG tự thành một chân dung. Chân dung cần một "
            "NỖI SỢ riêng và truy ngược được về HT-nnn — xem id-C §1.",
        ],
    }


# ──────────────────── chấm điểm nhân viên N1–N7 (bản QT) ─────────────────

TIEU_CHI = [
    ("N1", "Phản hồi & SLA", [
        ("N1.1", "Trả lời tin đầu ≤5′ (trong giờ 8–17 ICT)", 6),
        ("N1.2", "Không để khách bỏ sau 1 lượt", 4),
        ("N1.3", "Không bỏ sót câu hỏi của khách", 3),
        ("N1.4", "Theo đuổi lại khi khách im", 2)]),
    ("N2", "Khai thác tình trạng & bối cảnh", [
        ("N2.1", "Hỏi tình trạng trước khi báo giá / xin liên hệ", 7),
        ("N2.2", "Có ≥2 câu hỏi mở", 3),
        ("N2.3", "Mời gửi ảnh / tả vùng cụ thể", 4),
        ("N2.4", "Nhắc lại đúng điều khách vừa nói", 4)]),
    ("N3", "Trả lời đúng & minh bạch", [
        ("N3.1", "Nêu giá khi khách hỏi giá (giá đã công khai)", 5),
        ("N3.2", "Nêu phụ phí quốc tế 10%", 5),
        ("N3.3", "Không cam kết kết quả", 4),
        ("N3.4", "Không nói quá về bác sĩ / chứng chỉ", 3),
        ("N3.5", "Không hứa số ngày ở lại / mốc được bay", 3)]),
    ("N4", "Xử lý rào cản", [
        ("N4.1", "Nhận diện đúng mã O / OQ khách nêu", 5),
        ("N4.2", "Xử đúng RÀO (SỢ/NGỜ/NGẠI/XA)", 6),
        ("N4.3", "Giữ cửa mở", 4)]),
    ("N5", "Xin liên hệ & chốt", [
        ("N5.1", "Xin liên hệ có lý do cụ thể", 5),
        ("N5.2", "Xin lại lần 2 khác cách", 3),
        ("N5.3", "Hỏi khung giờ gọi KÈM MÚI GIỜ", 4),
        ("N5.4", "Mời lịch ngày + giờ + nói rõ giờ Việt Nam", 5)]),
    ("N6", "Ngôn từ & thái độ", [
        ("N6.1", "Không dán khối dài lệch câu hỏi", 2),
        ("N6.2", "Câu đọc hiểu được", 2),
        ("N6.3", "Không gắt, không ép khách", 1)]),
    ("N7", "★ Năng lực quốc tế", [
        ("N7.1", "Hỏi khách đang ở đâu", 2),
        ("N7.2", "Nhận ra đúng tầng và trả lời theo tầng", 2),
        ("N7.3", "Trả lời đúng ngôn ngữ của khách", 2),
        ("N7.4", "Dọn hộp thư ngoài giờ trong 12h", 2),
        ("N7.5", "Hỏi / ghi nhận múi giờ của khách", 1),
        ("N7.6", "Xử đúng câu OQ-01 mà không tự nêu số ngày", 1)]),
]
DIEM = {ma: d for _, _, ds in TIEU_CHI for ma, _, d in ds}


def cham_hoi_thoai(ht, td, ma_o, ma_oq=(), s4=(), lam_o_dau="", an_toan=""):
    """Trả về (bảng ✓/✗/—, điểm 0-100 hoặc None, danh sách cờ đỏ).

    ★ Bản quốc tế sẽ có NHIỀU ô "—" hơn bản nội địa, và đó là ĐÚNG: một hội
      thoại quốc tế điển hình chấm được 12–16 tiêu chí trong 27, không phải cả
      27. Bảy nhóm lỗi hệ ở id-F §7 rào ③ đều chấm "—", ⛔ không chấm "✗".
    """
    k = {}
    tin, kh_text, nv_text = ht["tin"], ht["kh_text"], ht["nv_text"]
    # ★ id-K §4b — hai tinh huong ⛔ KHONG phai co hoi ban. Cham N5/N3 vao day
    # la cham sai VIEC: nhan vien DUNG khi ⛔ khong xin so va ⛔ khong bao gia.
    khong_phai_ban = lam_o_dau.startswith("tai-kn") or an_toan == "cap-tinh"
    tin_kh = [t for t in tin if not t["nv"]]
    tin_nv = [t for t in tin if t["nv"]]
    tg = ht.get("_trong_gio")

    # ── N1
    moc = ht.get("moc_bat_dau") or (tin_kh[0]["tem"] if tin_kh else None)
    if moc and tin_nv:
        tra_loi = next((t for t in tin_nv if phut(moc, t["tem"]) is not None
                        and phut(moc, t["tem"]) >= 0), None)
        if tg is not True:
            # ★ Ngoài khung 8–17 ICT → "—". Trả lời trong 5 phút lúc 3 giờ sáng
            #   ⛔ không phải việc của nhân viên, đó là việc của LỊCH TRỰC.
            #   Phần đó chấm ở N7.4, ⛔ không chấm ở đây (id-L §4).
            k["N1.1"] = "—"
        elif tra_loi is None:
            k["N1.1"] = "✗"
        else:
            k["N1.1"] = "✓" if phut(moc, tra_loi["tem"]) <= SLA_PHUT else "✗"
    else:
        k["N1.1"] = "—"

    k["N1.2"] = "✓" if len(tin_kh) >= 2 else ("✗" if tin_nv else "—")

    hoi = [t for t in tin_kh if "?" in t["text"]
           or co_tu(t["text"], ["how much", "how long", "can i", "do you", "is it",
                                "bao nhiêu", "thế nào", "có không", "được không"])]
    if not hoi:
        k["N1.3"] = "—"
    else:
        tra = sum(1 for h in hoi if any(t["nv"] and phut(h["tem"], t["tem"]) is not None
                                        and phut(h["tem"], t["tem"]) >= 0 for t in tin))
        k["N1.3"] = "✓" if tra >= len(hoi) else "✗"

    duoi = False
    for i, t in enumerate(tin[:-1]):
        if not t["nv"] and tin[i + 1]["nv"]:
            d = phut(t["tem"], tin[i + 1]["tem"])
            if d is not None and d > 30:
                duoi = True
    if tg is not True:
        k["N1.4"] = "—"                       # ngoài giờ → không đòi đuổi theo
    else:
        k["N1.4"] = "✓" if duoi else ("—" if tin[-1]["nv"] else "✗")

    # ── N2
    vt_xin = next((i for i, t in enumerate(tin) if t["nv"] and co_tu(t["text"], td["nv_xin_so"])), None)
    vt_gia = next((i for i, t in enumerate(tin) if t["nv"] and co_tu(t["text"], td["nv_neu_gia"])), None)
    vt_moc = min([x for x in (vt_xin, vt_gia) if x is not None], default=None)
    vt_hoi = next((i for i, t in enumerate(tin) if t["nv"] and co_tu(t["text"], td["nv_hoi_tinh_trang"])), None)
    if vt_moc is None:
        k["N2.1"] = "✓" if vt_hoi is not None else "—"
    else:
        k["N2.1"] = "✓" if (vt_hoi is not None and vt_hoi < vt_moc) else "✗"

    so_hoi = sum(1 for t in tin_nv if "?" in t["text"])
    k["N2.2"] = "✓" if so_hoi >= 2 else "✗"
    k["N2.3"] = "✓" if co_tu(nv_text, td["nv_moi_anh"]) else "✗"

    nhac_lai = False
    for i, t in enumerate(tin[:-1]):
        if not t["nv"] and tin[i + 1]["nv"]:
            tu_kh = [w for w in khong_dau(t["text"]).split() if len(w) >= 4]
            if sum(1 for w in tu_kh if w in khong_dau(tin[i + 1]["text"])) >= 2:
                nhac_lai = True
    k["N2.4"] = "✓" if nhac_lai else "✗"

    # ── N3
    # ★ NGƯỢC HẲN BẢN NỘI ĐỊA: giá đã công khai tại /price-list/ (id-K §3③),
    #   nên né giá là LỖI NGƯỜI, ⛔ không còn là lỗi hệ.
    #   Ngoại lệ duy nhất chấm "—": dịch vụ khách hỏi không có trong bảng giá
    #   công khai → "bác sĩ chốt sau khám" là câu ĐẠT, cần người đối chiếu.
    co_neu_gia = co_tu(nv_text, td["nv_neu_gia"])
    if khong_phai_ban:
        # ★ id-K §4b — ⛔ KHONG bao gia la DUNG o ca khieu nai / ca co dau
        #   hieu an toan. ⛔ Khong tru diem ai vi viec do.
        k["N3.1"] = "—"
    elif "O-01" in ma_o:
        k["N3.1"] = "✓" if co_neu_gia else "✗"
    else:
        k["N3.1"] = "—"
    # ★ N3.2 — tiêu chí mới quan trọng nhất của nhóm. Bỏ dòng 10% là BOM NIỀM TIN:
    #   khách phát hiện ở quầy thanh toán thì mất cả ca VÀ nhận một review xấu.
    co_phu_phi = co_tu(nv_text, td["nv_phu_phi_10"])
    k["N3.2"] = "—" if khong_phai_ban else (("✓" if co_phu_phi else "✗") if co_neu_gia else "—")

    co_do = []
    for ma, tu in td["co_do"].items():
        if ma.startswith("_"):
            continue
        if co_tu(nv_text, tu):
            co_do.append({"ma": ma, "trich": (tu_khop(nv_text, tu) or [""])[0]})
    # ★ CĐ-7 nhận bằng LOGIC, không bằng từ khoá: có nêu giá mà không nêu phụ phí.
    if co_neu_gia and not co_phu_phi:
        co_do.append({"ma": "CĐ-7", "trich": "nêu giá mà không nêu phụ phí quốc tế 10%"})
    # ★ CĐ-4 nhận bằng LOGIC: gắn tên một bác sĩ KHÔNG có trong danh sách được
    #   duyệt cho site quốc tế. Cổng ① của id-K §3④: site nội địa và site quốc tế
    #   ⛔ KHÔNG trùng danh sách, và nhân sự ở site nội địa ⛔ không tự động dùng
    #   được cho khách quốc tế.
    for ten_bs in bac_si_la(nv_text, td):
        co_do.append({"ma": "CĐ-4",
                      "trich": "gắn bác sĩ «%s» — ngoài danh sách site quốc tế" % ten_bs})

    def co(ma):
        return any(c["ma"] == ma for c in co_do)

    k["N3.3"] = "✗" if co("CĐ-1") else "✓"
    k["N3.4"] = "✗" if co("CĐ-4") else "✓"
    k["N3.5"] = "✗" if co("CĐ-5") else ("✓" if "OQ-01" in ma_oq else "—")

    # ── N4
    if not [m for m in ma_o if m != "O-00"] and not ma_oq:
        k["N4.1"] = k["N4.2"] = k["N4.3"] = "—"
    else:
        k["N4.1"] = "✓" if len(nv_text) > 120 else "✗"
        # ★ Lỗi gỡ sai rào phổ biến nhất của bản quốc tế: khách hỏi rào XA
        #   ("bao nhiêu ngày") mà nhân viên trả lời bằng GIÁ / ƯU ĐÃI.
        #   Đây là tiêu chí trượt nhiều THỨ HAI của bản này (id-D §6).
        rao = gan_rao_chot(ma_o, ma_oq)
        if rao == "XA":
            k["N4.2"] = "✗" if (co_neu_gia and not co_tu(
                nv_text, td["nv_hoan_so_ngay"] + ["interpreter", "days", "ngày", "phiên dịch",
                                                  "airport", "hotel", "visa"])) else "✓"
        elif rao == "NGẠI" and "O-01" in ma_o:
            k["N4.2"] = "✓" if co_tu(nv_text, td["nv_neu_gia"] + ["installment", "trả góp"]) else "✗"
        else:
            k["N4.2"] = "✓" if len(nv_text) > 120 else "✗"
        k["N4.3"] = "✓" if co_tu(nv_text, td["nv_giu_cua_mo"]) else "✗"

    # ── N5
    xin = [t for t in tin_nv if co_tu(t["text"], td["nv_xin_so"])]
    if khong_phai_ban:
        # ★ Cham nhan vien vi "⛔ khong xin duoc so" trong mot ca khieu nai
        #   hoac mot ca co dau hieu an toan la CHAM SAI VIEC (id-K §4b).
        k["N5.1"] = k["N5.2"] = k["N5.3"] = k["N5.4"] = "—"
    elif not xin:
        k["N5.1"] = k["N5.2"] = "✗"
    else:
        k["N5.1"] = "✓" if co_tu(xin[0]["text"], td["nv_ly_do_xin_so"]) else "✗"
        k["N5.2"] = "✓" if len(xin) >= 2 and khong_dau(xin[0]["text"]) != khong_dau(xin[1]["text"]) else "✗"
    # ★ Hỏi giờ mà KHÔNG hỏi múi giờ = ✗: giờ không có múi giờ là một con số
    #   vô dụng, và cuộc gọi đó đơn giản là không diễn ra.
    if not khong_phai_ban:
        k["N5.3"] = "✓" if co_tu(nv_text, td["nv_khung_gio"]) else "✗"
        k["N5.4"] = "✓" if (co_tu(nv_text, td["nv_moi_lich"])
                            and re.search(r'\d{1,2}\s*[hg:apm]', nv_text, re.I)) else "✗"

    # ── N6
    dai = [t for t in tin_nv if len(t["text"]) > 400]
    k["N6.1"] = "✗" if len(dai) >= 2 else "✓"
    # ⚠ Chấm TÍNH DỄ HIỂU, ⛔ KHÔNG chấm ngữ pháp/văn phong tiếng Anh (id-L §3).
    #   Dấu hiệu dịch máy thô cho nội dung y khoa là cờ đỏ CĐ-9, không phải điểm trừ.
    k["N6.2"] = "✗" if co("CĐ-9") else "✓"
    k["N6.3"] = "✗" if co("CĐ-6") else "✓"

    # ── N7 · ★ nhóm của bản quốc tế
    da_biet_nuoc = bool(ht.get("nuoc_khai")) or ht.get("_can_cu_tt") == "khách tự nói"
    if da_biet_nuoc:
        k["N7.1"] = "✓"
    elif co_tu(nv_text, td["nv_hoi_o_dau"]):
        k["N7.1"] = "✓"
    else:
        # ⚠ Chỉ tính là trượt khi khách đã nhắn ≥4 lượt mà vẫn không ai hỏi.
        k["N7.1"] = "✗" if len(tin_kh) >= 4 else "—"

    tt = ht.get("_tt")
    if tt == "TT-D":
        # Nói đưa đón sân bay / khách sạn với người ĐANG SỐNG ở Hà Nội là chưa
        # nhận ra tầng.
        k["N7.2"] = "✗" if co_tu(nv_text, ["airport pickup", "airport transfer",
                                           "hotel recommendation", "đưa đón sân bay"]) else "✓"
    elif tt in ("TT-A", "TT-B", "TT-C"):
        k["N7.2"] = "✗" if co_tu(nv_text, ["come to the clinic today", "qua viện hôm nay",
                                           "mời chị qua viện ngay"]) else "✓"
    else:
        k["N7.2"] = "—"

    nn, nn_nv = ht.get("_ngon_ngu"), ht.get("_ngon_ngu_nv")
    if not nn_nv or "XX" in (nn, nn_nv):
        k["N7.3"] = "—"
    else:
        k["N7.3"] = "✓" if nn == nn_nv else "✗"

    if tg is False:
        ch = cho_bao_lau(ht)
        if ch is None:
            k["N7.4"] = "✗"                   # ngoài giờ mà KHÔNG AI trả lời
        else:
            k["N7.4"] = "✓" if ch <= SLA_NGOAI_GIO_GIO else "✗"
        if co_tu(nv_text, td["nv_xin_loi_lech_gio"]) and k["N7.4"] == "✓":
            pass
    else:
        k["N7.4"] = "—"                       # trong giờ → tiêu chí không phát sinh

    k["N7.5"] = "✓" if co_tu(nv_text, td["nv_khung_gio"] + td["tin_hieu_nong"]["5_khung_gio"]) else "✗"

    # ★ N7.6 ⛔ KHÔNG đo "nhân viên có biết số ngày hay không" — họ không thể
    #   biết, vì chưa ai cấp. Nó đo CÁCH XỬ LÝ một câu hỏi mình chưa có đáp án.
    if "OQ-01" not in ma_oq:
        k["N7.6"] = "—"
    elif co("CĐ-5"):
        k["N7.6"] = "✗"                       # tự nghĩ ra một con số
    elif co_tu(nv_text, td["nv_hoan_so_ngay"]):
        k["N7.6"] = "✓"                       # nói đúng kiểu "bác sĩ xác nhận sau khám"
    else:
        k["N7.6"] = "✗"                       # im lặng / lái sang giá

    tu_so = sum(DIEM[m] for m, v in k.items() if v == "✓")
    mau_so = sum(DIEM[m] for m, v in k.items() if v in ("✓", "✗"))
    diem = round(tu_so / mau_so * 100, 1) if mau_so else None
    if co_do and diem is not None:
        diem = min(diem, 49.0)           # id-F §4: có cờ đỏ → trần 49
    return k, diem, co_do


RE_BAC_SI = re.compile(r"\b(?:Dr\.?|Doctor|BS\.?|Bác sĩ)\s+"
                       r"((?:[A-ZÀ-Ỹ][\wÀ-ỹ-]*\s*){1,4})")


def bac_si_la(nv_text, td):
    """Tên bác sĩ bot/nhân viên nêu mà KHÔNG có trong danh sách duyệt quảng bá QT.

    ⚠ So theo HỌ+TÊN đã bỏ dấu, nên "Louis Trương" và "Louis Truong" là một.
      Danh sách duyệt nằm ở tu_dien.json → `bac_si_duyet_qt` (id-K §3④).
    """
    duyet = [khong_dau(x) for x in td.get("bac_si_duyet_qt", [])]
    ra = []
    for m in RE_BAC_SI.finditer(nv_text or ""):
        ten = re.sub(r'\s+', ' ', m.group(1)).strip(" .,;:")
        if not ten or len(ten) < 3:
            continue
        kd = khong_dau(ten)
        if any(kd in d or d in kd for d in duyet):
            continue
        if ten not in ra:
            ra.append(ten)
    return ra[:3]


def xep_loai(diem, so_ht, co_do):
    if so_ht < MAU_TOI_THIEU_NV or diem is None:
        return "chưa đủ mẫu"
    if co_do:
        return "B" if diem >= 70 else ("C" if diem >= 55 else "D")
    return "A" if diem >= 85 else ("B" if diem >= 70 else ("C" if diem >= 55 else "D"))


# ───────────────────────────── lệnh `doc` ────────────────────────────────

def lenh_doc(args):
    td = nap_tu_dien()
    hts = doc_hoi_thoai(args.file)
    if not hts:
        sys.exit("⛔ Không đọc được hội thoại nào.")

    pho, vi_sao = nap_phac_hoa(args.ky)

    ban_ghi, co_do_all, ngoai_pv = [], [], []
    for ht in hts:
        # ★ Thứ tự bắt buộc: ngôn ngữ → tầng → kênh → giờ ICT. Mọi hàm sau đó
        #   đọc lại từ bốn ô này, ⛔ không tự suy lại (luật MỘT LẦN CHẤM).
        ht["_ngon_ngu"] = gan_ngon_ngu(ht, td)
        ht["_ngon_ngu_nv"] = gan_ngon_ngu_nv(ht, td)
        ht["_kenh"] = gan_kenh(ht, td)
        tt, market, can_cu = gan_tt(ht, td)
        ht["_tt"], ht["_market"], ht["_can_cu_tt"] = tt, market, can_cu
        ht["_trong_gio"] = trong_gio(ht)

        # ★ Khách NỘI ĐỊA nhắn lạc vào kênh quốc tế → loại khỏi mẫu phân tích,
        #   ⛔ KHÔNG xếp vào TT-B (id-B §3).
        if ngoai_pham_vi(ht, td):
            ngoai_pv.append(ht["ma"])
            continue

        cd = gan_chan_dung(ht, pho)          # None khi chưa qua CỔNG 0
        chang = gan_chang(ht, td)
        ma_oq = gan_ma_oq(ht, td)
        ma_o = gan_ma_o(ht, td, ma_oq)
        rao_chot = gan_rao_chot(ma_o, ma_oq)
        s4 = s4_chua_dong(ht, td, ma_oq)
        nhiet, tin_hieu = gan_nhiet(ht, td)
        lam_o_dau = gan_lam_o_dau(ht, td)
        an_toan = co_dau_hieu_an_toan(ht, td)
        k, diem, co_do = cham_hoi_thoai(ht, td, ma_o, ma_oq, s4, lam_o_dau, an_toan)
        ht["chot_lich"] = bool(co_tu(ht["nv_text"], td["nv_moi_lich"])
                               and co_tu(ht["kh_text"], td["kh_dong_y_lich"]))
        roi = gan_vi_sao_roi(ht, td, diem, ma_oq, s4)
        rc = gan_rao_can(ht, td, ma_o, ma_oq)
        for c in co_do:
            co_do_all.append({"ma": c["ma"], "nguoi": ht["nv"], "ht": ht["ma"], "trich": c["trich"]})
        ban_ghi.append({
            "ma": ht["ma"], "nv": ht["nv"], "cd": cd, "chang": chang,
            "ma_o": ma_o, "ma_oq": ma_oq, "rao_chot": rao_chot, "s4_chua_dong": s4,
            "lam_o_dau": lam_o_dau, "dau_hieu_an_toan": an_toan,
            "tt": tt, "market": market, "can_cu_tt": can_cu,
            "ngon_ngu": ht["_ngon_ngu"], "ngon_ngu_nv": ht["_ngon_ngu_nv"],
            "kenh": ht["_kenh"], "trong_gio": ht["_trong_gio"], "cho_gio": cho_bao_lau(ht),
            "nhiet": nhiet, "tin_hieu": tin_hieu, "co_sdt": ht["co_sdt"],
            "chot_lich": ht["chot_lich"], "roi": roi, "rao_can": rc,
            "dich_vu": gan_dich_vu(ht, td), "he_so": he_so_gia_tri(ht, td, tt),
            "diem": diem, "cham": k, "co_do": [c["ma"] for c in co_do],
            "so_luot_kh": sum(1 for t in ht["tin"] if not t["nv"]),
        })

    n = len(ban_ghi)
    if not n:
        sys.exit("⛔ Không còn hội thoại nào sau khi loại %d HT ngoài phạm vi quốc tế."
                 % len(ngoai_pv))
    os.makedirs(RA, exist_ok=True)

    # bảng chấm từng hội thoại
    with open(os.path.join(RA, "cham-hoi-thoai.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        cot = [m for _, _, ds in TIEU_CHI for m, _, _ in ds]
        w.writerow(["ma", "nv", "tt", "market", "can_cu_tt", "ngon_ngu", "ngon_ngu_nv",
                    "kenh", "trong_gio", "cho_gio", "cd", "chang", "ma_o", "ma_oq",
                    "rao_chot", "s4_chua_dong", "lam_o_dau", "dau_hieu_an_toan", "nhiet", "co_lien_he", "chot_lich",
                    "vi_sao_roi", "rao_can", "dich_vu", "he_so", "diem", "co_do"] + cot)
        for r in ban_ghi:
            w.writerow([r["ma"], r["nv"], r["tt"], r["market"] or "", r["can_cu_tt"],
                        r["ngon_ngu"], r["ngon_ngu_nv"] or "", r["kenh"],
                        "" if r["trong_gio"] is None else ("Có" if r["trong_gio"] else "Không"),
                        r["cho_gio"] if r["cho_gio"] is not None else "",
                        r["cd"], r["chang"], " ".join(r["ma_o"]), " ".join(r["ma_oq"]),
                        r["rao_chot"] or "", " ".join(r["s4_chua_dong"]),
                        r["lam_o_dau"], r["dau_hieu_an_toan"], r["nhiet"],
                        "Có" if r["co_sdt"] else "", "Có" if r["chot_lich"] else "",
                        r["roi"], " · ".join(r["rao_can"]), r["dich_vu"], r["he_so"],
                        r["diem"] if r["diem"] is not None else "", " ".join(r["co_do"])]
                       + [r["cham"].get(c, "") for c in cot])

    # tổng hợp nhân viên
    theo_nv = defaultdict(list)
    for r in ban_ghi:
        theo_nv[r["nv"]].append(r)
    ca_nhan = []
    for nv, rs in sorted(theo_nv.items(), key=lambda x: -len(x[1])):
        ds = [r["diem"] for r in rs if r["diem"] is not None]
        d = round(sum(ds) / len(ds), 1) if ds else None
        cds = sorted({c for r in rs for c in r["co_do"]})
        yeu = min(TIEU_CHI, key=lambda g: _pct_nhom(rs, g[0]) if _pct_nhom(rs, g[0]) is not None else 999)
        manh = max(TIEU_CHI, key=lambda g: _pct_nhom(rs, g[0]) if _pct_nhom(rs, g[0]) is not None else -1)
        ca_nhan.append({"ten": nv, "ht": len(rs), "diem": d,
                        "loai": xep_loai(d, len(rs), cds),
                        "yeu_nhat": yeu[0], "manh_nhat": manh[0], "co_do": cds})

    # chỉ số nhóm toàn khối
    nhom = []
    for ma, ten, ds in TIEU_CHI:
        tc = []
        for m, t, d in ds:
            dat = sum(1 for r in ban_ghi if r["cham"].get(m) == "✓")
            chua = sum(1 for r in ban_ghi if r["cham"].get(m) == "✗")
            kad = sum(1 for r in ban_ghi if r["cham"].get(m) == "—")
            tc.append({"ma": m, "ten": t, "diem": d, "dat": dat, "chua": chua,
                       "khong_ap_dung": kad, "pct_dat": pct(dat, dat + chua)})
        nhom.append({"ma": ma, "ten": ten, "diem_toi_da": sum(d for _, _, d in ds),
                     "pct_dat": _pct_nhom(ban_ghi, ma), "tieu_chi": tc})

    ket = {
        "ky": args.ky, "so_ht": n, "nguon": os.path.basename(args.file),
        "tao": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "nhiet": dict(Counter(r["nhiet"] for r in ban_ghi)),
        "nhiet_x_sdt": [{"muc": m,
                         "chua": sum(1 for r in ban_ghi if r["nhiet"] == m and not r["co_sdt"]),
                         "co": sum(1 for r in ban_ghi if r["nhiet"] == m and r["co_sdt"])}
                        for m in ("HOT", "WARM", "COLD")],
        "tin_hieu": [{"nhan": t, "so": sum(1 for r in ban_ghi if t in r["tin_hieu"])}
                     for t in ("1_dich_vu", "2_cua_so_chuyen_di", "3_lien_he",
                               "4_dieu_kien", "5_khung_gio")],
        "nguyen_nhan_roi": dict(Counter(r["roi"] for r in ban_ghi)),
        "rao_can": [{"nhan": k2, "so": v} for k2, v in
                    Counter(rc for r in ban_ghi for rc in r["rao_can"]).most_common()],
        "ma_o": [{"ma": m, "so": sum(1 for r in ban_ghi if m in r["ma_o"]),
                  "pct": pct(sum(1 for r in ban_ghi if m in r["ma_o"]), n)}
                 for m in ["O-%02d" % i for i in range(1, 13)] + ["O-00", "(chưa nêu)"]],
        # ★ Tám mã chỉ có ở khách quốc tế — in CẢ mã bằng 0 (id-D §11)
        "ma_oq": [{"ma": m, "so": sum(1 for r in ban_ghi if m in r["ma_oq"]),
                   "pct": pct(sum(1 for r in ban_ghi if m in r["ma_oq"]), n),
                   "trang_thai_chan": MA_OQ_CHAN.get(m, "")}
                  for m in ["OQ-%02d" % i for i in range(1, 9)]],
        "rao_chot": {x: sum(1 for r in ban_ghi if r["rao_chot"] == x)
                     for x in ("SỢ", "NGỜ", "NGẠI", "XA")},
        "chang": {x: sum(1 for r in ban_ghi if r["chang"] == x)
                  for x in ("S1", "S2", "S3", "S4", "S5", "S6", "S7", "chưa rõ")},
        "s4_chua_dong": {
            "so": sum(1 for r in ban_ghi if r["s4_chua_dong"]),
            "cau": {c: sum(1 for r in ban_ghi if c in r["s4_chua_dong"])
                    for c in ("1_so_ngay", "2_ai_lo", "3_ai_tra_phi", "4_ngon_ngu")}},
        "thi_truong": _khoi_thi_truong(ban_ghi, ngoai_pv),
        "phac_hoa": {
            "trang_thai": "da_duyet" if pho else "chua_phac_hoa",
            "vi_sao": vi_sao,
            "file": "out/chan-dung.json",
            "nguyen_lieu": "out/nguyen-lieu-chan-dung.json",
            "so_chan_dung": len(pho["tep"]) if pho else 0,
            "duyet_boi": (pho or {}).get("duyet_boi"),
            "duyet_luc": (pho or {}).get("duyet_luc"),
        },
        "chan_dung": _bang_chan_dung(ban_ghi, pho),
        "ngoai_pham_vi": ngoai_pv,
        "nhan_vien": {"phan_bo": dict(Counter(c["loai"] for c in ca_nhan)),
                      "nhom": nhom, "ca_nhan": ca_nhan, "co_do": co_do_all,
                      "ghi_chu": "Điểm dùng để phân việc kèm cặp. "
                                 "Không phải căn cứ kỷ luật hay xếp hạng công khai."},
        "the_tong": _the_tong(ban_ghi),
    }
    with open(os.path.join(RA, "doc-hoi-thoai.json"), "w", encoding="utf-8") as f:
        json.dump(ket, f, ensure_ascii=False, indent=1)

    # Nguyên liệu phác họa ghi lại MỖI LẦN chạy: kỳ sau chân dung có thể khác,
    # và bản phác họa cũ phải đối chiếu được với chữ của khách kỳ này.
    nl = nguyen_lieu_chan_dung(ban_ghi, hts, td, args.ky, os.path.basename(args.file))
    with open(NGUYEN_LIEU, "w", encoding="utf-8") as f:
        json.dump(nl, f, ensure_ascii=False, indent=1)

    _in_tom_tat(ket, ban_ghi, nl)


# ★ Trạng thái chặn của tám mã OQ (id-D §2). Sáu trong tám mã đang bị chặn vì
#   THIẾU DỮ KIỆN GỐC — trực kênh né những câu này phần lớn là LỖI HỆ.
MA_OQ_CHAN = {
    "OQ-01": "🔴 CHẶN — chưa có số ngày ở lại (Khoa Chuyên môn)",
    "OQ-02": "🟠 thiếu thời hạn + kênh của chăm sóc sau khi về",
    "OQ-03": "🟠 chưa khai ngôn ngữ nào · có phí không",
    "OQ-04": "🔴 CHẶN — chưa có T&C bảo hành (Pháp chế)",
    "OQ-05": "🟠 không thấy trên site — Điều phối QT",
    "OQ-06": "🟠 không thấy trên site — rào cản chốt thật",
    "OQ-07": "🟢 có nêu — xác nhận miễn phí hay tính phí",
    "OQ-08": "🟠 site ghi Muslim-Friendly mà chưa khai gồm những gì",
}


def _khoi_thi_truong(ban_ghi, ngoai_pv):
    """★ Khối dữ liệu của tab ② — bốn bảng cắt bắt buộc của id-L §8.

    ⚠ Tầng dưới TANG_TOI_THIEU HT thì ô tỷ lệ để None: dashboard hiện
      «⚠ MẪU NHỎ», ⛔ không hiện một con số không ai dám dùng (id-J §3 luật ⑤).
    """
    n = len(ban_ghi)
    tang = []
    for tt in ("TT-A", "TT-B", "TT-C", "TT-D", TT_DU):
        rs = [r for r in ban_ghi if r["tt"] == tt]
        du = len(rs) >= TANG_TOI_THIEU
        mk = sorted({r["market"] for r in rs if r["market"]})
        nn = Counter(r["ngon_ngu"] for r in rs).most_common(1)
        tang.append({
            "tt": tt, "ten": TEN_TT[tt], "ht": len(rs), "pct": pct(len(rs), n),
            "hot": sum(1 for r in rs if r["nhiet"] == "HOT"),
            "warm": sum(1 for r in rs if r["nhiet"] == "WARM"),
            "cold": sum(1 for r in rs if r["nhiet"] == "COLD"),
            "co_lh": sum(1 for r in rs if r["co_sdt"]),
            "pct_lh": pct(sum(1 for r in rs if r["co_sdt"]), len(rs)) if du else None,
            "roi_truc": sum(1 for r in rs if r["roi"] == "trực kênh"),
            "s4_chua_dong": sum(1 for r in rs if r["s4_chua_dong"]),
            "ngon_ngu_chinh": nn[0][0] if nn else None,
            "market": mk,
            "du_mau": du,
        })

    ngoai = [r for r in ban_ghi if r["trong_gio"] is False]
    cho = [r["cho_gio"] for r in ngoai if r["cho_gio"] is not None]
    pct_tt0 = pct(sum(1 for r in ban_ghi if r["tt"] == TT_DU), n) or 0

    return {
        "nguon_suy": dict(Counter(r["can_cu_tt"] for r in ban_ghi)),
        "cong_m": {
            "pct_tt0": pct_tt0,
            "nguong": TT_NGUONG_CONG_M,
            "can_xac_nhan": pct_tt0 >= TT_NGUONG_CONG_M,
            "ghi_chu": "⚠ TT-0 ≥ %g%% mẫu → CỔNG M: in bảng căn cứ suy và chờ người "
                       "dùng xác nhận trước khi kết luận (id-L §1)." % TT_NGUONG_CONG_M},
        "tang": tang,
        "ngon_ngu": [{"kh": a, "nv": b, "so": c} for (a, b), c in
                     Counter((r["ngon_ngu"], r["ngon_ngu_nv"] or "—")
                             for r in ban_ghi).most_common()],
        "kenh": [{"ten": k2, "ht": v,
                  "pct_lh": pct(sum(1 for r in ban_ghi if r["kenh"] == k2 and r["co_sdt"]), v),
                  "truy_duoc_ads": k2 in ("Messenger", "WhatsApp")}
                 for k2, v in Counter(r["kenh"] for r in ban_ghi).most_common()],
        "mui_gio": {
            "trong_gio": sum(1 for r in ban_ghi if r["trong_gio"] is True),
            "ngoai_gio": len(ngoai),
            "pct_ngoai_gio": pct(len(ngoai), n),
            "cho_tb_gio": round(sum(cho) / len(cho), 1) if cho else None,
            "mat_qua_12h": sum(1 for x in cho if x > SLA_NGOAI_GIO_GIO),
            "theo_tang": [{"tt": tt,
                           "ngoai_gio": sum(1 for r in ngoai if r["tt"] == tt),
                           "cho_tb_gio": (round(sum(x["cho_gio"] for x in ngoai
                                                    if x["tt"] == tt and x["cho_gio"] is not None)
                                                / max(1, sum(1 for x in ngoai if x["tt"] == tt
                                                             and x["cho_gio"] is not None)), 1)
                                          if any(x["tt"] == tt and x["cho_gio"] is not None
                                                 for x in ngoai) else None)}
                          for tt in ("TT-A", "TT-B", "TT-C", "TT-D", TT_DU)],
            "ghi_chu": "Tin đến ngoài khung 8–17 ICT → N1.1 chấm «—», ⛔ không phải ✗. "
                       "Phần dọn hộp thư ngoài giờ chấm ở N7.4 (id-L §4)."},
        "ngoai_pham_vi": {"so": len(ngoai_pv), "ht": ngoai_pv,
                          "ghi_chu": "Khách nội địa nhắn lạc vào kênh quốc tế — đã loại "
                                     "khỏi mẫu, ⛔ không xếp vào TT-B (id-B §3)."},
    }


def _pct_nhom(rs, ma_nhom):
    ds = [m for g, _, lst in TIEU_CHI if g == ma_nhom for m, _, _ in lst]
    dat = sum(1 for r in rs for m in ds if r["cham"].get(m) == "✓")
    chua = sum(1 for r in rs for m in ds if r["cham"].get(m) == "✗")
    return pct(dat, dat + chua)


def _bang_chan_dung(ban_ghi, pho):
    """Bảng chân dung dựng theo bản phác họa ĐÃ DUYỆT.

    ⛔ Chưa qua CỔNG 0 → trả về bảng RỖNG. Script không có chân dung mặc định
    nào để điền vào, và không được bịa ra dòng nào.
    """
    if not pho:
        return []
    dong = [_dong_cd(ban_ghi, c["ma"], (c.get("ten") or c["ma"]), c) for c in pho["tep"]]
    dong.append(_dong_cd(ban_ghi, CD_DU, TEN_CD_DU, None))
    return dong


def _dong_cd(ban_ghi, cd, ten, dn):
    rs = [r for r in ban_ghi if r["cd"] == cd]
    hs = (dn or {}).get("he_so_gia_tri")
    tt = Counter(r["tt"] for r in rs).most_common(1)
    return {"cd": cd, "ten": ten, "ht": len(rs), "quan_sat": len(rs) < 5,
            "hot": sum(1 for r in rs if r["nhiet"] == "HOT"),
            "warm": sum(1 for r in rs if r["nhiet"] == "WARM"),
            "cold": sum(1 for r in rs if r["nhiet"] == "COLD"),
            "co_lh": sum(1 for r in rs if r["co_sdt"]),
            "chot_lich": sum(1 for r in rs if r["chot_lich"]),
            "bo_1_luot": sum(1 for r in rs if r["so_luot_kh"] <= 1),
            "roi_truc": sum(1 for r in rs if r["roi"] == "trực kênh"),
            "s4_chua_dong": sum(1 for r in rs if r["s4_chua_dong"]),
            # ★ Tầng đông nhất của chân dung + rào chốt khai trong bản phác họa.
            #   ⚠ Chân dung trải đều trên 3–4 tầng là dấu hiệu phác họa chưa tới (id-C §1).
            "tt": (dn or {}).get("tt") or ([tt[0][0]] if tt else []),
            "rao_chot": (dn or {}).get("rao_chot"),
            "rang_buoc_chuyen_di": (dn or {}).get("rang_buoc_chuyen_di"),
            "he_so": hs or max([r["he_so"] for r in rs], default=1)}


def _the_tong(ban_ghi):
    n = len(ban_ghi)
    bo1 = sum(1 for r in ban_ghi if r["so_luot_kh"] <= 1)
    lh = sum(1 for r in ban_ghi if r["co_sdt"])
    sla = [r for r in ban_ghi if r["cham"].get("N1.1") in ("✓", "✗")]
    nong_chua = sum(1 for r in ban_ghi if r["nhiet"] in ("HOT", "WARM") and not r["co_sdt"])
    roi_truc = sum(1 for r in ban_ghi if r["roi"] == "trực kênh")
    s4 = sum(1 for r in ban_ghi if r["s4_chua_dong"])
    nong_ngoai = sum(1 for r in ban_ghi
                     if r["nhiet"] in ("HOT", "WARM") and r["trong_gio"] is False
                     and (r["cho_gio"] is None or r["cho_gio"] > SLA_NGOAI_GIO_GIO))
    return [
        {"id": "ht", "nhan": "Hội thoại phân tích", "gia_tri": n, "kieu": "n"},
        {"id": "bo_1", "nhan": "Bỏ sau 1 lượt", "gia_tri": pct(bo1, n), "kieu": "pct",
         "tot": "thap", "phu": "%d/%d HT" % (bo1, n)},
        {"id": "co_lh", "nhan": "Có cách liên hệ", "gia_tri": pct(lh, n), "kieu": "pct",
         "tot": "cao", "phu": "%d/%d HT — số có mã quốc gia · WhatsApp · email" % (lh, n)},
        {"id": "sla", "nhan": "Trả lời tin đầu ≤5′", "gia_tri":
            pct(sum(1 for r in sla if r["cham"]["N1.1"] == "✓"), len(sla)), "kieu": "pct",
         "tot": "cao", "phu": "chỉ tính tin đến trong 8–17 ICT (%d/%d HT)" % (len(sla), n)},
        {"id": "nong_chua_lh", "nhan": "HOT/WARM chưa có liên hệ", "gia_tri": nong_chua,
         "kieu": "n", "tot": "thap", "phu": "lead nóng chưa vào tay ai"},
        # ★★ Thẻ đặc trưng của bản quốc tế: đo đúng chỗ khách ĐÃ MUỐN LÀM mà
        #    KHÔNG BAY ĐƯỢC. Không thẻ nào khác trong hệ đo được điều đó.
        {"id": "s4_chua_dong", "nhan": "S4 chưa đóng", "gia_tri": s4, "kieu": "n",
         "tot": "thap",
         "phu": "HT chạm rào XA mà bốn câu của id-D §6.1 chưa được trả lời đủ"},
        {"id": "nong_ngoai_gio", "nhan": "HOT/WARM ngoài giờ chờ >12h", "gia_tri": nong_ngoai,
         "kieu": "n", "tot": "thap",
         "phu": "lead nóng mất vì LỊCH TRỰC, ⛔ không vì năng lực — việc hệ thống"},
        {"id": "roi_truc", "nhan": "Rơi do trực kênh", "gia_tri": pct(roi_truc, n),
         "kieu": "pct", "tot": "thap",
         "phu": "%d/%d HT — câu trả lời của trực kênh làm khách dừng" % (roi_truc, n)},
    ]


def _in_tom_tat(k, ban_ghi, nl):
    p = print
    p("")
    p("═" * 66)
    p("  ĐỌC HỘI THOẠI · kỳ %s · %d hội thoại · nguồn %s" % (k["ky"], k["so_ht"], k["nguon"]))
    p("═" * 66)
    p("")
    p("  THẺ SỐ TỔNG")
    for t in k["the_tong"]:
        v = t["gia_tri"]
        p("    %-26s %s%s" % (t["nhan"], "—" if v is None else v,
                              "%" if t["kieu"] == "pct" and v is not None else ""))
    p("")
    T = k["thi_truong"]
    p("  ★ TẦNG THỊ TRƯỜNG — CỔNG M")
    p("    %-6s %-24s %4s %6s %4s %4s %6s %5s" %
      ("tầng", "tên", "HT", "%mẫu", "HOT", "LH", "%LH", "S4"))
    for x in T["tang"]:
        p("    %-6s %-24s %4d %5s%% %4d %4d %6s %5d%s" % (
            x["tt"], x["ten"][:24], x["ht"], x["pct"], x["hot"], x["co_lh"],
            ("%s%%" % x["pct_lh"]) if x["pct_lh"] is not None else "⚠ nhỏ",
            x["s4_chua_dong"], "" if x["du_mau"] else "  ⚠ MẪU NHỎ"))
    p("    căn cứ suy: " + " · ".join("%s %d" % (a, b) for a, b in T["nguon_suy"].items()))
    if T["cong_m"]["can_xac_nhan"]:
        p("")
        p("    ⛔ CỔNG M — TT-0 chiếm %s%% mẫu (ngưỡng %g%%)." % (T["cong_m"]["pct_tt0"],
                                                                 T["cong_m"]["nguong"]))
        p("       Trực kênh KHÔNG hỏi khách đang ở đâu. Đây là lỗi HỆ (lời chào/form)")
        p("       + lỗi KỸ NĂNG (tiêu chí N7.1) — đẩy lên CẢ HAI chỗ (id-L §1).")
        p("       ⛔ Chưa xác nhận bảng này thì chưa kết luận gì về các tỷ lệ bên dưới.")
    if T["ngoai_pham_vi"]["so"]:
        p("    ⚠ %d HT khách nội địa nhắn lạc — đã loại, ⛔ không xếp vào TT-B."
          % T["ngoai_pham_vi"]["so"])
    p("")
    mg = T["mui_gio"]
    p("  ★ MÚI GIỜ   trong giờ %d · ngoài giờ %d (%s%%) · chờ TB %s h · mất >12h: %d"
      % (mg["trong_gio"], mg["ngoai_gio"], mg["pct_ngoai_gio"],
         mg["cho_tb_gio"] if mg["cho_tb_gio"] is not None else "—", mg["mat_qua_12h"]))
    p("  ★ KÊNH      " + " · ".join("%s %d%s" % (x["ten"], x["ht"],
                                                 "" if x["truy_duoc_ads"] else " (⛔ không truy được ads)")
                                    for x in T["kenh"][:5]))
    p("  ★ CHẶNG     " + " · ".join("%s %d" % (a, b) for a, b in k["chang"].items() if b))
    p("  ★ RÀO CHỐT  " + " · ".join("%s %d" % (a, b) for a, b in k["rao_chot"].items()))
    p("")
    p("  MỨC NÓNG   " + " · ".join("%s %d" % (m, k["nhiet"].get(m, 0)) for m in ("HOT", "WARM", "COLD")))
    p("  VÌ SAO RƠI " + " · ".join("%s %d" % (a, b) for a, b in
                                   sorted(k["nguyen_nhan_roi"].items(), key=lambda x: -x[1])))
    p("")
    if k["chan_dung"]:
        p("  CHÂN DUNG — theo bản phác họa đã duyệt (%s · %s)"
          % (k["phac_hoa"]["duyet_boi"] or "—", k["phac_hoa"]["duyet_luc"] or "—"))
        p("    %-5s %-28s %-6s %4s %4s %4s %4s %5s" %
          ("mã", "tên", "tầng", "HT", "HOT", "LH", "S4", "rào"))
        for c in k["chan_dung"]:
            p("    %-5s %-28s %-6s %4d %4d %4d %4d %5s%s" % (
                c["cd"], c["ten"][:28], ",".join(c.get("tt") or []) or "—",
                c["ht"], c["hot"], c["co_lh"], c["s4_chua_dong"],
                c.get("rao_chot") or "—",
                "  👁 quan sát" if c["quan_sat"] else ""))
        du = next((c for c in k["chan_dung"] if c["cd"] == CD_DU), None)
        if du and du["ht"] >= CD_TOI_THIEU_DE_DE:
            p("")
            p("    ⚠ %d HT rơi %s. Nếu nhóm này có một NỖI SỢ riêng thì phác họa thêm"
              % (du["ht"], CD_DU))
            p("      một chân dung và xin duyệt lại CỔNG 0 — id-C §1.")
    else:
        p("  CHÂN DUNG — ⏳ CHƯA PHÁC HỌA")
        p("    %s" % (k["phac_hoa"]["vi_sao"] or ""))
        p("    Nguyên liệu đã ghi: out/nguyen-lieu-chan-dung.json")
        p("      · %d cụm chữ khách tự nói (ngưỡng ≥ %d HT)"
          % (len(nl["cum_chu"]), nl["nguong_cum"]))
        p("      · %d câu hỏi đầu đã ẩn danh" % len(nl["cau_dau"]))
        if nl["cum_chu"]:
            p("    Mười cụm đông nhất:")
            for c in nl["cum_chu"][:10]:
                p("      %-34s %3d HT  (%s)" % (c["cum"][:34], c["so_ht"], " ".join(c["ht"][:3])))
        p("")
        p("    → Agent đọc nguyên liệu, phác họa chân dung của kỳ, ghi out/chan-dung.json")
        p("      (`id.py chan-dung --ky %s --mau` để lấy khuôn), rồi người dùng duyệt:" % k["ky"])
        p("      `id.py chan-dung --ky %s --duyet \"<tên>\"` → chạy lại `id.py doc`." % k["ky"])
    p("")
    p("  MÃ O — 5 mã cao nhất")
    for o in sorted(k["ma_o"], key=lambda x: -x["so"])[:5]:
        p("    %-6s %4d  (%s%%)" % (o["ma"], o["so"], o["pct"]))
    p("")
    p("  ★ MÃ OQ — tám mã chỉ có ở khách quốc tế")
    for o in k["ma_oq"]:
        p("    %-6s %4d  (%5s%%)  %s" % (o["ma"], o["so"], o["pct"], o["trang_thai_chan"]))
    s4 = k["s4_chua_dong"]
    p("")
    p("  ★★ S4 CHƯA ĐÓNG — %d HT chạm rào XA mà bốn câu chưa được trả lời đủ" % s4["so"])
    for c, v in s4["cau"].items():
        if v:
            p("     %-14s %3d HT" % (c, v))
    if s4["so"]:
        p("     ⚠ Phần lớn nhóm này là LỖI HỆ, không phải lỗi người: sáu trong tám mã")
        p("       OQ đang bị chặn vì thiếu dữ kiện gốc (id-F §7 rào ③).")
    p("")
    p("  CHẤM ĐIỂM — % đạt theo nhóm")
    for g in k["nhan_vien"]["nhom"]:
        p("    %-3s %-28s %s%%" % (g["ma"], g["ten"], g["pct_dat"] if g["pct_dat"] is not None else "—"))
    p("")
    p("  PHÂN BỐ NHÂN VIÊN  " + " · ".join("%s %d" % (a, b) for a, b in
                                            sorted(k["nhan_vien"]["phan_bo"].items())))
    if k["nhan_vien"]["co_do"]:
        p("")
        p("  🔴 CỜ ĐỎ — %d" % len(k["nhan_vien"]["co_do"]))
        for c in k["nhan_vien"]["co_do"][:10]:
            p("    %-6s %-24s %s  « %s »" % (c["ma"], c["nguoi"][:24], c["ht"], c["trich"]))
    p("")
    p("  ⚠ Script chỉ làm phần ĐẾM. Phác họa chân dung, insight, câu hỏi ngầm,")
    p("    hướng nội dung, câu mẫu trong sổ tay — agent phải đọc và viết (SYSTEM-PROMPT §8).")
    p("")
    p("  Đã ghi: out/doc-hoi-thoai.json · out/cham-hoi-thoai.csv")
    p("          out/nguyen-lieu-chan-dung.json")
    p("")


# ──────────────────── lệnh `chan-dung` · CỔNG 0 ──────────────────────────

MAU_PHAC_HOA = {
    "schema": "chan-dung-ky/1",
    "ky": None,
    "nguon": "out/nguyen-lieu-chan-dung.json",
    "phac_hoa_luc": None,
    "trang_thai": "cho_duyet",
    "duyet_boi": None,
    "duyet_luc": None,
    "ke_thua_tu_ky": None,
    "_huong_dan": [
        "Chân dung của kỳ này phác họa TỪ HỘI THOẠI của kỳ này, ⛔ không chép từ "
        "một bộ chân dung có sẵn và ⛔ không suy ra từ dịch vụ.",
        "`ten` viết bằng CHỮ CỦA KHÁCH, ⛔ không bằng tính từ marketing.",
        "`noi_so` là nỗi sợ chi phối — hai nhóm cùng nỗi sợ thì là MỘT chân dung.",
        "`dau_hieu` là cụm chữ khách tự nói; script gán theo cụm này, xét TỪ TRÊN "
        "XUỐNG nên xếp chân dung HẸP trước, RỘNG sau.",
        "`khong_phai` (không bắt buộc): cụm loại trừ, dùng khi hai chân dung chồng chữ.",
        "`trich`: ít nhất một HT-nnn cho mỗi chân dung — không truy ngược được là bịa.",
        "★ `tt`: một hoặc nhiều tầng, TẦNG CHÍNH ĐỨNG TRƯỚC. Chân dung quốc tế "
        "không nói được khách ở tầng nào thì CHƯA DÙNG ĐƯỢC (id-C §1 điều ④). "
        "⚠ Chân dung trải đều trên 3–4 tầng là dấu hiệu phác họa chưa tới.",
        "★ `rao_chot`: ĐÚNG MỘT trong SỢ · NGỜ · NGẠI · XA. Chân dung gỡ cả bốn "
        "rào là chân dung chưa đọc xong (id-D §6).",
        "★ `rang_buoc_chuyen_di`: cửa sổ thời gian · số ngày ở lại được · đi một "
        "mình hay có người đi cùng · có cần visa không.",
        "⛔ KHÔNG gán QT1…QT7 của Agent-AdsOptimize-Kangnam-QT cho hội thoại — đó là "
        "khung mẫu dựng chiến dịch, chỉ dùng để ĐỐI CHIẾU sau CỔNG 0 (id-C §1).",
        "CD0 là mã DỰ TRỮ cho hội thoại không khớp dấu hiệu nào. ⛔ Không khai ở đây, "
        "⛔ không gọi là «rác» — CD0 đông là lỗi của quảng cáo, không phải của khách.",
        "Giữ lại mã của kỳ trước cho chân dung CÙNG NỖI SỢ (ghi `ke_thua_tu_ky`) — "
        "đổi mã giữa hai kỳ là mất mọi so sánh.",
        "⛔ Agent không tự điền `duyet_boi` / `trang_thai`. Duyệt bằng lệnh "
        "`id.py chan-dung --ky <kỳ> --duyet \"<tên người>\"`.",
    ],
    "tep": [
        {
            "ma": "CD1",
            "ten": "",
            "ho_la_ai": "",
            "noi_so": "",
            "dau_hieu": [],
            "khong_phai": [],
            "tt": [],
            "ngon_ngu": [],
            "rao_chot": None,
            "rang_buoc_chuyen_di": "",
            "he_so_gia_tri": None,
            "trich": [],
        }
    ],
    "ghi_chu": [],
}


def lenh_chan_dung(args):
    os.makedirs(RA, exist_ok=True)

    if args.mau:
        if os.path.exists(PHAC_HOA) and not args.ghi_de:
            sys.exit("⛔ out/chan-dung.json đã có. Thêm --ghi-de nếu muốn ghi lại khuôn trống.")
        mau = json.loads(json.dumps(MAU_PHAC_HOA))
        mau["ky"] = args.ky
        mau["phac_hoa_luc"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(PHAC_HOA, "w", encoding="utf-8") as f:
            json.dump(mau, f, ensure_ascii=False, indent=1)
        print("")
        print("  Đã ghi khuôn trống out/chan-dung.json cho kỳ %s." % args.ky)
        print("  → Agent đọc out/nguyen-lieu-chan-dung.json rồi điền `tep`.")
        print("  → Kiểm: id.py chan-dung --ky %s --kiem" % args.ky)
        print("")
        return

    if not os.path.exists(PHAC_HOA):
        sys.exit("⛔ chưa có out/chan-dung.json. Chạy: id.py chan-dung --ky %s --mau" % args.ky)
    with open(PHAC_HOA, encoding="utf-8") as f:
        pho = json.load(f)

    loi = kiem_phac_hoa(pho)
    if (pho.get("ky") or "") != args.ky:
        loi.insert(0, "`ky` trong file là «%s», không phải «%s»"
                   % (pho.get("ky") or "trống", args.ky))

    print("")
    print("═" * 66)
    print("  PHÁC HỌA CHÂN DUNG · kỳ %s · %d chân dung + %s dự trữ"
          % (pho.get("ky") or "—", len(pho.get("tep") or []), CD_DU))
    print("═" * 66)
    print("")
    for c in (pho.get("tep") or []):
        c = c or {}
        print("  %-5s %-34s hệ số %s · %d dấu hiệu · %d trích"
              % (c.get("ma") or "—", (c.get("ten") or "⚠ chưa đặt tên")[:34],
                 c.get("he_so_gia_tri") or "—",
                 len(c.get("dau_hieu") or []), len(c.get("trich") or [])))
        if c.get("noi_so"):
            print("        nỗi sợ: %s" % c["noi_so"])
    print("")

    if loi:
        print("  ⛔ CÒN %d LỖI — chưa duyệt được:" % len(loi))
        for x in loi:
            print("     · %s" % x)
        print("")
        sys.exit(1)

    if args.duyet:
        pho["trang_thai"] = "da_duyet"
        pho["duyet_boi"] = args.duyet.strip()
        pho["duyet_luc"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(PHAC_HOA, "w", encoding="utf-8") as f:
            json.dump(pho, f, ensure_ascii=False, indent=1)
        print("  ✅ CỔNG 0 ĐÃ MỞ — duyệt bởi %s lúc %s" % (pho["duyet_boi"], pho["duyet_luc"]))
        print("  → Chạy lại: id.py doc <file-hoi-thoai.md> --ky %s" % args.ky)
        print("")
        return

    print("  Bản phác họa sạch lỗi. Trạng thái: %s" % (pho.get("trang_thai") or "—"))
    if pho.get("trang_thai") != "da_duyet":
        print("  → Duyệt: id.py chan-dung --ky %s --duyet \"<tên người duyệt>\"" % args.ky)
        print("  ⛔ Agent không tự duyệt thay người dùng.")
    else:
        print("  Đã duyệt bởi %s lúc %s" % (pho.get("duyet_boi"), pho.get("duyet_luc")))
    print("")


# ───────────────────────────── lệnh `ads` ────────────────────────────────

def lenh_ads(args):
    """★ Bản quốc tế: số ads phải CẮT THEO THỊ TRƯỜNG mới đọc được (id-E §1).

    ⚠ Thiếu cột `market` là tình huống MẶC ĐỊNH, không phải ngoại lệ. Khi thiếu:
      ⛔ không gán số cho tầng nào, ghi cảnh báo, và đẩy "xin bản xuất có cột
      market" lên mục việc hệ thống (id-B §4).
    """
    with open(args.file, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("⛔ File ads rỗng.")

    co_cot_market = any((r.get("market") or "").strip() for r in rows)
    don_vi = "USD" if any((r.get("don_vi") or "").upper() == "USD" for r in rows) else "đ"

    def s(r, c):
        v = (r.get(c) or "").replace(",", "").replace(".", "").strip()
        try:
            return float(v)
        except ValueError:
            return 0.0

    COT = ("chi", "hien_thi", "click", "inbox", "lead", "booking", "den_kham")
    tong = {c: sum(s(r, c) for r in rows) for c in COT}

    def _n(x):
        return "{:,.0f}".format(x).replace(",", ".")

    chuoi = [
        # ★ Mắt xích 0: tiêu bao nhiêu. CPI, CPL, CPB đều là thương của con số này.
        {"ma": "CHI", "nhan": "Chi phí tổng", "gia_tri": tong["chi"] or None,
         "phu": "%d nội dung · %s hiển thị · %s inbox · %s lead · %s booking · %s đã khám"
                % (len({(r.get("noi_dung") or r.get("chien_dich") or "(không tên)").strip()
                        for r in rows}), _n(tong["hien_thi"]), _n(tong["inbox"]),
                   _n(tong["lead"]), _n(tong["booking"]), _n(tong["den_kham"]))},
        {"ma": "CPM", "nhan": "CPM", "gia_tri": _chia(tong["chi"], tong["hien_thi"] / 1000), "tot": "thap"},
        {"ma": "CTR", "nhan": "CTR", "gia_tri": _chia(tong["click"] * 100, tong["hien_thi"]), "tot": "cao", "kieu": "pct"},
        {"ma": "CPI", "nhan": "CPI — chi / inbox", "gia_tri": _chia(tong["chi"], tong["inbox"]), "tot": "thap"},
        {"ma": "CPL", "nhan": "CPL — chi / lead", "gia_tri": _chia(tong["chi"], tong["lead"]), "tot": "thap"},
        {"ma": "CPB", "nhan": "CPB — chi / booking", "gia_tri": _chia(tong["chi"], tong["booking"]), "tot": "thap"},
        # ★★ Mắt xích cuối của bản quốc tế. Với TT-B/TT-C, CPL đứng một mình gần
        #    như vô nghĩa: độ trễ lead → khám là 4–12 TUẦN (id-E §1).
        {"ma": "CPA_KHAM", "nhan": "★ CPA-KHÁM — chi / khách đã đến khám",
         "gia_tri": _chia(tong["chi"], tong["den_kham"]), "tot": "thap",
         "phu": "⚠ cần cửa sổ ≥8 tuần — con số của kỳ 2 tuần KHÔNG đọc được"},
    ]
    for c in chuoi:
        c.setdefault("kieu", "n")
        c["muc_tieu"] = None          # ⚠ chưa có mốc — id-E §1
        c["ky_truoc"] = None

    # ★ Cắt theo thị trường. ⛔ Không có cột market thì KHÔNG dựng bảng này —
    #   thà trống còn hơn gán sai tầng.
    theo_tang = []
    if co_cot_market:
        bang = nap_tu_dien()["thi_truong"]["tang_theo_nuoc"]
        gom = defaultdict(lambda: Counter())
        for r in rows:
            mk = (r.get("market") or "").strip().upper()
            tt = (r.get("tt") or "").strip().upper()
            if not tt:
                tt = ("TT-D" if mk == "VN-EXPAT" else
                      "TT-B" if mk.startswith("VN-DIASPORA") else
                      bang.get(mk, TT_DU))
            for c in COT:
                gom[(tt, mk)][c] += s(r, c)
        for (tt, mk), v in sorted(gom.items()):
            theo_tang.append({
                "tt": tt, "market": mk, "chi": v["chi"], "inbox": v["inbox"],
                "lead": v["lead"], "booking": v["booking"], "den_kham": v["den_kham"],
                "cpi": _chia(v["chi"], v["inbox"]), "cpl": _chia(v["chi"], v["lead"]),
                "cpa_kham": _chia(v["chi"], v["den_kham"])})

    theo_nd = defaultdict(lambda: Counter())
    nhan_nd = {}
    for r in rows:
        ten = (r.get("noi_dung") or r.get("chien_dich") or "(không tên)").strip()
        nhan_nd.setdefault(ten, {"market": set(), "geo_mode": set()})
        nhan_nd[ten]["market"].add((r.get("market") or "").strip().upper() or "?")
        nhan_nd[ten]["geo_mode"].add((r.get("geo_mode") or "").strip() or "?")
        for c in COT:
            theo_nd[ten][c] += s(r, c)
    dong = []
    for ten, v in sorted(theo_nd.items(), key=lambda x: -x[1]["chi"]):
        dong.append({"noi_dung": ten,
                     "market": sorted(nhan_nd[ten]["market"]),
                     "geo_mode": sorted(nhan_nd[ten]["geo_mode"]),
                     "chi": v["chi"], "inbox": v["inbox"],
                     "deal": v["lead"], "bk": v["booking"], "den_kham": v["den_kham"],
                     "cpi": _chia(v["chi"], v["inbox"]), "cpl": _chia(v["chi"], v["lead"]),
                     "cpb": _chia(v["chi"], v["booking"]),
                     "cpa_kham": _chia(v["chi"], v["den_kham"])})
    # ⚠ Trung vị tính trong CÙNG MỘT THỊ TRƯỜNG mới có nghĩa (id-E §4). Khi cột
    #   market còn thiếu thì chỉ chấm được ở mức tổng — và phải nói rõ như thế.
    tv = sorted([d["cpl"] for d in dong if d["cpl"]])
    gi = tv[len(tv) // 2] if tv else None
    for d in dong:
        d["danh_gia"] = "—" if not gi or not d["cpl"] else ("tot" if d["cpl"] <= gi else "kem")

    ghi_chu = [
        "Ô «Chi phí tổng» là mẫu số chung của CPI, CPL và CPB — CPL giảm mà chi "
        "cũng giảm theo thì chưa chắc đã tốt lên (id-E §1).",
        "★ Kiểm CƠ CẤU THỊ TRƯỜNG trước khi kết luận về CPM/CPL: chuyển chi từ KH "
        "sang AU thì CPM tăng mà KHÔNG có gì xấu đi (id-E §1).",
        "★ TT-B/TT-C: độ trễ lead → đến khám là 4–12 tuần → ⛔ không đánh giá trong "
        "cửa sổ ngắn hơn 8 tuần, và ⛔ không đặt CPL kỳ này cạnh CPA-KHÁM như thể "
        "chúng nói về cùng một tệp (id-E §1).",
        "⛔ Không so chéo CPL giữa hai thị trường khác nhau (id-E §2).",
        "⚠ Mốc mục tiêu chưa có — cần TB 30 ngày của CHÍNH THỊ TRƯỜNG đó (id-E §1).",
    ]
    if not co_cot_market:
        ghi_chu.insert(0, "⛔ BẢN XUẤT THIẾU CỘT `market` — ⛔ không gán số cho tầng nào. "
                          "Chỉ đọc được ở mức tổng. Xin bản xuất có cột market "
                          "(việc hệ thống — id-B §4).")

    os.makedirs(RA, exist_ok=True)
    ket = {"ky": args.ky, "nguon": os.path.basename(args.file), "don_vi": don_vi,
           "co_cot_market": co_cot_market, "tong": tong, "chuoi": chuoi,
           "theo_tang": theo_tang, "dong": dong, "ghi_chu": ghi_chu}
    with open(os.path.join(RA, "doc-ads.json"), "w", encoding="utf-8") as f:
        json.dump(ket, f, ensure_ascii=False, indent=1)

    print("")
    print("═" * 66)
    print("  CHỈ SỐ QUẢNG CÁO QUỐC TẾ · kỳ %s · %d dòng · đơn vị %s"
          % (args.ky, len(rows), don_vi))
    print("═" * 66)
    for c in chuoi:
        v = c["gia_tri"]
        so = "—" if v is None else ("%.1f%%" % v if c["kieu"] == "pct"
                                    else "{:,.0f}".format(v) + " " + don_vi)
        print("    %-34s %12s   %s" %
              (c["nhan"], so, c.get("phu") or "mục tiêu: ⚠ chưa có mốc so sánh"))
    print("")
    if co_cot_market:
        print("  ★ CẮT THEO THỊ TRƯỜNG")
        print("    %-6s %-12s %12s %6s %6s %8s" % ("tầng", "market", "chi", "inbox", "lead", "CPL"))
        for x in theo_tang:
            print("    %-6s %-12s %12s %6d %6d %8s" % (
                x["tt"], x["market"], "{:,.0f}".format(x["chi"]), x["inbox"], x["lead"],
                x["cpl"] if x["cpl"] is not None else "—"))
    else:
        print("  ⛔ THIẾU CỘT `market` — ⛔ không gán số cho tầng nào (id-B §4).")
    print("")
    print("  %d nội dung · đã ghi out/doc-ads.json" % len(dong))
    print("")


def _chia(a, b):
    return round(a / b, 1) if b else None


# ─────────────────────────── lệnh `bao-cao` ──────────────────────────────

def lenh_bao_cao(args):
    ht_f = os.path.join(RA, "doc-hoi-thoai.json")
    if not os.path.exists(ht_f):
        sys.exit("⛔ Chưa có out/doc-hoi-thoai.json. Chạy `id.py doc` trước.")
    with open(ht_f, encoding="utf-8") as f:
        H = json.load(f)
    A = None
    ads_f = os.path.join(RA, "doc-ads.json")
    if os.path.exists(ads_f):
        with open(ads_f, encoding="utf-8") as f:
            A = json.load(f)

    ky_id = args.ky.replace("/", "-").replace(" ", "")
    T = H["thi_truong"]
    D = {
        "schema": "insight-dashboard-knqt/1",
        "ky": {"id": ky_id, "nhan": args.ky, "tao": H["tao"], "nguon": H["nguon"]},
        "canh_bao": [],
        "the_tong": H["the_tong"],
        # ★ R8 — đủ điều kiện KCB cho người nước ngoài. ⛔ Script KHÔNG tự xác nhận:
        #   đây là điều kiện HOẠT ĐỘNG, do Pháp chế + Điều phối QT chốt (id-K §5).
        "r8": {"xac_nhan": False,
               "ghi_chu": "[CHỜ CẤP: R8 — đủ điều kiện KCB cho người nước ngoài · "
                          "Pháp chế + Điều phối QT]"},
        "ket_luan": {"marketing": [], "truc_kenh": [], "he_thong": [],
                     "cho_cap": [], "bu_quyet": []},
        "theo_doi": [],
        "pheu": {"so_ht_phan_tich": H["so_ht"], "nhiet": H["nhiet"],
                 "nhiet_x_lh": H["nhiet_x_sdt"], "tin_hieu": H["tin_hieu"],
                 "nguyen_nhan_roi": H["nguyen_nhan_roi"], "rao_can": H["rao_can"],
                 "rao_chot": H["rao_chot"], "chang": H["chang"],
                 "ma_o": H["ma_o"], "ma_oq": H["ma_oq"],
                 "s4_chua_dong": H["s4_chua_dong"], "van_de": []},
        "thi_truong": T,
        "chan_dung": {"phac_hoa": H.get("phac_hoa", {}), "tep": H["chan_dung"],
                      "insight": []},
        "nhan_vien": H["nhan_vien"],
        "meta": ({"nguon": A["nguon"], "don_vi": A["don_vi"], "chuoi": A["chuoi"],
                  "co_cot_market": A["co_cot_market"], "theo_tang": A["theo_tang"],
                  "noi_dung": A["dong"], "ghi_chu": A["ghi_chu"],
                  "cua_so_do": {"du_8_tuan": False,
                                "ghi_chu": "⚠ TT-B/TT-C cần cửa sổ ≥8 tuần — id-E §1"},
                  "van_de": []} if A else
                 {"co_du_lieu": False, "ghi_chu": "⚠ chưa có dữ liệu quảng cáo"}),
        "google": {"co_du_lieu": False, "ghi_chu": "⚠ chưa có dữ liệu Google Ads"},
        "ma_tran": {"trang_thai": "cho_duyet", "khoi": [], "sua_van_hanh": [],
                    "cho_cap": [], "quan_sat": []},
        "hook": {"dong": [], "ghi_chu": "chưa viết — ma trận chưa được duyệt"},
        "so_tay": {"da_sinh": False, "so_ban": 0, "duong_dan": "out/so-tay/"},
        "viec": [],
        "ghi_chu": [
            "Nguồn hội thoại: %s · %d hội thoại phân tích." % (H["nguon"], H["so_ht"]),
            "Tầng thị trường · ngôn ngữ · kênh · giờ ICT · chặng S1–S7 · mã O + OQ · "
            "mức nóng · rào cản · vì sao rơi · chấm N1–N7: đọc tự động bằng "
            "tools/id.py, CHƯA qua người soát.",
            "★ Tầng thị trường là SUY RA khi file không khai: %s. TT-0 ≥ %g%% mẫu thì "
            "phải qua CỔNG M trước khi kết luận (id-L §1)."
            % (" · ".join("%s %d" % (a, b) for a, b in T["nguon_suy"].items()),
               TT_NGUONG_CONG_M),
            "Chân dung KHÔNG có bộ mặc định: phác họa từ hội thoại của kỳ, gán theo dấu "
            "hiệu trong out/chan-dung.json sau khi người dùng duyệt ở CỔNG 0 (id-C §1).",
            "★ N1.1 chỉ tính tin đến trong 08:00–17:00 ICT; ngoài giờ chấm «—» và phần "
            "dọn hộp thư ngoài giờ chấm ở N7.4 — ⛔ không trừ điểm người vì lệch "
            "múi giờ (id-L §4).",
            "★ N3.1 chấm THẬT ở bản quốc tế vì giá đã công khai tại /price-list/ — "
            "né giá là lỗi người, ⛔ không còn là lỗi hệ (id-K §3③).",
            "★ Sáu trong tám mã OQ đang bị chặn vì thiếu dữ kiện gốc — những ô đó là "
            "VIỆC HỆ THỐNG, ⛔ không phải điểm trừ của nhân viên (id-F §7 rào ③).",
            "⛔ Agent KHÔNG đưa ra kết luận pháp lý. Cờ pháp chế phải soát CẢ HAI TẦNG: "
            "luật Việt Nam và luật nước người xem (id-K §4).",
            "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai.",
        ],
    }

    # ── cảnh báo đầu trang
    if T["cong_m"]["can_xac_nhan"]:
        D["canh_bao"].append({"muc": "bad",
                              "text": "CỔNG M — TT-0 chiếm %s%% mẫu: chưa biết khách ở đâu, "
                                      "mọi tỷ lệ bên dưới đọc với độ tin thấp (id-L §1)."
                                      % T["cong_m"]["pct_tt0"]})
    if H["nhan_vien"]["co_do"]:
        D["canh_bao"].append({"muc": "bad", "text": "Có %d cờ đỏ trong kỳ — xem tab Chấm điểm."
                                                   % len(H["nhan_vien"]["co_do"])})
    s4 = H["s4_chua_dong"]["so"]
    if s4:
        D["canh_bao"].append({"muc": "bad",
                              "text": "%d hội thoại chạm rào XA mà bốn câu của chặng S4 chưa "
                                      "được trả lời đủ — khách muốn làm mà không đặt được vé "
                                      "(id-D §6.1)." % s4})
    pha = H.get("phac_hoa") or {}
    if pha.get("trang_thai") != "da_duyet":
        D["canh_bao"].append({"muc": "bad",
                              "text": "Chân dung chưa qua CỔNG 0 — tab Chân dung còn trống (%s)."
                                      % (pha.get("vi_sao") or "chưa phác họa")})
    if not A:
        D["canh_bao"].append({"muc": "warn", "text": "Chưa có file chỉ số quảng cáo — tab Marketing trống."})
    elif not A.get("co_cot_market"):
        D["canh_bao"].append({"muc": "bad",
                              "text": "Bản xuất ads THIẾU CỘT `market` — ⛔ không gán số cho "
                                      "tầng nào, chỉ đọc được ở mức tổng (id-B §4)."})
    if T["ngoai_pham_vi"]["so"]:
        D["canh_bao"].append({"muc": "warn",
                              "text": "%d HT khách nội địa nhắn lạc vào kênh quốc tế — đã loại "
                                      "khỏi mẫu, ⛔ không xếp vào TT-B." % T["ngoai_pham_vi"]["so"]})
    mg = T["mui_gio"]
    if mg["mat_qua_12h"]:
        D["canh_bao"].append({"muc": "bad",
                              "text": "%d hội thoại đến ngoài giờ 8–17 ICT và chờ quá 12h — "
                                      "việc của LỊCH TRỰC, ⛔ không của nhân viên (id-L §4)."
                                      % mg["mat_qua_12h"]})
    D["canh_bao"].append({"muc": "warn", "text": "Chưa có dữ liệu Google Ads (id-B §5)."})
    D["canh_bao"].append({"muc": "bad", "text": "R8 chưa xác nhận — ⛔ không phát bản cuối "
                                                "khi chưa có xác nhận của Pháp chế (id-K §5)."})

    dd = os.path.join(GOC, "dashboard", "data")
    os.makedirs(dd, exist_ok=True)
    fp = os.path.join(dd, ky_id + ".json")
    with open(fp, "w", encoding="utf-8") as f:
        json.dump(D, f, ensure_ascii=False, indent=1)

    ip = os.path.join(dd, "index.json")
    idx = {"schema": "insight-dashboard-knqt#index", "ky": []}
    if os.path.exists(ip):
        with open(ip, encoding="utf-8") as f:
            idx = json.load(f)
    idx["cap_nhat"] = datetime.now().strftime("%Y-%m-%d")
    idx["ky"] = [k for k in idx.get("ky", []) if k["id"] != ky_id]
    idx["ky"].insert(0, {"id": ky_id, "nhan": args.ky, "file": "data/%s.json" % ky_id})
    with open(ip, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)

    print("\n  Đã ghi dashboard/data/%s.json và cập nhật index.json" % ky_id)
    print("  Mở dashboard/index.html để xem.")
    if T["cong_m"]["can_xac_nhan"]:
        print("  ⛔ CỔNG M — TT-0 %s%%: xác nhận bảng thị trường trước khi kết luận."
              % T["cong_m"]["pct_tt0"])
    print("  ⚠ Ma trận đang ở trạng thái CHỜ DUYỆT — tab Hook và Sổ tay còn trống.")
    print("  ⚠ R8 chưa xác nhận — ⛔ không phát bản cuối (id-K §5).\n")


# ──────────────────────────────── main ───────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Agent-InsightDashboard-KNQT · công cụ đếm (bản quốc tế)")
    sp = p.add_subparsers(dest="lenh", required=True)

    a = sp.add_parser("doc", help="đọc hội thoại → tầng thị trường + phân loại + chấm điểm")
    a.add_argument("file")
    a.add_argument("--ky", required=True)
    a.set_defaults(fn=lenh_doc)

    d = sp.add_parser("chan-dung", help="CỔNG 0 — khuôn · kiểm · duyệt bản phác họa chân dung")
    d.add_argument("--ky", required=True)
    d.add_argument("--mau", action="store_true", help="ghi khuôn trống out/chan-dung.json")
    d.add_argument("--ghi-de", dest="ghi_de", action="store_true", help="cho --mau ghi đè file cũ")
    d.add_argument("--kiem", action="store_true", help="soát bản phác họa (mặc định)")
    d.add_argument("--duyet", metavar="NGUOI", help="mở CỔNG 0 — ghi tên người duyệt")
    d.set_defaults(fn=lenh_chan_dung)

    b = sp.add_parser("ads", help="đọc chỉ số quảng cáo — cần cột `market`")
    b.add_argument("file")
    b.add_argument("--ky", required=True)
    b.set_defaults(fn=lenh_ads)

    c = sp.add_parser("bao-cao", help="gộp thành JSON cho dashboard")
    c.add_argument("--ky", required=True)
    c.set_defaults(fn=lenh_bao_cao)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
