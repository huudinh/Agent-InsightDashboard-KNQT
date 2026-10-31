# 03 · Kết quả mẫu — chạy thật trên `template/`

> Số dưới đây là **output thật** của `tools/id.py` trên 8 hội thoại mô phỏng trong [`template/MAU_hoi-thoai.md`](../template/MAU_hoi-thoai.md) và 8 dòng ads trong [`template/MAU_ads-quoc-te.csv`](../template/MAU_ads-quoc-te.csv).
>
> ⚠️ Cỡ mẫu 8 HT thì **⛔ không kết luận gì** (`id-A` §5). Mục đích của trang này là cho thấy **script đọc ra cái gì**, không phải đưa ra kết luận.

```bash
python tools/id.py doc template/MAU_hoi-thoai.md --ky "19-25/10"
python tools/id.py ads template/MAU_ads-quoc-te.csv --ky "19-25/10"
python tools/id.py bao-cao --ky "19-25/10"
```

---

## 1 · Tám thẻ số tổng

| Thẻ | Giá trị |
|---|---|
| Hội thoại phân tích | **8** |
| Bỏ sau 1 lượt | 0,0% |
| Có cách liên hệ | 25,0% |
| Trả lời tin đầu ≤5′ *(chỉ tính 5 HT đến trong giờ ICT)* | 100,0% |
| HOT/WARM chưa có liên hệ | 0 |
| ★ **S4 chưa đóng** | **3** |
| ★ HOT/WARM ngoài giờ chờ >12h | 0 |
| Rơi do trực kênh | 37,5% |

★ **Thẻ `S4 chưa đóng` là thẻ không có ở bản nội địa.** 3/8 hội thoại chạm rào `XA` mà bốn câu của `id-D` §6.1 chưa được trả lời đủ — khách **muốn làm** mà **không đặt được vé**.

---

## 2 · Tầng thị trường — CỔNG M

| Tầng | Tên | Market | HT | % mẫu | HOT | Có LH | S4 chưa đóng |
|---|---|---|---|---|---|---|---|
| `TT-A` | Khu vực lân cận | KH · PH | 2 | 25,0% | 0 | 0 | 1 |
| `TT-B` | Kiều bào | VN-DIASPORA-US | 1 | 12,5% | 1 | 1 | 0 |
| `TT-C` | Thị trường phát triển | AU · UK · US · AE | 4 | 50,0% | 0 | 0 | 1 |
| `TT-D` | Expat tại VN | VN-EXPAT | 1 | 12,5% | 0 | 1 | 1 |
| `TT-0` | Chưa khai được | — | 0 | 0,0% | 0 | 0 | 0 |

**Căn cứ suy:** khai sẵn 8 *(file mẫu có đủ dòng `_Kênh: … · Nước: … · Ngôn ngữ: …_`)*.

⚠️ Mọi tầng ở đây **dưới 10 HT** → dashboard hiện `⚠ MẪU NHỎ` thay cho tỷ lệ, và ⛔ không kết luận riêng cho tầng nào (`id-A` §5).

★ Nếu file không khai `Nước:` thì cột *căn cứ suy* sẽ phân thành *khách tự nói · suy từ chữ · suy từ kênh ⚠* — và `TT-0 ≥ 20%` sẽ **dừng ở CỔNG M**.

---

## 3 · Múi giờ · kênh · chặng · rào chốt

```
MÚI GIỜ   trong giờ 5 · ngoài giờ 3 (37,5%) · chờ TB 10,8 h · mất >12h: 1
KÊNH      WhatsApp 4 · Messenger 2 · Zalo 1 (⛔ không truy được ads)
                                   · Telegram 1 (⛔ không truy được ads)
CHẶNG     S2 1 · S3 1 · S4 4 · S5 1 · chưa rõ 1
RÀO CHỐT  SỢ 0 · NGỜ 1 · NGẠI 0 · XA 6
```

★ **Hai dòng đáng đọc nhất:**

