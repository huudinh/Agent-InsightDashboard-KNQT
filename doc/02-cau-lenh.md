# 02 · Dòng lệnh

Script làm phần **đếm được**. Phần **đọc hiểu** — **phác họa chân dung**, insight, câu hỏi ngầm, hướng nội dung, câu mẫu trong sổ tay, và **mọi phán đoán pháp chế hai tầng** — là việc của agent. ⛔ Script không thay được.

---

## Một kỳ đầy đủ

```bash
# ① đọc hội thoại → ★ tầng thị trường + phân loại + chấm điểm + nguyên liệu phác họa
python tools/id.py doc du-lieu/hoi-thoai.md --ky "19-25/10"

# ② lấy khuôn bản phác họa → AGENT đọc nguyên liệu và điền `tep`
python tools/id.py chan-dung --ky "19-25/10" --mau

# ③ soát bản phác họa
python tools/id.py chan-dung --ky "19-25/10" --kiem

# ④ ★ CỔNG 0 — NGƯỜI DÙNG duyệt, ⛔ không phải agent
python tools/id.py chan-dung --ky "19-25/10" --duyet "Tên người duyệt"

# ⑤ chạy lại: giờ mới có chân dung trong mọi bảng
python tools/id.py doc du-lieu/hoi-thoai.md --ky "19-25/10"

# ⑥ đọc số quảng cáo — ★ cần cột `market`
python tools/id.py ads du-lieu/ads-quoc-te.csv --ky "19-25/10"

# ⑦ gộp thành JSON cho dashboard
python tools/id.py bao-cao --ky "19-25/10"

# ⑧ sinh khung sổ tay (sau khi ma trận đã duyệt)
python tools/so_tay.py --ky "19-25/10"

# ⑨ xem dashboard
cd dashboard && python -m http.server 8080
```

⚠️ Bước ①→⑤ chạy `doc` **hai lần** là đúng thiết kế: lần đầu chưa có chân dung nên ô `cd` để trống, lần sau gán theo bản đã duyệt. Luật *một lần chấm* vẫn giữ — mọi ô khác (tầng, chặng, mã O/OQ, điểm `N1–N7`) đọc từ cùng một file và cho cùng kết quả.

★ **Và nhớ CỔNG M:** nếu bước ① in ra `TT-0 ≥ 20%` thì ⛔ đừng chạy tiếp sang ② trước khi người dùng xác nhận bảng thị trường.

---

## `id.py doc`

| Ra | Nội dung |
|---|---|
| `out/cham-hoi-thoai.csv` | Một dòng mỗi hội thoại · **25 cột dữ kiện + 27 ô `✓/✗/—`** · ★ `tt` · `market` · `can_cu_tt` · `ngon_ngu` / `ngon_ngu_nv` · `kenh` · `trong_gio` · `cho_gio` · `chang` · `ma_o` · `ma_oq` · `rao_chot` · `s4_chua_dong` · vì sao rơi · điểm · cờ đỏ |
| `out/doc-hoi-thoai.json` | Bản tổng hợp để `bao-cao` và `so_tay.py` đọc lại — gồm khối `thi_truong` |
| `out/nguyen-lieu-chan-dung.json` | ★ **Nguyên liệu phác họa**: cụm 2–3 chữ khách tự nói (đếm theo **số hội thoại**) · câu hỏi đầu từng HT đã ẩn danh · phân bố **tầng · ngôn ngữ · kênh · chặng** · rào cản |
| Màn hình | ★ Bảng tầng thị trường + CỔNG M · múi giờ · kênh · chặng · rào chốt · thẻ số tổng · vì sao rơi · bảng chân dung · top mã O · **8 mã OQ kèm trạng thái chặn** · **S4 chưa đóng** · % đạt 7 nhóm · phân bố A/B/C/D · cờ đỏ |

### ⚠ Năm chỗ script tự xử, cần biết

