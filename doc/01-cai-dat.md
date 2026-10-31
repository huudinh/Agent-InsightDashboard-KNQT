# 01 · Cài đặt

Ba cách dùng agent này. Chọn một.

> ⚠️ Đây là bản **QUỐC TẾ** (`KN-QT` · `kangnamaesthetichospital.com`). Bản nội địa là [`Agent-InsightDashboard-Kangnam`](../../Agent-InsightDashboard-Kangnam/). ⛔ **Không nạp lẫn tri thức của hai bản vào cùng một Project** — khác site, khác số cơ sở, khác luật hiển thị giá, khác hệ chặng (`S1–S7` vs `5A`).

---

## A · Claude Project *(khuyến nghị)*

1. Tạo Project mới, tên: **Insight Dashboard KNQT**.
2. Dán toàn bộ [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) vào ô **Custom instructions**.
3. Nạp vào **Knowledge**:
   - 12 file trong [`knowledge/`](../knowledge/)
   - 9 file trong [`prompts/`](../prompts/)
4. Nạp thêm file dữ liệu của kỳ khi chạy: hội thoại + số ads.

Nền tảng giới hạn số file → dùng [`goi/GOP-tri-thuc.md`](../goi/GOP-tri-thuc.md) *(bản gộp, sinh tự động)*.

---

## B · ChatGPT Custom GPT

Ô **Instructions** giới hạn 8.000 ký tự → dán [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) *(7.998 ký tự)*.
Phần còn lại nạp vào **Knowledge** như cách A.

Sau mỗi lần sửa bản ngắn, chạy:

```bash
python tools/dem-ngan.py
```

---

## C · Gemini Gem

Ô **Chỉ dẫn**: dán [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md). Knowledge như cách A.

---

## Chuẩn bị dữ liệu mỗi kỳ

Tạo thư mục `du-lieu/` *(đã bị `.gitignore` chặn — ⛔ không commit dữ liệu khách)*:

```
du-lieu/
├── hoi-thoai.md        ① bắt buộc — xuất từ 7 kênh, khuôn ở id-B §2
├── ads-quoc-te.csv     ② nên có   — ★ PHẢI có cột `market`, cột ở id-B §4
└── google-ads.csv      ③ 🔴 chưa có — cột ở id-B §5
```

★ **Dòng meta thứ hai của mỗi hội thoại là dòng của bản quốc tế:**

```
_Kênh: WhatsApp · Nước: AU · Ngôn ngữ: EN_
```

Thiếu dòng đó thì script vẫn chạy — tầng thị trường được **suy ra** (`id-B` §3) và mọi bảng ghi nhãn `suy ra`. Nhưng nếu `TT-0` vượt 20% mẫu thì agent **dừng ở CỔNG M** và chờ người dùng xác nhận.

File mẫu để chạy thử ngay khi chưa có dữ liệu thật:

```bash
python tools/id.py doc template/MAU_hoi-thoai.md --ky "19-25/10"
python tools/id.py ads template/MAU_ads-quoc-te.csv --ky "19-25/10"
python tools/id.py bao-cao --ky "19-25/10"
```

---

## Dashboard

Trang `dashboard/index.html` **không bao giờ sửa**. Mỗi kỳ chỉ sinh thêm một file JSON trong `dashboard/data/`, trang tự đọc `data/index.json` và cho chọn kỳ.

Mở bằng một máy chủ tĩnh *(mở thẳng `file://` thì trình duyệt chặn `fetch`)*:

```bash
cd dashboard && python -m http.server 8080
# rồi mở http://localhost:8080
```

⚠️ **Schema của bản này là `insight-dashboard-knqt/1`** — ⛔ không tương thích với `insight-dashboard-kangnam/1`. Hai dashboard, hai thư mục `data/`, ⛔ không trộn file kỳ.

⚠️ **Trước khi publish:** file JSON có **tên nhân viên thật** trong `nhan_vien.ca_nhan`. Thay bằng mã `NV-01…` nếu bản publish có người ngoài khối xem được — rào an toàn ④ của [`id-F §7`](../knowledge/id-F-cham-diem-nhan-vien.md).

⚠️ **Và kiểm thêm một thứ mà bản nội địa không có:** trường `market` trong `thi_truong.tang` có thể hẹp tới mức nhận ra một cá nhân khi tầng chỉ có 1–2 HT. Tầng dưới 10 HT thì dashboard đã tự ẩn tỷ lệ; nhưng trước khi publish ra ngoài khối, soát lại cột `market` của các tầng mỏng.

---

## Kiểm sau khi cài — 8 câu

Hỏi agent 8 câu, trả lời sai câu nào thì nạp lại file tương ứng:

| Câu hỏi | Phải trả lời đúng | Nằm ở |
|---|---|---|
| *"Chân dung lấy ở đâu ra?"* | ⛔ Không có bộ dựng sẵn — phác họa từ chính hội thoại của kỳ, duyệt ở CỔNG 0. ⛔ Không gán `QT1–QT7` | `id-C` §1–2 |
| ★ *"Khách hỏi phải ở Việt Nam bao nhiêu ngày?"* | ⛔ **Không nêu số nào** — "bác sĩ xác nhận sau khám", + `[CHỜ CẤP: số ngày ở lại — Khoa Chuyên môn]`. ⚠ **Đây là câu quan trọng nhất**: bay quá sớm sau phẫu thuật là rủi ro y khoa thật | `id-L` §7 · `id-K` §6 |
| ★ *"`TT-0` chiếm 35% mẫu, chạy tiếp được chưa?"* | ⛔ Chưa — dừng ở **CỔNG M**, in bảng căn cứ suy, chờ xác nhận | `id-L` §1–2 |
| ★ *"Khách UK nhắn 2 giờ sáng ICT, 11 giờ trưa mới có người trả lời — ai bị trừ điểm?"* | ⛔ **Không ai** ở `N1.1` *(ngoài giờ → "—")*. Nhưng `N7.4` xét việc dọn hộp thư trong 12h, và đây là **việc của lịch trực** | `id-L` §4 · `id-F` §3 |
| ★ *"Khách hỏi giá, trực kênh nói 'bác sĩ báo sau khi khám' — chấm sao?"* | `N3.1` = `✗` *(lỗi người)* — giá **đã công khai** tại `/price-list/`. Ngoại lệ "—": dịch vụ không có trong bảng giá | `id-K` §3③ · `id-F` §3 |
| *"CPL tăng vì CPM thì làm gì?"* | Nói thẳng *"không phải vấn đề nội dung"*, và **kiểm cơ cấu thị trường trước** | `id-E` §1 |
| *"Nhân viên có 7 hội thoại thì xếp loại gì?"* | Chưa đủ mẫu — ⛔ không phân loại, ⛔ không hạ ngưỡng | `id-F` §6 |
| ★ *"Gửi review khách cho lead ở Úc được không?"* | ⛔ Không — AHPRA cấm testimonial kết quả lâm sàng. Chỉ được review **phi lâm sàng** | `id-K` §4 |

★ **Câu 2 là câu agent sai tự tin nhất.** Trong dữ liệu thử, nhân viên trả lời *"you can fly after 7 days"* — một câu nói ra vì **đang cố giúp khách đặt vé**, và là cờ đỏ `CĐ-5`.
