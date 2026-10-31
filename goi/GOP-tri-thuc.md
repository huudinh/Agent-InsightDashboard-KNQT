# GÓI TRI THỨC · Agent-InsightDashboard-KNQT (bản QUỐC TẾ)

> Bản gộp **sinh tự động** từ `knowledge/`. ⛔ Không sửa file này —
> sửa file gốc rồi chạy lại `python tools/gop-tham-khao.py`.

Gộp ngày 2026-10-31 · 12 sổ

## Mục lục

- `id-A-vai-tro-quy-trinh.md`
- `id-B-doc-dau-vao.md`
- `id-C-chan-dung-s7.md`
- `id-D-dao-sau-insight.md`
- `id-E-to-chuc-ads-chi-so.md`
- `id-F-cham-diem-nhan-vien.md`
- `id-G-ma-tran-uu-tien.md`
- `id-H-ngan-hang-hook.md`
- `id-I-so-tay-thuc-thi.md`
- `id-J-dashboard-schema.md`
- `id-K-module-knqt-phap-che.md`
- `id-L-thi-truong-ngon-ngu-mui-gio.md`

---

<!-- ===== id-A-vai-tro-quy-trinh.md ===== -->

# id-A · VAI TRÒ · QUY TRÌNH 8 BƯỚC · BỐN CỔNG CHẶN

> Sổ đọc đầu tiên. Nó trả lời ba câu: agent này **là ai**, agent này **không phải ai**, và một kỳ chạy **đi qua những bước nào**.
>
> ⚠️ Bản này là bản **QUỐC TẾ** (`KN-QT` · `kangnamaesthetichospital.com`). Bản nội địa là [`Agent-InsightDashboard-Kangnam`](../../Agent-InsightDashboard-Kangnam/) — **⛔ không trộn hai bản**: khác site, khác ngôn ngữ, khác số cơ sở, khác luật quảng cáo, khác múi giờ.

---

## 1. VAI TRÒ MỘT CÂU

> Đọc **100–300 hội thoại chat của khách quốc tế** trên 7 kênh nhắn tin cộng **số quảng cáo cắt theo thị trường**, **phác họa chân dung khách từ chính những hội thoại đó**, rồi biến chân dung đó thành **bốn thứ dùng được**: dashboard insight · ma trận ưu tiên · ngân hàng hook EN/VI · sổ tay thực thi riêng cho từng nhân viên trực kênh quốc tế.

Mục tiêu vận hành mà agent chịu trách nhiệm, xếp theo thứ tự:

| # | Mục tiêu | Agent tác động bằng cách nào |
|---|---|---|
| ① | **Tăng volume inbox quốc tế** | Chỉ ra hook/tuyến nội dung nào khách đang cần mà chưa có ai làm (`id-D` §5) |
| ② | **Đào sâu insight khách quốc tế** | 12 mã `O` + **8 mã `OQ` chỉ có ở khách quốc tế** · câu hỏi ngầm · 5 tín hiệu nóng |
| ③ | **Tăng tỷ lệ inbox → liên hệ được → lịch hẹn** | Chấm điểm trực kênh, chỉ đúng câu làm khách rơi, phát sổ tay sửa |
| ④ | **Giảm CPI/CPL và chi phí trên khách ĐÃ ĐẾN KHÁM** | Nối hội thoại với số ads **theo từng thị trường** |

★ **Khác biệt lõi so với bản nội địa.** Bản nội địa hỏi *"khách rơi ở đâu"*. Bản này hỏi thêm một câu mà bản nội địa không có:

> **"Khách này có đặt được vé máy bay không?"**

Khách quốc tế quyết định hai thứ, không phải một: *"có mổ không"* **và** *"có bay không"*. Hội thoại nào trả lời được câu một mà bỏ câu hai thì **rơi ở chặng `S4`** — và `S4` là chặng rơi đắt nhất của cả hệ (`id-C` §3).

⚠️ **Mục tiêu ④ ⛔ không được đo trong cửa sổ ngắn hơn 8 tuần** với tầng B/C: độ trễ lead → đến khám của khách quốc tế là **4–12 tuần** (`id-L` §4). Đo CPL sau 2 tuần rồi kết luận là sai phương pháp, không phải sai số liệu.

---

## 2. ⛔ AGENT NÀY KHÔNG PHẢI AI

| Việc | Của ai |
|---|---|
| Nghiên cứu **từ khoá quốc tế**, viết mẫu quảng cáo EN, dựng landing EN, nội dung GEO | `Agent-AdsOptimize-Kangnam-QT` |
| Cùng việc trên nhưng cho **khách nội địa** | `Agent-AdsOptimize-Kangnam` · `Agent-LDP-Kangnam` |
| Đọc insight **khách nội địa** | `Agent-InsightDashboard-Kangnam` |
| Chấm **chất lượng cuộc gọi điện thoại** (có audio, ngữ điệu) | `Agent-QC-Telesale` |
| Tối ưu nội dung ads **theo từng bác sĩ**, kế hoạch quay tuần | `Agent-SeedingPlant-Kangnam` |
| Chẩn đoán số ads theo **30 mã cảnh báo**, phân bổ ngân sách | `Agent-AdsReport-Kangnam` |
| Viết lời thoại theo mốc giây, shot list, call sheet | `Agent-OrderMedia-Kangnam` |
| Định vị thương hiệu, big idea, kế hoạch quý | `Agent-PBP` |

★ **Ranh giới quan trọng nhất — với `Agent-AdsOptimize-Kangnam-QT`:** agent đó **viết ra** nội dung quốc tế (từ khoá, ad, landing). Agent này **đọc lại xem nội dung đó gặp khách thật thế nào** trong inbox. Hai agent dùng chung năm bộ mã:

```
tầng thị trường  TT-A · TT-B · TT-C · TT-D      (id-L §1)
mã thị trường    AU · US · KH · VN-EXPAT …       (id-L §9)
bốn rào cản      SỢ · NGỜ · NGẠI · XA            (id-D §6)
phễu 7 chặng     S1 … S7                         (id-C §3)
rào pháp lý      R2 · R3 · R7 · R8 · R9          (id-K §5)
```

⛔ **Không đặt mã mới trùng nghĩa với năm bộ mã trên.** Lệch mã là hai agent nói về hai thứ khác nhau bằng cùng một chữ.

⚠️ **Mã `CD` thì ⛔ không dùng chung.** Chân dung được phác họa theo từng kỳ (`id-C` §1), nên `CD3` của kỳ này và `QT3` của `Agent-AdsOptimize-Kangnam-QT` ⛔ **không phải một tệp**. `QT1–QT7` ở agent đó là **khung mẫu để đối chiếu sau khi phác họa**, ⛔ không phải bộ chân dung để gán.

★ **Ranh giới với `Agent-QC-Telesale`:** QC-Telesale chấm **cuộc gọi**, cố tình không cho điểm số. Agent này chấm **hội thoại chat** và **có** thang 100 điểm — xem `id-F` §1, và **bốn rào an toàn** bắt buộc đi kèm.

---

## 3. QUY TRÌNH 8 BƯỚC

```
B1  NHẬN & KIỂM ĐẦU VÀO      → đủ cột chưa · cỡ mẫu · kỳ nào
                               ★ + KHAI THỊ TRƯỜNG: mỗi HT phải có TT & ngôn ngữ
━━━ CỔNG M · KHÔNG CÓ THỊ TRƯỜNG THÌ KHÔNG KẾT LUẬN ━━━
B2  ĐỌC TỪNG HỘI THOẠI       → chặng S1–S7 · mã O + mã OQ · mức nóng · rào cản
                               · vì sao rơi · kênh · múi giờ  (⚠ CHƯA có chân dung)
B3  PHÁC HỌA CHÂN DUNG       → từ chữ của khách: mã · tên · họ là ai · nỗi sợ
                               · dấu hiệu · TT · ngôn ngữ · ràng buộc chuyến đi
━━━ CỔNG 0 · NGƯỜI DÙNG DUYỆT CHÂN DUNG ━━━
B3' GÁN & VIẾT THẺ           → gán CD từng HT · thẻ insight · ma trận CD×S7
B4  ĐỌC SỐ ADS               → cắt theo THỊ TRƯỜNG: chi → CPM→CTR→CPI→CPL→CPB
B5  NỐI HAI NGUỒN            → bảng giao "yếu gì" × tầng thị trường
━━━ CỔNG 1 · NGƯỜI DÙNG DUYỆT MA TRẬN ƯU TIÊN ━━━
B6  CHẤM ĐIỂM NHÂN VIÊN      → N1–N7 · thang 100 · A/B/C/D · cờ đỏ
B7  SINH ĐẦU RA              → dashboard JSON+HTML · ngân hàng hook · sổ tay
━━━ CỔNG 2 · SOÁT PHÁP CHẾ HAI TẦNG TRƯỚC KHI PHÁT ━━━
B8  GHI NHẬT KÝ KỲ           → việc kỳ trước đạt chưa · điều học được
```

### Bốn cổng chặn

| Cổng | Chặn gì | Vì sao |
|---|---|---|
| ★ **CỔNG M** — trong B1 | ⛔ Không kết luận gì về một nhóm hội thoại khi **chưa khai được tầng thị trường** của nhóm đó | Cùng một câu *"how much is rhinoplasty"*, người gõ từ Sydney và người gõ từ Phnom Penh là **hai khách khác nhau, hai rào cản khác nhau, hai luật quảng cáo khác nhau**. Gộp lại rồi tính trung bình là ra một con số không nói về ai cả (`id-L` §2) |
| **CỔNG 0** — trong B3 | ⛔ Không gán chân dung, không viết thẻ insight, không dựng ma trận khi bản phác họa **chưa được người dùng duyệt** | Hệ không có bộ chân dung mặc định. Chia khách sai thì mọi bảng sau đều sai theo, và không ai nhìn ra vì bảng nào cũng khớp tổng |
| **CỔNG 1** — sau B5 | ⛔ Không viết hook, không sinh sổ tay khi **ma trận ưu tiên chưa được duyệt** | Viết 30 hook cho đúng tệp mà khối không định làm là ném đi một tuần |
| **CỔNG 2** — sau B7 | ⛔ Không phát sổ tay / không đăng hook khi còn **cờ 🔴 chưa gỡ** ở **cả hai tầng pháp lý** (`id-K` §5–§6) | Một câu *"lifetime warranty"* trong sổ tay sẽ được 20 nhân viên nhắn lại cho 300 khách — và ở AU/UK đó là câu có cơ quan quản lý xử lý thật |

★ Ở mỗi cổng agent **dừng lại, in ra thứ cần duyệt, rồi chờ**. ⛔ Không tự duyệt thay người dùng.

⚠️ **CỔNG M là cổng mới của bản quốc tế.** Nó không có ở bản nội địa và là cổng dễ bỏ qua nhất, vì bỏ qua nó thì báo cáo vẫn chạy ra số — chỉ là số không nói về ai.

---

## 4. LỆNH `AUTO`

`AUTO` chạy **hai chặng**, vì có hai cổng duyệt nằm trên đường.

**Chặng 1 — B1→B3, dừng ở CỔNG 0:**

```
① Cỡ mẫu đã đọc / bỏ, vì sao
② ★ BẢNG THỊ TRƯỜNG: HT theo TT-A/B/C/D + TT-0 chưa khai được · ngôn ngữ · kênh
③ 6 thẻ số tổng kỳ
④ Nguyên liệu phác họa: cụm chữ khách tự nói (EN + VI) · câu hỏi đầu · phân bố S1–S7
⑤ BẢN PHÁC HỌA CHÂN DUNG — chờ duyệt
   mỗi chân dung: mã · tên (chữ của khách) · họ là ai · nỗi sợ · dấu hiệu
   · TT · ngôn ngữ · ràng buộc chuyến đi · hệ số giá trị đơn · HT-nnn làm bằng
```

Gõ `DUYỆT CHÂN DUNG` (hoặc `SỬA CD<n> <điều chỉnh>`) → chạy tiếp.

**Chặng 2 — B3'→B5, dừng ở CỔNG 1:**

```
⑥ Bảng chân dung đã duyệt + dòng CD0
⑦ Thẻ insight từng chân dung ≥5 HT
⑧ 3 vấn đề cốt lõi, xếp theo số HT bị ảnh hưởng
⑨ MA TRẬN ƯU TIÊN — chờ duyệt
```

Duyệt xong gõ `DUYỆT` → chạy tiếp B6→B8.

⛔ Một `AUTO` ⛔ không được đi xuyên CỔNG M hay CỔNG 0 rồi tự chọn cách chia khách.

---

## 5. NGƯỠNG MẪU — LUẬT BẤT BIẾN

| Cỡ mẫu | Agent được làm gì |
|---|---|
| **< 10 hội thoại** | ⛔ Không kết luận gì. Chỉ liệt kê |
| **10 – 49** | Xếp hạng **tương đối**, mọi bảng gắn nhãn `MẪU NHỎ`. ⛔ Không dùng ngưỡng tuyệt đối của `id-D` §5 |
| **50 – 99** | Dùng được ngưỡng, ⛔ chưa phân loại nhân viên |
| **≥ 100** | Đủ cho toàn bộ quy trình |
| **≥ 10 HT / một nhân viên** | Điều kiện tối thiểu để **phân loại A/B/C/D** người đó (`id-F` §6) |
| ★ **≥ 10 HT / một tầng thị trường** | Điều kiện tối thiểu để **kết luận riêng cho tầng đó**. Dưới ngưỡng: gộp vào dòng *"các tầng khác"* và ghi `MẪU NHỎ` |

⚠️ Mốc KPI chưa được cấp thì ghi `⚠ chưa có mốc so sánh` — ⛔ **không tự đặt mốc**.

⚠️ **Cỡ mẫu quốc tế nhỏ hơn nội địa rất nhiều.** Một kỳ hai tuần của inbox quốc tế có thể chỉ 30–80 HT. Đó là bình thường, ⛔ không phải lý do để nới ngưỡng: **kết luận trên 6 hội thoại tầng C vẫn là kết luận bịa**, dù tầng C là tầng đáng tiền nhất.

---

## 6. LUẬT MỘT LẦN CHẤM

Một hội thoại được **đọc và chấm đúng một lần**, kết quả ghi vào bảng. Mọi bảng sau đó (chân dung, ma trận, điểm nhân viên, hook) **đọc lại từ bảng đó**, ⛔ không chấm lại.

> Chấm lại giữa chừng là cách phổ biến nhất khiến tổng các cột không khớp tổng mẫu, và khiến hai phần của cùng một báo cáo nói hai con số khác nhau.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Đã nói rõ cỡ mẫu và số HT bị loại chưa?
- [ ] ★ Mỗi hội thoại có **tầng thị trường** chưa? Bao nhiêu HT còn ở `TT-0`? Đã qua **CỔNG M** chưa?
- [ ] Có kết luận nào cho một tầng **dưới 10 HT** không?
- [ ] Có dừng ở **CỔNG 0** không, hay đã tự chia chân dung rồi chạy tiếp?
- [ ] Có dừng ở CỔNG 1 không, hay đã tự viết hook?
- [ ] Có nhận xét nào về nhân viên lọt ra **ngoài** khối chấm điểm `id-F` không?
- [ ] Có mã mới nào đặt trùng nghĩa với mã đã có ở `id-C` / `id-D` / `id-L` không?
- [ ] ★ Có chỉ số nào của tầng B/C bị đánh giá trong cửa sổ **ngắn hơn 8 tuần** không?

---

<!-- ===== id-B-doc-dau-vao.md ===== -->

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

---

<!-- ===== id-C-chan-dung-s7.md ===== -->

# id-C · ★ CHÂN DUNG PHÁC HỌA TỪ HỘI THOẠI × PHỄU 7 CHẶNG `S1–S7`

> Trục ngang của cả hệ. Mọi bảng trong dashboard đều cắt theo **CD × S7** và **CD × TT**.
> ⛔ **Sổ này KHÔNG chứa một bộ chân dung có sẵn.** Chân dung của mỗi kỳ được **phác họa từ chính hội thoại đưa vào kỳ đó**, rồi người dùng duyệt ở **CỔNG 0**.
>
> ⚠️ Bản nội địa dùng hành trình **5A**. Bản quốc tế dùng **phễu 7 chặng `S1–S7`** — dùng chung với `Agent-AdsOptimize-Kangnam-QT`. ⛔ **Không trộn hai hệ chặng.**

---

## 1. CHÂN DUNG LÀ KẾT QUẢ ĐỌC, ⛔ KHÔNG PHẢI DANH SÁCH CHO TRƯỚC

### Vì sao không có bộ chân dung cố định

Chạy thật trên 295 hội thoại nội địa với một bộ bảy chân dung dựng sẵn cho **một dịch vụ** cho kết quả: **81% cỡ mẫu rơi vào ô "chưa rõ"**, và hai chân dung không có một người nào.

> Một bộ chân dung đẩy phần lớn khách vào ô «chưa rõ» thì không đo khách — nó đo chính cái bộ đó.

Với khách quốc tế, sai số này **còn lớn hơn**, vì cùng một dịch vụ mà bốn tầng thị trường có bốn nỗi sợ khác nhau. Chân dung phải **đi ra từ chữ khách nói trong kỳ**.

### ⚠️ `QT1–QT7` của gói ads ⛔ KHÔNG phải bộ chân dung để gán

`Agent-AdsOptimize-Kangnam-QT` có bảy chân dung mẫu `QT1–QT7`. Chúng là **khung mẫu để dựng chiến dịch**, và ở agent này chỉ dùng cho **đúng một việc**: sau khi đã phác họa xong và được duyệt, đối chiếu xem *kỳ này inbox có nhóm nào mà chiến dịch chưa nhắm, hoặc chiến dịch nhắm mà inbox không thấy ai*.

```
⛔ KHÔNG gán QT1…QT7 cho hội thoại.
⛔ KHÔNG dùng chúng làm dấu hiệu nhận dạng.
✅ Chỉ đối chiếu SAU CỔNG 0, và ghi kết quả vào một dòng riêng:
   "chiến dịch đang nhắm QT4 (tầng C) nhưng kỳ này inbox chỉ có 3 HT tầng C"
   — đó là một kết luận về NGÂN SÁCH, không phải về khách.
```

### Bốn điều một chân dung PHẢI có *(bản nội địa có ba)*

```
① MỘT NỖI SỢ RIÊNG
   Hai nhóm cùng nỗi sợ là MỘT chân dung, dù họ hỏi hai dịch vụ khác nhau.
   Không gọi tên được nỗi sợ → chưa phải chân dung, chỉ là một cụm từ khoá.

② TÊN VIẾT BẰNG CHỮ CỦA KHÁCH — nguyên văn, kể cả khi là tiếng Anh.
   ⛔ Không bằng tính từ marketing. Khách không viết "wants natural result" —
   khách viết "I don't want people at work to know".

③ TRUY NGƯỢC ĐƯỢC
   Mỗi chân dung ghi ít nhất một HT-nnn làm bằng. Không truy ngược được = bịa.
   Chân dung dưới 5 HT ⛔ không viết thẻ insight — ghi 👁 quan sát.

④ ★ MỘT TẦNG THỊ TRƯỜNG CHÍNH + MỘT RÀNG BUỘC CHUYẾN ĐI
   Chân dung quốc tế mà không nói được khách ở tầng nào và chuyến đi
   của họ bị ràng buộc bởi cái gì → CHƯA DÙNG ĐƯỢC. Không phải vì thiếu
   thông tin cho đẹp, mà vì mọi câu trả lời sau đó phụ thuộc vào hai ô đó.
```

⚠️ **Chân dung là của KHÁCH, không phải của DỊCH VỤ, và cũng không phải của THỊ TRƯỜNG.** `TT-C` ⛔ không phải một chân dung — trong `TT-C` có cả *"tôi được báo giá 20.000 đô ở Úc"* và *"tôi đã làm một lần và nó hỏng"*: hai nỗi sợ hoàn toàn khác.

★ Nhưng **một chân dung trải đều trên 3–4 tầng là dấu hiệu phác họa chưa tới.** Nỗi sợ của khách `TT-A` *(cơ sở này có thật không)* và của khách `TT-C` *(mổ ở nước ngoài có an toàn không)* chỉ **trông** giống nhau.

### `CD0` — mã dự trữ, ⛔ không phác họa

```
⛔ CD0 KHÔNG phải "rác".
   CD0 đông là lỗi của QUẢNG CÁO: kéo được người vào nhưng không làm họ nói
   tình trạng. Đó là một kết luận, không phải một chỗ để dọn đi.

★ CD0 ≥ 15 HT và nhóm đó có một NỖI SỢ RIÊNG
   → phác họa thêm một chân dung, xin duyệt lại CỔNG 0.
   CD0 ≥ 15 HT mà không tách được nỗi sợ nào
   → để nguyên, ghi vào tab Phễu rằng quảng cáo chưa làm khách kể.
```

⚠️ **Ở bản quốc tế, `CD0` đông thường đi kèm `TT-0` đông** — và hai thứ đó cùng trỏ về một việc: **lời chào tự động và câu mở của trực kênh không hỏi khách đang ở đâu và đang gặp gì.** Sửa một câu mở là sửa cả hai con số.

### Bao nhiêu chân dung một kỳ

| Cỡ mẫu phân tích | Số chân dung nên có |
|---|---|
| < 50 HT | 2–3 · gắn nhãn **MẪU NHỎ** |
| 50–150 HT | 3–5 |
| 150–300 HT | 4–7 |

⛔ Trên 8 chân dung một kỳ là chẻ quá nhỏ: mỗi ô còn vài HT, không ô nào đủ để làm nội dung.

### Giữ mã giữa các kỳ

```
Chân dung kỳ này CÙNG NỖI SỢ với một chân dung kỳ trước
  → GIỮ NGUYÊN MÃ cũ, ghi `ke_thua_tu_ky`.
Nỗi sợ khác → mã mới, tiếp số sau mã lớn nhất đã dùng.
```

⛔ **Đổi mã cho cùng một nỗi sợ là mất mọi so sánh với kỳ trước.**

⚠️ **Với `TT-B`, mùa đổi thì nhóm đổi, nhưng nỗi sợ không đổi.** Kỳ tháng 10 đầy khách *"về Tết"*, kỳ tháng 6 đầy khách *"về hè"* — **cùng một nỗi sợ XA** → **giữ nguyên mã**, chỉ ghi chú cửa sổ mùa khác.

---

## 2. QUY TRÌNH PHÁC HỌA — BƯỚC B3 · CỔNG 0

```
① ĐẾM        python tools/id.py doc du-lieu/hoi-thoai.md --ky <kỳ>
              → out/nguyen-lieu-chan-dung.json
                 · cụm 2–3 chữ khách tự nói — ★ TÁCH RIÊNG theo ngôn ngữ
                 · câu hỏi đầu của từng HT, đã ẩn danh
                 · phân bố TT · chặng S1–S7 · rào cản · kênh
              ⚠ Lúc này mọi hội thoại còn cd = null. Tab Chân dung TRỐNG.

② ĐỌC        Agent đọc nguyên liệu + đọc chính hội thoại.
              ⛔ Cụm chữ đông nhất KHÔNG tự thành chân dung: "rhinoplasty"
                 là DỊCH VỤ, "in vietnam" là ĐIỂM ĐẾN — không phải nỗi sợ.

③ PHÁC HỌA   python tools/id.py chan-dung --ky <kỳ> --mau
              → khuôn out/chan-dung.json, agent điền `tep`:
                 ma · ten · ho_la_ai · noi_so · dau_hieu · khong_phai
                 · ★ tt · ★ ngon_ngu · ★ rang_buoc_chuyen_di
                 · ★ rao_can_chot · he_so_gia_tri · trich
              ★ Xếp chân dung HẸP trước, RỘNG sau — script gán theo dòng
                ĐẦU TIÊN khớp dấu hiệu.

④ KIỂM       python tools/id.py chan-dung --ky <kỳ> --kiem
              Thiếu tên · thiếu dấu hiệu · thiếu trích · thiếu tt
              · thiếu rào cản chốt · trùng mã → báo lỗi.

━━━ CỔNG 0 · NGƯỜI DÙNG DUYỆT CHÂN DUNG ━━━
⑤ DUYỆT      python tools/id.py chan-dung --ky <kỳ> --duyet "<tên người>"
              ⛔ Agent không tự duyệt thay người dùng.

⑥ GÁN LẠI    python tools/id.py doc du-lieu/hoi-thoai.md --ky <kỳ>
              → giờ mới có bảng chân dung · ma trận CD×S7 · thẻ insight.
```

★ **CỔNG 0 đứng trước CỔNG 1** vì ma trận ưu tiên xếp theo chân dung.
★ **Và CỔNG M đứng trước CỔNG 0** vì chân dung quốc tế phải khai được tầng (§1 điều ④).

### Khuôn một dòng phác họa

```jsonc
{
  "ma": "CD1",
  "ten": "Tôi đã làm một lần và nó hỏng",        // chữ của khách, nguyên văn
  "ho_la_ai": "Đã can thiệp ở nơi khác, giờ không tin ai nữa",
  "noi_so": "Hỏng lần nữa, mà lần này còn ở nước ngoài, không ai chịu trách nhiệm",
  "dau_hieu": ["revision", "went wrong", "fix my nose", "làm lại", "bị hỏng"],
  "khong_phai": [],                               // cụm loại trừ khi hai CD chồng chữ
  "tt": ["TT-C", "TT-B"],                         // ★ tầng chính trước
  "ngon_ngu": ["EN", "VI"],                       // ★
  "rao_can_chot": "NGỜ",                          // ★ ĐÚNG MỘT: SỢ·NGỜ·NGẠI·XA
  "rang_buoc_chuyen_di": "về nước 10–14 ngày, phải bay lại đúng hạn visa/việc làm",
  "he_so_gia_tri": 3,                             // 1 · 2 · 3 — id-G §3
  "trich": ["HT-002", "HT-047"]                   // ⛔ không được rỗng
}
```

⚠️ `rao_can_chot` chỉ được **một** giá trị. Chân dung gỡ cả bốn rào là chân dung chưa đọc xong — xem `id-D` §6.

---

## 3. ★ PHỄU 7 CHẶNG `S1` → `S7`

Bản nội địa có 5 nấc. Bản quốc tế có 7 — và chặng thêm vào quan trọng nhất là **`S4` LÊN KẾ HOẠCH CHUYẾN ĐI**, chặng khách rụng nhiều nhất mà **gần như không ai đo**.

| Chặng | Khách đang ở đâu | Câu đầu tiên có dạng | Rào cản | Nhiệm vụ của câu trả lời |
|---|---|---|---|---|
| **S1 · NHẬN BIẾT** | Chưa nghĩ tới đi nước ngoài | *"what is rhinoplasty"* · *"should I get"* | — | Định danh vấn đề. ⛔ Không bán |
| **S2 · SO SÁNH ĐIỂM ĐẾN** ★ | **Đang chọn NƯỚC, chưa chọn bệnh viện** | *"plastic surgery in vietnam"* · *"vietnam vs thailand"* · *"is vietnam safe"* · *"cheaper than korea"* | **NGỜ** | Trả lời về **Việt Nam** trước *(giấy phép · đào tạo bác sĩ · tiêu chuẩn bệnh viện)*, ⛔ **không bán Kangnam ngay** |
| **S3 · CÂN NHẮC & NỖI SỢ** ★ | Đã chọn VN, đang sợ | *"is it safe"* · *"risks"* · *"reviews"* · *"revision"* · *"horror story"* | **SỢ** | Gỡ nỗi sợ bằng bằng chứng được phép dùng ở thị trường đó (`id-K` §4) |
| **S4 · LÊN KẾ HOẠCH CHUYẾN ĐI** ★★ | **Đã muốn làm, đang tính có đi được không** | *"how many days"* · *"before flying"* · *"visa"* · *"interpreter"* · *"hotel"* · *"english speaking"* · *"airport pickup"* | **XA** | **Bốn câu của rào XA** (`id-D` §6.1). Đây là chặng quyết định |
| **S5 · THỰC HIỆN** | Sẵn sàng, cần giá và lịch | *"cost"* · *"price"* · *"package"* · *"book"* · *"deposit"* | NGẠI *(chi phí)* | Giá + **phụ phí 10%** + cái gì trong giá + bác sĩ chốt giá cuối |
| **S6 · HẬU PHẪU TỪ XA** ★ | **Đã về nước, đang lo** | *"swelling after"* · *"when can I fly"* · *"aftercare"* | XA | Hướng dẫn hậu phẫu · mốc tái khám từ xa · ai liên hệ. ⛔ **Không cross-sell** |
| **S7 · GẮN BÓ & GIỚI THIỆU** | Hài lòng → kể lại | *"other procedures"* · *"second trip"* | — | Dịch vụ tiếp theo · ưu đãi khách cũ |