```
① Dòng hệ thống bị LOẠI khỏi lượt của khách:
   [Tệp đính kèm], 📞 Cuộc gọi thoại, "X đã gọi cho bạn"…
   Không loại thì "bỏ sau 1 lượt" luôn ra 0%.

② Đồng hồ SLA chạy từ TIN ĐẦU TIÊN của hội thoại (kể cả dòng hệ thống).

③ "Khách gửi ảnh" chỉ tính khi ảnh đến SAU lời mời gửi ảnh của nhân viên.

★④ Tin đến NGOÀI khung 08:00–17:00 ICT → N1.1 và N1.4 chấm "—", ⛔ không ✗.
   Phần dọn hộp thư ngoài giờ chấm riêng ở N7.4 (trong 12h) — id-L §4.

★⑤ Khách NỘI ĐỊA nhắn lạc vào kênh quốc tế (tiếng Việt, ⛔ không nhắc gì đến ở
   nước ngoài / về nước / bay) → LOẠI khỏi mẫu, đếm riêng ở `ngoai_pham_vi`,
   ⛔ KHÔNG xếp vào TT-B.
```

### Hiệu chỉnh nhận dạng

Sửa [`tools/tu_dien.json`](../tools/tu_dien.json), ⛔ không sửa `id.py`.

⚠️ Từ điển của bản này **song ngữ**: mỗi mã có cả cụm tiếng Anh và tiếng Việt. Thêm từ xong **phải chạy lại và nhìn cột `%`**.

| Dấu hiệu | Nghĩa |
|---|---|
| Một mã `O` > 60% mẫu | Từ khoá của mã đó quá rộng — cắt bớt |
| `O-00` > 10% mẫu | Danh sách thiếu — **báo lại**, ⛔ đừng tự thêm mã |
| ★ `TT-0` > 20% mẫu | **CỔNG M** — ⛔ không phải lỗi từ điển mà là lỗi **câu mở**: không ai hỏi khách đang ở đâu |
| ★ `chưa rõ` chặng cao | Câu đầu của khách quá ngắn — hoặc từ khoá chặng thiếu. ⛔ Không mặc định `S1` |
| ★ `kenh: chưa rõ` cao | File xuất thiếu dòng meta `_Kênh: …_` (`id-B` §2) |

★ **Ba khối mới trong từ điển, so với bản nội địa:** `ma_oq` *(8 mã)* · `thi_truong` *(nước → market → tầng · cụm "về nước" · cụm "đang ở VN")* · `ngon_ngu` + `kenh`.

---

## `id.py chan-dung` — CỔNG 0

| Cờ | Làm gì |
|---|---|
| `--mau` | Ghi khuôn trống `out/chan-dung.json`. Thêm `--ghi-de` để ghi lại lên file cũ |
| `--kiem` | Soát: trùng mã · thiếu tên · thiếu dấu hiệu · thiếu `HT-nnn` · `he_so_gia_tri` ngoài 1–3 · sai kỳ · ★ **thiếu `tt`** · ★ **`rao_chot` không đúng một trong SỢ/NGỜ/NGẠI/XA** · ★ **thiếu `rang_buoc_chuyen_di`**. Còn lỗi thì thoát mã 1 |
| `--duyet "<tên>"` | ★ Mở CỔNG 0: ghi `trang_thai: da_duyet` + tên người duyệt + thời điểm |

⛔ **Agent không chạy `--duyet`.** Lệnh này là của người dùng.

Một dòng trong `tep` — ★ bốn ô cuối là của bản quốc tế:

```jsonc
{
  "ma": "CD1",                                  // CD1, CD2… ⛔ CD0 là mã dự trữ
  "ten": "I was quoted 20 grand in Australia",  // NGUYÊN VĂN chữ của khách
  "ho_la_ai": "...",
  "noi_so": "Mổ ở nước ngoài có an toàn không, và bay về rồi thì ai lo cho tôi",
  "dau_hieu": ["quoted", "grand", "australia"],
  "khong_phai": [],                             // cụm loại trừ khi hai CD chồng chữ
  "tt": ["TT-C"],                               // ★ tầng chính đứng trước
  "ngon_ngu": ["EN"],                           // ★
  "rao_chot": "XA",                             // ★ ĐÚNG MỘT
  "rang_buoc_chuyen_di": "phải xin nghỉ việc, cần biết số ngày trước khi đặt vé",  // ★
  "he_so_gia_tri": 3,
  "trich": ["HT-001"]                           // ⛔ không được rỗng
}
```

★ Script xét **từ trên xuống, dòng đầu khớp thì lấy** → xếp chân dung **hẹp trước, rộng sau**. Không khớp dòng nào → `CD0`.

---

## `id.py ads`

