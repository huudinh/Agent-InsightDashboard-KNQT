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

## 4b. ★★ KHUÔN BA NHỊP · VÀ TRẠNG THÁI DUYỆT GẮN TRÊN TỪNG CÂU

### Khuôn ba nhịp

Mọi hook, và mọi **câu mẫu** trong sổ tay (`id-I` §3 phần 2), viết theo đúng ba nhịp:

```
<điều khách sợ, BẰNG CHỮ CỦA KHÁCH>  →  <điều mình làm khác>  →  <bằng chứng>
```

| Phải có | ⛔ Phải KHÔNG có |
|---|---|
| Một `HT-nnn` truy ngược được | Con số bảo hành *(đang có ba mức cùng lưu hành)* |
| **Chữ khách dùng**, ⛔ không phải tính từ | Cam kết kết quả chắc chắn |
| Một điều **mình làm khác được** | Testimonial kết quả lâm sàng *(🔴 chặn ở `TT-C`)* |
| Qua **CỔNG 2 hai tầng** trước khi phát | Giá chưa có trong bảng `/price-list/` hiện hành |

> ★ **Viết bằng chữ của khách.** Khách ⛔ không tìm *"natural-looking result"* — khách viết *"my nose tip is shiny and red"*. Khách ⛔ không tìm *"world-class surgeon"* — khách viết *"how do I know who actually operates on me"*.

★ **Ví dụ đủ ba nhịp**, cho rào `XA` / `OQ-01`:
> *"Is it safe to fly more than 15 hours on day 14?"* **→** bác sĩ xác nhận mốc bay **sau khám**, và khách có **kênh liên lạc sau khi về nước** **→** `[CHỜ CẤP: số ngày ở lại — Khoa Chuyên môn]`. *(`HT-021`)*

⚠️ Ví dụ trên **chưa phát được** — nhịp ③ còn là một ô chờ cấp. Đó là đúng: một hook thiếu nhịp ③ thì ⛔ **không được làm tròn bằng một câu nghe hay**.

```
Thiếu nhịp ③ → câu đó chỉ là lời hứa.
Thiếu nhịp ① → nó là lời người bán.
Thiếu nhịp ② → ⛔ không có gì để khách chọn mình.
```

### ★ Trạng thái duyệt — gắn trên TỪNG CÂU, ⛔ không gắn theo cả tuyến

```
✅ «đã duyệt»                      → phát được
🟠 «đề xuất – chưa duyệt»          → ⛔ KHÔNG phát ra ngoài
🟠 «chờ pháp chế duyệt»            → ⛔ KHÔNG phát ra ngoài
🟠 «chỉ dùng được ở TT-A / TT-B»   → ★ riêng bản quốc tế, xem dưới
⏸ «chờ dữ kiện <ô>»               → ⛔ chưa viết được, ghi rõ chờ ô nào
```

⚠️ **Một tuyến nội dung có thể gồm câu đã duyệt và câu chưa duyệt.** Duyệt theo tuyến là cách để một câu 🟠 đi ra ngoài dưới vỏ một tuyến 🟢. Trạng thái nằm trên **từng câu**.

### ★★ Và ở bản quốc tế, trạng thái duyệt có **hai tầng**

> Một câu **sạch theo luật Việt Nam vẫn có thể bị chặn ở nước người xem.** Nên trạng thái duyệt của một hook ⛔ không phải một ô — nó là **hai ô**.

| | Tầng VN | Tầng nước người xem |
|---|---|---|
| Ai soát | Pháp chế VN | Theo bảng `id-K` §4 |
| Ví dụ chặn riêng tầng ② | — | Testimonial kết quả lâm sàng: hợp ở `TT-A`, 🔴 **cấm ở AU (AHPRA)** |
| Kết luận | Cả hai ✅ → phát | Một bên 🟠 → ⛔ **không phát ở thị trường đó**, ⛔ không phát ở đâu cả nếu chưa cắt được theo thị trường |

★ Hook ⛔ không cắt được theo thị trường thì lấy **mức chặt nhất** trong các thị trường sẽ thấy nó. ⛔ Không lấy mức trung bình.

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