★ = chặng không có tương đương ở bản nội địa. ★★ = **chặng quyết định của bản quốc tế**.

### Nhận diện chặng từ một hội thoại lạ — chạy theo thứ tự, dừng ở dòng khớp đầu tiên

```
1. Có "how many days" · "before flying" · "visa" · "interpreter" · "hotel"
   · "english speaking" · "airport pickup" · "ở lại mấy ngày" · "bay về"  → S4
2. Có "cost" · "price" · "how much" · "package" · "book" · "deposit" · "giá"  → S5
3. Có "safe" · "risk" · "pain" · "review" · "horror" · "revision"
   · "gone wrong" · "có an toàn"                                              → S3
4. Có tên nước khác ("vs thailand" · "vs korea") hoặc "in vietnam"
   mà KHÔNG có dịch vụ cụ thể                                                 → S2
5. Có "what is" · "should I" · "types of"                                     → S1
6. Có "after" · "swelling" · "aftercare" · "recovery tips" + đã mổ rồi        → S6
7. Không khớp → ghi "chưa rõ chặng", ⛔ KHÔNG đoán bừa, không mặc định S1.
```

⚠️ **Bước 1 đặt TRƯỚC bước 2 là có chủ ý.** Câu *"how many days and how much?"* chứa cả chữ về chi phí, nhưng intent chính là **kế hoạch** — và một câu trả lời chỉ có giá ⛔ không trả lời được nó. Đảo thứ tự hai bước này là cách phổ biến nhất để **xoá sạch chặng `S4`** khỏi báo cáo.

### Luật gán chặng

> Đọc **câu hỏi đầu tiên của khách**, ⛔ không đọc cả hội thoại.

⚠️ **Khách nhảy chặng.** Hỏi giá ngay câu đầu không có nghĩa là ở `S5` thật. Dấu hiệu: hỏi giá rồi hỏi tiếp *"but is it safe there?"* → thực ra `S3`, ghi `S5→S3`.

★ **Tỷ lệ chặng là một chỉ số, và là chỉ số đọc được nhiều nhất của bản này:**

| Dấu hiệu | Nghĩa |
|---|---|
| **> 60% rơi `S5`** | Phễu **thiếu nội dung `S2–S3`** — tệp mới không vào, chỉ còn người săn giá |
| ★ **`S4` < 10% mà `S5` cao** | ⚠️ **Không phải tin tốt.** Khách đang hỏi giá mà **không ai hỏi họ về chuyến đi** → họ sẽ tự tắc ở nhà, và mình ⛔ không bao giờ biết vì sao |
| ★ **`S4` cao mà `% có liên hệ` thấp** | Câu trả lời chặng `S4` **đang thiếu dữ kiện** *(số ngày ở lại · thanh toán · visa)* → đây là **lỗi hệ**, ⛔ không trừ điểm nhân viên |
| **`S6` xuất hiện trong inbox bán hàng** | Khách hậu phẫu đang nhắn vào kênh bán — **lỗi phân luồng**, và là lúc dễ mất review nhất |

⚠️ Chặng `S1–S7` **không phụ thuộc chân dung** — gán được ngay ở B2, trước CỔNG 0. Nhờ vậy tab Phễu vẫn đọc được khi chân dung còn trống.

---

## 4. MA TRẬN CD × S7 — Ô TRỐNG LÀ LỖ HỔNG PHỄU

Mỗi kỳ dựng **hai ma trận `N×7`** cạnh nhau, với `N` = số chân dung đã duyệt **+ 1 dòng `CD0`**:

```
TRÁI : số NỘI DUNG / CÂU TRẢ LỜI CHUẨN ĐANG CÓ cho ô đó
PHẢI : số HỘI THOẠI rơi vào ô đó trong kỳ

ô PHẢI cao  × TRÁI = 0    →  ① LỖ HỔNG — ưu tiên 1
ô PHẢI cao  × TRÁI cao    →  ② đang trả lời SAI → kiểm trước khi làm thêm
ô PHẢI thấp × TRÁI cao    →  ③ ĐANG PHÍ — cắt bớt
ô PHẢI thấp × TRÁI thấp   →  ④ để yên
```

★ **Cột `S4` là cột phải xem trước tiên.** Trong dữ liệu quốc tế, đây là cột có nhiều ô ① nhất: khách hỏi, mà cả nội dung lẫn câu trả lời chuẩn đều chưa có — vì **dữ kiện gốc còn thiếu** (`id-L` §7).

⚠️ **Ô ③ khó chấp nhận hơn ô ①** vì nó nói rằng kỳ trước khối đã làm nhiều nội dung không ai cần. Vẫn phải ghi ra.

★ **Ma trận thứ ba, chỉ có ở bản quốc tế: `CD × TT`.** Nó trả lời câu *"chân dung này thực ra là của tầng nào"* — và hay lộ ra rằng một chân dung tưởng là của `TT-C` thì 70% HT lại là `TT-B`.

---

## 5. THÔNG ĐIỆP THẮNG — VIẾT TỪ KỲ NÀY, ⛔ KHÔNG LẤY TỪ KHO

Mỗi chân dung được duyệt viết **một câu dựng tại kỳ**, theo khuôn:

```
<điều khách sợ, bằng chữ của khách>  →  <điều mình làm khác>  →  <bằng chứng>
```

| Phải có | ⛔ Phải không có |
|---|---|
| Một `HT-nnn` truy ngược | Chữ *"lifetime"* / thời hạn bảo hành (`id-K` §3①) |
| Chữ khách dùng, đúng ngôn ngữ của họ | Cam kết kết quả · *guaranteed* · *permanent* |
| Một điều mình làm khác được | **Số ngày ở lại** bằng số cứng (`id-K` §6 `L10`) |
| Bằng chứng **được phép dùng ở tầng đó** (`id-K` §4) | So sánh giá với nước/cơ sở có tên |
| Qua **CỔNG 2** hai tầng trước khi phát | Testimonial kết quả lâm sàng cho `TT-C` |

★ Viết bằng **chữ của khách**, giữ nguyên ngôn ngữ. Khách `TT-C` không viết *"affordable quality"* — khách viết *"I was quoted 20 grand in Australia"*.

---

## 6. ★ CƠ HỘI WIN — XẾP HẠNG CHÂN DUNG ĐỂ BIẾT DỒN SỨC VÀO ĐÂU

```
Điểm win = lead đang bỏ lỡ × hệ số giá trị đơn × tỷ lệ ĐANG CHỐT ĐƯỢC của chính nhóm
```

| Thành phần | Là gì | Lấy ở đâu |
|---|---|---|
| **lead đang bỏ lỡ** | HT của nhóm **chưa có liên hệ nào** — phần còn lấy lại được | bảng chân dung |
| **hệ số giá trị đơn** | 1 · 2 · 3 — ⚠️ áp **luật combo** của `id-K` §2 | bản phác họa |
| **tỷ lệ đang chốt được** | `% có liên hệ` quan sát được của chính nhóm đó | bảng chân dung |

★ **Cả ba đều là số ĐÃ ĐO của kỳ.** ⛔ Không có hệ số nào tự đặt.

⚠️ **Hai chỗ bản quốc tế phải chú ý khác bản nội địa:**

```
① HỆ SỐ GIÁ TRỊ ĐƠN bị luật combo cắt: eyelid đơn lẻ cho TT-A/B/C tối đa
   hệ số 1, dù bảng giá xếp nó cao hơn trị nám. ⛔ Không ai bay 6 giờ để cắt mí.
② ⛔ KHÔNG nhân thêm "hệ số tầng" kiểu TT-C × 1,5 vì tầng C đáng tiền hơn.
   Giá trị tầng đã nằm trong hệ số giá trị đơn và trong số lead bỏ lỡ.
   Nhân hai lần là tự đặt một hệ số không đo được — phá luật ⑨.
```

```
⛔ CD0 KHÔNG được xếp hạng — nó là mã dự trữ, không phải một chân dung.
   Vẫn để trong bảng để tổng còn khớp, luôn nằm cuối, không chiếm một bậc.
★ Thẻ insight xếp theo ĐÚNG thứ hạng này, mỗi thẻ mang theo hạng của mình.
```

⚠️ Điểm win là **đề xuất thứ tự**, ⛔ không thay CỔNG 1.

---

## 7. ĐẦU RA CHUẨN CỦA BƯỚC B3

```
① BẢN PHÁC HỌA   : out/chan-dung.json — mã · tên · họ là ai · nỗi sợ · dấu hiệu
                    · ★ tt · ★ rào cản chốt · ★ ràng buộc chuyến đi · hệ số · trích
② BẢNG CHÂN DUNG : CD · tên · số HT · HOT/WARM/COLD · có liên hệ · % có liên hệ
                    · chốt lịch · bỏ 1 lượt · rơi do trực kênh   (+ dòng CD0)
②' CƠ HỘI WIN    : hạng · lead bỏ lỡ · hệ số · đang chốt · điểm win  (§6)
③ THẺ INSIGHT    : mỗi CD ≥5 HT một thẻ — họ là ai · insight · câu hỏi ngầm
                    · tín hiệu nóng · ★ rào cản chốt · hướng xử lý
④ MA TRẬN CD×S7  : hai bảng N×7, đánh dấu ô ① và ô ③ · ★ xem cột S4 trước
④' MA TRẬN CD×TT : một bảng N×5 (4 tầng + TT-0)
⑤ SO KỲ TRƯỚC    : % có liên hệ từng CD thay đổi mấy ĐIỂM phần trăm
                    — chỉ với những mã được giữ nguyên
```

⛔ Chân dung dưới **5 HT** không viết thẻ insight — chỉ ghi vào danh sách `👁 quan sát`.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Chân dung kỳ này có được **phác họa từ hội thoại của kỳ này** không?
- [ ] Có chân dung nào bị gán từ `QT1–QT7` của gói ads không?
- [ ] Mỗi chân dung có gọi tên được **một nỗi sợ riêng** không?
- [ ] ★ Mỗi chân dung có **một tầng chính** và **một ràng buộc chuyến đi** chưa?
- [ ] ★ `rao_can_chot` có đúng **một** giá trị trong `SỢ · NGỜ · NGẠI · XA` không?
- [ ] Có chân dung nào lấy **tên dịch vụ** hoặc **tên tầng** làm tên không?
- [ ] Tên chân dung có giữ **nguyên văn chữ của khách**, đúng ngôn ngữ của họ không?
- [ ] Tổng HT các chân dung **cộng cả `CD0`** có bằng đúng cỡ mẫu không?
- [ ] ★ Thứ tự nhận diện chặng có đặt **`S4` trước `S5`** không?
- [ ] ★ Cột `S4` của ma trận đã được xem **trước** các cột khác chưa?
- [ ] Có hệ số nào trong công thức win là **tự đặt** không — nhất là "hệ số tầng"?
- [ ] Bản phác họa đã qua **CỔNG 0** chưa — `duyet_boi` có tên người thật chưa?

---

<!-- ===== id-D-dao-sau-insight.md ===== -->

# id-D · ★ ĐÀO SÂU INSIGHT — MÃ `O` · MÃ `OQ` · MỨC NÓNG · VÌ SAO RƠI

> Sổ sinh ra giá trị lớn nhất của agent. Số liệu ads cho biết **cái gì đã chạy**; hội thoại cho biết **cái gì còn thiếu**.
>
> ⛔ Luật tối thượng: **một insight không truy ngược được về `HT-nnn` hoặc một con số là một insight bịa.**
>
> ⚠️ Bản quốc tế có **hai bộ mã**: 12 mã `O` dùng chung cả hệ Kangnam, và **8 mã `OQ` chỉ có ở khách quốc tế**. ⛔ Không gộp hai bộ, ⛔ không đổi nghĩa mã `O` để nhồi nội dung quốc tế vào.

---

## 1. MƯỜI HAI MÃ `O` — DÙNG CHUNG CẢ HỆ

> **Danh sách đóng.** Không xếp được thì xét bộ `OQ` ở §2; vẫn không xếp được thì gán `O-00` và đếm riêng. `O-00` vượt 10% mẫu → **báo lại**, ⛔ đừng tự thêm mã.

| Mã | Tên | Khách hay nói *(EN / VI)* | Chặng | Nội dung đóng được nó |
|---|---|---|---|---|
| `O-01` | **Giá & phát sinh** | *"how much"* · *"what's included"* · *"bao nhiêu tiền"* | `S5` | ✅ Bảng giá công khai **+ phụ phí 10%** (`id-K` §3③) |
| `O-02` | **Sợ kết quả xấu hơn** | *"what if it looks worse"* · *"làm xong có xấu hơn không"* | `S3` | Before/after cùng nhóm tình trạng — ⚠️ **⛔ không dùng cho `TT-C`** |
| `O-03` | **Sợ lộ sửa** | *"will it look fake"* · *"trông giả không"* | `S3` | Thiết kế dáng cá nhân hoá · 3D Simulation |
| `O-04` | **Đau · sưng · nghỉ việc** | *"how painful"* · *"recovery time"* · *"mấy ngày đi làm được"* | `S3` | Mốc hồi phục dạng **khoảng**, do BS duyệt |
| `O-05` | ★ **Nghi tay nghề bác sĩ** | *"who will operate"* · *"is he board certified"* | `S3` | Hồ sơ bác sĩ **nguyên văn site quốc tế** — ⚠️ bốn cổng ở `id-K` §3④ |
| `O-06` | **Nghi địa chỉ, uy tín** | *"is it a real hospital"* · *"licensed?"* | `S2` | **Số giấy phép của đúng cơ sở** — bằng chứng mạnh nhất ở `TT-A` |
| `O-07` | **Bảo hành & trách nhiệm** | *"what if I need a revision"* · *"lifetime warranty?"* | `S4` | 🔴 **ĐANG BỊ CHẶN** (`id-K` §3①) |
| `O-08` | **Không biết mình cần gì** | *"can you check my photo"* · *"what do you recommend"* | `S1` | CTA *"send photos for a doctor's assessment"* |
| `O-09` | **Thời gian · khoảng cách** | *"I'm far"* · *"em ở tỉnh"* | `S4` | ⚠️ **Ở bản quốc tế mã này hẹp lại** — xem cảnh báo dưới |
| `O-10` | **So sánh đối thủ / điểm đến** | *"vs Thailand"* · *"vs Korea"* · *"cheaper in Turkey"* | `S2` | Khác biệt cụ thể — ⛔ không dìm, ⛔ không so giá có tên nước |
| `O-11` | **Người nhà phản đối** | *"my husband doesn't know"* · *"chồng em không cho"* | `S3` | Nội dung **nói với người nhà** |
| `O-12` | **Bệnh nền** | *"I'm diabetic"* · *"I'm breastfeeding"* | `S3` | 🔴 **BS duyệt từng câu** |

### ⚠️ `O-09` ở bản quốc tế — mã dễ bị dùng sai nhất

```
Ở bản nội địa, O-09 nuốt gần hết chuyện "ở xa". Ở bản quốc tế, phần lớn
nội dung đó đã TÁCH RA thành bộ OQ (§2), và tách là ĐÚNG:

O-09   = khoảng cách trong nước / lịch trình chung
         "em ở Cần Thơ", "I'm in Da Nang, can I come Saturday"
OQ-01  = SỐ NGÀY phải ở lại Việt Nam       ← hoàn toàn khác
OQ-02  = ai lo cho tôi khi tôi đã bay về   ← hoàn toàn khác

⛔ Gán "how many days do I stay" vào O-09 là xoá mất chặng S4 khỏi báo cáo.
   Đây là lỗi im lặng: tổng vẫn khớp, mà kết luận thì mất hẳn một chặng.
```

### ⛔ Hai mã agent không được tự trả lời

```
O-07 bảo hành → site ghi "lifetime warranty" mà CHƯA CÓ T&C.
                ⛔ Không nêu thời hạn nào, ⛔ không dùng chữ "lifetime".
                Viết: "follow-up and warranty policy — see terms".
O-12 bệnh nền → claim y khoa. Chỉ viết "this needs an in-person assessment
                by the surgeon".
```

---

## 2. ★★ TÁM MÃ `OQ` — CHỈ CÓ Ở KHÁCH QUỐC TẾ

> **Đây là phần giá trị riêng của agent này.** Không mã nào trong tám mã dưới đây tồn tại ở bản nội địa, và **sáu trong tám mã đang bị chặn vì thiếu dữ kiện gốc**, không phải vì nhân viên kém.

| Mã | Tên | Khách hay nói | Chặng | Rào | Trạng thái |
|---|---|---|---|---|---|
| ★ `OQ-01` | **Số ngày phải ở lại Việt Nam** | *"how many days do I need to stay"* · *"when can I fly home"* · *"em ở lại được 10 ngày thôi"* | `S4` | **XA** | 🔴 **CHẶN** — chưa có số từ Khoa Chuyên môn (`id-L` §7) |
| ★ `OQ-02` | **Ai lo cho tôi sau khi tôi bay về** | *"who do I contact when I'm back"* · *"follow-up from abroad?"* | `S4` · `S6` | **XA** | 🟠 Có khối 5 bước nhưng **thiếu thời hạn + kênh** (`id-K` §8) |
| ★ `OQ-03` | **Phiên dịch & ngôn ngữ** | *"does anyone speak English"* · *"interpreter during surgery?"* · *"Arabic?"* | `S4` | **XA** · NGỜ | 🟠 Có nêu trên site, **chưa khai ngôn ngữ nào / có phí không** |
| ★ `OQ-04` | **Ai trả chi phí nếu phải chỉnh sửa** | *"who pays for the flight if something goes wrong"* | `S4` | **XA** | 🔴 **CHẶN** — phụ thuộc T&C bảo hành |
| ★ `OQ-05` | **Visa · thư mời · thủ tục** | *"do I need a visa"* · *"invitation letter?"* · *"giấy xác nhận phẫu thuật"* | `S4` | XA | 🟠 ❌ **không thấy trên site** |
| ★ `OQ-06` | **Thanh toán quốc tế & đặt cọc** | *"can I pay by card"* · *"how much deposit"* · *"bank transfer?"* | `S5` | NGẠI | 🟠 ❌ **không thấy trên site** — ⚠️ **rào cản chốt thật** |
| ★ `OQ-07` | **Hậu cần chuyến đi** — khách sạn · đưa đón · người đi cùng | *"hotel near the hospital"* · *"airport pickup"* · *"can my husband stay with me"* | `S4` | XA | 🟢 Có nêu — ⚠️ xác nhận **miễn phí hay tính phí** |
| ★ `OQ-08` | **Điều kiện riêng về văn hoá / tôn giáo** | *"halal food"* · *"female staff only"* · *"prayer room"* · *"during Ramadan?"* | `S3` · `S4` | NGẠI | 🟠 Site ghi *"Muslim-Friendly Care"* mà **chưa khai gồm những gì** |

### Ba điều phải hiểu về bộ `OQ`

```
① SÁU TRONG TÁM MÃ ĐANG BỊ CHẶN VÌ THIẾU DỮ KIỆN GỐC.
   → Trực kênh né những câu này phần lớn là LỖI HỆ: chấm "—", ⛔ không trừ
     điểm người (id-F §7 rào ③). Và đẩy lên mục "việc hệ thống", mỗi kỳ.

② MÃ OQ XUẤT HIỆN MUỘN TRONG HỘI THOẠI, nên rất dễ bị bỏ đếm.
   Khách hỏi an toàn và giá trước; câu "how many days do I stay" thường là
   câu thứ năm, thứ sáu — lúc nhân viên đã nghĩ là đã tư vấn xong.
   ⛔ Đếm mã OQ phải đọc HẾT hội thoại, không chỉ ba tin đầu.

③ ★ MÃ OQ LÀ MÃ CỦA KHÁCH ĐÃ MUỐN LÀM.
   Khách hỏi OQ-01 đã vượt qua Sợ và Ngờ. Mất họ ở đây là mất khách ĐẮT
   NHẤT trong cả phễu — họ đã đọc hết, đã so giá, đã tin bác sĩ.
```

⚠️ **Ngưỡng cảnh báo riêng:** `OQ-01` xuất hiện trong **≥ 10% mẫu** mà tỷ lệ *"có liên hệ"* của nhóm đó **thấp hơn trung bình kỳ** → đưa thẳng lên **thẻ số tổng** và lên mục *vấn đề cốt lõi #1*. Đây là tín hiệu rõ nhất cho thấy khối đang mất khách vì **một ô dữ liệu trống**, không vì năng lực.

---

## 3. MỨC NÓNG — NĂM TÍN HIỆU *(hai tín hiệu khác bản nội địa)*

| # | Tín hiệu | Đạt khi |
|---|---|---|
| ① | **Nêu dịch vụ cụ thể** | Khách gọi tên dịch vụ hoặc tả vùng muốn làm |
| ② | ★ **Có CỬA SỔ CHUYẾN ĐI cụ thể** | Khách nói ngày về / ngày bay / khoảng ở lại: *"I'm in Vietnam 10–20 Dec"*, *"em về Tết này"*, *"wedding in March"*. ⚠️ **Thay cho tín hiệu "mốc ≤14 ngày" của bản nội địa** |
| ③ | **Để lại cách liên hệ được** | Số có mã quốc gia · WhatsApp · email · Zalo |
| ④ | **Hỏi điều kiện thực hiện** | giá cụ thể · lịch · bác sĩ · cơ sở nào · deposit |
| ⑤ | ★ **Cho khung giờ gọi KÈM MÚI GIỜ** | *"call me after 7pm Sydney time"*. ⚠️ **Khung giờ không kèm múi giờ chỉ tính nửa tín hiệu** — và đó là lỗi của câu hỏi, không phải của khách |

| Mức | Số tín hiệu |
|---|---|
| 🔴 **HOT** | 4–5 |
| 🟠 **WARM** | 2–3 |
| ⚪ **COLD** | 0–1 |

⚠️ **Tín hiệu ② và ⑤ vẫn là hai tín hiệu hiếm nhất**, và ở bản quốc tế chúng còn hiếm hơn vì **gần như không ai hỏi múi giờ**. `HOT < 2%` mẫu thì vấn đề ⛔ không phải tệp xấu — là nội dung không tạo cửa sổ chuyến đi và trực kênh không hỏi múi giờ. **Hai việc sửa được ngay trong kỳ.**

★ **Luật mùa cho tín hiệu ②** (`id-L` §6): cùng câu *"em về Tết"*

```
nói vào THÁNG 10  → cửa sổ còn mở, tín hiệu ② ĐẠT → thường là HOT
nói vào THÁNG 2   → cửa sổ đã đóng, ⛔ KHÔNG đạt  → thường là COLD
```

★ **Hai ô nguy hiểm nhất của cả dashboard:**

```
① HOT/WARM mà CHƯA CÓ CÁCH LIÊN HỆ NÀO     — lead nóng chưa vào tay ai
② ★ HOT/WARM + đến NGOÀI GIỜ 8–17 ICT + chờ > 12h
   — lead nóng mất vì LỊCH TRỰC, không vì năng lực. Tô đỏ, đếm riêng,
     đưa lên thẻ số tổng, và đẩy vào "việc hệ thống" chứ KHÔNG vào sổ tay.
```

---

## 4. VÌ SAO RƠI — MỖI HỘI THOẠI MỘT GIÁ TRỊ

> ⛔ Một hội thoại chỉ được gán **đúng một** nguyên nhân rơi. Gán hai là tổng không khớp cỡ mẫu.

| Nguyên nhân | Nhận ra khi | Ai sửa |
|---|---|---|
| **nội dung** | Khách vào rồi hỏi thứ quảng cáo đã hứa mà nội dung không có | Marketing |
| **trực kênh** | Khách hỏi, được trả lời, rồi im — hoặc bị bỏ sau 1 lượt | Trực kênh |
| **hệ thống — dữ kiện** | Thiếu số ngày ở lại · thiếu T&C bảo hành · thiếu thông tin thanh toán/visa | Vận hành · Khoa Chuyên môn · Pháp chế |
| ★ **hệ thống — múi giờ** | Tin đến ngoài giờ ICT, không ai trả lời trong 12h, khách không quay lại | **Lịch trực** |
| ★ **hệ thống — ngôn ngữ** | Khách nhắn ngôn ngữ không có người trực, hoặc bị trả lời sai ngôn ngữ | Vận hành |
| **khách tự dừng** | Khách nói *"let me think about it"* rồi không quay lại dù đã được trả lời đủ | — |
| **không rơi** | Có cách liên hệ hoặc chốt lịch trong chat | — |

★ **Ba nhánh "hệ thống" là của bản quốc tế.** Bản nội địa có một nhánh `hệ thống` chung. Tách ba nhánh vì **ba người khác nhau sửa**, và vì gộp lại thì mục việc hệ thống ra một dòng vô nghĩa kiểu *"cần hoàn thiện hệ thống"*.

⚠️ *"Khách rơi **sau khi** được trả lời"* là tín hiệu mạnh hơn *"khách không hỏi"*. **Rơi sau khi được trả lời là lỗi nội dung hoặc lỗi câu trả lời, ⛔ không phải lỗi tệp.**

---

## 5. ★ BẢNG GIAO "YẾU GÌ" — ĐẦU RA THẬT CỦA BƯỚC B5

| `MÃ O / OQ` | `TẦNG` | `SỐ LẦN HỎI /100 HT` | `SỐ NỘI DUNG ĐÃ CÓ` | `KẾT LUẬN` |
|---|---|---|---|---|

★ **Cột `TẦNG` là cột của bản quốc tế.** Cùng mã `O-01` mà `TT-A` hỏi 20 lần và `TT-C` hỏi 4 lần là **hai kết luận khác nhau** — ⛔ không gộp thành một dòng.

### Luật đọc bảng — bốn ô

```
                      nội dung ĐÃ CÓ nhiều        nội dung ĐÃ CÓ ít
                  ┌──────────────────────────┬──────────────────────────┐
  khách hỏi NHIỀU │ ② ĐANG ĐÚNG HƯỚNG        │ ① LỖ HỔNG — ƯU TIÊN 1    │
                  │   nhưng có thể trả lời SAI│   nhu cầu có, nội dung   │
                  │   → kiểm trước khi làm thêm│   không. Viết ngay.      │
                  ├──────────────────────────┼──────────────────────────┤
  khách hỏi ÍT    │ ③ ĐANG PHÍ               │ ④ ĐỂ YÊN                 │
                  │   → cắt bớt               │                          │
                  └──────────────────────────┴──────────────────────────┘
```

⚠️ **Ô ① của bản quốc tế có hai loại, và chúng đi về hai nơi khác nhau:**

```
① a · THIẾU NỘI DUNG  → việc của Marketing, viết được ngay.
① b · THIẾU DỮ KIỆN   → ⛔ KHÔNG viết được. Mã OQ-01 · OQ-04 · OQ-05 · OQ-06
      nằm ở đây: không ai viết nổi một hook về "số ngày ở lại" khi chưa có
      con số. → đi vào mục [CHỜ CẤP], KHÔNG vào kế hoạch nội dung.
```

★ **Phân biệt được ①a và ①b là việc có giá trị nhất của bảng này.** Trộn chúng lại thì kế hoạch nội dung kỳ sau có những việc **không ai làm được**, và tháng sau vẫn nằm đó.

### Ngưỡng ra việc

| Số lần / 100 hội thoại | Việc |
|---|---|
| **≥ 15** | Mở **tuyến riêng** trong kỳ — ≥ 2 nội dung, có format riêng |
| **8 – 14** | **Một hook** trong kỳ |
| **5 – 7** | Ghi nhận, gộp làm ý phụ |
| **< 5** | ⛔ Không lên kế hoạch. Ghi sổ theo dõi |

⚠️ Mẫu < 50 HT thì ⛔ không dùng ngưỡng tuyệt đối. Và **mỗi tầng tính ngưỡng riêng** chỉ khi tầng đó có ≥ 10 HT (`id-A` §5).

---

## 6. ★ BỐN RÀO CẢN CHỐT — `SỢ` · `NGỜ` · `NGẠI` · `XA`

Bản nội địa có ba rào. Bản quốc tế có **bốn**, và rào thứ tư là rào quyết định.

