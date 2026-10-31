# CHANGELOG

## v1.0 — 2026-10-31 · DỰNG MỚI BẢN QUỐC TẾ

Dựng `Agent-InsightDashboard-KNQT` từ `Agent-InsightDashboard-Kangnam` `v1.1`.

> ★ **Đây không phải bản dịch.** Bảy thứ dưới đây là thay đổi **logic**, không phải đổi tên. Giữ nguyên lõi *(phác họa chân dung qua CỔNG 0 · luật truy ngược · bốn rào an toàn của điểm số · luật một lần chấm)*, thay phần phụ thuộc **vị trí · ngôn ngữ · múi giờ · pháp lý**.

---

### ① ★ Thêm CỔNG M — không có thị trường thì không kết luận

Bản nội địa có 3 cổng. Bản này có **4**: thêm `CỔNG M` nằm trong `B1`.

```
Cùng câu "How much is rhinoplasty in Hanoi?"
  gõ từ Sydney    = TT-C — cần giá · an toàn · số ngày ở lại · bảo hành từ xa
  gõ từ Hà Nội    = TT-D — cần địa chỉ · bác sĩ nói tiếng Anh · hẹn tuần này
  tiếng Việt từ Sydney = TT-B — cần lịch khớp chuyến về · người nhà không biết
Một câu trả lời cho cả ba → mất cả ba.
```

→ Sổ lõi mới **`id-L` · Tầng thị trường · ngôn ngữ · múi giờ · kênh** *(không có tương đương ở bản nội địa)*. Mọi tỷ lệ phải cắt được theo tầng; tầng <10 HT ⛔ không kết luận riêng; `TT-0` ≥ 20% → dừng chờ xác nhận.

### ② ★ Phễu `5A` → `S1–S7`, và `S4` là chặng quyết định

Dùng chung hệ chặng với `Agent-AdsOptimize-Kangnam-QT`. Chặng thêm vào quan trọng nhất là **`S4` · lên kế hoạch chuyến đi** — chặng khách rụng nhiều nhất mà **gần như không ai đo**, vì nó xảy ra **sau khi lead đã vào CRM**.

```
Khách quốc tế quyết định HAI thứ: "có mổ không" VÀ "có bay không".
Phép thử mới của một hội thoại:
  "đọc hết hội thoại này, khách có đủ thông tin để mở app hàng không
   và chọn ngày bay chưa?"
Chưa → hội thoại chưa xong, dù khách đã cho số.
```

→ Thẻ số tổng mới **`S4 chưa đóng`**. Khối ma trận mới **② MỞ CHẶNG `S4`**, đứng **thứ hai** — trước cả *Giảm COLD*.

### ③ ★ Thêm 8 mã `OQ` — và sáu trong tám đang bị chặn vì thiếu dữ kiện

12 mã `O` giữ nguyên *(dùng chung cả hệ)*. Thêm `OQ-01`…`OQ-08`: số ngày ở lại · ai lo khi về nước · phiên dịch · ai trả phí chỉnh sửa · visa · thanh toán · hậu cần · điều kiện văn hoá.

⚠️ **`OQ-01` là mã nặng nhất của cả repo** và ⛔ agent không được tự trả lời: số ngày được phép bay là **mốc y khoa**, bay quá sớm sau phẫu thuật là **rủi ro thật**.

⚠️ Và: câu *"how many days do I stay"* mà gán vào `O-09` thì **xoá mất chặng `S4`** khỏi báo cáo — tổng vẫn khớp nên ⛔ không ai nhìn ra.

### ④ ★ `N1`–`N6` → `N1`–`N7`, và SLA tính theo múi giờ

| Chỗ | Nội địa | Quốc tế |
|---|---|---|
| Ngưỡng SLA | 2′ | **5′** — khách quốc tế hỏi câu dài hơn, cần tra dữ kiện hơn |
| Khung giờ | 8h30–22h | **08:00–17:00 ICT** *(giờ công bố trên site)* |
| Tin ngoài khung | — | `N1.1` = `—`, và phần dọn hộp thư ngoài giờ chấm riêng ở **`N7.4`** *(trong 12h)* |
| Trọng số `N1` | 20 | **15** — phần dôi chuyển sang `N7` |
| Nhóm mới | — | **`N7` · Năng lực quốc tế** *(10đ)*: hỏi khách ở đâu · đúng tầng · đúng ngôn ngữ · dọn hộp thư ngoài giờ · ghi múi giờ · **xử đúng `OQ-01` mà không tự nêu số** |

