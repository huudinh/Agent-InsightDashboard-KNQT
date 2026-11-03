# id-B · ĐỌC ĐẦU VÀO — BA DÒNG DỮ LIỆU

> Agent nhận **ba dòng dữ liệu**. Dòng ① bắt buộc. Dòng ② nên có. Dòng ③ hiện **chưa có** — khung đã dựng sẵn, chờ cấp.
>
> ⚠️ Khác bản nội địa ở ba chỗ: hội thoại đến từ **7 kênh** chứ không phải 3 · mỗi hội thoại phải khai được **thị trường + ngôn ngữ + múi giờ** · số ads phải **cắt theo thị trường** mới đọc được.

---

## 1. BA DÒNG

| Dòng | Nguồn | Trạng thái | Thiếu thì sao |
|---|---|---|---|
| ① **Hội thoại chat khách quốc tế** | WhatsApp · Telegram · Viber · Line · KakaoTalk · Zalo · Messenger *(xuất qua Caresoft hoặc xuất tay)* | ✅ Có thật | ⛔ Không chạy được gì |
| ② **Chỉ số quảng cáo Meta / Google cắt theo thị trường** | Bản xuất của khối Ads, **có cột `market`** | 🟠 Có nhưng **thường thiếu cột `market`** | Chạy được tab Phễu + Chấm điểm, ⛔ mất tab Marketing & ma trận có điểm |
| ③ **Chỉ số Google Ads (search term)** | 🔴 **[CHỜ CẤP]** | ⛔ Chưa có | Tab Marketing–Google ghi `⚠ chưa có dữ liệu`, ⛔ không suy đoán |

⚠️ **Dòng ② thiếu cột `market` là tình huống mặc định, không phải ngoại lệ.** Khi đó: ⛔ **không gán số ads cho một tầng nào**, ghi `⚠ số ads chưa cắt theo thị trường — chỉ đọc được ở mức tổng`, và đưa *"xin bản xuất có cột market"* lên mục việc hệ thống.

---

## 2. DÒNG ① — HỘI THOẠI

### Khuôn file (Markdown — giống bản nội địa, thêm ba trường)

```
### <a id="ht-1"></a>1. <Tên khách>

_Cập nhật: 2026-10-13 14:46:52 · NV: <Tên nhân viên> · SĐT: Có|Không · ID: t_xxxxx_
_Kênh: WhatsApp · Nước: AU · Ngôn ngữ: EN_          ← ★ dòng của bản quốc tế

- `10-13 14:26` **KH:** <nội dung>
- `10-13 14:29` **NV <Tên nhân viên>:** <nội dung>
```

★ **Dòng thứ hai là dòng của bản quốc tế.** Thiếu nó thì agent vẫn chạy được: `tt` suy ra từ chữ của khách (§3), nhưng **độ tin cậy thấp hơn** và phải ghi nhãn `tt: suy ra`.

| Trường | Bắt buộc | Dùng để |
|---|---|---|
| Mã hội thoại | ✅ | Truy ngược — mọi hook, mọi điểm trừ phải chỉ về được `HT-nnn` |
| Dấu thời gian từng tin | ✅ | SLA **theo giờ ICT** · ô trong giờ/ngoài giờ (`id-L` §4) |
| `KH:` / `NV <tên>:` | ✅ | Tách hai nửa hội thoại · gán nhân viên |
| Có thông tin liên hệ hay không | ✅ | Chỉ số lõi `% có liên hệ` |
| ★ **Kênh** | 🔶 nên có | Bảng cắt ③ của `id-L` §8. Thiếu → suy từ khuôn file, ghi `kênh: chưa rõ` |
| ★ **Nước / market** | 🔶 nên có | **CỔNG M.** Thiếu → suy ra (§3), không suy được → `TT-0` |
| ★ **Ngôn ngữ** | ⬜ tự suy ra | Suy từ chữ của khách — đáng tin, ⛔ không cần khai |
| Page / nguồn quảng cáo | 🔶 nên có | Nối hội thoại ↔ nội dung ads (`id-E` §6) — **chỉ Messenger** |
| Dịch vụ khách hỏi | ⬜ tự suy ra | Hệ số giá trị đơn · luật combo. ⛔ **Không** dùng để gán chân dung, ⛔ **không** dùng để suy tầng |

### ⛔ Mười hai thứ phải bỏ trước khi ghi ra bất cứ đâu

