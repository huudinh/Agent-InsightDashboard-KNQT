# CHANGELOG

## v1.1 — 2026-10-31 · CHẠY THẬT TRÊN 119 HỘI THOẠI AI CHATBOX

Kỳ thật đầu tiên: **04/09–31/10/2026**, 127 hội thoại Quốc Tế xuất từ AI Chatbox, 119 vào mẫu phân tích.

### Ba artifact đã publish

| | Link | Dạng |
|---|---|---|
| 📘 Trang hướng dẫn | <https://claude.ai/artifact/E5U9He8ox1xmzxUz4hWN7E> | trang HTML sinh từ `tools/huong-dan.json` |
| 📈 Báo cáo kỳ 04/09–31/10 | <https://claude.ai/artifact/UnEJMD37Lc3ydC31skNSwH> | `dashboard/index.html` + JSON kỳ nhúng |
| 📋 Kế hoạch nội dung 11/2026 | <https://claude.ai/artifact/X1NaLkUJveCxtkY4sAL53Y> | **doc** — sửa và comment trực tiếp |

⚠️ Cả ba đang ở chế độ *"ai có link đều mở được"*. Báo cáo và kế hoạch chứa lời khách *(đã ẩn danh)*, tên bác sĩ và kết luận pháp chế nội bộ — ⛔ nếu repo là public thì gỡ hai link đó khỏi README hoặc đổi artifact về riêng tư.

★ **Kế hoạch nội dung là bản `ST-ND` của `id-I §5` viết ra thành tài liệu**, không phải một tab mới của dashboard: 6 ô chia **3 cụm làm được ngay / 3 ô chờ dữ kiện** · bảng 14 hook · cờ pháp chế hai tầng · hình **2x2 đòn bẩy × độ chặn** · 5 con số đo kỳ sau. Dạng doc để Content sửa thẳng và comment vào từng ô.

### Thêm `tools/doi-khuon-chatbox.py`

Bản xuất `GET /api/conversations` của AI Chatbox có khuôn riêng → đổi sang khuôn `id-B §2`, và **suy `Nước:` từ mã quốc gia của số điện thoại** *(căn cứ chắc nhất có trong dữ liệu — `id-B §3` dòng 1)*.

★ **Và nó ghi rõ ba điều về dữ liệu này:** người trả lời là **bot**, không phải nhân viên → mọi điểm `N` là điểm của **câu trả lời của bot**, đầu ra đi về **người huấn luyện bot**, ⛔ không vào sổ tay cá nhân · SLA của bot luôn đạt nên `N1` và `N7.4` ⛔ không đọc được như báo cáo trực kênh · ô *"ngoài giờ"* ở đây là chỉ số về **khách**, không về lịch trực.

### Bốn lỗi của chính bộ công cụ, phát hiện khi chạy thật

| Lỗi | Hậu quả nếu để nguyên | Sửa |
|---|---|---|
| Nhận ngôn ngữ **bỏ dấu** rồi so | Tên bác sĩ Việt trong câu tiếng Anh khớp *"chị · mình · giá"* → **46 HT bị gắn oan** *"hệ thống — ngôn ngữ"* | `dem_dau_viet()` — so chữ **có dấu**, ngưỡng 2 (khách) / 3 (NV) |
| Số điện thoại không có `+` | `2813894741` thành *"+281"* → **gán sai tầng**, đúng lỗi im lặng mà `id-L §2` cảnh báo | Nhận NANP theo mã vùng; nước ngoài schema thì **gọi đúng tên, để trống mã** |
| `O-00` nuốt cả câu hỏi dịch vụ thuần | O-00 phình lên **51%** che mất tín hiệu thật | Thêm `hoi_thong_tin` → tách `(chưa nêu)`; O-00 còn 26% |
| `OQ-01` không bắt *"safe to fly … after rhinoplasty"* | **Bỏ sót đúng mã quan trọng nhất của repo** — HT-021 là ví dụ | Thêm 11 cụm: `safe to fly` · `fly after` · `day 14` · `travel after`… |

⚠️ `O-00` vẫn **26,1% > ngưỡng 10%** của `id-D §1` → **báo lại**, ⛔ agent không tự thêm mã.

### Thêm cờ đỏ nhận bằng LOGIC

- ★ **`CĐ-4` theo danh sách bác sĩ.** `tu_dien.json` → `bac_si_duyet_qt` *(5 bác sĩ của site quốc tế)*. Bot/nhân viên gắn tên ngoài danh sách → cờ. Kỳ đầu: **60 lần, 25 cách viết tên, ⛔ không một ai trong 5 người**.
- `CĐ-8` mở rộng: tên 5 viện tỉnh + *"3 hospitals"* · *"branches in"*. Kỳ đầu **14 HT**.

### Tối ưu hiển thị tab Hook cho bản quốc tế

| Bản nội địa | Bản quốc tế |
|---|---|
| Lọc **Dịch vụ · Tuyến · Nhân viên** | ★ Lọc **Tầng · Ngôn ngữ · Rào chốt · Dịch vụ** |
| Cột `Giai đoạn` = nấc `A1–A5` | Cột **`Tầng · ngôn ngữ`** + cột `Chặng` = `S1–S7` |
| Một cờ pháp chế | ★ **Hai cờ**: luật VN và luật nước người xem |
| `L13`–`L16` *"chưa có định nghĩa"* | ★ Đặt tên: 5 bước khách xa · phiên dịch & hậu phẫu từ xa · hậu cần · giấy phép |
| — | ★ Chip **`⏸ chờ dữ kiện`** · format bị chặn ở `TT-C` tự tô đỏ kèm `⛔ chặn ở TT-C` |
| Cột `Win` | Bỏ khi không xếp được điểm Win → *Kế hoạch theo chân dung* sắp theo **số hook** và nói rõ lý do |

### Hai thay đổi nhỏ của trang dashboard

- ★ **File kỳ tự khai `bo_cuc`.** Bản một file *(JSON nhúng vào `#kn-data`)* không có `data/index.json` để đọc bố cục → giờ đọc `bo_cuc` ngay trong file kỳ. Nhờ vậy một báo cáo gửi đi được **là bản `insight` đúng như bản nhiều kỳ**.
- Thẻ số tô đỏ theo **ba ô nguy hiểm của bản quốc tế**: `nong_chua_lh` · `s4_chua_dong` · `nong_ngoai_gio`.

### ⚠ Điều kỳ đầu dạy ra

```
Báo cáo kỳ này KHÔNG xếp được điểm Win. Công thức của id-C §6 nhân với
TỶ LỆ ĐANG CHỐT của chính nhóm — mà cả kỳ chỉ 2/119 khách để lại liên hệ
thật (1,7%), nên mọi nhóm đều ≈ 0.
⛔ Không tự đặt một hệ số thay thế (luật ⑪). Thay vào đó xếp theo ĐỘ CHẶN:
   ô nào đang chờ dữ kiện, ô nào làm được ngay.
```

★ Và con số thô là 3 — nhưng **HT-096 là một bản pentest** *("My name is Test Pentest")*, ⛔ không phải khách. Đã thành việc #11 của kỳ.

---

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