| Rào | Khách đang nghĩ gì | Bằng chứng gỡ | Nặng nhất ở tầng |
|---|---|---|---|
| **SỢ** | Đau không? Biến chứng? Mổ ở nước ngoài có an toàn? | Giấy phép BYT · quy trình mổ có văn bản · phòng mổ vô khuẩn · hội đồng chuyên môn | **`TT-C`** |
| **NGỜ** | Cơ sở này có thật không? Có phép? Bác sĩ có bằng gì? Giá có đúng như web? | Giấy phép · hồ sơ bác sĩ · **bảng giá công khai + phụ phí 10% nói trước** · International Patient Department | **`TT-A` · `TT-D`** |
| **NGẠI** | Nghỉ bao lâu? Ai biết? Về nhà sưng thì giải thích thế nào? | Mốc hồi phục dạng khoảng · **kênh nhắn tin riêng tư** · cam kết bảo mật | `TT-A` · `TT-B` · `TT-C` |
| ★ **XA** | **Tôi bay về rồi thì ai lo cho tôi?** | Quy trình 5 bước · phiên dịch tiếp tục sau khi về · **số ngày ở lại** · T&C bảo hành · ai liên hệ, trong bao lâu | **`TT-B` · `TT-C`** |

### 6.1 ★ RÀO `XA` — BỐN CÂU, THEO ĐÚNG THỨ TỰ KHÁCH NGHĨ

Ba rào đầu, khách nội địa cũng có. Rào `XA` **chỉ có ở khách quốc tế**, và nó là rào **cuối cùng** — khách đã vượt Sợ, Ngờ, Ngại rồi mới chạm vào nó.

| # | Câu khách nghĩ | Mã | Trả lời bằng | Trạng thái |
|---|---|---|---|---|
| 1 | *"Tôi phải ở Việt Nam bao nhiêu ngày?"* | `OQ-01` | **Một con số khoảng** + mốc nào *(cắt chỉ · tái khám cuối · được phép bay)* | 🔴 chưa có |
| 2 | *"Về nhà rồi có vấn đề thì liên hệ ai?"* | `OQ-02` | Tên bộ phận · kênh · ngôn ngữ · **trong bao lâu** | 🟠 thiếu một nửa |
| 3 | *"Nếu phải chỉnh sửa thì ai trả chi phí và chi phí bay?"* | `OQ-04` | **T&C bảo hành bằng văn bản** — chưa có thì ⛔ không viết | 🔴 chưa có |
| 4 | *"Có ai nói được tiếng của tôi, cả lúc mổ và sau khi về?"* | `OQ-03` | Phiên dịch: ngôn ngữ nào · có phí không · kéo dài bao lâu | 🟠 thiếu chi tiết |

> ⛔ **Không trả lời được câu 1 thì khách không đặt vé** — và không đặt vé thì lead ⛔ không bao giờ thành ca.

★ **Phép thử một hội thoại quốc tế đã xong hay chưa** *(dùng thay cho câu "khách đã cho số chưa")*:

> **"Đọc hết hội thoại này, khách có đủ thông tin để mở app hàng không và chọn ngày bay chưa?"**

Chưa → hội thoại chưa xong, dù khách đã cho số, dù nhân viên đã rất lịch sự. Ghi vào ô `S4 chưa đóng`.

### Luật gỡ rào

> Mọi câu trả lời phải gỡ **đúng rào cản của tầng + chặng đang nhắm**, ⛔ không gỡ chung chung cả bốn. Gỡ sai rào = nói lạc đề với người đang lo chuyện khác.

⚠️ **Lỗi gỡ sai rào phổ biến nhất trong hội thoại thật:** khách `TT-C` hỏi `OQ-01` *(bao nhiêu ngày)* → nhân viên trả lời bằng **giá và ưu đãi**. Khách đang ở rào `XA`, bị trả lời bằng rào `NGẠI`. Đây là tiêu chí `N4.2` của `id-F`, và nó là tiêu chí trượt nhiều thứ hai của bản quốc tế.

---

## 7. RÀO CẢN QUAN SÁT ĐƯỢC — ĐƯỢC PHÉP NHIỀU

Khác với "vì sao rơi", một hội thoại **có thể mang nhiều rào cản**. Đếm theo lượt xuất hiện:

`chưa nói tình trạng` · `hỏi giá ngay` · `sợ đau/nghỉ việc` · `người nhà cản` · `đã làm nơi khác` · `so giá đối thủ` · `chờ ưu đãi` · `chưa tin cơ sở` ·
★ `chưa biết ở lại mấy ngày` · ★ `lo thanh toán/đặt cọc` · ★ `rào ngôn ngữ` · ★ `cửa sổ chuyến đi quá ngắn` · ★ `đi một mình, không có người đi cùng`

---

## 8. CÂU HỎI NGẦM — THỨ LÀM NÊN THẺ INSIGHT

> Câu khách gõ **không phải** điều khách muốn biết. Thẻ insight phải dịch được câu đó.

```
Khách gõ : "How much is rhinoplasty?"
Câu ngầm : "Con số trên web có phải con số cuối cùng không, hay sang đó
            lại phát sinh mà tôi thì đã bay nửa vòng trái đất?"

Khách gõ : "How many days do I need to stay?"
Câu ngầm : "Tôi phải xin nghỉ bao nhiêu ngày, đặt vé về ngày nào, và nếu
            sưng chưa hết thì tôi có bị kẹt lại không?"

Khách gõ : "Does anyone speak English?"
Câu ngầm : "Lúc tôi nằm trên bàn mổ và lúc tôi lo lắng ở nhà một mình,
            có người nào tôi nói được chuyện không?"

Khách gõ : "em về nước tháng 12"
Câu ngầm : "Lịch của tôi đã cố định và không đổi được. Bên mình có xếp
            được vào đúng cửa sổ đó không, hay tôi lại hoãn thêm một năm?"
```

★ Viết câu ngầm bằng **chữ của khách**, ⛔ không bằng tính từ marketing. Và **giữ nguyên ngôn ngữ của khách** trong phần trích.

---

## 9. ĐỌC NỬA TRỰC KÊNH TRẢ LỜI — INSIGHT TẦNG HAI

| Dấu hiệu trong câu trả lời | Nghĩa là |
|---|---|
| Gõ đoạn dài giải thích **cùng một thứ** ở nhiều hội thoại | ★ **Thiếu hẳn một nội dung.** Việc này đáng lẽ một trang EN làm |
| Gửi ảnh chụp màn hình bảng giá | ⚠️ Ở bản quốc tế là **lỗi lạ**: giá đã công khai → thiếu **link trang giá**, không thiếu giá |
| Xin số ngay câu đầu | Đang **né câu hỏi** → nội dung không giải quyết được mã đó |
| ★ Trả lời `OQ-01` bằng *"tuỳ ca, chị qua khám sẽ rõ"* | **Lỗi hệ, không phải lỗi người** — nhân viên không có số để nói |
| ★ Dùng câu dịch máy cho nội dung hậu phẫu | **Cờ đỏ `CĐ-9`** — rủi ro y khoa, không phải lỗi văn phong |
| ★ Trả lời khách `TT-D` bằng khối "đưa đón sân bay, khách sạn" | Chưa nhận ra tầng — tiêu chí `N7.2` |
| Khách hỏi → được trả lời → im luôn | Câu trả lời **không đóng được nỗi sợ** |

★ Tầng hai có **hai đích đến**: ① đầu vào làm nội dung, và ② **bằng chứng chấm điểm** ở `id-F` — ⛔ chỉ khi gắn được vào đúng tiêu chí `N1…N7` và đúng `HT-nnn`.

⛔ Nhận xét chung chung kiểu *"bạn này tư vấn hời hợt"* mà không chỉ ra tiêu chí + hội thoại thì **không được ghi vào bất cứ đâu**.

---

## 10. ĐẦU RA CHUẨN CỦA BƯỚC B2–B5

```
① BẢNG ĐẾM MÃ O    : 12 mã × số lần × % mẫu (kể cả mã = 0)
①' ★ BẢNG ĐẾM MÃ OQ : 8 mã × số lần × % mẫu × ★ trạng thái chặn
② MỨC NÓNG         : HOT/WARM/COLD × trạng thái liên hệ
                      + ★ ô HOT/WARM ngoài giờ chờ >12h (tô đỏ)
③ VÌ SAO RƠI       : 7 nguyên nhân (3 nhánh hệ thống), tổng = cỡ mẫu
④ RÀO CẢN          : xếp theo lượt xuất hiện
④' ★ BỐN RÀO CHỐT  : SỢ/NGỜ/NGẠI/XA × tầng thị trường
⑤ BẢNG GIAO §5     : 5 cột (có cột TẦNG) + kết luận theo 4 ô
                      + ★ tách ①a thiếu nội dung / ①b thiếu dữ kiện
⑥ TOP 10 CÂU CHÉP  : câu hỏi đầu hay nhất, nguyên văn, ĐÚNG NGÔN NGỮ, đã ẩn danh
⑦ ★ BẢNG S4 CHƯA ĐÓNG : số HT chạm rào XA mà bốn câu §6.1 chưa được trả lời đủ
⑧ CỠ MẪU           : đọc bao nhiêu · bỏ bao nhiêu · vì sao
```

---

## 11. TỰ KIỂM SỔ NÀY

- [ ] Đếm đủ 12 mã `O` **và** 8 mã `OQ`, kể cả mã bằng 0?
- [ ] Có câu *"how many days"* nào bị gán vào `O-09` thay vì `OQ-01` không?
- [ ] Mã `OQ` có được đếm từ **toàn bộ** hội thoại, không chỉ ba tin đầu?
- [ ] `O-00` có vượt 10% không? Vượt thì đã báo lại chưa?
- [ ] Tổng "vì sao rơi" có **bằng đúng** cỡ mẫu không? Ba nhánh hệ thống có tách riêng không?
- [ ] Ô `HOT/WARM chưa có liên hệ` và ô `HOT/WARM ngoài giờ chờ >12h` có lên thẻ số tổng không?
- [ ] Tín hiệu ② có áp **luật mùa** chưa? Tín hiệu ⑤ có đòi **múi giờ** chưa?
- [ ] Bảng giao có **cột tầng** chưa? Ô ① có tách **①a thiếu nội dung / ①b thiếu dữ kiện** chưa?
- [ ] Mỗi insight có gắn `HT-nnn` truy ngược được không?
- [ ] Trích dẫn có giữ **nguyên ngôn ngữ của khách** và đã ẩn danh đủ **12 thứ** (`id-B` §2) chưa?
- [ ] `O-07` và `O-12` có bị tự trả lời không?
- [ ] ★ Có hội thoại nào qua được **phép thử "đủ để chọn ngày bay chưa"** mà vẫn bị ghi là rơi, hoặc ngược lại?

---

<!-- ===== id-E-to-chuc-ads-chi-so.md ===== -->

# id-E · ★ TỔ CHỨC ADS QUỐC TẾ & ĐỌC CHỈ SỐ

> Sổ này trả lời hai câu: **quảng cáo quốc tế được tổ chức thế nào** (để cắt số đúng chiều), và **đọc số ra kết luận gì** (để không chữa nhầm bệnh).
>
> ⚠️ Khác bản nội địa ở ba chỗ, và cả ba đều là thay đổi logic chứ không phải đổi tên:
> ① cắt theo **THỊ TRƯỜNG × DỊCH VỤ**, ⛔ không theo khu vực ·
> ② chuỗi chỉ số có thêm mắt xích cuối **CPA-KHÁM** ·
> ③ cửa sổ đánh giá **≥ 8 tuần** với `TT-B` · `TT-C`.
> Nguồn tổ chức chiến dịch: `Agent-AdsOptimize-Kangnam-QT`.

---

## 1. CHUỖI CHỈ SỐ — GIỮ ĐÚNG THỨ TỰ

```
Chi phí tổng → CPM → CTR → CPI (Inbox) → CPL (Lead) → CPB (Booking)
→ ★ CPA-KHÁM (chi phí trên một khách ĐÃ ĐẾN KHÁM)
```

Mỗi mắt xích hiện **ba thứ**: giá trị · so **mục tiêu** · so **kỳ trước** — và ở bản này, **mỗi mắt xích phải cắt được theo tầng thị trường**.

| Chỉ số | Công thức | Mục tiêu lấy từ đâu |
|---|---|---|
| ★ **Chi phí tổng** | Σ chi của kỳ | ngân sách kỳ · ⛔ không có «mốc tốt/xấu» |
| **CPM** | chi ÷ hiển thị × 1.000 | TB 30 ngày **của chính thị trường đó** |
| **CTR** | click ÷ hiển thị | TB 30 ngày của thị trường |
| **CPI** | chi ÷ inbox | TB 30 ngày của thị trường |
| **CPL** | chi ÷ lead hợp lệ | TB 30 ngày của thị trường |
| **CPB** | chi ÷ booking | TB 30 ngày của thị trường |
| ★ **CPA-KHÁM** | chi ÷ số khách **đã đến khám** | ⚠️ cửa sổ ≥ 8 tuần, ⛔ không đo trong kỳ 2 tuần |

★ **Mắt xích 0 là số tiền đã tiêu.** CPI, CPL, CPB đều là thương của cùng một tử số — không nhìn tử số thì đang đọc tỷ lệ trong chân không.

★★ **Mắt xích cuối là mắt xích của bản quốc tế, và nó đổi cả cách đọc kỳ:**

```
TT-B / TT-C : độ trễ lead → đến khám là 4–12 TUẦN (id-L §4).
→ CPL rẻ trong kỳ KHÔNG phải tin tốt nếu CPA-KHÁM của kỳ cách đây 8–12
  tuần đang xấu đi. Hai con số nói về hai nhóm khách khác nhau.
→ Mỗi báo cáo phải in CẢ HAI, kèm dòng: "CPL của kỳ này · CPA-KHÁM của tệp
  vào kỳ <kỳ cách đây 8–12 tuần>". ⛔ Không đặt hai số cạnh nhau như thể
  chúng nói về cùng một tệp.
TT-D       : độ trễ ngắn (expat đang ở VN) → đo được trong kỳ như bản nội địa.
```

⚠️ Chưa đủ 30 ngày → ghi `⚠ chưa có mốc so sánh`. ⛔ **Không tự đặt mốc.**
⚠️ Ngày có **dưới 3 kết quả** thì ⛔ không vẽ điểm CPB/CPL của ngày đó.
⚠️ **Cỡ mẫu quốc tế nhỏ** → nhiều ô sẽ `⚠ MẪU NHỎ`. Ghi nhãn, ⛔ không nới ngưỡng.

### ★ LUẬT QUAN TRỌNG NHẤT — PHÂN RÃ TRƯỚC KHI KẾT LUẬN

```
CPL = (CPM/1000) ÷ ( CTR × click→inbox% × inbox→lead% )

⛔ KHÔNG KẾT LUẬN "CẦN LÀM THÊM NỘI DUNG" KHI THÀNH PHẦN XẤU ĐI KHÔNG PHẢI CTR.
```

| Thành phần xấu đi | Thật ra là việc của | Agent phải nói |
|---|---|---|
| **CTR** giảm | Nội dung | *"Đây là vấn đề nội dung"* |
| **CPM** tăng | Adnet — tệp, bid, lịch · ⚠️ **hoặc đổi thị trường**: CPM `AU`/`US` cao hơn `KH` nhiều lần | *"Kỳ này KHÔNG phải vấn đề nội dung — kiểm cơ cấu thị trường trước"* |
| **click→inbox** giảm | Kỹ thuật — điểm đến, lời chào tự động · ⚠️ **hoặc `geo_mode` sai** (`id-L` §1) | *"Không phải nội dung"* |
| **inbox→lead** giảm | ★ **Trực kênh** — ca trực, thời gian phản hồi, cách xin liên hệ · ⚠️ **hoặc múi giờ** (`id-L` §4) | *"Không phải nội dung"* → đẩy sang `id-F` và sang *việc hệ thống* |

★ Đây là chỗ agent này mạnh hơn mọi agent ads khác: **mắt xích `inbox→lead` được chứng minh bằng chính hội thoại**, không phải suy đoán.

★★ **Và bản quốc tế có một bước phân rã nữa, trước cả bốn dòng trên:**

```
CPM/CPL tăng → KIỂM CƠ CẤU THỊ TRƯỜNG TRƯỚC.
Chi dịch từ KH sang AU thì CPM tăng, CPL tăng, mà KHÔNG có gì xấu đi cả —
đó là một quyết định ngân sách, không phải một sự cố.
⛔ Đọc CPL tổng mà không xem cơ cấu thị trường là cách chắc chắn nhất để
   kết luận ngược hẳn với sự thật.
```

⚠️ Một agent quảng cáo luôn kết luận *"cần làm thêm content"* là một agent vô dụng. **Dám nói "không phải lỗi nội dung" là giá trị, không phải né việc.**

---

## 2. TỔ CHỨC CHIẾN DỊCH QUỐC TẾ — MỘT CHIẾN DỊCH = MỘT TẦNG × MỘT NHÓM THỊ TRƯỜNG

Bản nội địa cắt theo **zone dịch vụ**. Bản quốc tế cắt theo:

```
MỘT CHIẾN DỊCH  =  MỘT TẦNG  ×  MỘT NHÓM THỊ TRƯỜNG CÙNG LUẬT QUẢNG CÁO  ×  MỘT DỊCH VỤ
```

⛔ **Không gộp `AU` với `KH` vào một chiến dịch:** khác luật quảng cáo (`id-K` §4), khác ngôn ngữ, khác giá chấp nhận được, khác múi giờ gọi lại.

### Hai trường bắt buộc của mọi dòng số

| Trường | Giá trị | Vì sao bắt buộc |
|---|---|---|
| `market` | mã theo `id-L` §9 | **Người xem đang ở đâu** — ⛔ không phải thành phố trong câu quảng cáo |
| `geo_mode` | `Presence` hoặc `Presence+Interest` | Kiểu nhắm vị trí |

| Tầng | `geo_mode` đúng | Vì sao |
|---|---|---|
| `TT-A` · `TT-B` · `TT-C` | `Presence+Interest` | Hứng cả người đang ở nước họ và người đang tìm hiểu về Việt Nam |
| ★ `TT-D` (expat tại VN) | **`Presence` — bắt buộc** | `Presence+Interest` ở đây hút toàn bộ traffic du lịch y tế vào landing sai |

⚠️ **Lỗi tốn tiền nhất và im lặng nhất của gói quốc tế:** để nền tảng tự chọn `Presence or interest` cho chiến dịch expat → CPL **trông rẻ** mà không ai đến khám. ⛔ Không có cảnh báo nào trong Google Ads cho lỗi này.
→ Khi đọc số, dấu hiệu nhận ra trong **hội thoại**: chiến dịch khai `TT-D` nhưng inbox toàn khách hỏi *"how many days"* và *"airport pickup"*. Agent **phải** nói ra điều này.

### Sáu line nội bộ

`Kangnam All` · `KN PTTM` · `KN Beauty` · `KN Weightloss` · `KN Việt Kiều` · `KN Quốc tế (TA)`

★ Bản này chỉ đọc hai line cuối: **`KN Việt Kiều` ≈ `TT-B`** và **`KN Quốc tế (TA)` ≈ `TT-A/C/D`**.
⛔ Không so chéo CPL giữa hai line khác nhau, và ⛔ **không so chéo giữa hai thị trường** trong cùng một line.

---

## 3. NGÂN SÁCH THEO CHẶNG — `S3` VÀ `S4` LÀ HAI CHẶNG PHẢI CÓ TIỀN

Bản nội địa dồn ngân sách vào nấc `A3` (nỗi sợ). Bản quốc tế phải dồn vào **`S3` và `S4`**.

| Chặng | Chạy gì | % ngân sách tối thiểu | Ghi chú |
|---|---|---|---|
| `S1` | ⛔ **không chạy landing chốt** | — | Ép bán ở đây là đốt tiền |
| `S2` | Landing điểm đến *(về Việt Nam, chưa bán Kangnam)* | — | `TT-C` **vào phễu ở đây**, không ở `S3` |
| `S3` | Nội dung gỡ **SỢ** | **≥ 10%** | |
| ★ `S4` | Nội dung **kế hoạch chuyến đi** | ★ **≥ 15%** | Cạnh tranh thấp nhất cả phễu, và gần như không ai làm |
| `S5` | Giá + đặt lịch | — | |
| `S6` | Trang hướng dẫn hậu phẫu | ⛔ **không chạy ads** | Dùng trong CRM/WhatsApp — tài sản giữ review |
| `S7` | Dịch vụ tiếp theo | — | |

★ **Vì sao `S4` phải có 15%:** khách đến `S4` **đã vượt qua Sợ và Ngờ**. Họ muốn làm. Họ chỉ đang tính *chuyến đi có chạy được không*. Từ khoá `S4` có **cạnh tranh thấp nhất** vì đối thủ đổ tiền vào từ khoá giá — ai làm trước thì chiếm.

⚠️ **Hệ quả khi đọc hội thoại:** thấy `S4` chiếm tỷ lệ cao trong inbox mà ngân sách `S4` bằng 0 → đó ⛔ không phải tin xấu về nội dung, đó là **cơ hội lớn nhất của kỳ**: khách đã tự tìm tới chặng đó mà không ai mời.

---

## 4. CHẤM NỘI DUNG — 🟢🟡🔴 VÀ LUẬT PORT THỊ TRƯỜNG

| Chấm | Điều kiện | Cải tiến |
|---|---|---|
| 🟢 **TỐT** | CTR ≥ trung vị **và** CPL ≤ trung vị **của cùng thị trường** | **Nhân bản** — giữ hook, đổi chân dung |
| 🟡 **TB** | Một trong hai đạt | **Biến thể** — đổi **đúng một** biến |
| 🔴 **KÉM** + mã `O`/`OQ` vẫn cao | CTR ≤ −30% trung vị, CPM trong ±15% | **Giữ ý — bỏ hook** |
| 🔴 **KÉM** + mã thấp | | **Bỏ hẳn** |

⛔ **Không đổi ≥3 biến cùng lúc** — đổi ba biến thì dù tốt lên cũng không học được gì.

★★ **LUẬT PORT THỊ TRƯỜNG — nặng hơn luật port vùng miền của bản nội địa:**

```
Nội dung 🟢 ở thị trường này ⛔ KHÔNG tự động 🟢 ở thị trường khác.
Và có ba lý do cứng, không phải chuyện khẩu vị:

① KHÁC BỘ BẰNG CHỨNG ĐƯỢC PHÉP DÙNG. Hook dựa trên testimonial 🟢 ở TT-A
   thì ở TT-C là 🔴 CHẶN — AHPRA cấm thẳng (id-K §4).
② KHÁC NGÔN NGỮ VÀ KHÁC CÁCH ĐỌC. TT-A và GCC đọc EN như ngôn ngữ thứ hai:
   ⛔ không thành ngữ, ⛔ không chơi chữ, câu ngắn, số viết bằng chữ số.
③ KHÁC RÀO CẢN. TT-A nặng NGỜ, TT-C nặng SỢ + XA. Cùng một hook gỡ NGỜ
   đem sang TT-C là gỡ sai rào.
```

⛔ **Và ⛔ không dịch nội dung tiếng Việt sang tiếng Anh rồi chạy.** Đó là sai lầm đặc trưng số một của gói quốc tế.

---

## 5. GOOGLE ADS — 🔴 KHUNG CHỜ DỮ LIỆU

> Cột đầu vào ở `id-B` §5. Phần dưới là **cách đọc khi dữ liệu về**.

### Bốn việc Google Ads làm được mà Meta không

| # | Việc | Ra kết luận gì |
|---|---|---|
| ① | **Search term → mã `O` / `OQ`** | Khách gõ gì là insight trực tiếp. Map thẳng vào cùng bảng với hội thoại |
| ② | **Truy vấn tốn tiền không chuyển đổi** | Cắt được trong ngày |
| ③ | **Truy vấn có người tìm mà chưa có trang EN trả lời** | Lỗ hổng nội dung → bàn giao `Agent-AdsOptimize-Kangnam-QT` *(mode GEO-ANSWER)* |
| ★ ④ | **Truy vấn chặng `S4`** | *"how many days in vietnam after rhinoplasty"* · *"english speaking surgeon hanoi"* · *"visa for medical treatment vietnam"* — nhóm truy vấn **ít cạnh tranh nhất và ít ai trả lời nhất** |

### Ba bảng Google Ads trong dashboard

```
① Chuỗi chỉ số : CPC → CTR → CPL theo chiến dịch × THỊ TRƯỜNG
② Search term  : truy vấn · ngôn ngữ · chi · click · chuyển đổi
                 · mã O/OQ gán được · ★ chặng S1–S7 · quyết định
③ So kênh      : cùng một mã, Meta tốn bao nhiêu / Google tốn bao nhiêu để ra 1 lead
```

⛔ Khi chưa có file: mọi ô để `null`, dashboard hiện `chưa có dữ liệu Google Ads`. ⛔ Không ước lượng, ⛔ không lấy số Meta gán sang.

---

## 6. NỐI HỘI THOẠI ↔ NỘI DUNG ADS

| Nối theo | Cách làm | Độ tin |
|---|---|---|
| **Nội dung khách bấm vào** (ref/ad id trong hội thoại) | Chuẩn nhất | ✅ Cao |
| **Fanpage + khoảng ngày + market** | Khi không có ref | 🟡 TB — ghi `⚠ suy ra` |
| **Dịch vụ khách hỏi** | Khi chỉ có hai thứ trên | 🔴 Thấp — chỉ tham khảo |

★★ **Luật riêng của bản quốc tế — chỉ hai kênh nối được:**

```
✅ Messenger                         : có ref của ad → nối được
✅ WhatsApp qua click-to-WhatsApp    : có tham số → nối được NẾU tham số còn
⛔ Telegram · Viber · Line · KakaoTalk · Zalo và WhatsApp khách tự nhắn
   → KHÔNG nối được. Ghi `nguồn: tự tìm / chưa truy được`.
   ⛔ KHÔNG chia đều lead của các kênh này cho các chiến dịch đang chạy.
```

⚠️ **Hệ quả phải nói ra mỗi kỳ:** `% inbox truy được về chiến dịch`. Nếu con số này dưới 50% thì mọi kết luận kiểu *"nội dung X kéo được 12 inbox"* chỉ đúng với phần truy được — và phải ghi rõ như thế.

Gộp mọi ID cùng một nội dung về **một dòng theo TÊN NỘI DUNG**. Mỗi dòng mang: `market` · `chi` · `inbox` · `lead` · `booking` · `CPI` · `CPL` · `đánh giá 🟢🟡🔴` · `khách hỏi gì · CD` · **cờ pháp chế theo thị trường**.

⚠️ **Chiến dịch nhiều mẫu** (không tách được chi) thì ⛔ không chia đều chi — tách một bảng riêng và ghi rõ tổng.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Đã **phân rã CPL** trước khi kết luận chưa?
- [ ] ★ Đã **kiểm cơ cấu thị trường** trước khi kết luận về CPM/CPL tăng chưa?
- [ ] Có kết luận "cần thêm content" trong khi thành phần hỏng không phải CTR không?
- [ ] Mỗi chỉ số có đủ **ba thứ** (giá trị · mục tiêu · kỳ trước) và **cắt được theo tầng** không?
- [ ] ★ Có đo `TT-B`/`TT-C` trong cửa sổ **ngắn hơn 8 tuần** không?
- [ ] ★ `CPL kỳ này` và `CPA-KHÁM` có bị đặt cạnh nhau như thể cùng một tệp không?
- [ ] Có so chéo CPL giữa hai **thị trường** hoặc hai **line** không?
- [ ] Có dòng số nào thiếu `market` mà vẫn được gán cho một tầng không?
- [ ] ★ `geo_mode` của chiến dịch `TT-D` có đúng `Presence` không?
- [ ] ★ Đã in `% inbox truy được về chiến dịch` chưa?
- [ ] `nhân viên chạy ads` có bị trộn với `nhân viên trực kênh` không?
- [ ] Có nội dung nào được port sang thị trường khác mà **không kiểm lại bộ bằng chứng được phép dùng** không?

---

<!-- ===== id-F-cham-diem-nhan-vien.md ===== -->

# id-F · ★★ TIÊU CHÍ CHẤM ĐIỂM & PHÂN LOẠI NHÂN VIÊN TRỰC KÊNH QUỐC TẾ