Bản nội địa bỏ 8 thứ. Bản quốc tế bỏ **12** — bốn thứ thêm vào là dữ liệu đặc thù của khách bay sang:

```
tên thật khách · số điện thoại (kể cả mã quốc gia) · ảnh khách · email
địa chỉ nhà · link cá nhân · mã đơn hàng · tên người nhà khách nhắc tới
★ số hộ chiếu            ★ quốc tịch cụ thể của một cá nhân
★ số hiệu chuyến bay      ★ tên khách sạn khách đang ở / sẽ ở
```

⚠️ **Vì sao bỏ quốc tịch cá nhân mà vẫn giữ tầng thị trường.** `TT-C · AU` là một **nhóm**; *"nữ Việt kiều Úc 42 tuổi ở Melbourne, bay 12/12"* là một **con người cụ thể**. Nhóm thì đưa vào báo cáo được; con người thì không.

⛔ **Và ⛔ không nạp ảnh khách · ảnh hộ chiếu · hồ sơ bệnh án vào bất kỳ công cụ AI nào** — gồm cả agent này (`id-K` §6 `L12`).

### Mười một ô tự suy ra, ⛔ không hỏi người dùng

`mức nóng` · `chặng S1–S7` · `mã O` · `mã OQ` · `rào cản` · `vì sao rơi` ·
`có chốt lịch trong chat không` · `tin đầu khách hỏi gì` · `ngôn ngữ khách` · `ngôn ngữ nhân viên trả lời` · `trong giờ / ngoài giờ ICT`

⚠️ **Hai ô KHÔNG nằm trong danh sách này:**

```
① chân dung CD → phác họa từ chữ của khách rồi người dùng duyệt ở CỔNG 0
                  (id-C §1-2). Trước khi duyệt: cd = null.
② tầng TT      → suy ra được, NHƯNG phải in ra bảng "căn cứ suy" và chờ
                  người dùng xác nhận ở CỔNG M nếu TT-0 ≥ 20% mẫu (id-L §1).
```

---

## 3. ★ SUY TẦNG THỊ TRƯỜNG TỪ HỘI THOẠI — khi file không khai

Chạy **theo đúng thứ tự này**, dừng ở dòng khớp đầu tiên. ⛔ Không đảo thứ tự.

| # | Dấu hiệu | Kết luận | Độ tin |
|---|---|---|---|
| 1 | File khai `Nước:` | lấy đúng theo khai | ✅ **chắc** |
| 2 | Khách tự nói nước/thành phố mình đang ở *("I'm in Sydney", "em ở bên Mỹ")* | theo nước đó | ✅ chắc |
| 3 | Khách nhắn **tiếng Việt** + nói *"về nước"* · *"về Tết"* · *"em ở bên …"* · *"bay về"* | **`TT-B`** | ✅ chắc |
| 4 | Khách nhắn EN + hỏi *"living in Hanoi/HCMC"* · *"I live here"* · *"this week"* + ⛔ không hỏi gì về bay | **`TT-D`** | 🔶 khá |
| 5 | Khách nhắn EN + hỏi *"how many days"* · *"flight"* · *"visa"* · *"from Australia/UK/US…"* | **`TT-C`** | 🔶 khá |
| 6 | Khách nhắn **Khmer / Bahasa**, hoặc EN + nhắc KH · LA · MM · ID · PH · MY · IN | **`TT-A`** | 🔶 khá |
| 7 | Kênh là **KakaoTalk / Line** mà không có dấu hiệu khác | `TT-A` *(KR/JP/TW)* · ghi `suy từ kênh` | ⚠️ yếu |
| 8 | Không khớp dòng nào | **`TT-0`** | — |

```
⛔ BA CÁCH SUY TẦNG SAI, hay gặp:
① Suy từ DỊCH VỤ khách hỏi        → dịch vụ không nói gì về vị trí.
② Suy từ NGÔN NGỮ một mình        → tiếng Việt có thể là TT-B (kiều bào)
                                     HOẶC khách nội địa nhắn lạc vào page QT.
③ Suy từ TÊN THÀNH PHỐ trong câu  → "plastic surgery in Hanoi" là NƠI MỔ,
                                     không phải NƠI KHÁCH ĐANG Ở (id-L §2).
```

⚠️ **Khách nội địa nhắn lạc vào kênh quốc tế là chuyện có thật và phải đếm riêng.** Dấu hiệu: tiếng Việt, ⛔ không nhắc gì đến ở nước ngoài / về nước / bay. Xử lý: **loại khỏi mẫu phân tích**, ghi vào ô *"ngoài phạm vi — chuyển bản nội địa"*, ⛔ không xếp vào `TT-B`.