- `XA 6/8` — rào quyết định của bản quốc tế chiếm phần lớn mẫu. Đây là rào **cuối cùng**: khách đã vượt Sợ, Ngờ, Ngại rồi mới chạm vào nó.
- `ngoài giờ 3/8 · 1 HT mất quá 12h` — và cả 3 HT ngoài giờ đều thuộc `TT-C`. Đây là **việc của lịch trực**, ⛔ không của nhân viên (`id-L` §4).

⚠️ `Zalo` và `Telegram` ⛔ **không truy được về chiến dịch** → ⛔ không gán nguồn ads cho chúng (`id-E` §6).

---

## 4 · Vì sao rơi — ba nhánh hệ thống

```
trực kênh 3 · không rơi 2 · hệ thống — dữ kiện 2 · hệ thống — múi giờ 1
```

★ Bản nội địa có **một** nhánh `hệ thống`. Bản này tách **ba** vì **ba người khác nhau sửa**: dữ kiện *(Khoa Chuyên môn · Pháp chế · Điều phối QT)* · múi giờ *(lịch trực)* · ngôn ngữ *(vận hành)*.

---

## 5 · ★ Tám mã OQ — kèm trạng thái chặn

| Mã | HT | % mẫu | Trạng thái |
|---|---|---|---|
| `OQ-01` số ngày ở lại | 2 | 25,0% | 🔴 **CHẶN** — chưa có số *(Khoa Chuyên môn)* |
| `OQ-02` ai lo khi về nước | 0 | 0,0% | 🟠 thiếu thời hạn + kênh |
| `OQ-03` phiên dịch | 2 | 25,0% | 🟠 chưa khai ngôn ngữ nào · có phí không |
| `OQ-04` ai trả phí chỉnh sửa | 1 | 12,5% | 🔴 **CHẶN** — chưa có T&C bảo hành |
| `OQ-05` visa | 1 | 12,5% | 🟠 không thấy trên site |
| `OQ-06` thanh toán | 0 | 0,0% | 🟠 không thấy trên site |
| `OQ-07` khách sạn / đưa đón | 0 | 0,0% | 🟢 có nêu — xác nhận phí |
| `OQ-08` halal / riêng tư | 1 | 12,5% | 🟠 chưa khai gồm những gì |

★ **Bốn mã có mặt trong mẫu, ba trong số đó đang bị chặn.** Trực kênh né những câu này phần lớn là **lỗi hệ** → chấm `—`, ⛔ không trừ điểm người.

### S4 chưa đóng — phân rã theo bốn câu

| Câu của rào XA | HT chưa được trả lời đủ |
|---|---|
| ③ Ai trả chi phí nếu phải chỉnh sửa? | 1 |
| ④ Có ai nói được tiếng của tôi? | 2 |

---

## 6 · Chấm điểm — bảy nhóm

| Nhóm | Điểm tối đa | % đạt |
|---|---|---|
| `N1` Phản hồi & SLA | 15 | 82,6% |
| `N2` Khai thác tình trạng & bối cảnh | 18 | 34,5% |
| `N3` Trả lời đúng & minh bạch | 20 | 85,7% |
| `N4` Xử lý rào cản | 15 | 52,4% |
| `N5` Xin liên hệ & chốt | 17 | **9,4%** |
| `N6` Ngôn từ & thái độ | 5 | 100,0% |
| ★ `N7` Năng lực quốc tế | 10 | 75,0% |

**Phân bố:** `chưa đủ mẫu: 4` — ⛔ không ai được phân loại A/B/C/D, vì không ai đủ 10 hội thoại (`id-F` §6).

⚠️ `N5` thấp nhất là đúng với dữ liệu mẫu: gần như không hội thoại nào hỏi **khung giờ kèm múi giờ** — tiêu chí `N5.3`. Đây là tiêu chí trượt nhiều nhất của bản quốc tế, và nó sửa được ngay bằng **một câu**.

---