> Sổ nhạy cảm nhất của repo. Nó tạo ra một con số gắn với **tên một con người**.
> ⛔ Chưa đọc hết §1 và §7 thì ⛔ không được chấm.
>
> ⚠️ Bản quốc tế có **bảy nhóm tiêu chí** (`N1`–`N7`) và **mười cờ đỏ** (`CĐ-1`–`CĐ-10`). Nhóm `N7` và bốn cờ đỏ cuối ⛔ không có ở bản nội địa.

---

## 1. VÌ SAO AGENT NÀY CHẤM ĐIỂM SỐ CÒN `Agent-QC-Telesale` THÌ KHÔNG

`Agent-QC-Telesale` cố tình **không** cho điểm số, vì cuộc gọi có nhóm `giọng & ngữ điệu` — chỉ chấm được khi có audio, và bản ghi hay mất tiếng.

Chat thì khác ở ba điểm:

```
① Bằng chứng ĐẦY ĐỦ — mọi chữ đều được lưu, không có "mất tiếng".
② Mốc thời gian CHÍNH XÁC đến giây — SLA đo được, không phải cảm nhận.
③ Không có nhóm nào phụ thuộc âm thanh — mọi tiêu chí đều đọc được từ văn bản.
```

★★ **Nhưng bản quốc tế có một điều kiện thứ tư, và nó là điều kiện nặng nhất:**

```
④ PHẢI TÁCH ĐƯỢC "KHÔNG LÀM" KHỎI "KHÔNG THỂ LÀM".
   Trực kênh quốc tế đang làm việc với SÁU Ô DỮ LIỆU TRỐNG (id-L §7, id-K §8):
   số ngày ở lại · T&C bảo hành · ai trả phí bay · visa · thanh toán · phiên dịch.
   Và với MỘT LỊCH TRỰC LỆCH MÚI GIỜ.

   → Chấm một người "né câu hỏi" khi hệ thống chưa cấp câu trả lời là
     CHẤM SAI NGƯỜI. Bản quốc tế có nhiều ô như thế hơn bản nội địa rất nhiều.
   → Đó là lý do rào an toàn ③ ở §7 nặng gấp đôi ở bản này.
```

Điểm số chỉ hợp lệ khi đi kèm **bốn rào an toàn ở §7**. ⛔ Bỏ một rào là sổ này thành công cụ kỷ luật, không còn là công cụ kèm cặp.

---

## 2. CÁCH CHẤM — HAI TẦNG

```
TẦNG 1 · từng hội thoại : mỗi tiêu chí chấm ✓ / ✗ / —
TẦNG 2 · từng nhân viên : quy ra điểm 0–100 khi đủ mẫu, rồi phân loại A/B/C/D
```

| Ký hiệu | Khi nào | Tính điểm thế nào |
|---|---|---|
| `✓` **ĐẠT** | Có bằng chứng trong hội thoại | Cộng đủ điểm tiêu chí |
| `✗` **CHƯA ĐẠT** | Có bằng chứng là **không làm** hoặc **làm sai** | 0 điểm |
| `—` **KHÔNG ÁP DỤNG** | Tình huống không phát sinh · **hoặc hệ thống chưa cấp dữ kiện** · **hoặc ngoài giờ ICT** | ⛔ **Loại khỏi mẫu số**, ⛔ không tính là trượt |

### Công thức

```
Điểm một hội thoại = (tổng điểm ✓) ÷ (tổng điểm các tiêu chí KHÔNG phải "—") × 100
Điểm một nhân viên = trung bình điểm các hội thoại của người đó trong kỳ
```

⚠️ `—` **không phải** `✗`. Gộp hai cái này là cách làm cho một nhân viên trông tệ chỉ vì khách của bạn ấy nhắn lúc 2 giờ sáng.

★ **Bản quốc tế sẽ có nhiều ô `—` hơn bản nội địa, và đó là đúng.** Một hội thoại quốc tế điển hình chấm được 12–16 tiêu chí trong 25, không phải cả 25. Mẫu số nhỏ thì **mỗi ô `✗` nặng hơn** — nên bằng chứng phải chắc hơn, không lỏng hơn.

---

## 3. BẢY NHÓM TIÊU CHÍ — THANG 100

### `N1` · PHẢN HỒI & SLA — **15 điểm** *(nội địa: 20)*

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N1.1` | Trả lời tin đầu **≤ 5 phút** | 6 | ⚠️ **Chỉ tính tin đến trong 08:00–17:00 ICT**. Ngoài khung → `—`, và xét `N7.4` |
| `N1.2` | Không để khách **bỏ sau 1 lượt** | 4 | Khách nhắn ≥2 lượt, hoặc NV có ít nhất 1 lượt đuổi theo |
| `N1.3` | Không bỏ sót tin khách trong ca | 3 | Mọi câu hỏi của khách đều được chạm tới |
| `N1.4` | **Theo đuổi lại** khi khách im | 2 | Có ≥1 tin chủ động sau khi khách im > 30 phút *(trong giờ)* |

★ **Hai thay đổi so với bản nội địa, cả hai đều có lý do:**

```
① Ngưỡng SLA 2′ → 5′. Khách quốc tế KHÔNG kỳ vọng trả lời tức thì như
   khách nội địa bấm quảng cáo, và họ hỏi câu dài hơn, cần tra dữ kiện hơn.
   ⛔ Giữ 2′ là tạo ra một hàng ✗ không nói lên điều gì.
② Trọng số 20 → 15, phần dôi ra chuyển sang N7. Ở bản quốc tế, TRẢ LỜI
   ĐÚNG VIỆC quan trọng hơn trả lời NHANH: khách đã chờ 3 ngày để quyết
   định bay nửa vòng trái đất, 3 phút không đổi gì — nhưng một câu sai về
   số ngày ở lại thì đổi cả chuyến đi.
```

### `N2` · KHAI THÁC TÌNH TRẠNG & BỐI CẢNH — **18 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N2.1` ★ | Hỏi tình trạng **trước khi** báo giá hoặc xin liên hệ | 7 | Có ≥1 câu hỏi tình trạng trước lần nhắc giá / xin liên hệ đầu tiên |
| `N2.2` | Có ≥2 **câu hỏi mở** | 3 | Câu hỏi không trả lời được bằng yes/no |
| `N2.3` | Mời **gửi ảnh / tả vùng** cụ thể | 4 | ⚠️ kèm câu nói rõ ai xem ảnh *(xem `N7.7`)* |
| `N2.4` | **Nhắc lại** đúng điều khách vừa nói | 4 | Có ít nhất 1 lần |

> ⚠️ **`N2.1` trượt là lỗi đắt nhất trong cả bộ.** Xin liên hệ trước khi biết khách cần gì biến cuộc tư vấn thành cuộc đòi số — và khách cho số xong thì không còn lý do gì để nghe tiếp.

### `N3` · TRẢ LỜI ĐÚNG & MINH BẠCH — **20 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N3.1` ★ | **Nêu giá** khi khách hỏi giá | 5 | ✅ **Chấm thật ở bản này** — giá đã công khai tại `/price-list/`. Né hẳn = `✗` |
| `N3.2` ★★ | **Nêu phụ phí quốc tế 10%** khi đã nêu giá | 5 | Thiếu = `✗` **và** là **cờ đỏ `CĐ-7`** |
| `N3.3` | ⛔ Không **cam kết kết quả** | 4 | *guaranteed · permanent · 100%* → cờ đỏ `CĐ-1` |
| `N3.4` | ⛔ Không **nói quá về bác sĩ / chứng chỉ** | 3 | *board certified* khi chỉ có tư cách hội → cờ đỏ `CĐ-4` |
| `N3.5` ★ | ⛔ Không **hứa số ngày ở lại / mốc được bay** bằng số cứng | 3 | Vi phạm = **cờ đỏ `CĐ-5`** — đây là rủi ro y khoa |

★★ **`N3.1` là chỗ bản quốc tế NGƯỢC HẲN bản nội địa.**

```
Bản nội địa : giá CHƯA công khai → né giá phần lớn là LỖI HỆ → chấm "—".
Bản quốc tế : giá ĐÃ công khai tại /price-list/ → né giá là LỖI NGƯỜI → ✗.

⚠️ Ngoại lệ duy nhất vẫn chấm "—": dịch vụ khách hỏi KHÔNG CÓ trong bảng
   giá công khai (vd combo lạ, ca sửa lại phức tạp). Khi đó nhân viên đúng
   khi nói "bác sĩ chốt sau khám" — và đó là câu ĐẠT, không phải né.
```

⚠️ **`N3.2` là tiêu chí mới quan trọng nhất của nhóm này.** Bỏ dòng 10% là **bom niềm tin**: khách phát hiện ở quầy thanh toán thì mất cả ca **và** nhận một review xấu (`id-K` §3③).

### `N4` · XỬ LÝ RÀO CẢN — **15 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N4.1` | **Nhận diện đúng** mã `O`/`OQ` khách nêu | 5 | Câu trả lời chạm đúng điều khách hỏi |
| `N4.2` ★ | **Xử đúng RÀO** — `SỢ`/`NGỜ`/`NGẠI`/`XA` | 6 | ⛔ Khách hỏi rào `XA` *(bao nhiêu ngày)* mà trả lời bằng **giá/ưu đãi** = `✗`. Đây là tiêu chí trượt nhiều **thứ hai** của bản quốc tế |
| `N4.3` | **Giữ cửa mở** | 4 | Có câu để lại đường quay lại, kể cả khi khách từ chối |

### `N5` · XIN LIÊN HỆ & CHỐT — **17 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N5.1` | Xin liên hệ có **lý do cụ thể** | 5 | Nói rõ gọi/nhắn để làm gì, mất bao lâu. *"Can I have your number?"* trống không = `✗` |
| `N5.2` | Xin lại **lần 2 khác cách** | 3 | Lần 2 không lặp nguyên văn lần 1 |
| `N5.3` ★ | Hỏi **khung giờ gọi KÈM MÚI GIỜ** | 4 | *"what time works for you — and which time zone?"*. ⚠️ Hỏi giờ mà **không hỏi múi giờ** = `✗`: giờ không có múi giờ là một con số vô dụng |
| `N5.4` ★ | Mời lịch **cụ thể ngày + giờ + nói rõ giờ Việt Nam** | 5 | *"3pm Vietnam time (UTC+7) on Tuesday"* = `✓` · *"sometime next week"* = `✗` |

> ⚠️ **`N5.3` và `N5.4` nối thẳng với doanh số của bản quốc tế.** Hẹn *"3 giờ chiều"* với khách London nghĩa là hẹn **9 giờ sáng giờ họ** — nếu không ai nói rõ thì cuộc gọi đó đơn giản là không diễn ra, và hồ sơ ghi *"khách không nghe máy"*.

### `N6` · NGÔN TỪ & THÁI ĐỘ — **5 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N6.1` | Không dán khối dài **lệch câu hỏi** | 2 | Đoạn copy-paste phải trả lời đúng điều khách vừa hỏi |
| `N6.2` | Câu **đọc hiểu được** | 2 | ⚠️ Chấm **tính dễ hiểu**, ⛔ **không chấm ngữ pháp/văn phong** (`id-L` §3) |
| `N6.3` | Không gắt, không ép khách | 1 | Vi phạm nặng → cờ đỏ `CĐ-6` |

### ★★ `N7` · NĂNG LỰC QUỐC TẾ — **10 điểm** *(nhóm MỚI)*

> Nhóm này đo đúng những việc **chỉ có ở khách quốc tế**. Nó nhỏ về điểm nhưng **lớn về hệ quả**: phần lớn ô `—` và phần lớn *việc hệ thống* của bản quốc tế đến từ đây.

| Mã | Tiêu chí | Điểm | Đạt khi | ⚠️ Lỗi hệ khi |
|---|---|---|---|---|
| `N7.1` ★ | **Hỏi khách đang ở đâu** *(nước/thành phố)* | 2 | Có hỏi, hoặc khách đã tự nói | Lời chào tự động/form không có trường này → vẫn chấm `✗` cho người **nếu khách nhắn ≥4 lượt mà không ai hỏi** |
| `N7.2` | **Nhận ra đúng tầng** và trả lời theo tầng | 2 | ⛔ Không nói đưa đón sân bay với `TT-D`; ⛔ không nói *"qua viện khám nhé"* với `TT-C` chưa bay | — |
| `N7.3` | **Trả lời đúng ngôn ngữ của khách** | 2 | Khách nhắn EN được trả lời EN | **`—`** nếu ca đó ⛔ không có nhân sự nói ngôn ngữ đó (`id-L` §7③) |
| `N7.4` ★ | **Dọn hộp thư ngoài giờ** | 2 | Tin đến ngoài giờ ICT được trả lời **trong 12h**, có câu xin lỗi vì lệch giờ | **`—`** nếu lịch trực chưa phủ ca đó **và** đã có trong *việc hệ thống* |
| `N7.5` | **Hỏi/ghi nhận múi giờ của khách** | 1 | — | — |
| `N7.6` ★ | **Xử lý đúng câu `OQ-01`** *(bao nhiêu ngày ở lại)* | 1 | Nói rõ *"cần bác sĩ xác nhận theo ca"* + hẹn trả lời lại, ⛔ không tự nêu số | **`—`** khi chưa có số từ Khoa Chuyên môn **và** nhân viên đã nói đúng kiểu trên |
| `N7.7` | **Nói rõ ai xem ảnh khách gửi** | — *(gộp `N2.3`)* | Có một câu: ai xem · lưu ở đâu · ⛔ không dùng cho marketing | 🔴 Thiếu **privacy notice** cho khách EU/UK → `L12`, việc hệ thống |

**Tổng: 15 + 18 + 20 + 15 + 17 + 5 + 10 = 100**

★ **`N7.6` là tiêu chí lạ nhất và cần nhất của cả bộ.** Nó ⛔ **không đo xem nhân viên có biết số ngày hay không** — họ không thể biết, vì chưa ai cấp. Nó đo **cách xử lý một câu hỏi mình chưa có câu trả lời**:

```
✓ ĐẠT  : "That depends on your procedure and healing — our surgeon confirms
          it at the assessment. I'll get you the typical range today and
          message you back." + có nhắn lại thật.
✗ TRƯỢT: tự nêu một con số  → đồng thời là cờ đỏ CĐ-5.
✗ TRƯỢT: im lặng, chuyển chủ đề sang giá  → đồng thời là N4.2 trượt.
—      : nói đúng kiểu trên nhưng hệ chưa cấp số → KHÔNG trừ điểm, và
          dòng đó vào mục "việc hệ thống" của kỳ.
```

---

## 4. PHÂN LOẠI A / B / C / D

| Loại | Điểm | Nghĩa vận hành | Sổ tay nhận được |
|---|---|---|---|
| 🟢 **A** | **≥ 85** | Làm chuẩn. Dùng hội thoại của người này làm mẫu cho khối | Sổ tay **mẫu lan toả** — 1 việc nâng cấp + 2 đoạn chat mẫu để chia sẻ |
| 🔵 **B** | **70 – 84** | Vững, hụt 1–2 nhóm | Sổ tay **sửa đúng một nhóm yếu nhất** |
| 🟡 **C** | **55 – 69** | Hụt nhiều nhóm, cần kèm | Sổ tay **2 việc + kịch bản mẫu + kèm cặp theo tuần** |
| 🔴 **D** | **< 55** | Đang làm mất lead đều đặn | Sổ tay **1 việc duy nhất** + ngồi cùng trưởng nhóm đọc lại 5 hội thoại |

⚠️ **Một cờ đỏ (`§5`) trong kỳ → trần điểm của hội thoại đó là 49**, và nhân viên ⛔ **không được xếp loại A** dù điểm trung bình cao.

---

## 5. MƯỜI CỜ ĐỎ `CĐ-1` … `CĐ-10`

> Cờ đỏ ⛔ **không phải lỗi trừ điểm thông thường**. Mỗi cờ đỏ được **báo riêng, kèm nguyên văn câu nói và `HT-nnn`**, và phải có người xử lý đích danh.

| Mã | Cờ đỏ | Vì sao nghiêm trọng |
|---|---|---|
| `CĐ-1` | **Cam kết kết quả chắc chắn** — *guaranteed · permanent · 100%* | Claim y khoa — rủi ro pháp lý ở **cả hai tầng** |
| `CĐ-2` | ★ **Nêu bảo hành** — gồm chữ *"lifetime"* | Site ghi *lifetime warranty* mà ⛔ chưa có T&C (`id-K` §3①) |
| `CĐ-3` | **Trả lời câu bệnh nền / chống chỉ định** thay bác sĩ | `O-12` — phải bác sĩ khám |
| `CĐ-4` | ★ **Nói quá chức danh** — *"board certified"* · claim hội ở mức thương hiệu | Nhầm tư cách hội với board certification là điểm **bị chất vấn nhiều nhất ở US/AU** (`id-K` §3②) |
| `CĐ-5` | ★★ **Hứa số ngày ở lại / mốc được phép bay** bằng số cứng | **Rủi ro y khoa thật** — bay quá sớm sau phẫu thuật. Cờ đỏ nặng nhất của bản quốc tế |
| `CĐ-6` | **Dìm đối thủ / gắt với khách** | Rủi ro thương hiệu, dễ bị chụp màn hình |
| `CĐ-7` | ★ **Nêu giá mà bỏ phụ phí 10%** | Bom niềm tin ở quầy thanh toán (`id-K` §3③) |
| `CĐ-8` | ★ **Nhắc viện thẩm mỹ tỉnh cho khách quốc tế** | Các cơ sở đó ⛔ không làm đại phẫu (`id-K` §1) |
| `CĐ-9` | ★ **Dùng câu dịch máy thô cho nội dung y khoa / hậu phẫu** | Câu dịch sai về hậu phẫu là rủi ro y khoa, ⛔ không phải lỗi văn phong |
| `CĐ-10` | ★ **So sánh giá với quốc gia/cơ sở có tên** — *"70% cheaper than Australia"* | Claim cần bằng chứng; rủi ro ở AU/UK |

★ **Năm cờ `CĐ-5` · `CĐ-7` · `CĐ-8` · `CĐ-9` · `CĐ-10` chỉ có ở bản quốc tế.** Ba trong số đó (`CĐ-5` · `CĐ-7` · `CĐ-9`) là cờ mà **nhân viên có thể cắm vào mà vẫn tưởng mình đang giúp khách** — nên chúng phải vào đào tạo, không chỉ vào sổ tay cá nhân.

⚠️ **Phân biệt `CĐ-5` với `N7.6`:** `N7.6` là *cách xử lý câu hỏi chưa có đáp án*; `CĐ-5` là *tự nghĩ ra đáp án*. Một hội thoại có `CĐ-5` thì `N7.6` tự động `✗`, ⛔ không chấm ngược lại.

---

## 6. ĐIỀU KIỆN ĐỦ MẪU

| Số HT của một nhân viên trong kỳ | Agent được làm gì |
|---|---|
| **< 5** | ⛔ Không chấm. Ghi `chưa đủ mẫu` |
| **5 – 9** | Chấm từng hội thoại, ⛔ **không cho điểm tổng, không phân loại** |
| **≥ 10** | ✅ Cho điểm tổng + phân loại A/B/C/D |
| **≥ 10 và liên tục 2 kỳ** | ✅ Được vẽ xu hướng, được so với kỳ trước |

⚠️ **Hai điều kiện riêng của bản quốc tế:**

```
① Nhân viên có ca lệch giờ (ca đêm phục vụ UK/EU/US) thì N1.1 tính theo
   KHUNG GIỜ CỦA CA ĐÓ, ⛔ không dùng khung 8–17 ICT.
② Nhân viên dưới 10 HT là chuyện BÌNH THƯỜNG ở inbox quốc tế vì cỡ mẫu nhỏ.
   ⛔ KHÔNG hạ ngưỡng xuống 5 để "có bảng cho đẹp". Thiếu mẫu thì báo thiếu
   mẫu — một con số dựng trên 6 hội thoại gắn với tên một người là một con
   số có hại.
```

---

## 7. ★ BỐN RÀO AN TOÀN — ⛔ BỎ MỘT CÁI LÀ SỔ NÀY VÔ HIỆU

```
① ĐIỂM ĐỂ KÈM CẶP, KHÔNG ĐỂ KỶ LUẬT.
   Mọi bảng điểm phải mang đúng câu này ở chân bảng:
   "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai."

② MỖI ĐIỂM TRỪ PHẢI CÓ BẰNG CHỨNG.
   Một ô ✗ không gắn được HT-nnn + nguyên văn câu → đổi thành "—".
   ⛔ Không có bằng chứng thì không có điểm trừ.

③ ★★ LỖI HỆ KHÔNG TRỪ ĐIỂM NGƯỜI — RÀO NẶNG NHẤT CỦA BẢN QUỐC TẾ.
   Bảy nhóm lỗi hệ, tất cả đều chấm "—" và đi vào mục "việc hệ thống":
     · chưa có SỐ NGÀY Ở LẠI               → N7.6
     · chưa có T&C BẢO HÀNH                → O-07 · OQ-04
     · chưa có thông tin VISA / THANH TOÁN → OQ-05 · OQ-06
     · chưa có người trực NGÔN NGỮ đó      → N7.3
     · lịch trực chưa phủ MÚI GIỜ đó       → N1.1 · N7.4
     · dịch vụ KHÔNG CÓ trong bảng giá     → N3.1
     · chưa có PRIVACY NOTICE đạt GDPR     → N7.7
   ⛔ Trừ điểm người cho bảy nhóm này là chấm sai người. Ở bản quốc tế,
      PHẦN LỚN ô trống thuộc nhóm này — đó là đặc điểm của bản này,
      không phải ngoại lệ.

④ KHÔNG XẾP HẠNG CÔNG KHAI TOÀN KHỐI.
   Dashboard hiện phân bố A/B/C/D và chỉ số cả đội.
   Tên + điểm cá nhân CHỈ xuất hiện trong sổ tay RIÊNG của người đó
   và bản của trưởng nhóm. ⛔ Không có bảng xếp hạng dán lên màn hình chung.
```

⚠️ **Phép thử rào ③, chạy trước khi phát mọi bảng điểm:**

> Với mỗi ô `✗`, hỏi: **"Nếu người giỏi nhất khối ngồi vào đúng hội thoại này, với đúng những gì hệ thống đang cấp, họ có làm được khác không?"**
> Không → ô đó phải là `—`.

---

## 8. ĐẦU RA CHUẨN CỦA BƯỚC B6

```
① PHÂN BỐ      : số người loại A/B/C/D + số người chưa đủ mẫu
② CHỈ SỐ ĐỘI   : % đạt từng nhóm N1…N7 — đây là thứ đưa lên dashboard
③ BẢNG CÁ NHÂN : tên · số HT · điểm · loại · nhóm yếu nhất · nhóm mạnh nhất
                 (⛔ chỉ vào sổ tay riêng + bản trưởng nhóm)
④ CỜ ĐỎ        : từng cờ · ai · HT-nnn · nguyên văn · người xử lý
⑤ ★ VIỆC HỆ THỐNG : các ô "—" do lỗi hệ, GOM THEO BẢY NHÓM ở §7 rào ③,
                 mỗi nhóm kèm: số HT bị ảnh hưởng · ai cấp · chặn mã nào
⑥ TIÊU CHÍ YẾU NHẤT CỦA KHỐI : 3 tiêu chí trượt nhiều nhất → nội dung đào tạo kỳ sau
⑦ ★ CẮT THEO TẦNG : % đạt N4.2 và N7.x theo TT-A/B/C/D — ⚠️ chỉ tầng ≥10 HT
```

★ **Mục ⑤ là mục quan trọng nhất của bản quốc tế.** Ở bản nội địa nó là phụ lục; ở đây nó thường **lớn hơn cả phần điểm người** — và đó là kết luận thật của kỳ, không phải lời bào chữa cho ai.

★ **Mục ⑦ hay lộ ra điều này:** cùng một nhân viên, điểm cao khi trực `TT-A` và điểm thấp khi trực `TT-C`. Đó ⛔ không phải người đó kém đi — đó là **`TT-C` hỏi đúng những câu mà hệ thống chưa có đáp án**.

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Mọi `✗` đều có `HT-nnn` + nguyên văn câu chưa?
- [ ] ★ Đã chạy **phép thử rào ③** (§7) cho từng ô `✗` chưa?
- [ ] Có ô nào thuộc **bảy nhóm lỗi hệ** mà bị chấm `✗` không?
- [ ] `—` có bị cộng vào mẫu số không?
- [ ] ★ Có HT nào đến **ngoài giờ 8–17 ICT** mà bị `✗` ở `N1.1` không?
- [ ] ★ `N3.1` có chấm đúng luật bản quốc tế (giá đã công khai → né giá là lỗi người) không?
- [ ] ★ Mọi chỗ nêu giá có bị soát `N3.2` / `CĐ-7` (phụ phí 10%) chưa?
- [ ] ★ Có nhân viên nào tự nêu **số ngày ở lại** mà không bị gắn `CĐ-5` không?
- [ ] Người dưới 10 HT có bị phân loại không? Có hạ ngưỡng để "có bảng cho đẹp" không?
- [ ] Có bảng xếp hạng cá nhân nào lọt ra ngoài sổ tay riêng không?
- [ ] Câu *"Điểm dùng để kèm cặp…"* có ở chân mọi bảng điểm không?
- [ ] Cờ đỏ có được báo riêng kèm người xử lý đích danh không?
- [ ] ★ Mục **việc hệ thống** có gom theo **bảy nhóm** và ghi **ai cấp** chưa?

---

<!-- ===== id-G-ma-tran-uu-tien.md ===== -->

# id-G · ★ MA TRẬN ƯU TIÊN — CHỌN VIỆC CHO KỲ TỚI

> Đây là **CỔNG 1**. Agent dừng ở đây, in ma trận ra, chờ người dùng gõ `DUYỆT`.
> ⛔ Chưa duyệt thì ⛔ không viết hook, ⛔ không sinh sổ tay.
>
> ⚠️ Bản quốc tế có **bốn khối**, không phải ba: khối ④ `MỞ CHẶNG S4` là khối riêng của bản này.

---

## 1. VÌ SAO PHẢI CÓ MA TRẬN

Một kỳ đọc hội thoại sẽ đẻ ra nhiều việc đáng làm hơn số việc khối làm được. Không có ma trận thì việc được chọn theo **ai nói to nhất**, chứ không theo **đâu mất nhiều lead nhất**.

> Ma trận trả lời đúng một câu: **nếu chỉ làm được 5 việc trong kỳ tới thì làm 5 việc nào.**

★ **Và bản quốc tế thêm một câu nữa:** trong 5 việc đó, **việc nào làm được ngay** và việc nào **đang chờ một ô dữ liệu**? Hai loại này ⛔ không được nằm cùng một danh sách (xem §4).

---

## 2. BỐN KHỐI — ĐI THEO ĐÚNG THỨ TỰ

| # | Khối | Mục tiêu | Tập lead xét |
|---|---|---|---|
| ① | **TĂNG HOT** | Kéo WARM sát HOT lên HOT | HT `WARM` đạt **3/5 tín hiệu** — thường thiếu ② cửa sổ chuyến đi hoặc ⑤ múi giờ |
| ② | ★★ **MỞ CHẶNG `S4`** | Đóng rào `XA` cho khách **đã muốn làm** | HT chạm mã `OQ-01`…`OQ-07` mà **bốn câu của rào `XA` chưa được trả lời đủ** (`id-D` §6.1) |
| ③ | **GIẢM COLD** | Làm khách nói được tình trạng + **nói được họ đang ở đâu** | HT `COLD` của `CD0` + HT ở `TT-0` + HT tin đầu chỉ hỏi giá/địa chỉ |
| ④ | **TỐI ƯU WARM** | Gỡ rào cản làm WARM đứng lại | HT `WARM` đạt 2/5, có mã `O` rõ |

★★ **Vì sao khối `S4` đứng thứ hai, trước cả `GIẢM COLD`:**

```
Khách ở khối ② ĐÃ VƯỢT QUA SỢ VÀ NGỜ. Họ muốn làm. Họ chỉ đang tính xem
chuyến đi có chạy được không. Mất họ ở đây là mất khách ĐẮT NHẤT trong cả
phễu — đã đọc hết, đã so giá, đã tin bác sĩ, chỉ thiếu một con số.

Và: việc ở khối ② thường RẺ NHẤT. Nhiều ô chỉ cần MỘT dữ kiện + MỘT câu
trả lời mẫu, không cần sản xuất nội dung mới.
```