Đọc CSV theo cột ở `id-B §4`, ra `out/doc-ads.json` + chuỗi `Chi → CPM → CTR → CPI → CPL → CPB → ★ CPA-KHÁM` và **bảng cắt theo thị trường** trên màn hình.

★ **Không có cột `market` thì script ⛔ không dựng bảng cắt theo tầng**, in một dòng chặn và ghi cảnh báo vào file kỳ. Thà trống còn hơn gán sai tầng.

⚠️ Cột `muc_tieu` luôn `null` cho tới khi có mốc TB 30 ngày **của chính thị trường đó**. Script ⛔ không tự đặt mốc.
⚠️ Đơn vị: có dòng nào khai `don_vi = USD` thì cả bảng giữ USD, ⛔ không tự quy đổi.

---

## `id.py bao-cao`

Ghi `dashboard/data/<ky>.json` *(schema `insight-dashboard-knqt/1`)* + cập nhật `index.json`.

Ma trận luôn khởi tạo ở `trang_thai: "cho_duyet"` → tab **Ngân hàng hook** và **Sổ tay** còn khoá.
Chân dung chưa qua CỔNG 0 → `chan_dung.tep` rỗng, dashboard khoá tab Chân dung kèm lý do.
★ `r8.xac_nhan` luôn khởi tạo `false` — script ⛔ không tự xác nhận điều kiện hoạt động.

Bố cục hẹp: thêm `"bo_cuc": "insight"` hoặc `"bo_cuc": "truc-kenh"` vào `index.json`. Không khai thì ra bản đầy đủ **10 tab** (`id-J` §1).
★ Tab **Thị trường & kênh** có mặt trong **cả ba bố cục** — ⛔ không bố cục nào được bỏ nó.

---

## `so_tay.py`

| Ra | Cho ai |
|---|---|
| `out/so-tay/ST-CN_<tên>.md` | Từng nhân viên ≥10 hội thoại — ★ có **mục 6 "việc không phải của bạn"** |
| `out/so-tay/ST-TN_truong-nhom.md` | Trưởng nhóm — ★ có **mục 5 bảy nhóm lỗi hệ** + **mục 6 lịch trực theo múi giờ** |
| `out/so-tay/ST-ND_noi-dung.md` | Người làm nội dung — ★ có **mục 5 ô chờ dữ kiện** + **mục 6 cờ pháp chế hai tầng** |

`--chi "<tên>"` để sinh lại một người.

Mọi chỗ `«agent điền: …»` là phần đọc hiểu — agent phải viết trước khi phát. Dùng [`prompts/prompt-so-tay.md`](../prompts/prompt-so-tay.md).

---

## Phụ trợ

```bash
python tools/gop-tham-khao.py   # gộp knowledge/ → goi/GOP-tri-thuc.md (chạy sau mỗi lần sửa)
python tools/dem-ngan.py        # canh giới hạn 8.000 ký tự của bản ngắn
python tools/trang-huong-dan.py # sinh lại tools/huong-dan.html
```

### `trang-huong-dan.py`

Generator **dùng chung** cho cả bộ agent trong `Project/Agent`. Phần riêng của gói này nằm ở [`tools/huong-dan.json`](../tools/huong-dan.json) — ⛔ **sửa JSON, không sửa generator**.

Nút Copy trên trang **đọc thẳng file nguồn trong repo**, nên sửa `knowledge/` rồi chạy lại là nút Copy tự khớp. Script cũng **chặn** nếu Thẻ B vượt 8.000 ký tự.

---

## Khi script báo lỗi

| Lỗi | Xử |
|---|---|
| `⛔ Không nhận ra khuôn file hội thoại` | File không đúng khuôn — xem `id-B §2` |
| `⛔ Không còn hội thoại nào sau khi loại … ngoài phạm vi` | Cả file là khách nội địa — ⛔ đây là dữ liệu của bản nội địa, không phải bản QT |
| `⛔ Chưa có out/doc-hoi-thoai.json` | Chạy `id.py doc` trước |
| Tiếng Việt vỡ trên Windows | `set PYTHONIOENCODING=utf-8` trước khi chạy |
| Dashboard báo *"Không tải được danh sách kỳ"* | Chưa chạy `bao-cao`, hoặc đang mở bằng `file://` thay vì máy chủ tĩnh |
| Dashboard hiện tab trống / báo lỗi dựng phần | File kỳ là schema **bản nội địa** — ⛔ hai schema không đọc chéo |
