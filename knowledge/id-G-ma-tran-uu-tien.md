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