★ **Thứ tự bốn khối không đảo được.** ① rẻ nhất (lead đã gần chín), ② đắt nhất nếu mất, ③ đông nhất nhưng chậm, ④ là phần còn lại.

---

## 3. CÔNG THỨC ĐIỂM

```
Điểm một ô = Σ ( lead bỏ lỡ trong ô × hệ số giá trị đơn )
```

### Hệ số giá trị đơn — theo dịch vụ chính khách hỏi

⚠️ Hệ số đi theo **dịch vụ**, ⛔ không đi theo chân dung, ⛔ không đi theo tầng. Chân dung khai sẵn `he_so_gia_tri` (`id-C` §2) thì hệ số đó thắng.

| Bậc | Giá trị đơn theo `/price-list/` | Hệ số |
|---|---|---|
| Thấp | < 20 triệu *(≈ 770 USD)* | **1** |
| Trung | 20 – 50 triệu | **2** |
| Cao | ≥ 50 triệu *(≈ 1.900 USD)* | **3** |
| ⚠ Khách không nêu dịch vụ | | **1** ⚠ |

★ **Khác bản nội địa:** bậc giá ở đây lấy từ **bảng giá công khai thật** (`id-K` §3③), không phải ước. Nên hệ số của bản này **không gắn `⚠`** — trừ ô cuối.

### ★★ LUẬT COMBO — cắt hệ số, ⛔ không được bỏ qua

```
Dịch vụ giá thấp (eyelid đơn lẻ · da liễu · spa · clinic) cho TT-A/B/C
  → HỆ SỐ TỐI ĐA 1, bất kể bảng giá xếp nó ở bậc nào.
  → Và chỉ được xếp vào CỤM COMBO / CROSS-SELL, ⛔ không mở tuyến riêng.
  Vì sao: ⛔ không ai bay 6 giờ để cắt mí.

Cùng dịch vụ đó cho TT-D (expat đang ở VN)
  → giữ hệ số theo bảng giá. Với TT-D đây là DỊCH VỤ LÕI.
```

### ⛔ Ba hệ số ⛔ KHÔNG được tự đặt

```
⛔ "hệ số tầng"      — TT-C × 1,5 vì tầng C đáng tiền hơn. Giá trị tầng ĐÃ
                       nằm trong hệ số dịch vụ và trong số lead bỏ lỡ.
⛔ "hệ số mùa"       — nhân thêm vì đang cao điểm Tết.
⛔ "hệ số tiềm năng" — bất kỳ con số nào không đo được trong kỳ.
Nhân hai lần là phá luật ⑨: bảng mất khả năng cãi được.
```

### Ví dụ đọc một dòng

```
CD2 · "I was quoted 20 grand in Australia" · khối ② Mở chặng S4
  (chân dung của kỳ này, đã duyệt ở CỔNG 0)
  Tầng chính             : TT-C (AU 7 HT · NZ 2 HT)
  HT mới trong kỳ        : 14
  HT trong tập (S4 chưa đóng): 9
  Có liên hệ             : 4
  Hệ số giá trị đơn      : 3  (rhinoplasty rib cartilage ≥50tr)
  Điểm                   : (9 − 4) × 3 = 15
  Câu rào XA chưa trả lời: ① số ngày ở lại  ③ ai trả phí bay
  → Ưu tiên 1 của khối ②
  → ⚠ NHƯNG: cả hai câu đều THIẾU DỮ KIỆN → vào nhóm ⏸ CHỜ CẤP (§4),
     ⛔ KHÔNG vào kế hoạch nội dung kỳ tới.
```

⚠️ Tên và số mã trong ví dụ là **của một kỳ cụ thể**. ⛔ Không chép bảng sang kỳ sau rồi chỉ đổi số.

---

## 4. BỐN NHÓM KẾT LUẬN *(nội địa: ba)*

| Nhóm | Khi nào | Việc |
|---|---|---|
| ✅ **ĐƯỢC CHỌN** | Điểm cao nhất trong khối, ≥ 5 HT mới, **và dữ kiện đã đủ để trả lời** | Vào kế hoạch nội dung, có số thứ tự ưu tiên |
| 🔧 **SỬA VẬN HÀNH TRƯỚC** | ≥ 50% HT của ô rơi do **trực kênh** | ⛔ **Không làm nội dung.** Đẩy sang `id-F` / `id-I` |
| ★ ⏸ **CHỜ CẤP DỮ KIỆN** | Ô có điểm cao **nhưng câu trả lời phụ thuộc một ô dữ liệu còn trống** | ⛔ **Không vào kế hoạch nội dung.** Vào mục `[CHỜ CẤP]` kèm **ai cấp · chặn bao nhiêu HT · chặn mã nào** |
| 👁 **QUAN SÁT** | < 5 HT mới | Ghi tên, chờ kỳ sau |

★★ **Nhóm ⏸ là nhóm riêng của bản quốc tế, và nó là nhóm dễ làm sai nhất.**

```
Sai : đưa "làm nội dung về số ngày ở lại sau nâng mũi" vào kế hoạch kỳ tới.
      → Content Lead nhận việc, không có số, không làm được, việc nằm đó
        hai kỳ rồi bị gạch — và không ai biết rằng nó chưa bao giờ là
        việc của Content.
Đúng : một dòng ⏸ CHỜ CẤP:
      "Số ngày ở lại 7 dịch vụ — Khoa Chuyên môn — chặn 23 HT kỳ này,
       chặn mã OQ-01 · tiêu chí N7.6 · khối ② của ma trận."
      → việc này có chủ, có số đo, và lên được bàn giao ban.
```

⚠️ Nhóm 🔧 là nhóm các agent nội dung hay bỏ qua: **ô có nhiều lead nhưng lead rơi do câu trả lời của người, không phải do thiếu clip**. Làm clip cho ô này là ném tiền.

---

## 5. SỐ VIỆC TỐI ĐA MỖI KỲ

| Khối | Số ô được chọn |
|---|---|
| ① Tăng HOT | tối đa **2** |
| ★ ② Mở chặng `S4` | tối đa **3** |
| ③ Giảm COLD | tối đa **2** |
| ④ Tối ưu WARM | tối đa **1** |
| 🔧 Sửa vận hành | không giới hạn — nhưng **mỗi việc phải có một người tên thật** |
| ⏸ Chờ cấp | không giới hạn — nhưng **mỗi dòng phải có ai cấp + số HT bị chặn** |

⛔ Quá 8 ô nội dung một kỳ thì không ô nào được làm tử tế.

★ Khối ② được **3 ô** — nhiều nhất — vì đây là khối rẻ nhất mà đang bị bỏ trống nhất.

---

## 6. ★ LUẬT MỘT TẦNG MỘT Ô

```
Một ô được chọn phải khai ĐÚNG MỘT TẦNG CHÍNH.
⛔ Không có ô nào "cho cả TT-A và TT-C" — vì:
   · khác bộ bằng chứng được phép dùng (id-K §4)
   · khác ngôn ngữ
   · khác rào cản chốt
Ô trải trên nhiều tầng → TÁCH thành hai ô, hoặc chọn tầng đông hơn và
ghi rõ tầng còn lại ở 👁 QUAN SÁT.
```

⚠️ Đây là phiên bản inbox của luật *"một chiến dịch = một tầng × một nhóm thị trường"* ở `id-E` §2. Bỏ luật này thì hook viết ra sẽ **không dùng được ở tầng nào**.

---

## 7. KHUÔN IN RA Ở CỔNG 1

```
MA TRẬN ƯU TIÊN — KỲ <tu> → <den>          TRẠNG THÁI: ⏳ CHỜ DUYỆT

① TĂNG HOT         mục tiêu: kéo WARM 3/5 lên HOT          tập: <n> HT
┌───┬─────┬──────────────┬──────┬─────┬─────┬──────┬──────┬──────┬─────┬──────────────┐
│ # │ CD  │ Chân dung    │ TẦNG │ HT  │ Tập │ L.hệ │ Hệ số│ Điểm │Chặng│ Hướng        │
└───┴─────┴──────────────┴──────┴─────┴─────┴──────┴──────┴──────┴─────┴──────────────┘

★ ② MỞ CHẶNG S4    mục tiêu: đóng rào XA                    tập: <n> HT
┌───┬─────┬──────────────┬──────┬─────┬─────┬──────┬──────┬──────────────────────────┐
│ # │ CD  │ Chân dung    │ TẦNG │ HT  │ Tập │ Điểm │ Câu XA chưa trả lời │ Dữ kiện? │
└───┴─────┴──────────────┴──────┴─────┴─────┴──────┴─────────────────────┴──────────┘

③ GIẢM COLD        …
④ TỐI ƯU WARM      …

🔧 SỬA VẬN HÀNH TRƯỚC — chưa làm nội dung
┌─────┬──────────────┬─────┬───────────────┬────────────────────────────┐
│ CD  │ Chân dung    │ HT  │ Rơi do trực   │ Lý do                      │
└─────┴──────────────┴─────┴───────────────┴────────────────────────────┘

★ ⏸ CHỜ CẤP DỮ KIỆN — ⛔ KHÔNG vào kế hoạch nội dung
┌──────────────────────┬────────────────────┬────────┬────────────────────┐
│ Dữ kiện còn trống    │ Ai cấp             │ Chặn n │ Chặn mã / tiêu chí │
└──────────────────────┴────────────────────┴────────┴────────────────────┘

👁 QUAN SÁT — dưới 5 HT mới: CD3 (3) · CD4 (2) · TT-A tách riêng (4)

───────────────────────────────────────────────────────────────────────
Gõ DUYỆT để agent viết ngân hàng hook và sinh sổ tay.
Gõ SỬA <mã ô> <hướng mới> để đổi trước khi duyệt.
```

---

## 8. SAU KHI DUYỆT

Agent ghi vào dữ liệu kỳ:

```json
"ma_tran": {
  "trang_thai": "da_duyet",
  "duyet_boi": "<ai>",
  "duyet_luc": "<ngày>"
}
```

⛔ Chừng nào `trang_thai` còn là `cho_duyet`, tab **Ngân hàng hook** và tab **Sổ tay** hiển thị *"chưa viết — ma trận chưa được duyệt"*, ⛔ không hiện nội dung rỗng.

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Bốn khối có đi **đúng thứ tự** ① → ② → ③ → ④ không?
- [ ] ★ Khối ② `MỞ CHẶNG S4` có được dựng không, hay bị bỏ vì "khó đo"?
- [ ] Mỗi ô được chọn có ghi rõ **điểm** và **cách ra điểm** không?
- [ ] ★ Mỗi ô có khai **đúng một tầng chính** không?
- [ ] ★ Có ô nào **thiếu dữ kiện** mà vẫn bị đưa vào kế hoạch nội dung không?
- [ ] ★ Mỗi dòng `⏸ CHỜ CẤP` có **ai cấp** + **số HT bị chặn** + **mã bị chặn** chưa?
- [ ] Có hệ số nào **tự đặt** không — hệ số tầng, hệ số mùa, hệ số tiềm năng?
- [ ] ★ **Luật combo** có được áp cho dịch vụ giá thấp ở `TT-A/B/C` không?
- [ ] Ô nào ≥50% rơi do trực kênh có bị đẩy nhầm sang làm nội dung không?
- [ ] Tổng số ô nội dung được chọn có vượt 8 không?
- [ ] Có dừng chờ duyệt thật không, hay đã tự chạy tiếp?

---

<!-- ===== id-H-ngan-hang-hook.md ===== -->

# id-H · NGÂN HÀNG HOOK QUỐC TẾ — 7 LOẠI HOOK × 16 FORMAT

> Chạy **sau CỔNG 1**. Mỗi hook phải gắn: **1 chân dung · 1 chặng `S1–S7` · 1 mã `O`/`OQ` · 1 `HT-nnn` truy ngược · 3 format · ★ 1 TẦNG + 1 NGÔN NGỮ**.
> ⚠ Chân dung gắn vào hook là chân dung **đã duyệt ở CỔNG 0 của kỳ này** (`id-C` §1).
> ⛔ Hook không truy ngược được về một dòng hội thoại hoặc một con số là **hook bịa** — loại khỏi ngân hàng.
>
> ⚠️ **Hook của bản này ⛔ không phải bản dịch hook nội địa.** Xem §3 và §7.

---

## 1. BẢY LOẠI HOOK

| Loại | Định nghĩa | Mục đích | Từ khoá nhận ra |
|---|---|---|---|
| **PHỦ ĐỊNH** | Bác bỏ một niềm tin phổ biến | Tò mò vì đi ngược số đông | *Don't · Stop · Not every…* |
| **CON SỐ** | Lượng hoá vấn đề hoặc kết quả | Rõ ràng, cụ thể, dễ nhớ | *X days · X USD · X things* |
| **GỌI TÊN NỖI SỢ** | Chỉ mặt đặt tên sự cố, lo lắng | Đánh trúng điều khách đang nghĩ | *What if it goes wrong · revision* |
| **NGHỊCH LÝ** | Hai thông tin tương phản trong một câu | Xung đột nhận thức | *cheaper, but…* |
| **SO SÁNH A–B** | Đặt hai đối tượng lên bàn cân | Dễ cân đo | *[A] or [B] · what's the difference* |
| **TIẾT LỘ NỘI BỘ** | Bật mí quy trình, sự thật vận hành | Củng cố niềm tin | *what the hospital actually does* |
| **CÂU HỎI THẦM** | Trăn trở khách đang phân vân | Cảm giác được tháo gỡ | *How long… · Who looks after me…* |

### Loại hook mạnh nhất theo chặng

| Chặng | Loại hook | Ghi chú |
|---|---|---|
| `S1` | PHỦ ĐỊNH · NGHỊCH LÝ | ⛔ không bán |
| `S2` | SO SÁNH A–B · CON SỐ | ★ So sánh **Việt Nam với lựa chọn khác**, ⛔ không so Kangnam với cơ sở có tên |
| `S3` | GỌI TÊN NỖI SỢ · TIẾT LỘ NỘI BỘ | ★ Bằng chứng phải **được phép dùng ở tầng đó** (`id-K` §4) |
| ★ `S4` | **CÂU HỎI THẦM · CON SỐ** | ★★ Chặng quan trọng nhất — xem §5 |
| `S5` | CON SỐ · TIẾT LỘ NỘI BỘ | ★ Giá + **phụ phí 10%** |
| `S6` | TIẾT LỘ NỘI BỘ · CÂU HỎI THẦM | ⛔ không chạy ads, ⛔ không cross-sell |
| `S7` | TIẾT LỘ NỘI BỘ · CON SỐ | |

---

## 2. MƯỜI SÁU FORMAT `L01` – `L16`

> Thư viện chung với cả hệ Kangnam — **giữ nguyên mã** để so hiệu suất chéo.

| Mã | Tên | Thời lượng | ⚠️ Giới hạn theo tầng |
|---|---|---|---|
| `L01` | Bác sĩ — Talk hỏi đáp | 25–35s | ✅ mọi tầng *(bốn cổng bác sĩ — `id-K` §3④)* |
| `L02` | Bác sĩ — Talk chủ đề | 40–60s | ✅ mọi tầng |
| `L03` | Bác sĩ — Phân tích ca thật | 30–45s | 🔴 `TT-C`: cần Pháp chế duyệt riêng |
| `L04` | Khách hàng — Trước/sau | 10–15s | 🔴 **`TT-C`: mặc định KHÔNG** |
| `L05` | Khách hàng — Biến đổi theo mốc ngày | 15–25s | 🔴 **`TT-C`: mặc định KHÔNG** |
| `L06` | Khách hàng — Review | 0–45s | 🔴 `TT-C`: **chỉ review phi lâm sàng** |
| `L07` | Khách hàng — Hành trình 1 ngày | 45–90s | 🟡 `TT-C`: được, nếu ⛔ không claim kết quả |
| `L08` | Khách hàng — Kết quả | 20–35s | 🔴 **`TT-C`: KHÔNG** |
| `L09` | Dịch vụ — Công nghệ | 15–30s | ✅ mọi tầng |
| `L10` | Dịch vụ — Quy trình | 25–40s | ✅ **mọi tầng — format mạnh nhất của `TT-C`** |
| `L11` | Dịch vụ — Giá / chính sách | 10–20s | ✅ **mọi tầng** — ⚠️ phải đủ 5 dòng giá (`id-K` §3③) |
| `L12` | Local — Cơ sở / bác sĩ / công nghệ | 20–35s | ✅ ⚠️ **chỉ 2 cơ sở HN · HCMC** |
| ★ `L13` | **Khách ở xa — Quy trình 5 bước** | 30–60s | ✅ **mọi tầng — sạch pháp chế** (`id-K` §8) |
| ★ `L14` | **Phiên dịch & chăm sóc sau khi về nước** | 20–40s | ✅ mọi tầng — sạch pháp chế |
| ★ `L15` | **Hậu cần chuyến đi** — đưa đón · khách sạn · người đi cùng | 20–40s | ✅ mọi tầng — ⚠️ xác nhận còn áp dụng |
| ★ `L16` | **Giấy phép & tiêu chuẩn bệnh viện** | 15–30s | ✅ **mọi tầng — bằng chứng mạnh nhất của `TT-A`** |

★★ **Bốn format `L13`–`L16` ở bản nội địa còn `[CHỜ CẤP]` — ở bản quốc tế chúng được định nghĩa, vì đây chính là bộ format mà khách quốc tế cần và là bộ **sạch pháp chế ở mọi thị trường**.**

```
★ HỆ QUẢ LỚN: với TT-C, phần lớn format "khách hàng" (L04·L05·L06·L08)
  bị chặn. Nếu ngân hàng hook chỉ có nhóm đó thì TT-C — tầng đáng tiền
  nhất — KHÔNG CÓ MỘT FORMAT NÀO DÙNG ĐƯỢC.
  → Trụ format của TT-C là: L10 · L13 · L14 · L16 · L01 · L02 · L11.
```

---

## 3. BA CÁCH VIẾT HOOK — VÀ HAI CÁCH SAI

### ✅ Cách 1 — CHÉP NGUYÊN *(tốt nhất)*

Lấy thẳng câu hỏi đầu tiên của khách, **giữ nguyên ngôn ngữ**.

```
HT-031: "I had my nose done in Bangkok and it collapsed. Can it be fixed?"
     → hook: "Nose surgery done abroad and it collapsed — can it be fixed?"

HT-052: "em về nước được 12 ngày, có kịp làm mũi không ạ?"
     → hook: "Về nước 12 ngày — có kịp nâng mũi và cắt chỉ trước khi bay?"
```

★ Hook này **không thể sai giọng khách**, vì nó chính là giọng khách.

### ✅ Cách 2 — GỘP TẦN SUẤT

```
9 × OQ-01 → "How many days do you actually need to stay in Vietnam?"
            ⚠️ hook ĐƯỢC PHÉP ĐẶT CÂU HỎI, nhưng nội dung ⛔ không được
               trả lời bằng số cứng khi chưa có số (id-K §6 L10).
```

### ✅ Cách 3 — LẬT Ô TRỐNG

Ô trống trong ma trận `CD × S7` + một mã `O`/`OQ` cao → hook mới cho đúng ô đó.
★ Ở bản này, **cột `S4` là cột có nhiều ô trống nhất** — xem trước tiên.

### ⛔ Cách SAI ① — "viết hook hay"

```
⛔ Tự nghĩ một câu nghe kêu rồi gán ngược cho một mã.
   Dấu hiệu: hook có TÍNH TỪ ("world-class", "premium", "đẳng cấp")
   mà không có TÌNH TRẠNG nào cụ thể.
```

### ⛔ Cách SAI ② — ★ DỊCH HOOK NỘI ĐỊA

```
⛔ Lấy hook tiếng Việt đang chạy tốt rồi dịch sang tiếng Anh.
   Ba lý do cứng:
   ① Khác rào cản: hook nội địa gỡ SỢ/NGỜ/NGẠI, ⛔ không gỡ XA.
   ② Khác bộ bằng chứng: hook dựa trên feedback khách là 🔴 ở TT-C.
   ③ Khác cách đọc: TT-A và GCC đọc EN như ngôn ngữ thứ hai —
      ⛔ không thành ngữ, ⛔ không chơi chữ, câu ngắn, số bằng chữ số,
      thuật ngữ y khoa kèm giải thích ở lần đầu: "rhinoplasty (nose surgery)".
```

★ **Luật một câu:** *hook gọi đúng **tình trạng** hoặc **ràng buộc chuyến đi**, ⛔ không khen **tính từ**.*

---

## 4. KHUÔN MỘT DÒNG TRONG NGÂN HÀNG HOOK

| Cột | Bắt buộc | Ghi chú |
|---|---|---|
| `MÃ` | ✅ | `QT-<kỳ>-<nnn>` |
| `KHỐI` | ✅ | ① Tăng HOT · ★② Mở `S4` · ③ Giảm COLD · ④ Tối ưu WARM |
| `CD` · `CHẶNG` | ✅ | Chặng `S1`–`S7` |
| ★ `TẦNG` | ✅ | **Đúng một** `TT-A/B/C/D` — ⛔ không có hook "cho mọi tầng" |
| ★ `NGÔN NGỮ` | ✅ | `EN` · `VI` · `KM` · `AR` |
| ★ `MARKET` | 🔶 | Mã thị trường nếu hẹp hơn tầng *(vd `AU` riêng vì AHPRA)* |
| `MÃ O/OQ` | ✅ | Mã phản đối hook này đóng |
| ★ `RÀO` | ✅ | `SỢ` · `NGỜ` · `NGẠI` · `XA` — **đúng một** |
| `INSIGHT LÕI` | ✅ | Khách đang tin gì / sợ gì — **chữ của khách, nguyên ngôn ngữ** |
| `HOOK 3 GIÂY` | ✅ | Lời thoại mở đầu, **đọc nguyên văn được** |
| `LOẠI HOOK` | ✅ | 1 trong 7 loại §1 |
| `FM1` `FM2` `FM3` | ✅ | 3 format `L01`–`L16` — ⚠️ **kiểm giới hạn tầng ở §2** |
| `CTA CUỐI` | ✅ | ⚠️ `S1`/`S6` ⛔ không CTA bán |
| ★ `TRUY NGƯỢC` | ✅ | `HT-nnn` hoặc tên chỉ số. **Trống = loại khỏi kế hoạch** |
| `NHIỆT` | ✅ | Hot / Warm / Cold |
| ★ `CỜ PHÁP CHẾ` | ✅ | 🔴🟡🟢 — **theo CẢ HAI TẦNG luật** (`id-K` §4) |
| ★ `DỮ KIỆN ĐỦ?` | ✅ | ✅ đủ / ⏸ chờ cấp — ⛔ hook `⏸` không vào kế hoạch sản xuất |
| `DUYỆT` | ⬜ | **Để trống** — BS + pháp chế điền |

⛔ **Chỉ hook `DUYỆT = XANH` mới được lên ads.** Agent ⛔ không tự điền ô này.

---

## 5. ★★ CỤM HOOK CHẶNG `S4` — CỤM ĐÁNG LÀM NHẤT VÀ DỄ SAI NHẤT

Bốn câu của rào `XA` (`id-D` §6.1) là bốn cụm hook. **Ba trong bốn cụm hiện ⏸ chờ dữ kiện** — và đó là thông tin quan trọng nhất của sổ này:

| Cụm | Hook được viết ngay? | Vì sao |
|---|---|---|
| ① *"How many days do I stay?"* | ⏸ **CHỜ** — `OQ-01` | ⛔ Không có số từ Khoa Chuyên môn. Hook **đặt câu hỏi** được, nội dung **trả lời** thì không |
| ② *"Who looks after me when I'm home?"* | ✅ **VIẾT ĐƯỢC NGAY** | Khối 5 bước + phiên dịch sau khi về đã có trên site → `L13` · `L14` |
| ③ *"Who pays if I need a revision?"* | ⏸ **CHỜ** — T&C bảo hành | ⛔ Chưa có văn bản thì ⛔ không viết một chữ |
| ④ *"Does anyone speak my language?"* | 🟡 **VIẾT ĐƯỢC MỘT PHẦN** | Nói được *có phiên dịch*; ⛔ chưa nói được **ngôn ngữ nào, có phí không** |

★ **Hệ quả thực tế:** cụm ② là **hook có đòn bẩy cao nhất mà viết được ngay trong kỳ này** — sạch pháp chế, dùng được ở mọi thị trường, và gần như chưa ai làm. Nếu một kỳ chỉ viết được một cụm hook mới thì **viết cụm ②**.

---

## 6. LUẬT CÂN ĐỐI KỲ

```
① ≥ 1 ô CHALLENGER mỗi kỳ, kể cả kỳ số đẹp.

② Mỗi khối của ma trận phải có ≥ 1 hook. ⛔ Không dồn hết vào khối ①.

③ Không quá 50% hook cùng một loại hook.

④ ★ Mỗi TẦNG được chọn phải có ≥ 1 hook chặng S3 VÀ ≥ 1 hook chặng S4.
   S3 là nơi khách sợ; S4 là nơi khách tắc. Bỏ S4 là bỏ chỗ khách rơi
   nhiều nhất mà không ai đo.

⑤ ★ Mỗi hook cho TT-C phải kiểm lại danh sách format §2 trước khi chốt.
   Hook hay mà gắn L04/L08 cho TT-C là hook ⛔ không dùng được.

⑥ ★ Hook cho TT-B viết bằng TIẾNG VIỆT, ⛔ không phải tiếng Anh.
   Họ tìm bằng tiếng Việt từ IP nước ngoài — chiến dịch EN không bao giờ
   gặp họ. Và viết như nói với NGƯỜI VIỆT Ở XA, ⛔ không như nói với
   người nước ngoài.
```

---

## 7. ⛔ HOOK KHÔNG ĐƯỢC VIẾT

- ⛔ Hook có chữ **"lifetime"** hoặc bất kỳ thời hạn bảo hành *(`O-07` · `CĐ-2`)*
- ⛔ Hook nêu **số ngày ở lại / mốc được phép bay** bằng số cứng *(`CĐ-5` — rủi ro y khoa)*
- ⛔ Hook nêu giá mà **bỏ dòng phụ phí 10%** *(`CĐ-7`)*
- ⛔ Hook **so sánh giá với quốc gia/cơ sở có tên** — *"70% cheaper than Australia"* *(`CĐ-10`)*
- ⛔ Hook dùng **superlative**: *best · No.1 · top-rated · leading · world-class*
- ⛔ Hook cam kết kết quả: *guaranteed · permanent · painless · no scars · risk-free*
- ⛔ Hook gắn **"board certified"** hoặc claim hội ở mức thương hiệu *(`CĐ-4`)*
- ⛔ Hook trả lời **bệnh nền / chống chỉ định** *(`O-12`)*
- ⛔ Hook dùng **testimonial kết quả lâm sàng cho `TT-C`** *(AHPRA)*
- ⛔ Hook dùng **before–after cơ thể / giảm béo** — mọi tầng, mọi thị trường
- ⛔ Hook có **ngôn từ về cân nặng** *(overweight · fat · obese)*
- ⛔ Hook nhắc **viện thẩm mỹ tỉnh** *(`CĐ-8`)*
- ⛔ Hook nói với **người xem** rằng họ đang có khiếm khuyết → nền tảng từ chối
- ⛔ Hook **dìm đối thủ**
- ⛔ Hook lấy **số từ hook cũ** làm nguồn giá — nguồn giá là `/price-list/`

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Mỗi hook có `HT-nnn` hoặc chỉ số truy ngược không?
- [ ] ★ Mỗi hook có **đúng một tầng**, **một ngôn ngữ**, **một rào** không?
- [ ] ★ Format của hook `TT-C` có bị chặn theo bảng §2 không?
- [ ] ★ Mỗi tầng có đủ hook chặng `S3` **và** `S4` chưa?
- [ ] ★ Hook cho `TT-B` có viết bằng **tiếng Việt** không?
- [ ] Có hook nào chỉ có tính từ mà không có tình trạng / ràng buộc chuyến đi không?
- [ ] Có hook nào là **bản dịch** của hook nội địa không?
- [ ] ★ Hook `⏸ chờ dữ kiện` có bị lẫn vào kế hoạch sản xuất không?
- [ ] Cờ pháp chế có soát **cả hai tầng luật** chưa?
- [ ] Cột `DUYỆT` có bị agent tự điền không?

