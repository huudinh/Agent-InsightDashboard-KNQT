# prompt-ma-tran · dựng ma trận ưu tiên (CỔNG 1)

---

```
DỰNG MA TRẬN ƯU TIÊN QUỐC TẾ

KỲ: <tu> → <den>

Theo id-G, dựng BỐN khối ĐÚNG THỨ TỰ:

① TĂNG HOT        tập: HT WARM đạt 3/5 tín hiệu (thường thiếu ② cửa sổ chuyến đi
                  hoặc ⑤ khung giờ gọi kèm múi giờ)
★② MỞ CHẶNG S4    tập: HT chạm mã OQ-01…OQ-07 mà bốn câu của rào XA chưa được
                  trả lời đủ (id-D §6.1)
③ GIẢM COLD       tập: HT COLD của CD0 + HT ở TT-0 + HT tin đầu chỉ hỏi giá/địa chỉ
④ TỐI ƯU WARM     tập: HT WARM đạt 2/5, có mã O rõ

★ Vì sao khối S4 đứng thứ hai, trước cả GIẢM COLD: khách ở khối đó ĐÃ VƯỢT QUA
  SỢ VÀ NGỜ. Họ muốn làm. Họ chỉ đang tính xem chuyến đi có chạy được không.
  Mất họ ở đây là mất khách ĐẮT NHẤT trong cả phễu — và việc ở đây thường RẺ
  NHẤT: một dữ kiện + một câu trả lời mẫu, không cần sản xuất nội dung mới.

Mỗi dòng một chân dung **đã duyệt ở CỔNG 0** (⛔ không tự thêm chân dung), các cột:
  CD · tên · ★ TẦNG (đúng một) · HT mới · HT trong tập · có liên hệ
  · hệ số giá trị đơn · ĐIỂM · chặng · ★ câu XA chưa trả lời
  · ★ DỮ KIỆN ĐỦ? · hướng nội dung (một câu, cụ thể) · chọn hay không · ưu tiên

ĐIỂM = Σ (lead bỏ lỡ × hệ số giá trị đơn)
  hệ số theo /price-list/: <20tr = 1 · 20–50tr = 2 · ≥50tr = 3 · chưa nêu dịch vụ = 1 ⚠
  ★ LUẬT COMBO: dịch vụ giá thấp (cắt mí đơn lẻ · da liễu · clinic) cho TT-A/B/C
    → hệ số TỐI ĐA 1, và chỉ được xếp vào cụm combo / cross-sell, ⛔ không mở
    tuyến riêng. ⛔ Không ai bay 6 giờ để cắt mí. Với TT-D thì ngược lại: lõi.
  ⛔ BA HỆ SỐ KHÔNG ĐƯỢC TỰ ĐẶT: hệ số tầng ("TT-C × 1,5") · hệ số mùa
     · hệ số tiềm năng. Giá trị tầng ĐÃ nằm trong hệ số dịch vụ và trong số
     lead bỏ lỡ — nhân hai lần là phá luật ⑪.

★ LUẬT MỘT TẦNG MỘT Ô: mỗi ô khai ĐÚNG MỘT tầng chính. Ô trải trên nhiều tầng
  → TÁCH thành hai ô, hoặc chọn tầng đông hơn và ghi tầng còn lại ở 👁 QUAN SÁT.
  Vì sao: khác bộ bằng chứng được phép dùng · khác ngôn ngữ · khác rào cản.

BỐN NHÓM KẾT LUẬN:
  ✅ ĐƯỢC CHỌN            điểm cao nhất trong khối, ≥5 HT mới, VÀ dữ kiện đã đủ
  🔧 SỬA VẬN HÀNH TRƯỚC   ≥50% HT của ô rơi do TRỰC KÊNH
                          → ⛔ KHÔNG làm nội dung
  ★⏸ CHỜ CẤP DỮ KIỆN      ô điểm cao nhưng câu trả lời phụ thuộc một ô dữ liệu
                          còn trống → ⛔ KHÔNG vào kế hoạch nội dung.
                          Mỗi dòng ghi: dữ kiện trống · AI CẤP · chặn bao nhiêu
                          HT · chặn mã/tiêu chí nào.
  👁 QUAN SÁT             <5 HT mới

★ Phân biệt ✅ và ⏸ là việc có giá trị nhất của bảng này. Trộn chúng lại thì
  kế hoạch nội dung kỳ sau có những việc KHÔNG AI LÀM ĐƯỢC, và hai kỳ sau
  chúng vẫn nằm đó rồi bị gạch — mà không ai biết nó chưa bao giờ là việc
  của Content.

SỐ Ô TỐI ĐA: ① 2 · ★② 3 · ③ 2 · ④ 1. ⛔ Quá 8 ô thì không ô nào làm tử tế.
Nhóm 🔧 không giới hạn, nhưng MỖI VIỆC PHẢI CÓ MỘT NGƯỜI TÊN THẬT.
Nhóm ⏸ không giới hạn, nhưng MỖI DÒNG PHẢI CÓ AI CẤP + SỐ HT BỊ CHẶN.

In xong ghi:
TRẠNG THÁI: ⏳ CHỜ DUYỆT
và dừng. ⛔ Không viết hook. ⛔ Không sinh sổ tay.
```

---

## Sửa trước khi duyệt

```
SỬA <mã ô> <hướng mới>
```

## Duyệt

```
DUYỆT
```
Agent ghi `trang_thai: da_duyet` + ai duyệt + ngày duyệt, rồi chạy tiếp B6–B8.