---

## 4. DÒNG ② — CHỈ SỐ QUẢNG CÁO CẮT THEO THỊ TRƯỜNG

Cột tối thiểu:

| Cột | Kiểu | Ghi chú |
|---|---|---|
| `ngay` | ngày | |
| `chien_dich` | chữ | Tên theo quy ước ở `id-E` §2 |
| ★ `market` | chữ | **Mã thị trường** theo `id-L` §9. ⛔ Thiếu cột này → ⛔ không gán số cho tầng nào |
| ★ `tt` | chữ | `TT-A/B/C/D` — suy được từ `market`, nên không bắt buộc |
| ★ `geo_mode` | chữ | `Presence` hoặc `Presence+Interest`. ⚠️ `TT-D` **phải** là `Presence` |
| `tai_khoan` · `fanpage` | chữ | |
| `chi` | số | **Chỉ lấy cột Chi theo chiến dịch** |
| `hien_thi` · `click` | số | Để tính CTR |
| `inbox` | số | Hội thoại tin nhắn bắt đầu |
| `lead` | số | Liên hệ hợp lệ *(số ĐT có mã quốc gia / WhatsApp / email)* |
| `booking` | số | |
| ★ `den_kham` | số | **Khách đã đến khám thật** — ⚠️ chỉ số thật của tầng B/C |
| `nhan_vien_chay` | chữ | Người chạy ads — ⛔ **không phải** nhân viên trực kênh |

### Chuỗi chỉ số bắt buộc giữ đúng thứ tự

```
Chi phí tổng → CPM → CTR → CPI (Inbox) → CPL (Lead) → CPB (Booking)
→ ★ CPA-KHÁM (chi phí trên một khách ĐÃ ĐẾN KHÁM)
```

Mỗi mắt xích hiển thị **ba thứ**: giá trị · so **mục tiêu** · so **kỳ trước**.

★ **Mắt xích cuối là mắt xích của bản quốc tế.** Với `TT-B/TT-C`, `CPL` gần như vô nghĩa nếu đứng một mình: độ trễ lead → khám là **4–12 tuần** (`id-L` §4), nên một kỳ có CPL rẻ mà không ai bay sang là **kỳ tệ**, không phải kỳ tốt.

⚠️ **Hai luật đo của bản quốc tế:**

```
① ⛔ KHÔNG đánh giá chiến dịch TT-B/TT-C trong cửa sổ ngắn hơn 8 TUẦN.
② ⛔ KHÔNG so chéo CPL giữa hai thị trường khác nhau — khác giá chấp nhận
   được, khác luật quảng cáo, khác CPM. So AU với KH là so hai thế giới.
```

⚠️ **Tiền:** số VND quy về **nghìn đồng**; nếu bản xuất là USD thì **giữ USD** và ghi đơn vị ở đầu bảng — ⛔ không tự quy đổi, ⛔ không trộn hai đơn vị trong một bảng.

---

## 5. DÒNG ③ — GOOGLE ADS · 🔴 KHUNG CHỜ DỮ LIỆU

> Agent **đã có sẵn khối đọc**; chỉ thiếu file. Có file thì thả vào `du-lieu/google-ads.csv` đúng cột dưới đây là chạy được ngay.

| Cột | Khớp với cột Meta |
|---|---|
| `ngay` · `chien_dich` | `ngay` · `chien_dich` |
| ★ `market` · `geo_mode` | `market` · `geo_mode` |
| `nhom_quang_cao` | — |
| ★ `tu_khoa` / `search_term` | **không có đối ứng bên Meta** — giá trị riêng của Google |
| `loai_doi_sanh` | — |
| `chi` · `hien_thi` · `click` | như Meta |
| `chuyen_doi` · `loai_chuyen_doi` | ≈ `lead` |
| `diem_chat_luong` · `ty_le_hien_thi_top` | — |

### Bốn câu Google Ads trả lời được mà Meta không — bản quốc tế

```
① Khách gõ CHỮ GÌ bằng NGÔN NGỮ NÀO trước khi vào.
② Truy vấn nào đang tốn tiền mà không ra chuyển đổi — cắt được ngay.
③ Truy vấn nào có người tìm mà Kangnam chưa có trang EN trả lời
   → bàn giao Agent-AdsOptimize-Kangnam-QT (mode GEO-ANSWER).
④ ★ Truy vấn chặng S4 ("how many days in vietnam after rhinoplasty",
   "english speaking surgeon hanoi") — chặng CẠNH TRANH THẤP NHẤT mà
   gần như không ai làm trang trả lời.
```