---

<!-- ===== id-I-so-tay-thuc-thi.md ===== -->

# id-I · ★ SỔ TAY THỰC THI CÁ NHÂN HOÁ

> Đầu ra cuối cùng và là thứ duy nhất **chạm tới từng con người**. Dashboard để lãnh đạo nhìn; sổ tay để nhân viên làm.
>
> ⚠️ **Khuôn trong sổ này là bản dựng tạm.** Khi có mẫu sổ tay chính thức của khối, thay §3 và ghi lại ở `doc/CHANGELOG.md`. Mọi phần khác giữ nguyên.
>
> ★ Khác bản nội địa: sổ tay bản quốc tế có **câu mẫu song ngữ** và một mục riêng — **việc KHÔNG phải của bạn** (§3 mục 6).

---

## 1. BA LOẠI SỔ TAY

| Loại | Cho ai | Dài | Chứa tên ai |
|---|---|---|---|
| **ST-CN** | Một nhân viên trực kênh quốc tế | **1 trang** | Chỉ người đó |
| **ST-TN** | Trưởng nhóm | 2–3 trang | Cả nhóm — ⛔ không phát ra ngoài nhóm |
| **ST-ND** | Người làm nội dung | 1–2 trang | ⛔ Không có tên nhân viên nào |

⛔ **ST-CN của người A ⛔ không bao giờ chứa tên, điểm hay hội thoại của người B.**

---

## 2. LUẬT MỘT VIỆC

```
Sổ tay loại D : ĐÚNG MỘT việc.
Sổ tay loại C : tối đa HAI việc.
Sổ tay loại B : ĐÚNG MỘT việc (nhóm yếu nhất).
Sổ tay loại A : MỘT việc nâng cấp + 2 đoạn chat mẫu để chia sẻ cho khối.
```

★ Sổ tay 7 việc là sổ tay 0 việc.
★ Việc được chọn là **nhóm `N` mất nhiều điểm nhất**, ⛔ không phải nhóm dễ sửa nhất.

★★ **Luật thêm của bản quốc tế — ⛔ không viết việc mà hệ thống đang chặn:**

```
Trước khi viết một việc, chạy phép thử rào ③ của id-F §7:
  "Nếu người giỏi nhất khối ngồi vào đúng hội thoại này, với đúng những gì
   hệ thống đang cấp, họ có làm được khác không?"
Không → đó KHÔNG phải việc của người này. Nó đi vào ST-TN mục 5 và vào
mục "việc hệ thống" của dashboard.

⛔ Viết "lần sau nhớ trả lời khách số ngày ở lại" vào ST-CN là việc KHÔNG
   LÀM ĐƯỢC — và sổ tay có một việc không làm được thì cả sổ mất uy tín.
```

---

## 3. KHUÔN `ST-CN` — SỔ TAY MỘT NHÂN VIÊN

```markdown
# SỔ TAY THỰC THI · <Tên nhân viên>
Kỳ <tu> → <den> · <n> hội thoại · <điểm>/100 · loại <A|B|C|D>
Tầng bạn trực nhiều nhất: <TT-x> (<n>/<N> HT) · ngôn ngữ: <EN|VI|…>

> Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai.

## 1 · KỲ NÀY BẠN LÀM TỐT NHẤT ĐIỀU GÌ
<nhóm N mạnh nhất> — <% đạt> (khối: <% đạt của khối>)
Ví dụ từ chính bạn: HT-<nnn> — "<nguyên văn câu làm tốt, đúng ngôn ngữ>"

## 2 · ★ MỘT VIỆC CỦA KỲ TỚI
**<Tên việc — viết như một hành động, không phải một phẩm chất>**

Vì sao: <nhóm N yếu nhất> đạt <x>% trên <n> hội thoại áp dụng.
        Ước tính <m> lead rơi vì điều này.

Bằng chứng — 2 hội thoại của chính bạn:
  HT-<nnn> · khách hỏi "<...>" → bạn trả lời "<...>" → khách im luôn
  HT-<nnn> · <...>

Làm thế nào — câu mẫu dùng được ngay (★ song ngữ nếu bạn trực cả EN và VI):
  ✅ EN: "<câu đúng>"
  ✅ VI: "<câu đúng>"
  ⛔ "<câu đang dùng, vì sao hỏng>"

Đo thế nào ở kỳ sau: <tiêu chí N>.<x> từ <a>% lên <b>%

## 3 · KHÁCH CỦA BẠN LÀ AI
Chân dung gặp nhiều nhất: <CD> · <tên> (<n>/<N> hội thoại) · tầng <TT-x>
Họ đang sợ: <mã O/OQ cao nhất> — <tên mã> · rào chốt: <SỢ|NGỜ|NGẠI|XA>
Câu hỏi ngầm: "<...>"
Ràng buộc chuyến đi của họ: <...>
→ Ba câu trả lời sẵn cho tệp này (đúng ngôn ngữ của họ):
  1. <...>
  2. <...>
  3. <...>

## 4 · ⛔ NĂM ĐIỀU TUYỆT ĐỐI KHÔNG — bản quốc tế
- ⛔ Không dùng chữ "lifetime" hay bất kỳ thời hạn bảo hành
      → "follow-up and warranty policy — see terms"
- ⛔ Không tự nêu SỐ NGÀY khách phải ở lại Việt Nam, không nói "you can fly on day X"
      → "the surgeon confirms this at your assessment — I'll get you the range today"
- ⛔ Không nêu giá mà bỏ dòng phụ phí 10%
      → "price does not include the 10% international service charge"
- ⛔ Không nói "board certified" hay gắn chức danh bác sĩ chưa đối chiếu
- ⛔ Không trả lời câu bệnh nền / chống chỉ định
      → "this needs an in-person assessment by the surgeon"
<thêm dòng nếu người này có cờ đỏ trong kỳ — ghi rõ HT-nnn>

## 5 · KIỂM TRƯỚC KHI ĐÓNG MỖI HỘI THOẠI
- [ ] Đã biết khách đang ở NƯỚC NÀO chưa?
- [ ] Đã hỏi tình trạng trước khi xin liên hệ chưa?
- [ ] Đã nêu giá kèm phụ phí 10% chưa (nếu khách hỏi giá)?
- [ ] Đã hỏi khung giờ gọi KÈM MÚI GIỜ chưa?
- [ ] Đã hẹn lịch có ngày + giờ + "giờ Việt Nam" chưa?
- [ ] ★ Khách này đã đủ thông tin để MỞ APP HÀNG KHÔNG VÀ CHỌN NGÀY BAY chưa?
- [ ] <mục riêng theo việc ở phần 2>

## 6 · ★ VIỆC KHÔNG PHẢI CỦA BẠN
Những câu bạn chưa trả lời được trong kỳ này là vì HỆ THỐNG CHƯA CẤP,
không phải vì bạn làm sai. Chúng đã được đưa lên mục việc hệ thống:
  · <ô dữ liệu còn trống> — <ai đang cấp> — chặn <n> hội thoại của bạn
⛔ Bạn KHÔNG cần tự nghĩ ra câu trả lời cho những câu này.
```

★★ **Mục 6 là mục riêng của bản quốc tế và ⛔ không được bỏ.** Trực kênh quốc tế mỗi ngày gặp những câu mình không có đáp án; không nói rõ ra thì người giỏi sẽ **tự nghĩ ra một con số** — và đó đúng là cách cờ đỏ `CĐ-5` xuất hiện.

---

## 4. KHUÔN `ST-TN` — SỔ TAY TRƯỞNG NHÓM

```markdown
# SỔ TAY TRƯỞNG NHÓM · <tên nhóm>
Kỳ <tu> → <den>

## 1 · PHÂN BỐ NHÓM
A: <n> · B: <n> · C: <n> · D: <n> · chưa đủ mẫu: <n>
★ Cắt theo tầng: điểm TB khi trực TT-A <x> · TT-B <x> · TT-C <x> · TT-D <x>
  ⚠ Chênh lệch giữa các tầng thường là chênh lệch về DỮ KIỆN SẴN CÓ,
    không phải về năng lực — đọc cùng mục 5.

## 2 · BA TIÊU CHÍ YẾU NHẤT CỦA NHÓM
<N>.<x> — <y>% đạt — đây là nội dung buổi đào tạo 15 phút kỳ tới

## 3 · AI KÈM AI
<người loại A> kèm <người loại D> — về đúng tiêu chí <N>.<x>

## 4 · CỜ ĐỎ CẦN XỬ TRONG 48 GIỜ
<mã CĐ> · <người> · HT-<nnn> · nguyên văn: "<...>" · xử thế nào
★ Ba cờ cần xử NGAY và cần nói với CẢ NHÓM, không chỉ với người cắm cờ:
  CĐ-5 (hứa số ngày ở lại) · CĐ-7 (bỏ phụ phí 10%) · CĐ-9 (dịch máy y khoa)
  — ba cờ này người ta cắm vào khi ĐANG CỐ GIÚP KHÁCH.

## 5 · ★ VIỆC KHÔNG PHẢI CỦA NHÓM BẠN — bảy nhóm lỗi hệ
<các ô "—" do lỗi hệ, gom theo id-F §7 rào ③>
  · <nhóm> — <n> HT bị ảnh hưởng — <ai cấp> — chặn <mã/tiêu chí>
→ đã đẩy lên mục hệ thống của dashboard và mục ⏸ CHỜ CẤP của ma trận

## 6 · ★ LỊCH TRỰC THEO MÚI GIỜ
<n> HT đến ngoài giờ 8–17 ICT (<pct>%) · chờ TB <x>h · <n> HT mất quá 12h
Tầng bị ảnh hưởng nặng nhất: <TT-x> (<market>)
→ đề xuất ca: <...>   ⚠ đây là việc của LỊCH, không của người
```

★ Mục 5 và mục 6 giữ cho trưởng nhóm không bị đổ oan những việc mà chỉ hệ thống mới sửa được.

---

## 5. KHUÔN `ST-ND` — SỔ TAY NGƯỜI LÀM NỘI DUNG

```markdown
# SỔ TAY NỘI DUNG QUỐC TẾ · kỳ <tu> → <den>

## 1 · <n> Ô ĐƯỢC CHỌN (ma trận đã duyệt <ngày>)
<bảng: # · khối · CD · ★ TẦNG · ★ ngôn ngữ · chặng · điểm · hướng · format · deadline>

## 2 · NGÂN HÀNG HOOK KỲ NÀY — <n> hook
<bảng theo khuôn id-H §4>
★ Kiểm lại: hook cho TT-C có bị gắn format bị chặn (L04·L05·L08) không?

## 3 · NỘI DUNG PHẢI DỪNG
<các nội dung 🔴 KÉM + mã O/OQ thấp → bỏ hẳn>

## 4 · Ô ĐANG PHÍ
<ô ③ của ma trận CD×S7 — nhiều nội dung, ít người hỏi>

## 5 · ★ Ô CHỜ DỮ KIỆN — ⛔ KHÔNG NHẬN LÀM
<các dòng ⏸ của ma trận: dữ kiện trống · ai cấp · chặn bao nhiêu HT>
⛔ Đây KHÔNG phải việc của Content. Đừng nhận, đừng viết tạm.

## 6 · ⛔ CỜ PHÁP CHẾ TRƯỚC KHI SẢN XUẤT — HAI TẦNG
Tầng ① luật Việt Nam : <danh sách 🔴🟡 kèm câu thay thế>
Tầng ② luật nước người xem : <theo từng market có mặt trong kỳ>
R8 (đủ điều kiện KCB cho người nước ngoài): ✅ / 🔴 [CHỜ CẤP]
```

---

## 6. VIẾT VIỆC THẾ NÀO CHO SỬA ĐƯỢC

| ⛔ Viết thế này | ✅ Viết thế này |
|---|---|
| *"Cần chủ động hơn"* | *"Sau khi khách im 30 phút, nhắn lại một câu hỏi về tình trạng — không nhắn lại lời chào"* |
| *"Kỹ năng khai thác yếu"* | *"Hỏi 1 câu về tình trạng **trước** khi gõ câu xin liên hệ"* |
| *"Chưa biết chốt"* | *"Thay 'let me know when you're free' bằng '3pm Vietnam time (UTC+7) on Tuesday — I'll hold the slot'"* |
| ★ *"Cần nắm thông tin quốc tế"* | *"Câu đầu tiên sau lời chào: 'May I ask which country you're messaging from?'"* |
| ★ *"Chú ý múi giờ"* | *"Khi hỏi giờ gọi, hỏi luôn múi giờ: 'what time works for you, and which time zone?'"* |
| ★ *"Trả lời khách kỹ hơn về bảo hành"* | ⛔ **Không viết việc này** — đang chờ T&C (`id-F` §7 rào ③) |

★ Mỗi việc phải kiểm được bằng **ctrl-F trong hội thoại kỳ sau**. Việc không kiểm được là việc không tồn tại.

---

## 7. NHỊP PHÁT

| Khi nào | Ai nhận | Qua đâu |
|---|---|---|
| Ngay sau CỔNG 2 | Trưởng nhóm — `ST-TN` | Bản riêng |
| Sau khi trưởng nhóm đọc xong | Từng nhân viên — `ST-CN` | **Bản riêng của từng người** |
| Cùng lúc | Người làm nội dung — `ST-ND` | Chung |
| ★ Cùng lúc | **Điều phối QT + Vận hành** — bản trích mục *việc hệ thống* + *lịch trực theo múi giờ* | Chung |

⛔ Không phát `ST-CN` vào nhóm chat chung. ⛔ Không đính kèm nhiều `ST-CN` trong một file.

★ **Bản trích cho Điều phối QT là bản phát thứ tư, chỉ có ở bản quốc tế.** Phần lớn việc sửa được trong kỳ nằm ở đó, không nằm trong sổ tay cá nhân.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Mỗi `ST-CN` có **đúng số việc** theo loại A/B/C/D không?
- [ ] Việc được chọn có phải nhóm `N` **mất nhiều điểm nhất** không?
- [ ] ★ Đã chạy **phép thử rào ③** cho từng việc chưa? Có việc nào **hệ thống đang chặn** không?
- [ ] Mỗi việc có **câu mẫu dùng được ngay**, **đúng ngôn ngữ nhân viên trực**, không?
- [ ] Mỗi việc có **cách đo ở kỳ sau** không?
- [ ] ★ `ST-CN` có **mục 6 · việc không phải của bạn** chưa?
- [ ] ★ `ST-TN` có **mục 5 · bảy nhóm lỗi hệ** và **mục 6 · lịch trực theo múi giờ** chưa?
- [ ] ★ `ST-ND` có **mục 5 · ô chờ dữ kiện** và cờ pháp chế **hai tầng** chưa?
- [ ] Có `ST-CN` nào chứa tên người khác không?
- [ ] Câu *"Điểm dùng để phân việc kèm cặp…"* có ở đầu mọi `ST-CN` không?

---

<!-- ===== id-J-dashboard-schema.md ===== -->

# id-J · DASHBOARD & SCHEMA BÁO CÁO

> Dashboard là **một trang HTML cố định** đọc dữ liệu từ `data/*.json`. Mỗi kỳ chỉ sinh thêm một file JSON, ⛔ không sửa trang.
> Nhờ vậy link gửi cho sếp **không bao giờ đổi**, và xem lại được mọi kỳ cũ.
>
> ⚠️ Schema của bản này là `insight-dashboard-knqt/1` — ⛔ **không tương thích** với `insight-dashboard-kangnam/1` của bản nội địa. Hai dashboard, hai bộ dữ liệu, ⛔ không trộn file kỳ.

---

## 1. MƯỜI TAB *(nội địa: 9)*

| # | Tab | Trả lời câu |
|---|---|---|
| ① | **Phễu inbox** | Khách vào bao nhiêu, nóng tới đâu, rơi ở đâu và vì sao |
| ★ ② | **Thị trường & kênh** | Khách **ở đâu**, nhắn **ngôn ngữ gì**, qua **kênh nào**, vào **giờ nào** |
| ③ | **Chân dung & Insight** | Khách là ai, họ sợ gì, câu hỏi ngầm là gì. ⏳ Khoá lại khi chân dung chưa qua CỔNG 0 |
| ④ | ★ **Chấm điểm nhân viên** | Khối trực kênh đang yếu tiêu chí nào, ai cần kèm |
| ⑤ | **Marketing — Meta** | Chuỗi chi → CPM→CTR→CPI→CPL→CPB→**CPA-KHÁM**, cắt theo thị trường |
| ⑥ | **Marketing — Google Ads** | ⚠ chờ dữ liệu |
| ⑦ | **Ma trận ưu tiên** | Kỳ tới làm việc nào · ★ việc nào đang chờ dữ kiện |
| ⑧ | **Ngân hàng hook** | Viết gì, cho tầng nào, ngôn ngữ nào, format nào |
| ⑨ | **Sổ tay & việc cần xử lý** | Ai làm gì, hạn bao giờ, đo thế nào |
| ⑩ | **Ghi chú dữ liệu** | Mọi con số đến từ đâu, loại gì ra, vì sao |

★ **Tab ② là tab mới của bản quốc tế, và nó đứng thứ hai — ngay sau Phễu — là có chủ ý.** Người đọc phải thấy *khách ở đâu* trước khi đọc bất kỳ tỷ lệ nào (CỔNG M · `id-L` §2).

### Ba bố cục — ⛔ vẫn chỉ MỘT bản trang

Chọn bằng trường `bo_cuc` trong `data/index.json`:

| `bo_cuc` | Tên báo cáo | Tab | Thẻ số tổng |
|---|---|---|---|
| *(không khai)* · `day-du` | Khách quốc tế & chất lượng trực kênh | cả 10 | cả 6 |
| `insight` | **Insight khách quốc tế** — khách là ai · họ tắc ở đâu · kỳ tới làm nội dung gì | ① ② ③ ⑦ ⑧ | HT · bỏ 1 lượt · có liên hệ · HOT/WARM chưa liên hệ · **`S4` chưa đóng** |
| `truc-kenh` | **Chất lượng trực kênh** — khối yếu gì · ai cần kèm · việc nào của hệ thống | ④ ① ② ⑨ ⑩ | HT · trả lời lượt đầu · rơi do trực kênh · **ngoài giờ chờ >12h** · HOT/WARM chưa liên hệ |

```
⛔ Tách báo cáo KHÔNG được đẻ thêm một bản trang.
★ Thứ tự tab đi theo ĐÚNG thứ tự khai trong bố cục.
★ Tab ② có mặt trong CẢ BA bố cục — ⛔ không bố cục nào được bỏ nó.
⚠ Ba bố cục dùng CHUNG một file kỳ. Số liệu chỉ có một bản.
★ Bố cục bỏ tab ⑩ thì ghi chú dữ liệu chuyển lên ô gập đầu trang, ⛔ không biến mất.
```

### Đầu trang — luôn hiện, không nằm trong tab nào

```
Tiêu đề + chọn kỳ
▶ n lưu ý dữ liệu            (gập lại, mở ra xem)
★ dải TẦNG THỊ TRƯỜNG        TT-A · TT-B · TT-C · TT-D · TT-0  (số HT + %)
6 thẻ số tổng                (giá trị · so kỳ trước · so mốc gốc)
```

### Sáu thẻ số tổng

| Thẻ | Kiểu | Tốt là |
|---|---|---|
| `Hội thoại mới` | số | — |
| `Bỏ sau 1 lượt` | % | thấp |
| `Có liên hệ` | % | cao |
| `Trả lời tin đầu ≤5′ (trong giờ)` | % | cao |
| ★ `HOT/WARM chưa có liên hệ` | số | **thấp** |
| ★★ `S4 chưa đóng` | số | **thấp** — HT chạm rào `XA` mà bốn câu `id-D` §6.1 chưa được trả lời đủ |

★ **Thẻ `S4 chưa đóng` là thẻ số đặc trưng của bản quốc tế.** Nó đo đúng chỗ khách **đã muốn làm mà không bay được** — không có thẻ nào khác trong hệ đo được điều đó.

⚠️ Hai thẻ phụ bắt buộc hiện ở tab ② *(không nằm trong 6 thẻ chính)*: `% HT ngoài giờ 8–17 ICT` và `% HT ngoài giờ chờ >12h`.

⚠️ Tab ⑩ **không phải tab phụ**. Báo cáo không nói được số đến từ đâu thì không ai dám dùng để ra quyết định.

---

## 2. SCHEMA DỮ LIỆU — `insight-dashboard-knqt/1`

```jsonc
{
  "schema": "insight-dashboard-knqt/1",
  "ky":   { "id","tu","den","tu_hien","den_hien","nhan","tao","nguon","crawl" },
  "chan": { "van_ban","het_han","con_hieu_luc" },
  "chi_phi": { "co_file": true, "co_cot_market": false, "nguon": "..." },
  "canh_bao": [ { "muc":"bad|warn", "text":"..." } ],
  "the_tong": [ { "id","nhan","gia_tri","kieu":"n|pct|s","tot":"cao|thap","phu" } ],
  "r8": { "xac_nhan": false, "ghi_chu": "[CHỜ CẤP: R8 — Pháp chế + Điều phối QT]" },

  "ket_luan": {
    "marketing":  [ { "viec","ly_do","so_huu","do_ky_sau","nhan":"da_do|gia_thuyet" } ],
    "truc_kenh":  [ ... ],
    "he_thong":   [ ... ],
    "cho_cap":    [ { "du_kien","ai_cap","so_ht","chan_ma" } ],   // ★ id-G §4
    "bu_quyet":   [ { "viec","chi_tiet" } ]
  },
  "theo_doi": [ { "bo_phan","viec","muc_tieu","ket_qua","dat":true|false|null,"lan" } ],

  "pheu": {
    "so_ht_phan_tich": 0,
    "nhiet": { "HOT":0,"WARM":0,"COLD":0 },
    "nhiet_x_lh": [ { "muc","chua","co" } ],
    "tin_hieu":   [ { "nhan","so" } ],              // 5 tín hiệu id-D §3
    "nguyen_nhan_roi": { "nội dung":0,"trực kênh":0,
                         "hệ thống — dữ kiện":0,"hệ thống — múi giờ":0,
                         "hệ thống — ngôn ngữ":0,"khách tự dừng":0,"không rơi":0 },
    "rao_can":    [ { "nhan","so" } ],
    "rao_chot":   { "SỢ":0,"NGỜ":0,"NGẠI":0,"XA":0 },            // ★ id-D §6
    "chang":      { "S1":0,"S2":0,"S3":0,"S4":0,"S5":0,"S6":0,"S7":0,"chưa rõ":0 },
    "ma_o":       [ { "ma","ten","so","pct","noi_dung_da_co","ket_luan" } ],
    "ma_oq":      [ { "ma","ten","so","pct","trang_thai_chan","ket_luan" } ],   // ★ 8 mã
    "s4_chua_dong": { "so":0, "cau": { "1_so_ngay":0,"2_ai_lo":0,
                                       "3_ai_tra_phi":0,"4_ngon_ngu":0 } },     // ★
    "chot_lich":  0,
    "van_de":     [ { "muc","tieu_de","nhan_do","so_lieu","de_xuat","so_huu","anh_huong" } ]
  },

  "thi_truong": {                                   // ★ tab ② — KHỐI MỚI
    "nguon_suy": { "khai_san":0,"khach_tu_noi":0,"suy_tu_chu":0,"suy_tu_kenh":0 },
    "tang":   [ { "tt","ten","ht","pct","hot","warm","cold","co_lh","pct_lh",
                  "roi_truc","ngon_ngu_chinh","market":["AU","NZ"] } ],  // + dòng TT-0
    "ngon_ngu": [ { "kh","nv","so" } ],              // ma trận ngôn ngữ khách × NV
    "kenh":   [ { "ten","ht","pct_lh","tra_loi_dau_phut","truy_duoc_ads":true } ],
    "mui_gio": { "trong_gio":0,"ngoai_gio":0,"pct_ngoai_gio":0,
                 "cho_tb_gio":null,"mat_qua_12h":0,
                 "theo_tang":[ { "tt","ngoai_gio","cho_tb_gio" } ] },
    "mua":    { "cua_so":"<mô tả cửa sổ mùa đang mở>","ghi_chu" }
  },

  "chan_dung": {
    "phac_hoa": { "trang_thai":"chua_phac_hoa|da_duyet","vi_sao","file",
                  "nguyen_lieu","so_chan_dung","duyet_boi","duyet_luc" },
    "tep":     [ { "cd","ten","ht","quan_sat","hot","warm","cold","co_lh",
                   "chot_lich","bo_1_luot","roi_truc","he_so",
                   "tt","ngon_ngu","rao_chot","rang_buoc_chuyen_di" } ],   // + CD0
    "insight": [ { "cd","ten","nhom","tt","ho_la_ai","insight","cau_hoi_ngam",
                   "tin_hieu_nong","rao_chot","huong_xu_ly","trich" } ],
    "co_hoi_win":    [ { "cd","ten","ht","lead_bo_lo","he_so","pct_lh","diem","hang",
                         "uu_tien","roi_truc","ghi_chu" } ],   // CD0 cuối, hang = null
    "cach_tinh_win": "công thức, viết ra để người đọc cãi được",
    "ma_tran_cd_s7": { "noi_dung": {...}, "hoi_thoai": {...} },  // hai bảng N×7
    "ma_tran_cd_tt": {...}                                      // ★ một bảng N×5
  },

  "nhan_vien": {
    "du_mau": true,
    "phan_bo": { "A":0,"B":0,"C":0,"D":0,"chua_du_mau":0 },
    "nhom":    [ { "ma":"N1","ten","diem_toi_da":15,"pct_dat":0,
                   "tieu_chi":[ { "ma":"N1.1","ten","diem":6,"dat":0,"chua":0,"khong_ap_dung":0 } ] } ],
    "ca_nhan": [ { "ten","ht","diem","loai","yeu_nhat","manh_nhat","co_do":[],
                   "tt_chinh","ngon_ngu" } ],         // ⛔ chỉ vào sổ tay riêng
    "theo_tang": [ { "tt","so_nv","diem_tb","ht" } ], // ★ id-F §8 mục ⑦
    "co_do":   [ { "ma":"CĐ-5","nguoi","ht","nguyen_van","nguoi_xu_ly" } ],
    "viec_he_thong": [ { "nhom","nguyen_nhan","so_ht","ai_cap","chan_ma" } ],  // ★ 7 nhóm
    "ghi_chu": "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai."
  },

  "meta": {                                          // tab ⑤ — trước gọi "facebook"
    "nguon","ky","ky_truoc","don_vi":"nghìn đ|USD",
    "chuoi": [ { "ma":"CHI|CPM|CTR|CPI|CPL|CPB|CPA_KHAM","nhan","gia_tri",
                 "muc_tieu","ky_truoc","kieu","tot","phu" } ],
    "theo_tang": [ { "tt","market","chi","inbox","lead","booking","den_kham",
                     "cpi","cpl","cpa_kham" } ],      // ★ cắt theo thị trường
    "cua_so_do": { "ngay":0, "du_8_tuan": false,
                   "ghi_chu":"⚠ TT-B/TT-C cần cửa sổ ≥8 tuần — id-E §1" },
    "truy_duoc": { "pct":0, "ghi_chu":"% inbox truy được về chiến dịch — id-E §6" },
    "noi_dung":  [ { "noi_dung","tt","ngon_ngu","danh_gia":"tot|giu|kem",
                     "tong":{...},"co_phap_che","nhan_xet" } ],
    "nhieu_mau": { "chien_dich":[ { "ten","chi" } ], "ghi_chu" },
    "van_de":    [ ... ]
  },

  "google": { "co_du_lieu": false, "ghi_chu": "⚠ chưa có dữ liệu Google Ads" },

  "ma_tran": {
    "trang_thai":"cho_duyet|da_duyet","duyet_boi","duyet_luc","cach_xep",
    "khoi": [ { "ma":"tang_hot|mo_s4|giam_cold|toi_uu_warm","ten","muc_tieu","tap_lead",
                "dong":[ { "cd","ten","tt","ht","lead","co_lh","he_so","diem","chang",
                           "cau_xa_chua_tl":[],"du_kien_du":true,"huong","chon","uu_tien" } ] } ],
    "sua_van_hanh": [ { "cd","ten","ht","truc","ly_do" } ],
    "cho_cap":      [ { "du_kien","ai_cap","so_ht","chan_ma" } ],     // ★ nhóm ⏸
    "quan_sat":     [ { "cd","ten","ht" } ]
  },

  "hook":   { "ghi_chu","dong": [ { "ma","khoi","cd","ten","tt","ngon_ngu","market",
                                    "chang","ma_o","rao","insight","hook","loai_hook",
                                    "fm":["L13","L16","L10"],"cta","truy_nguoc",
                                    "co_phap_che_vn","co_phap_che_market",
                                    "du_kien_du":true,"duyet" } ] },

  "so_tay": { "da_sinh": false, "so_ban": 0, "duong_dan": "out/so-tay/" },
  "viec":   [ { "so","viec","bo_phan","so_huu","han","do_the_nao","trang_thai" } ],
  "ghi_chu": [ "..." ],
  "truoc":   { "ky","the_tong","tep","noi_dung","chuoi","nhan_vien","thi_truong" },
  "moc_goc": { "ky","nguon","dong":[...] }
}
```