★ **Vì sao tách `N1.1` và `N7.4`:** trả lời trong 5 phút lúc 3 giờ sáng ⛔ không phải việc của nhân viên — đó là việc của **lịch trực**. Nhưng *"đến 11h trưa hôm sau vẫn chưa ai mở tin của khách UK"* **là** việc của nhân viên. Gộp hai thứ này là cách chắc chắn nhất để **vừa trừ điểm sai người, vừa bỏ qua lỗi thật**.

### ⑤ ★ `N3.1` NGƯỢC HẲN bản nội địa — vì giá đã công khai

```
Nội địa : giá CHƯA công khai → né giá phần lớn là LỖI HỆ → chấm "—"
Quốc tế : giá ĐÃ công khai tại /price-list/ → né giá là LỖI NGƯỜI → ✗
```

Và thêm tiêu chí **`N3.2` · nêu phụ phí quốc tế 10%** — thiếu dòng đó là **cờ đỏ `CĐ-7`**: khách phát hiện ở quầy thanh toán thì mất cả ca **và** nhận một review xấu.

### ⑥ ★ 6 cờ đỏ → 10, và pháp chế thành HAI TẦNG

Bốn cờ mới: `CĐ-7` *(bỏ phụ phí 10%)* · `CĐ-8` *(nhắc viện tỉnh)* · `CĐ-9` *(dịch máy y khoa)* · `CĐ-10` *(so giá có tên nước)*. `CĐ-5` đổi nghĩa thành **hứa số ngày ở lại** — cờ nặng nhất của bản này. `CĐ-2` mở rộng sang chữ *"lifetime"*.

★ **Ba cờ `CĐ-5` · `CĐ-7` · `CĐ-9` là cờ người ta cắm vào khi ĐANG CỐ GIÚP KHÁCH** → phải vào **đào tạo cả nhóm**, ⛔ không chỉ vào sổ tay cá nhân.

`CỔNG 2` giờ soát **hai tầng**: luật Việt Nam **và** luật nước người xem *(AHPRA · ASA · FTC · GDPR · GCC)*, cộng dòng xác nhận **`R8`** — đủ điều kiện KCB cho người nước ngoài. `R8` ⛔ không phải rào câu chữ, nó là **điều kiện hoạt động**: lead đổ về khi chưa đủ `R8` là **rủi ro, không phải thành tích**.

### ⑦ ★ Chỉ số thêm `CPA-KHÁM` và cửa sổ đo ≥8 tuần

Độ trễ lead → đến khám của `TT-B`/`TT-C` là **4–12 tuần**. → ⛔ không đánh giá trong cửa sổ ngắn hơn 8 tuần, và ⛔ không đặt `CPL` kỳ này cạnh `CPA-KHÁM` như thể chúng nói về cùng một tệp khách.

Và thêm một bước phân rã **trước** bốn thành phần của `CPL`: **kiểm cơ cấu thị trường**. Chuyển chi từ `KH` sang `AU` thì CPM tăng, CPL tăng, mà **không có gì xấu đi cả** — đó là một quyết định ngân sách, không phải một sự cố.

---

## Bảng đối chiếu nhanh