## 7 · ★ Bốn cờ đỏ — và vì sao chúng đáng chú ý

| Cờ | Ai | HT | Nguyên văn |
|---|---|---|---|
| `CĐ-5` | Mai P | HT-001 | *"you can fly after 7"* |
| `CĐ-7` | Mai P | HT-001 | nêu giá mà không nêu phụ phí quốc tế 10% |
| `CĐ-2` | Lan T | HT-003 | *"lifetime warranty"* |
| `CĐ-4` | Lan T | HT-003 | *"board certified"* |

★★ **Ba trong bốn cờ này là cờ chỉ có ở bản quốc tế** — và `CĐ-5` là cờ nặng nhất:

> Nhân viên nói *"you can fly after 7 days"* vì khách đang **cần một con số để đặt vé**. Đó là một câu nói ra khi **đang cố giúp khách**. Nhưng số ngày được phép bay là **mốc y khoa** — và bay quá sớm sau phẫu thuật là **rủi ro thật**, không phải rủi ro câu chữ.
>
> → Vì vậy `CĐ-5` · `CĐ-7` · `CĐ-9` phải vào **đào tạo cả nhóm**, ⛔ không chỉ vào sổ tay của người cắm cờ (`id-I` §4).

⚠️ `CĐ-7` được script nhận ra bằng **logic**, không bằng từ khoá: có nêu giá mà không nêu phụ phí 10% (`id-F` §3 `N3.2`).

---

## 8 · Số quảng cáo — cắt theo thị trường

```
Chi phí tổng           33.370.000 đ   8 nội dung · 195.100 hiển thị · 236 inbox
                                      · 34 lead · 14 booking · 7 đã khám
CPM                       171.040 đ
CTR                            1,9%
CPI                       141.398 đ
CPL                       981.471 đ
★ CPA-KHÁM             4.767.143 đ   ⚠ cần cửa sổ ≥8 tuần — số của kỳ 2 tuần KHÔNG đọc được
```

| Tầng | Market | Chi | Inbox | Lead | CPL |
|---|---|---|---|---|---|
| `TT-A` | KH | 2.140.000 | 58 | 4 | 535.000 |
| `TT-A` | PH | 1.960.000 | 33 | 3 | 653.333 |
| `TT-B` | VN-DIASPORA-US | 4.410.000 | 28 | 7 | 630.000 |
| `TT-C` | AE | 5.240.000 | 8 | 1 | 5.240.000 |
| `TT-C` | AU | 11.370.000 | 73 | 11 | 1.033.636 |
| `TT-C` | UK | 6.380.000 | 12 | 2 | 3.190.000 |
| `TT-D` | VN-EXPAT | 1.870.000 | 24 | 6 | 311.667 |

★ **Đọc bảng này là lý do CỔNG M tồn tại.** CPL tổng là 981k. Nhưng `VN-EXPAT` là 312k và `AE` là 5.240k — **chênh gần 17 lần**. Một con số trung bình ⛔ không nói về ai cả.

⚠️ Và ⛔ **không so chéo** 312k với 5.240k để kết luận *"nên dồn tiền vào expat"*: khác giá chấp nhận được, khác giá trị ca, khác luật quảng cáo (`id-E` §2).

---

## 9 · Những gì script ⛔ KHÔNG làm

```
⛔ Phác họa chân dung                → id-C §2, agent đọc và viết
⛔ Thẻ insight · câu hỏi ngầm         → id-C §7 · id-D §8
⛔ Hướng nội dung · hook              → id-H
⛔ Câu mẫu trong sổ tay               → id-I §3, mọi chỗ «agent điền: …»
⛔ Phán đoán pháp chế hai tầng        → id-K §4, agent chỉ nêu cơ quan phải tra
⛔ Xác nhận R8                        → điều kiện HOẠT ĐỘNG, do Pháp chế chốt
⛔ Xác nhận CỔNG M khi TT-0 vượt ngưỡng → người dùng xác nhận
```