★ Khi dòng ③ về, **search term đổ thẳng vào bảng mã `O`/`OQ`** ở `id-D` như một nguồn thứ hai bên cạnh hội thoại.

⛔ **Cho tới lúc đó:** mọi ô Google Ads để `null`, hiển thị `chưa có dữ liệu`. ⛔ Không ước lượng, ⛔ không lấy số Meta gán sang.

---

## 6. KIỂM ĐẦU VÀO — IN RA TRƯỚC KHI CHẠY

```
CỠ MẪU
  Đã đọc            : <n> hội thoại
  Loại khỏi phân tích: <n>  (lý do: trùng · dưới 2 tin · ngoài kỳ ·
                             ★ khách nội địa nhắn lạc vào kênh quốc tế)
  Còn lại           : <n>

★ THỊ TRƯỜNG
  TT-A <n> · TT-B <n> · TT-C <n> · TT-D <n> · TT-0 <n> (<pct>%)
  Căn cứ suy        : khai sẵn <n> · khách tự nói <n> · suy từ chữ <n> · suy từ kênh <n>
  ⚠ TT-0 ≥ 20% → CỔNG M: in bảng này ra và chờ người dùng xác nhận

★ NGÔN NGỮ         : EN <n> · VI <n> · KM <n> · AR <n> · XX <n>
★ KÊNH             : <kênh> <n> · …
★ MÚI GIỜ          : trong giờ 8–17 ICT <n> · ngoài giờ <n> (<pct>%)

KỲ                 : <tu> → <den>
NGUỒN              : <tên file / xuất lúc nào>
DÒNG ②             : có / không — nếu có: CÓ cột market? <có/không>
DÒNG ③             : ⚠ chưa có
MỐC SO SÁNH        : kỳ trước <có/không> · mục tiêu 30 ngày <có/không>
★ R8               : ✅ đã xác nhận / 🔴 [CHỜ CẤP]   (id-K §5)
```

⚠️ **Kỳ trước chồng lấn kỳ này** thì vẫn so được nhưng phải ghi *"trùng x/y ngày — chỉ để tham khảo"*.

---

## 6b. ★★ TIỀN SỬ ĐIỀU TRỊ LÀ **DỮ LIỆU SỨC KHOẺ** — VÀ Ở BẢN QUỐC TẾ NÓ CÓ **HAI TẦNG**

> ⚠️ Mục này ⛔ **không phải chuyện ẩn danh** — nó là chuyện **loại dữ liệu**. Và nó là mục mà bản quốc tế nặng hơn bản nội địa, vì dữ liệu còn **đi qua biên giới**.

Những thứ sau, trong hội thoại thẩm mỹ, là **dữ liệu sức khoẻ**:

```
tiền sử can thiệp ("I had rhinoplasty 3 years ago, it collapsed")
bệnh nền khách tự nêu · thuốc đang dùng · tình trạng mang thai
ảnh vùng cần làm · ảnh before–after của chính khách
chẩn đoán hoặc phác đồ nơi khác đã đưa ra
```

### Tầng ①: luật Việt Nam — **áp cho MỌI hội thoại**

**Luật 91/2025/QH15.** Ba luật vận hành:

| | Luật | Nghĩa trong repo này |
|---|---|---|
| ① | **Chỉ lưu NHÃN + câu bằng chứng ngắn** | Lưu mã `OQ-xx` / `O-xx` + **một câu** đủ chứng minh. ⛔ Không chép cả đoạn khách kể bệnh sử |
| ② | **Giới hạn người xem** | Ô này ⛔ không đi vào bản phát ra ngoài khối. Sổ tay chỉ giữ **đúng cặp câu** làm bằng cho ô `✗` đang xét |
| ③ | **Cần đồng ý xử lý** | ⛔ Không đưa ảnh khách vào bất cứ file nào. ⛔ Không nạp lên công cụ công cộng |

### Tầng ②: luật nước người xem — **cộng thêm, ⛔ không thay thế**

★ `id-K` §4 đã có bảng này. Hai điểm phải nối vào đây:

```
EU/EEA · UK  → dữ liệu sức khoẻ là SPECIAL CATEGORY (GDPR Art. 9).
               Cần cơ sở xử lý RIÊNG, ⛔ không dùng chung cơ sở "hợp đồng".
               → chưa có privacy notice đạt GDPR thì mọi lead EU/UK
                 vướng `L12`, và tiêu chí `N7.7` chấm theo đó.
MỌI THỊ TRƯỜNG NGOÀI VN → phải nêu việc CHUYỂN DỮ LIỆU SANG VIỆT NAM.
               ⛔ Không nêu là một thiếu sót pháp lý, ⛔ không phải
                 một ô trống trong form.
```

⚠️ **Hệ quả ngược mà dễ bỏ sót:** `N2` yêu cầu nhân viên **khai thác tình trạng**, và `N7` yêu cầu khai thác **đúng thị trường**. Hai tiêu chí đó bắt nhân viên **thu dữ liệu sức khoẻ của người nước ngoài**. Nghĩa là:

> ⛔ **Chưa có privacy notice đạt GDPR thì việc chấm `N2` cao cho một hội thoại EU/UK là đang khen một việc lẽ ra ⛔ chưa được phép làm.**
> → Khi `L12` còn treo, hội thoại `EU`/`UK` ghi thêm nhãn `⚠ thu dữ liệu khi L12 chưa gỡ` vào `loi_he`, và việc đó vào **mục việc hệ thống**, ⛔ không vào điểm của người.

★ Nhân viên **phải hỏi** (`N2`) nhưng báo cáo **chỉ lưu nhãn**. Hai việc khác nhau — hỏi là đúng, lưu nguyên văn bệnh sử là sai.

---

## 7. QUY ƯỚC MÃ — ⛔ KHÔNG ĐỔI

| Mã | Nghĩa | Định nghĩa ở |
|---|---|---|
| `HT-nnn` | Một hội thoại | sổ này |
| ★ `TT-A … TT-D` | Tầng thị trường · `TT-0` = chưa khai được | `id-L` §1 |
| ★ `AU · US · KH · VN-EXPAT · VN-DIASPORA-<nước>` | Mã thị trường | `id-L` §9 |
| ★ `S1 … S7` | Chặng phễu quốc tế | `id-C` §3 |
| `CD0` | Mã **dự trữ** — hội thoại không khớp dấu hiệu chân dung nào. ⛔ Không phác họa, ⛔ không đổi nghĩa | `id-C` §1 |
| `CD1 … CDn` | Chân dung **của từng kỳ** | `id-C` §1 · `out/chan-dung.json` |
| `O-01 … O-12`, `O-00` | 12 mã phản đối dùng chung cả hệ | `id-D` §1 |
| ★ `OQ-01 … OQ-08` | **8 mã phản đối chỉ có ở khách quốc tế** | `id-D` §2 |
| `SỢ · NGỜ · NGẠI · XA` | Bốn rào cản chốt | `id-D` §6 |
| `L01 … L16` | Format thể hiện | `id-H` |
| `N1 … N7` | **Bảy** nhóm tiêu chí chấm nhân viên | `id-F` |
| `CĐ-1 … CĐ-10` | **Mười** cờ đỏ trong hội thoại | `id-F` §5 |
| `R2 · R3 · R7 · R8 · R9` | Rào pháp lý dùng chung với gói ads QT | `id-K` §5 |

★ Các mã này **được tham chiếu chéo trong repo này và ở `Agent-AdsOptimize-Kangnam-QT`**. Đổi tên mã = hỏng cả hệ.

⚠️ Ngoại lệ duy nhất là `CD1 … CDn`: **nội dung** đổi theo kỳ, chỉ **khuôn mã** là cố định. Gửi số liệu theo chân dung cho người khác thì gửi kèm `out/chan-dung.json` của kỳ.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Đã in bảng **cỡ mẫu** và lý do loại chưa?
- [ ] ★ Đã in **bảng thị trường + căn cứ suy** chưa? `TT-0` bao nhiêu %?
- [ ] Có HT nào suy tầng từ **dịch vụ** hoặc từ **tên thành phố trong câu** không?
- [ ] Có khách nội địa nhắn lạc nào bị xếp vào `TT-B` không?
- [ ] Đã bỏ hết **12 thứ** ở §2 chưa — gồm hộ chiếu, chuyến bay, khách sạn?
- [ ] Số ads có cột `market` không? Không có mà vẫn gán cho tầng nào không?
- [ ] Có so chéo CPL giữa hai thị trường không?
- [ ] Có bảng nào trộn **VND và USD** không?
- [ ] Đã in dòng xác nhận **`R8`** chưa?