| | Nội địa `v1.1` | Quốc tế `v1.0` |
|---|---|---|
| Sổ tri thức | 11 *(`id-A`…`id-K`)* | **12** *(thêm `id-L`)* |
| Prompt mẫu | 8 | **9** *(thêm `prompt-thi-truong-mui-gio`)* |
| Cổng chặn | 3 | **4** *(thêm `CỔNG M`)* |
| Phễu | `A1`–`A5` | **`S1`–`S7`** |
| Mã phản đối | 12 `O` | 12 `O` + **8 `OQ`** |
| Rào cản chốt | 3 | **4** *(thêm `XA`)* |
| Nhóm tiêu chí | `N1`–`N6` *(22 tiêu chí)* | **`N1`–`N7`** *(27 tiêu chí)* |
| Cờ đỏ | 6 | **10** |
| Tab dashboard | 9 | **10** *(thêm ★ Thị trường & kênh)* |
| Thẻ số tổng | 6 | **8** *(thêm `S4 chưa đóng`, `HOT/WARM ngoài giờ >12h`)* |
| Khối ma trận | 3 | **4** *(thêm `MỞ CHẶNG S4`)* + nhóm `⏸ CHỜ CẤP` |
| Tầng pháp lý | 1 | **2** |
| Schema | `insight-dashboard-kangnam/1` | `insight-dashboard-knqt/1` |
| Cơ sở | 7 *(có bẫy TUYẾN)* | **2, cả hai tuyến bệnh viện** |
| Giá | 🔴 chưa công khai | ✅ **công khai** tại `/price-list/` |

---

## ⚠ Việc còn lại

| # | Việc | Ai | Chặn gì |
|---|---|---|---|
| ★ ① | **Số ngày ở lại Việt Nam** theo 7 dịch vụ | Khoa Chuyên môn | 🔴 `OQ-01` · `N7.6` · `CĐ-5` · mọi hook `S4`. **Chặn lớn nhất** |
| ② | **T&C bảo hành** *(site đang ghi "lifetime warranty")* | Pháp chế | 🔴 `O-07` · `OQ-04` · `CĐ-2` |
| ③ | **`R8`** — đủ điều kiện KCB cho người nước ngoài | Pháp chế + Điều phối QT | 🔴 toàn bộ site EN |
| ④ | **Lịch trực theo múi giờ** cho `TT-C` *(UK/EU/US)* | Vận hành + Điều phối QT | 🔴 mọi ô SLA ngoài giờ |
| ⑤ | **Một dòng dùng chung cho cả hai site** về claim hội–hiệp hội | Pháp chế | 🔴 `CĐ-4` |
| ⑥ | **Visa · thanh toán quốc tế · ngôn ngữ phiên dịch** | Điều phối QT | 🟠 `OQ-03` · `OQ-05` · `OQ-06` |
| ⑦ | **Privacy notice đạt GDPR** | Pháp chế | 🔴 `L12` — mọi lead EU/UK |
| ⑧ | **Bản xuất ads có cột `market`** | Khối Ads | 🟠 ⛔ không gán được số cho tầng nào |
| ⑨ | **Mốc mục tiêu TB 30 ngày theo từng thị trường** | Khối Ads | 🟠 mọi chỉ số ghi `⚠ chưa có mốc so sánh` |
| ⑩ | **Dữ liệu Google Ads** | Khối Ads | 🟠 tab ⑥ trống — khung đọc đã dựng |
| ⑪ | **Mẫu sổ tay chính thức** | Người dùng | 🟠 khuôn `ST-CN` hiện là bản dựng tạm |

---

## Ghi chú kỹ thuật

- **Từ điển song ngữ.** `tools/tu_dien.json` có cả cụm EN và VI cho mọi mã; thêm ba khối mới: `ma_oq` · `thi_truong` *(nước → market → tầng)* · `ngon_ngu` + `kenh`.
- **Ẩn danh 12 thứ** *(nội địa: 8)*. Bốn thứ thêm: hộ chiếu · quốc tịch của một cá nhân · số hiệu chuyến bay · tên khách sạn. Và regex số điện thoại đã mở rộng cho **mã quốc gia**.
- **Khách nội địa nhắn lạc** vào kênh quốc tế được đếm riêng và **loại khỏi mẫu** — ⛔ không xếp vào `TT-B`.
- **Khối `facebook` đổi tên thành `meta`** trong schema. ⛔ Hai schema không đọc chéo được.
- **Bốn format `L13`–`L16`** ở bản nội địa còn `[CHỜ CẤP]` thì ở bản này **được định nghĩa**: 5 bước khách xa · phiên dịch & hậu phẫu từ xa · hậu cần · giấy phép — đây là bộ format **sạch pháp chế ở mọi thị trường**, và là trụ format duy nhất dùng được cho `TT-C`.