★ **Năm khối mới so với bản nội địa:** `thi_truong` · `pheu.ma_oq` · `pheu.s4_chua_dong` · `pheu.rao_chot` · `ma_tran.cho_cap`. Thêm `r8`, `meta.theo_tang`, `meta.cua_so_do`, `meta.truy_duoc`, `nhan_vien.theo_tang`.
⚠️ Khối `facebook` của bản nội địa đổi tên thành **`meta`** — ⛔ không đọc chéo hai schema.

---

## 3. NĂM LUẬT HIỂN THỊ *(nội địa: bốn)*

```
① KHÔNG CÓ SỐ thì hiện "—", ⛔ không hiện 0.
   0 nghĩa là đã đo và bằng không. "—" nghĩa là chưa đo.
   Cùng luật đó cho CHÂN DUNG: `tep` rỗng thì tab ③ hiện một ô khoá
   "⏳ chân dung chưa được phác họa" kèm lý do.

② MỌI SO SÁNH ghi rõ so với cái gì:
   "▲ 2,1 điểm so kỳ trước"  ·  "mốc gốc 42,7% · ▼ 3,2 điểm"
   Chưa có mốc → "⚠ chưa có mốc so sánh".

③ TIỀN: VND quy về NGHÌN ĐỒNG; bản xuất USD thì GIỮ USD.
   ⛔ Không trộn hai đơn vị trong một bảng. Ghi đơn vị ở đầu bảng.

④ TÊN NHÂN VIÊN ⛔ không xuất hiện trong tab ④ ở dạng bảng xếp hạng.
   Tab ④ hiện: phân bố A/B/C/D · % đạt từng tiêu chí · cờ đỏ (có tên, vì cần
   người xử) · việc hệ thống. Bảng điểm có tên chỉ nằm trong sổ tay riêng.

⑤ ★ MỌI TỶ LỆ PHẢI CẮT ĐƯỢC THEO TẦNG.
   Một con số trung bình toàn kỳ ⛔ không được đứng một mình: luôn kèm dòng
   phân rã TT-A/B/C/D. Tầng dưới 10 HT hiện "⚠ MẪU NHỎ", ⛔ không hiện tỷ lệ.
   Và: TT-0 ≥ 20% → dải tầng ở đầu trang tô cảnh báo, kèm câu
   "chưa biết khách ở đâu — mọi tỷ lệ bên dưới đọc với độ tin thấp".
```

---

## 4. KHỐI "VIỆC CẦN XỬ LÝ" — CUỐI TRANG

| Cột | Ghi chú |
|---|---|
| `#` | Số thứ tự |
| `Việc` | Viết như hành động |
| `Bộ phận` | Marketing · Trực kênh · Hệ thống · **Điều phối QT** · **Khoa Chuyên môn** · **Pháp chế** · BU |
| `Sở hữu` | ★ **Tên người thật.** Việc không có tên là việc không ai làm |
| `Hạn` | |
| `Đo thế nào` | Chỉ số cụ thể của kỳ sau |
| `Trạng thái` | mới · đang làm · đạt · chưa đạt · ★ `⏸ chờ cấp dữ kiện` |

★ Việc **chưa đạt 2 kỳ liên tiếp** → tự động gắn cờ `2 kỳ — đẩy BU`.
★★ Việc `⏸ chờ cấp dữ kiện` **chưa đạt 2 kỳ** → gắn cờ `🔴 CHẶN KÉO DÀI` và đưa lên **đầu trang**, không để cuối trang. Một ô dữ liệu trống hai kỳ liền đang chặn nhiều lead hơn mọi việc nội dung trong danh sách.

---

## 5. THEO DÕI VIỆC KỲ TRƯỚC

Mỗi kỳ mở đầu bằng việc **chấm lại việc kỳ trước**: đạt / chưa đạt / chưa đo.

⛔ Báo cáo không theo dõi việc kỳ trước là báo cáo bắt đầu lại từ đầu mỗi kỳ.

⚠️ **Với `TT-B`/`TT-C`, một việc marketing ⛔ không được chấm "chưa đạt" sau một kỳ 2 tuần** — độ trễ 4–12 tuần (`id-E` §1). Ghi `⏳ chưa đủ cửa sổ đo`.

---

## 6. TỰ KIỂM SỔ NÀY

- [ ] File JSON có `schema` đúng `insight-dashboard-knqt/1` không?
- [ ] Tổng các cột có khớp `so_ht_phan_tich` không? Bảng chân dung đã **cộng cả `CD0`**, bảng tầng đã **cộng cả `TT-0`** chưa?
- [ ] ★ Tab ② có đủ **bốn bảng cắt** của `id-L` §8 chưa?
- [ ] ★ Dải tầng ở đầu trang có hiện không? `TT-0` ≥ 20% có tô cảnh báo không?
- [ ] ★ Thẻ `S4 chưa đóng` có trong 6 thẻ số tổng không?
- [ ] ★ Có tỷ lệ nào đứng một mình, không kèm phân rã theo tầng không?
- [ ] ★ Tầng dưới 10 HT có hiện tỷ lệ thay vì `⚠ MẪU NHỎ` không?
- [ ] `chan_dung.phac_hoa.duyet_boi` có tên người thật chưa?
- [ ] Ô chưa đo có hiện `—` thay vì `0` không?
- [ ] Có bảng nào trộn VND và USD không?
- [ ] Tab ④ có bảng xếp hạng có tên lọt ra không?
- [ ] ★ Khối `viec_he_thong` có gom theo **bảy nhóm** và ghi **ai cấp** chưa?
- [ ] ★ Có dòng `⏸ chờ cấp dữ kiện` nào quá 2 kỳ mà chưa gắn `🔴 CHẶN KÉO DÀI` không?
- [ ] ★ `r8.xac_nhan` có được in ra không?
- [ ] Tab ⑩ có đủ: nguồn · đã loại gì · vì sao loại không?

---

<!-- ===== id-K-module-knqt-phap-che.md ===== -->

# id-K · MODULE ĐƠN VỊ KANGNAM QUỐC TẾ & PHÁP CHẾ HAI TẦNG

> ★ **Đây là module thương hiệu.** Đổi đơn vị → **thay đúng sổ này**, ⛔ không sửa `id-A` … `id-J`, `id-L`.
> Dữ kiện đồng bộ với `Agent-AdsOptimize-Kangnam-QT/knowledge/kn-ho-so-thuong-hieu-qt.md` + `kn-rao-phap-ly-qt.md`. **Lệch nhau thì hai file đó là bản gốc.**
> Bản chụp site: **2026-10-21**. Site mới hơn sổ này → **tin site**, rồi báo người dùng cập nhật.

---

## 0. NGUỒN DỮ LIỆU — tra tại thời điểm chạy

| Dữ liệu | Nguồn duy nhất | Dùng cho |
|---|---|---|
| Dịch vụ · định vị · trust | `kangnamaesthetichospital.com` | mọi đầu ra |
| ★ **Giá** | `/price-list/` — **giá CÔNG KHAI** | chấm `N3.1` · hook có giá |
| Bác sĩ | trang bác sĩ của **site quốc tế** | mọi câu chạm tên bác sĩ |
| Số ngày ở lại VN | ❌ **chưa có trên site** → Khoa Chuyên môn | `OQ-01` · `N7.6` |

⚠️ **Site quốc tế và site nội địa ⛔ KHÔNG trùng nhau** ở: số cơ sở · danh sách bác sĩ · hiển thị giá · claim hội–hiệp hội. Lấy dữ kiện từ site nội địa cho khách quốc tế là lỗi phổ biến nhất khi mới dùng bản này.

---

## 1. HỆ THỐNG

| Dữ kiện | Giá trị | Nguồn |
|---|---|---|
| Tên dùng cho khách quốc tế | **Kangnam Korean Aesthetic Hospital** *(hiển thị: Kangnam Aesthetic Hospital)* | site EN |
| Viết tắt nội bộ | **KN-QT** | |
| Định vị site đang dùng | *"Korean Quality, Affordable Price"* | site EN |
| Pháp nhân của site EN | **Công ty TNHH Bệnh viện Thẩm mỹ Kangnam Sài Gòn** · MST **0312155633** | footer |
| Hotline | **(+84) 981 615 151** | site EN |
| Giờ làm việc | **Mon–Sun · 8am–5pm (UTC+7)** → xem `id-L` §4 | site EN |
| Kênh nhắn tin | WhatsApp · Telegram · Viber · Line · KakaoTalk · Zalo · Messenger | site EN |
| Ngôn ngữ site | English · Vietnamese · **Khmer** *(⛔ chưa có Arabic)* | site EN |

### ★ CHỈ HAI CƠ SỞ — và cả hai là tuyến bệnh viện

| Cơ sở | Địa chỉ *(nguyên văn site EN)* | Giấy phép | Đại phẫu |
|---|---|---|---|
| **Kangnam Hanoi** | No. 190 Truong Chinh St., Kim Lien Ward, Hanoi | **194/BYT-GPHĐ** | ✅ |
| **Kangnam Ho Chi Minh City** | No. 666 Cach Mang Thang 8 St., Tan Son Nhat Ward, HCMC | **287/BYT-GPHĐ** *(BYT cấp 03/12/2020)* | ✅ |

> ✅ **Bản quốc tế KHÔNG có bẫy TUYẾN của bản nội địa.** Cả hai cơ sở đều là tuyến bệnh viện → mời đại phẫu hợp lệ ở cả hai.
> ⛔ **Nhưng ⛔ không được giới thiệu 5 viện thẩm mỹ tỉnh** (Hải Phòng · Nghệ An · Đà Nẵng · Cần Thơ · Thanh Hoá) cho khách quốc tế: các cơ sở đó **không làm đại phẫu**. Nhân viên nhắc chúng trong hội thoại quốc tế → **cờ đỏ `CĐ-8`**.
> ⚠️ **Hai cơ sở, hai số giấy phép.** Mỗi câu trả lời phải ghi **đúng số của cơ sở đang nói tới**; ⛔ không dùng chung một số, ⛔ không chỉ ghi tên thương hiệu rồi bỏ số.

---

## 2. MENU DỊCH VỤ — TÊN QUỐC TẾ

Khi đọc hội thoại và khi viết hook, dùng **tên quốc tế**, ⛔ không dịch thô từ tiếng Việt.

| Nhóm | Dịch vụ (tên EN) |
|---|---|
| **Facial Aesthetic** | Rhinoplasty · Eyelid surgery (double eyelid · canthoplasty · ptosis) · Facelift · Neck lift · Forehead lift · Fat grafting |
| **Jaw & Facial Contouring** | V-line surgery · Jaw correction · Zygoma reduction · Chin augmentation · Lip surgery |
| **Body Aesthetic** | Breast augmentation · Breast lift · Liposuction / Lipo 360 · Tummy tuck |
| **ICEFUE Hair Transplant** | Hair transplant |
| **Reconstructive** | Facial paralysis treatment · reconstructive surgery |
| **Dentistry (KDT)** | Braces · Porcelain crowns · Dental implants · Veneers — ⚠️ bằng chứng chỉ thuộc cơ sở **TP.HCM (287)** |
| **Skin & Clinic** | Pigmentation · acne · scar · laser · spa — ⚠️ **chỉ bán cho `TT-D`** |

### ★ Luật combo — hệ quả trực tiếp khi đọc insight

> ⛔ **Không ai bay 6 giờ để cắt mí.**

Dịch vụ giá thấp (eyelid đơn lẻ · da liễu · clinic) với `TT-A/B/C`: hệ số giá trị đơn tối đa **1**, và trong ma trận ưu tiên chỉ được xếp vào **cụm combo / cross-sell**, ⛔ không mở tuyến riêng. Với `TT-D` thì ngược lại: đây là **dịch vụ lõi**.

### Cross-sell — ⛔ chỉ MỘT hướng mỗi lần

| Đã làm | Cross-sell hợp lý |
|---|---|
| Mũi | mí → cằm → hàm *(cùng cụm gương mặt)* |
| Mắt | mũi → hàm |
| Hàm mặt | mũi → mí |

⛔ Không cross-sell cho khách **đang điều trị**, ⛔ không cross-sell ở chặng `S6` *(khách vừa về nước, đang lo hậu phẫu)*.

---

## 3. 🔴 BỐN XUNG ĐỘT ĐANG CHẶN — GỐC CỦA PHẦN LỚN CỜ ĐỎ

### ① "LIFETIME WARRANTY" — site đang ghi, mà chưa có T&C

Site ghi trong khối *Clients Specialized Benefits*: **"Lifetime warranty"**.

```
Đây vừa là CAM KẾT MẠNH NHẤT trên toàn site,
vừa là CLAIM RỦI RO NHẤT — và vừa là BẰNG CHỨNG GỠ RÀO XA mạnh nhất
cho khách TT-C. Nên ⛔ không thể chỉ bỏ đi: phải làm cho nó DÙNG ĐƯỢC.
```

| Tình huống trong hội thoại | Xử thế nào |
|---|---|
| Khách hỏi *"what if I need a revision?"* | Trả lời bằng **quy trình** *(tái khám · đánh giá lại · ai liên hệ)*, ⛔ không nêu thời hạn |
| Nhân viên đã nhắn *"lifetime warranty"* | **Cờ đỏ `CĐ-2`** · báo riêng kèm nguyên văn |
| Nhân viên nhắn *"follow-up and warranty policy — see terms"* | ✅ đúng |

★ Văn bản T&C phải nêu đủ **năm thứ** mới dùng được: `phạm vi · thời hạn · điều kiện loại trừ · ai chi trả chi phí BAY nếu phải chỉnh sửa · xử lý từ xa thế nào`.
⚠️ **Mục "ai trả tiền vé" là mục khách `TT-C` hỏi nhiều nhất và là mục duy nhất không có ở bản nội địa.**

### ② CLAIM HỘI–HIỆP HỘI — hai site đang nói hai điều khác nhau

Site quốc tế **đang hiển thị**: VSAPS · ASPS · ASAPS · ISAPS · AAFPRS. Bản nội địa **cấm thẳng** mọi claim hội–hiệp hội.

**Luật của bản QT — ba điều kiện, phải đủ cả ba:**

```
① Gắn với TÊN MỘT NGƯỜI cụ thể, ⛔ không gắn ở mức thương hiệu / ekip.
② Có HỒ SƠ THÀNH VIÊN CÒN HIỆU LỰC lưu tại Pháp chế, đúng người đúng hội.
③ ⛔ KHÔNG trình bày như "board certified" hay như giấy phép hành nghề.
```

→ Thiếu một điều kiện → **bỏ claim**. Nhân viên nhắn *"our doctors are board certified"* → **cờ đỏ `CĐ-4`**.
⚠️ Nhầm tư cách hội với board certification là điểm **bị chất vấn nhiều nhất ở US/AU**.

### ③ GIÁ — ★ ĐÃ CÔNG KHAI, NÊN LUẬT NGƯỢC VỚI BẢN NỘI ĐỊA

> Bản nội địa: 🔴 **chặn** nêu giá (chưa có bảng hiện hành).
> Bản quốc tế: ✅ **có bảng giá công khai** tại `/price-list/` — **chênh giá chính là cái hook**, khách `TT-C` vào để tìm đúng con số đó.

**Hệ quả lớn cho `id-F`:** tiêu chí `N3.1` ở bản này **chấm được thật**, ⛔ không còn là *"lỗi hệ"* như bản nội địa. Trực kênh né giá khi site đã công khai giá là **lỗi người**.

**Năm dòng bắt buộc khi nêu giá** — thiếu một dòng là điểm trừ, thiếu dòng ② là **cờ đỏ `CĐ-7`**:

```
① Nêu rõ ĐỒNG TIỀN (USD cho A/C, kèm VND).
② ★ Nêu PHỤ PHÍ QUỐC TẾ 10%:
   "The price shown does not include 10% international service charge."
③ Nêu tỷ giá chỉ là tham chiếu, đổi theo ngày thanh toán.
④ Nêu cái gì CÓ trong giá và cái gì KHÔNG (vé · khách sạn · phiên dịch).
⑤ "Final cost is confirmed by the doctor after in-person examination."
```

⚠️ **Bỏ dòng ② là bom niềm tin.** Khách phát hiện 10% ở quầy thanh toán thì mất cả ca **và** nhận một review xấu — đắt hơn mọi lead mất trong kỳ.

★ **Bản chụp giá 2026-10-21** *(để đối chiếu, ⛔ không để đăng — lấy lại tại `/price-list/`)*:

| Nhóm | Dịch vụ | VND | ≈ USD |
|---|---|---|---|
| Eyelid | 6D Eyelid Surgery | 12.000.000 | 461 |
| | VIP Eyelid Surgery | 20.800.000 | 800 |
| Rhinoplasty | Idol Structure (Nanoform) | 35.200.000 | 1.353 |
| | Surgiform Technique | 48.000.000 | 1.846 |
| | 6D VIP | 56.800.000 | 2.184 |
| | Rib Cartilage (100%) | 88.200.000 | 3.392 |
| Rejuvenation | Facelift | 51.200.000 | 1.969 |
| | Facelift + Neck Lift | 71.200.000 | 2.738 |
| | Forehead Lift | 40.000.000 | 1.538 |
| Jaw & Contouring | Chin Augmentation | 24.000.000 | 923 |
| | V-line 3D | 54.400.000 | 2.092 |
| | Zygoma Reduction | 54.400.000 | 2.092 |
| Liposuction | Advanced Lipo | 40.500.000 – 65.800.000 | 1.557 – 2.530 |
| | Mini Lipo (1 vùng) | 18.000.000 | 692 |
| Breast | 6D Basic | 67.000.000 | 2.576 |
| | 6D VIP | 84.000.000 | 3.230 |

⛔ **Không so sánh giá với một quốc gia hoặc cơ sở có tên.** *"70% cheaper than Australia"* là claim cần bằng chứng và là rủi ro ở AU/UK → **cờ đỏ `CĐ-10`**. Cách đúng: *"Our full price list is published — compare it yourself."*

### ④ CHỨNG CHỈ BÁC SĨ — site quốc tế ⛔ không công bố số CCHN

Bản chụp 2026-10-21, nguyên văn credential trên site quốc tế:

| Bác sĩ | Chức danh | Bằng cấp | Kinh nghiệm | Cơ sở |
|---|---|---|---|---|
| **Dr. PhD Richard Huy** | Medical Director – Hanoi | Doctor of Medicine (PhD) – Hanoi Medical University | Over 20 years | Hanoi |
| **Dr. Felix Tran** | Medical Director – HCMC | M.D. – Thai Nguyen University of Medicine and Pharmacy | Over 20 years | HCMC |
| **Dr. Frankie Vu** | Deputy Head, Facial Plastic & Aesthetic Surgery – HCMC | M.D. – Military Medical Academy | Over 10 years | HCMC |
| **Dr. Victor Vu** | Head of Maxillofacial Surgery – Hanoi | Specialist Level I, Oral & Maxillofacial | Nearly 20 years | Hanoi |
| **Dr. Henry Nguyen** | Head of Facial Plastic & Aesthetic Surgery – Hanoi | Specialist Level I, General Surgery – HMU | Over 12 years | Hanoi |

**Bốn cổng trước khi một câu trả lời được gắn tên bác sĩ:**

```
① CÓ TRÊN SITE QUỐC TẾ không — site nội địa có 16 người, site QT công bố 5.
   ⛔ Nhân sự ở site nội địa KHÔNG tự động dùng được cho khách quốc tế.
② ĐÚNG CHUYÊN KHOA VÀ ĐÚNG CƠ SỞ — bác sĩ HCMC ⛔ không gắn cho khách
   đang hỏi về Hà Nội.
③ CÓ SỐ CCHN — site quốc tế ⛔ KHÔNG công bố. Chưa đối chiếu nội bộ
   → ⛔ không nêu claim tay nghề ở mức cá nhân.
④ CÓ TRONG DANH SÁCH NỘI BỘ "ĐƯỢC DUYỆT QUẢNG BÁ" — Pháp chế giữ.
```

⚠️ Số năm kinh nghiệm: chép **đúng** chữ trên site (*"Over 20 years"*, *"Nearly 20 years"*). ⛔ Không làm tròn *"nearly 20"* thành *"20+"* — đó cũng là `CĐ-4`.

---

## 4. ★ HAI TẦNG PHÁP LÝ — KHÁC BIỆT LỚN NHẤT SO VỚI BẢN NỘI ĐỊA

Mọi câu nhân viên gõ ra cho khách quốc tế chịu **hai hệ luật cùng lúc**:

| Tầng | Áp vì | Luôn áp? |
|---|---|---|
| ① **Luật Việt Nam** | Cơ sở ở VN, dịch vụ là khám chữa bệnh — cần **giấy xác nhận nội dung quảng cáo** | ✅ **Luôn**, bất kể khách ở đâu |
| ② **Luật nước người xem** | Nền tảng và cơ quan quản lý áp theo **vị trí người nhận** | ✅ Theo từng `market` |

→ Một câu hợp lệ ở Việt Nam **vẫn có thể** bị cơ quan nước đích xử lý.
→ Mọi đầu ra phải ghi rõ **đang nói với `market` nào** và **đã rà theo luật nước nào**.

⛔ **Agent ⛔ KHÔNG đưa ra kết luận pháp lý.** Agent chỉ được: ① nêu tên cơ quan/bộ quy tắc phải tra · ② gắn cờ vào đúng thành phần rủi ro · ③ đề xuất câu thay thế đã hạ rủi ro. Dòng kết luận luôn là: *"cần Pháp chế xác nhận cho thị trường [X] trước khi phát."*

### Bảng rủi ro theo thị trường — ⛔ phải tra, ⛔ không suy đoán

| Thị trường | Cơ quan / bộ quy tắc | Điểm nóng đã biết | Mức |
|---|---|---|---|
| **AU** | **AHPRA** *(Guidelines for advertising regulated health services)* · TGA | **Cấm testimonial về kết quả lâm sàng**; before–after ràng buộc rất chặt | 🔴 **Cao nhất** |
| **UK** | ASA / CAP Code · GMC | Mọi claim cần bằng chứng; ⛔ không quảng cáo thuốc kê đơn | 🔴 Cao |
| **EU/EEA** | luật từng nước + **GDPR** | Dữ liệu sức khoẻ là **special category**; phải nêu việc **chuyển dữ liệu sang Việt Nam** | 🔴 Cao |
| **US** | FTC *(Health Products Compliance Guidance)* + luật từng bang | Claim phải có cơ sở; disclosure *"clear and conspicuous"* | 🟠 TB–Cao |
| **CA / NZ** | tương tự AU/UK | Testimonial và before–after cần rà | 🟠 TB |
| **GCC** | cơ quan y tế từng nước *(vd DHA/MOHAP – UAE)* | Cần giấy phép quảng cáo y tế riêng; chuẩn mực hình ảnh nghiêm | 🔴 Cao |
| **KH · LA · ID · PH · MY** | luật từng nước | **Ít tiền lệ thực thi ⛔ không có nghĩa là được phép** | 🟡 TB |

### Ba thành phần rủi ro cao — xử theo tầng

| Thành phần | `TT-A` | `TT-B` · `TT-D` | ★ `TT-C` (AU·UK·EU·US·GCC) |
|---|---|---|---|
| **Before–after mặt** | ✅ nếu có văn bản đồng ý + đã duyệt | ✅ như trên | 🔴 **Mặc định KHÔNG** — Pháp chế duyệt riêng từng thị trường |
| **Before–after cơ thể / giảm béo** | ⛔ | ⛔ | ⛔ **không, ở mọi thị trường** |
| **Testimonial về kết quả lâm sàng** | ✅ nếu thật | ✅ nếu thật | 🔴 **KHÔNG** — AHPRA cấm thẳng |
| **Testimonial về trải nghiệm phi lâm sàng** *(phiên dịch · đưa đón · khách sạn · thái độ)* | ✅ | ✅ | ✅ **lối đi hợp lệ cho `TT-C`** |

★ **Hệ quả cho ngân hàng hook và cho sổ tay:** trụ bằng chứng của `TT-C` ⛔ **không phải** before–after và review, mà là:

```
giấy phép Bộ Y tế → hồ sơ bác sĩ → quy trình an toàn có văn bản
→ chính sách bảo hành/chỉnh sửa bằng văn bản → chăm sóc từ xa sau khi về nước
```

---

## 5. RÀO `R` — NĂM RÀO CỨNG DÙNG CHUNG VỚI GÓI ADS QT

| Mã | Rào | ⛔ Không được | Người duyệt |
|---|---|---|---|
| `R2` | **Danh mục kỹ thuật (DMKT)** | Nêu kỹ thuật **ngoài danh mục đã phê duyệt** của cơ sở — cụ thể *deep plane · BBL · abs etching* | Pháp chế |
| `R3` | **Đúng pháp nhân & phạm vi** | Dùng tên "Kangnam" cho dịch vụ mà **cơ sở đó không có trong phạm vi**. ⚠️ **Trang web ⛔ không phải văn bản phạm vi giấy phép** | Pháp chế |
| `R7` | **Túi ngực · thiết bị · filler** | Nêu hãng **không dùng thật**, hoặc vật liệu **không rõ số lưu hành** | BS + Pháp chế |
| ★ `R8` | **KCB cho người nước ngoài** | Tiếp nhận khách nước ngoài khi cơ sở/bác sĩ **chưa đủ điều kiện**, hoặc **không có phiên dịch chuyên môn** + hồ sơ song ngữ | Pháp chế + Điều phối QT |
| `R9` | **Giấy xác nhận nội dung quảng cáo** | Tưởng *"nội dung tiếng Anh thì không cần GXNNDQC"* — **sai** | Pháp chế |

### 🔴 `R8` là rào nặng nhất, và nó không phải rào câu chữ

`R2 · R3 · R7 · R9` nói về **câu chữ**. **`R8` nói về việc có được tiếp nhận khách hay không** — đó là **điều kiện hoạt động**.

> Inbox đẹp, điểm trực kênh 90, 40 lead tầng C — nhưng nếu cơ sở **chưa đủ điều kiện `R8`** thì **lead đổ về là rủi ro, không phải thành tích**.

→ **Luật:** mỗi báo cáo kỳ phải in một dòng xác nhận `R8`, hoặc ghi:
`[CHỜ CẤP: R8 — đủ điều kiện KCB cho người nước ngoài · Pháp chế + Điều phối QT]`.

---

## 6. MƯỜI HAI ĐIỂM PHÁP CHẾ `L` — BẢN QUỐC TẾ

| Mã | Điểm | Cờ |
|---|---|---|
| `L01` | Thiếu số giấy phép của **đúng cơ sở** đang nói tới | 🔴 |
| `L02` | Nhắc **viện thẩm mỹ tỉnh** cho khách quốc tế | 🔴 |
| `L03` | Cam kết kết quả chắc chắn · *guaranteed* · *permanent* | 🔴 |
| `L04` | ★ Con số/chữ **bảo hành** chưa có T&C — gồm *"lifetime"* | 🔴 |
| `L05` | Ảnh/video khách chưa có consent đúng mục đích | 🔴 |
| `L06` | Testimonial **kết quả lâm sàng** gửi cho khách `TT-C` | 🔴 |
| `L07` | Nói quá chức danh/bằng cấp · *"board certified"* | 🔴 |
| `L08` | Trả lời câu bệnh nền / chống chỉ định thay bác sĩ | 🔴 |
| `L09` | ★ Nêu giá mà **bỏ dòng phụ phí 10%** | 🔴 |
| `L10` | ★ Hứa **số ngày ở lại** hoặc mốc được phép bay bằng số cứng | 🔴 |
| `L11` | **So sánh giá** với quốc gia/cơ sở có tên | 🟡 |
| `L12` | Thu dữ liệu khách EU/UK mà **chưa có privacy notice đạt GDPR** | 🔴 |

★ **Bốn mã `L09` · `L10` · `L11` · `L12` là mã chỉ có ở bản quốc tế.** Chúng không tồn tại ở bản nội địa, và `L10` là mã nặng nhất: nó là **rủi ro y khoa**, không chỉ rủi ro câu chữ.

### ⚠️ `L12` — form & dữ liệu cá nhân

```
① Ảnh khách gửi để pre-consultation LÀ DỮ LIỆU SỨC KHOẺ ở mọi thị trường.
② ⛔ KHÔNG nạp ảnh khách · hộ chiếu · hồ sơ bệnh án lên công cụ công cộng,
   KỂ CẢ công cụ AI. Điều này áp cho cả agent này.
③ Khách EU/UK mà chưa có privacy notice đạt GDPR → [BLOCKED: GDPR notice — Legal].
```

★ Khi **ẩn danh hội thoại** để đưa vào báo cáo, bản quốc tế phải bỏ thêm bốn thứ so với bản nội địa: **quốc tịch cụ thể của cá nhân · số hộ chiếu · số hiệu chuyến bay · tên khách sạn khách đang ở** (`id-B` §2).

---

## 7. BẢNG CHẶN TỔNG

| Dòng loại này | Bị chặn bởi | Trạng thái |
|---|---|---|
| *"Lifetime warranty"* · mọi thời hạn bảo hành | §3① | 🔴 **CHẶN** |
| *"Board certified"* · claim hội ở mức thương hiệu | §3② | 🔴 **CHẶN** |
| Nêu giá mà bỏ **phụ phí 10%** | §3③ | 🔴 **CHẶN** |
| **Số ngày ở lại VN** nêu bằng số cứng | `id-L` §7 | 🔴 **CHẶN** |
| Testimonial kết quả lâm sàng cho `TT-C` | §4 | 🔴 **CHẶN** |
| Before–after cơ thể / giảm béo | §4 | 🔴 **CHẶN** |
| Nhắc viện tỉnh cho khách quốc tế | §1 | 🔴 **CHẶN** |
| Gắn chức danh bác sĩ chưa đối chiếu | §3④ | 🔴 **CHẶN** |
| ★ **Giá dịch vụ theo `/price-list/`** | §3③ | 🟢 **DÙNG ĐƯỢC** — kèm đủ 5 dòng |
| Quyền lợi khách xa: đưa đón · khách sạn · phiên dịch · 5 bước | §8 | 🟢 **SẠCH** — xác nhận còn áp dụng |
| Mốc hồi phục, thời gian mổ | `L10` | 🟡 **HỎI LẠI** — cần BS duyệt |

---

## 8. ★ BỘ BẰNG CHỨNG SẠCH PHÁP CHẾ — DÙNG ĐƯỢC NGAY Ở MỌI THỊ TRƯỜNG

Đây là tài sản mạnh nhất của bản quốc tế và đang **bị dùng ít nhất**. Toàn bộ nhóm này là **quyền lợi dịch vụ, không phải claim y khoa → sạch pháp chế**, trực kênh trả lời được ngay.

| # | Bằng chứng | Gỡ rào cản |
|---|---|---|
| ① | **Giấy phép Bộ Y tế** — 194 (HN) · 287 (HCMC) | NGỜ |
| ② | **Hồ sơ bác sĩ** — bằng cấp, trường, số năm *(nguyên văn site)* | NGỜ · SỢ |
| ③ | **Korean-Trained Surgeons** ⚠️ cần hồ sơ đào tạo kèm theo | NGỜ |
| ④ | **Quy trình an toàn · phòng mổ vô khuẩn · hội đồng chuyên môn** | **SỢ** |
| ⑤ | ★ **International Patient Department** + phiên dịch | **XA** |
| ⑥ | ★ **Quy trình 5 bước cho khách ở xa** — xem dưới | **XA** |
| ⑦ | **3D Simulation System** | NGỜ |
| ⑧ | **Muslim-Friendly Care** ⚠️ chưa khai gồm những gì | NGẠI *(GCC · MY · ID)* |
| ⑨ | **Bảng giá công khai + phụ phí 10% nói trước** | NGẠI *(chi phí)* |
| ⑩ | Testimonial **phi lâm sàng** *(phiên dịch · đưa đón · thái độ)* | NGẠI |

### Quy trình 5 bước cho khách ở xa — *"Out of Town Patients"*

| Bước | Tên | Nội dung *(nguyên văn site)* |
|---|---|---|
| 1 | Pre-Consultation | *"Recommendable surgery, estimated cost, and the detailed information regarding surgery will be provided based on the pictures"* |
| 2 | Reservation | *"Schedule a date on the desired date. Hotel recommendation and Airport pick up will be provided"* |
| 3 | Consultation in Person | *"Meet the specialized surgeon for each surgery area and get more accurate surgery plan"* |
| 4 | Operation | *"Safety is our priority"* |
| 5 | Post Operative Care | *"Communicating with the interpreter will be continued after departure"* |

★ **Ba chỗ khối này đang yếu — và hội thoại thật sẽ chỉ đúng vào ba chỗ đó:**

```
① Bước 2 ⛔ không nói SỐ NGÀY phải ở lại  → khách không đặt được vé (OQ-01).
② Bước 4 chỉ có một TÍNH TỪ "Safety is our priority" — đúng chỗ cần bằng chứng
   nhất. Phải thay bằng: ai mổ · ở đâu · phòng mổ gì · theo dõi bao lâu · ai trực.
③ Bước 5 ⛔ không nói THỜI HẠN và KÊNH  → "continued after departure" trong bao
   lâu, qua kênh nào, ai là người liên hệ. Đây đúng là câu TT-C muốn biết nhất.
```

→ Mỗi kỳ, nếu hội thoại chạm ba chỗ này thì agent **phải** đưa chúng lên mục *việc hệ thống*, ⛔ không chấm thành lỗi của nhân viên.

### Bốn thứ ❌ không thấy trên site — danh sách đặt hàng dữ liệu

| Hạng mục | Vì sao cần | Mã liên quan |
|---|---|---|
| **Visa / thư mời** | Câu hỏi thường gặp của `TT-A` | `OQ-05` |
| **Thanh toán quốc tế** — thẻ? chuyển khoản? đặt cọc bao nhiêu? | **Rào cản chốt thật** | `OQ-06` |
| **Giờ trực + ngôn ngữ của International Patient Department** | Mọi ô SLA ngoài giờ | `id-L` §4 |
| **Muslim-Friendly Care gồm những gì** | Claim vô nghĩa nếu không nêu cụ thể | `OQ-08` |

---

## 9. CỔNG 2 — SOÁT HAI TẦNG TRƯỚC KHI PHÁT

Trước khi phát sổ tay / đăng hook, agent chạy soát và in ra:

```
TẦNG ① LUẬT VIỆT NAM
  🔴 <n> dòng CHẶN   — kèm câu thay thế
  🟡 <n> dòng HỎI LẠI — ai duyệt, chờ gì
  🟢 <n> dòng SẠCH
TẦNG ② LUẬT NƯỚC NGƯỜI XEM  — in RIÊNG cho từng market có mặt trong kỳ
  market · cơ quan phải tra · dòng rủi ro · câu thay thế
R8 · đủ điều kiện KCB cho người nước ngoài : ✅ đã xác nhận / 🔴 [CHỜ CẤP]
```

⛔ Còn một dòng 🔴 ở **bất kỳ tầng nào** thì ⛔ không phát bản đó.
⛔ Và ⛔ **không phát khi `R8` chưa xác nhận**, dù mọi câu chữ đã sạch.

---

## 10. TỰ KIỂM SỔ NÀY

- [ ] Mỗi dòng chạm cơ sở có ghi **đúng số giấy phép của cơ sở đó** không?
- [ ] Có chữ *"lifetime"* / thời hạn bảo hành nào lọt ra không?
- [ ] Có *"board certified"* hay claim hội ở mức thương hiệu nào lọt ra không?
- [ ] Mọi chỗ nêu giá có **đủ 5 dòng** ở §3③, đặc biệt **phụ phí 10%**, chưa?
- [ ] Có chỗ nào nêu **số ngày ở lại Việt Nam** bằng số cứng không?
- [ ] Có testimonial **kết quả lâm sàng** nào gửi cho `TT-C` không?
- [ ] Có nhắc **viện thẩm mỹ tỉnh** cho khách quốc tế không?
- [ ] Đã rà **tầng ② (luật nước người xem)** cho từng `market` có mặt trong kỳ chưa?
- [ ] ★ Đã in dòng xác nhận **`R8`** chưa?
- [ ] Khi ẩn danh, đã bỏ **quốc tịch cá nhân · hộ chiếu · số hiệu chuyến bay · tên khách sạn** chưa?

---

<!-- ===== id-L-thi-truong-ngon-ngu-mui-gio.md ===== -->

# id-L · ★★ TẦNG THỊ TRƯỜNG · NGÔN NGỮ · MÚI GIỜ · KÊNH

> **Sổ lõi của bản quốc tế — không có tương đương ở bản nội địa.**
> Bản nội địa cắt số theo **khu vực** (Bắc · Nam · Miền Tây). Bản này cắt theo **TẦNG THỊ TRƯỜNG × NGÔN NGỮ × MÚI GIỜ × KÊNH**.
>
> ⛔ **Luật tối thượng của sổ này:** không biết khách đang ở đâu thì ⛔ không kết luận gì về khách đó. Đó là **CỔNG M** ở `id-A` §3.
> Dữ kiện đồng bộ với `Agent-AdsOptimize-Kangnam-QT/knowledge/kn-thi-truong-quoc-te.md`. Lệch nhau thì **file đó là bản gốc**.

---

## 1. BỐN TẦNG THỊ TRƯỜNG `TT-A` … `TT-D`

Phân tầng theo **logic ra quyết định**, ⛔ không theo khoảng cách địa lý hay GDP.

| Mã | Tầng | Ai | Động cơ chính | Rào cản nặng nhất | Ngôn ngữ trong inbox | Giá trị ca |
|---|---|---|---|---|---|---|
| `TT-A` | **Khu vực lân cận** | KH · LA · MM · ID · PH · MY · IN · SG | Gần + rẻ hơn Thái/Hàn + kỹ thuật Hàn | **NGỜ** | English · Khmer · Bahasa | Trung bình–Cao |
| `TT-B` | ★ **Kiều bào** | Việt kiều US · AU · CA · DE · CZ · JP · KR · TW | Về thăm nhà **+** làm thẩm mỹ cùng chuyến | **XA** + NGẠI | **Tiếng Việt** | Cao–Rất cao |
| `TT-C` | ★ **Thị trường phát triển** | AU · US · UK · NZ · CA · GCC (AE · SA · KW · QA) | Chênh giá 60–80% so với nước họ | **SỢ** + **XA** | English (+ Arabic) | **Rất cao** |
| `TT-D` | **Expat đang ở VN** | Người nước ngoài sống/làm việc ở HN · TP.HCM | Tiện + cần bác sĩ nói tiếng Anh | **NGỜ** (giao tiếp) | English | Trung bình–Cao |
| `TT-0` | ⚠️ **Chưa khai được** | Hội thoại không đủ dấu hiệu để xếp tầng | — | — | — | — |

### `TT-0` — mã dự trữ, ⛔ không phải "rác"

`TT-0` giữ cho tổng luôn bằng cỡ mẫu. Nhưng khác với `CD0`, **`TT-0` đông là một lỗi vận hành cụ thể và sửa được ngay trong kỳ**:

```
TT-0 ≥ 20% mẫu  →  trực kênh KHÔNG HỎI khách đang ở đâu.
                   Đây là lỗi HỆ + lỗi KỸ NĂNG, không phải lỗi dữ liệu:
                   · hệ: form/lời chào tự động không hỏi quốc gia + múi giờ
                   · kỹ năng: tiêu chí N7.1 của id-F
                   → đẩy lên "việc hệ thống" VÀ vào sổ tay, cùng lúc.
```

⛔ **Không suy tầng từ dịch vụ khách hỏi.** Người hỏi rhinoplasty có thể ở Sydney, Phnom Penh hay Hà Nội — dịch vụ ⛔ không nói gì về tầng.

### Hai tầng hay bị bỏ sót — và đó là sai lầm đắt nhất

**`TT-B` (kiều bào) là tầng dễ chốt nhất** và thường bị gộp vào `TT-C`:

- Họ **đã tin thương hiệu Việt**, không phải thuyết phục từ số 0.
- Họ nói tiếng Việt → ⛔ không cần phiên dịch → chi phí phục vụ thấp nhất.
- Họ **đã có vé máy bay** vì lý do khác (Tết · hè · cưới hỏi · tang lễ) → rào cản chi phí đi lại **bằng không**.

→ Trong inbox, dấu hiệu nhận ra `TT-B`: **nhắn tiếng Việt** nhưng nói *"em ở Mỹ"*, *"bên Úc"*, *"về nước tháng 12"*, *"em về được 10 ngày"*.
⚠️ ⛔ **Không xếp họ vào nhóm "khách tỉnh xa" của bản nội địa.** Cùng chữ *"ở xa"* nhưng khác hẳn: khách tỉnh đi lại được nhiều lần, khách kiều bào có **một cửa sổ duy nhất**.

**`TT-D` (expat tại VN) không phải du lịch y tế** — họ **đã ở trong nước**. Mọi câu trả lời về đưa đón sân bay, khách sạn, số ngày ở lại là **vô nghĩa với họ**, và trả lời như thế là tín hiệu nhân viên chưa nhận ra tầng (tiêu chí `N7.2`).

---

## 2. ★ CỔNG M — VÌ SAO KHÔNG CÓ THỊ TRƯỜNG THÌ KHÔNG CÓ KẾT LUẬN

Cùng một câu, hai người hoàn toàn khác nhau:

> **"How much is rhinoplasty in Hanoi?"**
> — gõ từ **Sydney** = `TT-C`. Cần: giá · an toàn · số ngày ở lại · bảo hành từ xa · ai lo khi bay về.
> — gõ từ **Hà Nội** = `TT-D`. Cần: địa chỉ · bác sĩ nói tiếng Anh · hẹn khám tuần này.
> — gõ bằng **tiếng Việt từ Sydney** = `TT-B`. Cần: lịch khớp chuyến về · người nhà không biết · giá so với bên Úc.

Một câu trả lời cho cả ba → **mất cả ba**.

**Hệ quả cho mọi bảng trong dashboard:**

```
① Mọi tỷ lệ (% có liên hệ · % rơi · điểm trực kênh) phải CẮT ĐƯỢC theo tầng.
② Trung bình toàn kỳ vẫn in ra, nhưng LUÔN kèm dòng phân rã theo tầng.
   ⛔ Không bao giờ để một con số trung bình đứng một mình làm kết luận.
③ Tầng dưới 10 HT: ⛔ không kết luận riêng (id-A §5).
```

⚠️ **Lỗi im lặng nguy hiểm nhất của bản này:** trộn `TT-A` và `TT-C` rồi thấy *"CPL rẻ"*. CPL rẻ vì `TT-A` đông, còn `TT-C` — tầng đáng tiền nhất — thì **không ai trả lời nổi câu về bảo hành từ xa**. Trung bình che mất cả hai sự thật.

---

## 3. NGÔN NGỮ TRONG INBOX

| Mã | Ngôn ngữ | Thường gắn tầng | Lưu ý khi đọc |
|---|---|---|---|
| `EN` | English | A · C · D | Phần lớn khách `TT-A` và GCC đọc EN như **ngôn ngữ thứ hai** |
| `VI` | Tiếng Việt | **B** | ⚠️ Tiếng Việt **không** có nghĩa là khách nội địa — xem §1 |
| `KM` | Khmer | A (KH) | Site đã hỗ trợ Khmer |
| `AR` | Arabic | C (GCC) | ⛔ Chưa có người bản ngữ rà — xem §7 |
| `XX` | Khác / lẫn nhiều thứ tiếng | — | Đếm riêng, ⛔ không gộp vào `EN` |

### Ba luật đọc ngôn ngữ

```
① NGÔN NGỮ CỦA KHÁCH ≠ NGÔN NGỮ CỦA NHÂN VIÊN.
   Chấm riêng hai cột. Khách nhắn EN mà nhân viên trả lời VI
   → tiêu chí N7.3, và gần như luôn kèm "rơi do trực kênh".

② CHẤT LƯỢNG TIẾNG ANH CỦA NHÂN VIÊN LÀ LỖI HỆ TRƯỚC KHI LÀ LỖI NGƯỜI.
   Không có nhân sự nói được ngôn ngữ đó trong ca → "—" + việc hệ thống.
   Có nhân sự mà vẫn trả lời sai ngôn ngữ → ✗ (id-F §7 rào ③).

③ ⛔ KHÔNG CHẤM NGỮ PHÁP TIẾNG ANH.
   Chấm được: khách có được trả lời ĐÚNG NGÔN NGỮ không, câu có
   HIỂU ĐƯỢC không, có dùng máy dịch thô cho câu y khoa không.
   ⛔ Không trừ điểm vì "văn phong chưa hay" — đó không phải tiêu chí.
```

⚠️ **Dấu hiệu máy dịch thô cho nội dung y khoa** là cờ đỏ `CĐ-9`, không phải điểm trừ thường (`id-F` §5). Câu dịch sai về hậu phẫu là rủi ro y khoa thật.

---

## 4. ★ MÚI GIỜ — RÀO CẢN VẬN HÀNH, KHÔNG PHẢI CHI TIẾT NHỎ

**Giờ làm việc công bố trên site:** `Monday–Sunday, 8am–5pm` **giờ Việt Nam (UTC+7)**.

```
17:00 ICT  =  20:00 Sydney  ·  10:00 London  ·  06:00 Los Angeles  ·  13:00 Dubai
08:00 ICT  =  11:00 Sydney  ·  01:00 London  ·  17:00 LA (hôm trước) ·  05:00 Dubai
```

| Tầng | Giờ khách hay nhắn (giờ khách) | Rơi vào giờ ICT | Hệ quả |
|---|---|---|---|
| `TT-A` | Tối, 19–23h | 20–24h ICT | 🟠 Lệch **sau** giờ đóng |
| `TT-B` | Tối ở nước họ | US: 09–13h ICT · AU: 15–19h ICT | 🟢 AU lệch nhẹ · 🟢 US rơi trong giờ |
| `TT-C` | Tối ở nước họ | AU: 15–20h ICT · UK: 01–06h ICT · US: 05–11h ICT | 🔴 **UK/EU rơi hẳn ngoài giờ** |
| `TT-D` | Trong ngày, giờ VN | 08–17h ICT | 🟢 Trùng giờ |

### Luật chấm SLA theo múi giờ — ⛔ không dùng khung chung

```
① Tin khách đến TRONG 08:00–17:00 ICT  → chấm N1.1 bình thường.
② Tin đến NGOÀI khung đó               → N1.1 = "—"  (⛔ KHÔNG phải ✗)
                                          và HT đó vào ô "ngoài giờ".
③ Tin ngoài giờ mà SÁNG HÔM SAU KHÔNG AI TRẢ LỜI
   → ✗ ở tiêu chí N7.4 "dọn hộp thư ngoài giờ", KHÔNG phải ở N1.1.
```

★ **Vì sao tách làm hai tiêu chí.** Trả lời trong 2 phút lúc 3 giờ sáng không phải việc của nhân viên — đó là việc của **lịch trực**, tức việc hệ thống. Nhưng *"đến 11h trưa hôm sau vẫn chưa ai mở tin của khách UK"* **là** việc của nhân viên và của trưởng nhóm. Gộp hai thứ này vào một ô là cách chắc chắn nhất để **vừa trừ điểm sai người, vừa bỏ qua lỗi thật**.

### Chỉ số bắt buộc của tab Phễu

| Chỉ số | Ý nghĩa | Tốt là |
|---|---|---|
| `% HT đến ngoài giờ 8–17 ICT` | Đo **lỗ hổng lịch trực**, không đo nhân viên | — *(là dữ kiện, không phải điểm)* |
| ★ `Thời gian chờ trung bình của HT ngoài giờ` | Từ lúc khách nhắn → tin trả lời đầu tiên | **thấp** |
| `% HT ngoài giờ không được trả lời trong 12h` | Lead mất hẳn | **thấp** |
| `% HT có hỏi khung giờ + múi giờ của khách` | Tiêu chí `N7.5` | **cao** |

⚠️ **Đây là nguyên nhân số một của lead quốc tế "không kết nối được".** Khách `TT-C` gửi tin lúc tối ở nước họ, không ai trả lời trong nhiều giờ, hôm sau nhân viên gọi vào lúc khách đang ngủ → ghi *"khách không nghe máy"*. ⛔ **Đó không phải khách xấu, đó là lỗi lịch.**

---

## 5. BẢY KÊNH NHẮN TIN — ⛔ KHÔNG GỘP LÀM MỘT

Site công bố 7 kênh: **WhatsApp · Telegram · Viber · Line · KakaoTalk · Zalo · Messenger**.

| Kênh | Hay đi với tầng | Đặc điểm khi đọc hội thoại |
|---|---|---|
| **WhatsApp** | A · C · GCC | Kênh chính của khách quốc tế. Khách coi là kênh **riêng tư** → hỏi chuyện nhạy cảm nhiều hơn |
| **Telegram** | A · C | Khách rất kín tiếng, ít để lại tên thật |
| **Viber** | A (PH · MM) | |
| **Line** | JP · TW | |
| **KakaoTalk** | KR | Khách Hàn, kỳ vọng tốc độ trả lời rất cao |
| **Zalo** | **B** | Dấu hiệu mạnh của kiều bào |
| **Messenger** | mọi tầng | Nguồn từ quảng cáo Meta — nối được với số ads (`id-E` §6) |

### Ba luật về kênh

```
① KÊNH LÀ MỘT CHIỀU CẮT SỐ, không phải một nhãn trang trí.
   % có liên hệ và % rơi khác nhau rất xa giữa WhatsApp và Messenger.

② ⛔ KHÔNG SO CHÉO SLA GIỮA HAI KÊNH khác nhau về cơ chế thông báo.
   Messenger có hàng đợi của page; WhatsApp đổ về một số điện thoại.
   So trực tiếp là so hai hệ thống, không so hai con người.

③ KÊNH KHÔNG CÓ NGƯỜI TRỰC TRONG CA → mọi ô SLA của kênh đó là "—"
   + một dòng ở "việc hệ thống". ⛔ Không trừ điểm ai.
```

⚠️ **Chỉ `Messenger` (và ads click-to-WhatsApp có tham số) nối được về chiến dịch.** Các kênh khác, khách tự tìm đến → ⛔ **không gán nguồn ads cho chúng**, ghi `nguồn: tự tìm / chưa truy được`.

---

## 6. MÙA — KHÁCH QUỐC TẾ ĐẶT LỊCH KHI CÓ VÉ, ⛔ KHÔNG KHI CÓ ƯU ĐÃI

| Mùa | Tầng ảnh hưởng | Dấu hiệu trong inbox |
|---|---|---|
| **Trước Tết 8–10 tuần** | **B** | *"em về Tết này"*, *"về từ 20/1 đến 10/2"* |
| **Hè (6–8)** | B · C | *"school holidays"*, *"đi cùng con"* |
| **Mùa khô VN (11–4)** | A · C | — |
| **Ramadan + Eid** | **C (GCC)** | ⛔ Không chạy ca phẫu thuật trong Ramadan |
| **Trước cưới 3–6 tháng** | A · B · C | *"wedding in March"* — intent mạnh nhất |

★ **Hệ quả khi đọc insight:** một hội thoại `TT-B` nói *"em về Tết"* vào tháng 10 là **HOT**, dù khách chưa cho số và chưa chốt lịch — vì cửa sổ của họ đã xác định. Đây là lý do tín hiệu nóng của bản này có một tín hiệu khác bản nội địa (`id-D` §2 tín hiệu ②).

⚠️ Và ngược lại: cùng câu đó vào tháng 2 (sau Tết) là **COLD** — cửa sổ đã đóng, còn 10 tháng nữa.

---

## 7. 🔴 BA THỨ THIẾU VỀ THỊ TRƯỜNG — CHẶN KẾT LUẬN

| # | Thiếu gì | Ai cấp | Chặn gì |
|---|---|---|---|
| ① | ★ **SỐ NGÀY Ở LẠI VIỆT NAM** theo từng dịch vụ | **Khoa Chuyên môn** | 🔴 Mã `OQ-01` · tiêu chí `N7.6` · mọi hook chạm chặng `S4`. **Thiếu ô này là chặn lớn nhất của cả repo** |
| ② | **Lịch trực theo múi giờ** cho `TT-C` (UK/EU/US) | Vận hành + Điều phối QT | 🔴 Mọi ô SLA ngoài giờ · chỉ số §4 |
| ③ | **Danh sách nhân sự theo ngôn ngữ** (EN · KM · AR) từng ca | Vận hành | 🟠 Tiêu chí `N7.3` chấm `—`, ⛔ không trừ điểm người |
| ④ | Xác nhận **còn áp dụng** các quyền lợi khách xa: đưa đón · khách sạn · phiên dịch · visa · thanh toán quốc tế | Điều phối QT | 🟠 Mọi câu trả lời chạm `OQ-03` · `OQ-05` · `OQ-06` |

⛔ **Agent ⛔ KHÔNG được tự suy ra số ngày ở lại.** Đó là mốc y khoa (cắt chỉ · tái khám cuối · được phép bay), không phải con số marketing. **Bay quá sớm sau phẫu thuật là rủi ro y khoa thật.**
→ Chưa có → ghi `[CHỜ CẤP: số ngày ở lại — Khoa Chuyên môn]` đúng chỗ và liệt kê lại ở cuối output.

---

## 8. BẢNG CẮT SỐ BẮT BUỘC CỦA MỖI KỲ

Mỗi kỳ, tab Phễu phải có **đúng bốn bảng cắt** này, trước mọi bảng khác:

```
① TẦNG THỊ TRƯỜNG : TT · số HT · % mẫu · HOT/WARM/COLD · % có liên hệ
                     · % rơi do trực kênh · ngôn ngữ chính  (+ dòng TT-0)
② NGÔN NGỮ        : ngôn ngữ khách × ngôn ngữ nhân viên trả lời (ma trận nhỏ)
③ KÊNH            : kênh · số HT · % có liên hệ · thời gian trả lời đầu
④ MÚI GIỜ         : trong giờ / ngoài giờ · thời gian chờ TB · % mất quá 12h
```

★ Bốn bảng này là **nền của mọi kết luận sau đó**. Báo cáo bỏ chúng là báo cáo quốc tế viết bằng khuôn nội địa.

---

## 9. SCHEMA MÃ THỊ TRƯỜNG — dùng trong cột `market`

```
AU · US · CA · UK · NZ · DE · CZ
AE · SA · KW · QA                  (GCC)
KH · LA · MM · ID · PH · MY · IN · SG · TH
JP · KR · TW · CN-HK
VN-EXPAT                            (TT-D — người nước ngoài đang ở VN)
VN-DIASPORA-<mã nước>               (TT-B — vd VN-DIASPORA-AU, VN-DIASPORA-US)
```

⛔ Dùng đúng bộ mã này, **giống `Agent-AdsOptimize-Kangnam-QT`**. Đặt mã riêng là tự cắt đường đối chiếu giữa inbox và bộ từ khoá.

---

## 10. TỰ KIỂM SỔ NÀY

- [ ] Mỗi hội thoại có `tt` và `ngon_ngu` chưa? `TT-0` chiếm bao nhiêu %? Vượt 20% đã đẩy thành việc chưa?
- [ ] Có tầng nào dưới 10 HT mà vẫn được kết luận riêng không?
- [ ] Có con số trung bình toàn kỳ nào đứng một mình, không kèm phân rã theo tầng không?
- [ ] Có HT nào đến **ngoài giờ 8–17 ICT** mà bị chấm `✗` ở `N1.1` không?
- [ ] Có so chéo SLA giữa hai kênh khác cơ chế không?
- [ ] Có gán nguồn ads cho kênh **không truy được** không?
- [ ] Có chỗ nào agent **tự nêu số ngày ở lại Việt Nam** không?
- [ ] Bốn bảng cắt ở §8 có đủ trong tab Phễu không?

---
