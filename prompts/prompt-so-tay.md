# prompt-so-tay · viết sổ tay thực thi cá nhân hoá

> Chạy `python tools/so_tay.py --ky …` trước để có khung đã điền phần đếm được, rồi dùng prompt này điền phần đọc hiểu.

---

```
VIẾT SỔ TAY THỰC THI QUỐC TẾ

KỲ: <tu> → <den>
KHUNG ĐÃ SINH: out/so-tay/

Theo id-I, điền mọi chỗ «agent điền: …» trong từng file.

LUẬT MỘT VIỆC:
  loại D : ĐÚNG MỘT việc
  loại C : tối đa HAI việc
  loại B : ĐÚNG MỘT việc (nhóm yếu nhất)
  loại A : MỘT việc nâng cấp + 2 đoạn chat mẫu để chia sẻ cho khối
★ Việc được chọn là nhóm N MẤT NHIỀU ĐIỂM NHẤT, ⛔ không phải nhóm dễ sửa nhất.
★ Sổ tay 7 việc là sổ tay 0 việc.

★★ LUẬT THÊM CỦA BẢN QUỐC TẾ — ⛔ KHÔNG VIẾT VIỆC MÀ HỆ THỐNG ĐANG CHẶN
   Trước khi viết một việc, chạy phép thử rào ③ của id-F §7:
   "nếu người giỏi nhất khối ngồi vào đúng hội thoại này, với đúng những gì
    hệ thống đang cấp, họ có làm được khác không?"
   Không → đó KHÔNG phải việc của người này. Nó đi vào ST-TN mục 5 và vào mục
   "việc hệ thống" của dashboard.
   ⛔ Viết "lần sau nhớ trả lời khách số ngày ở lại" vào ST-CN là viết một việc
      KHÔNG LÀM ĐƯỢC — và sổ tay có một việc không làm được thì cả sổ mất uy tín.

MỖI VIỆC PHẢI CÓ ĐỦ BỐN THỨ:
  ① viết như một HÀNH ĐỘNG, không phải một phẩm chất
  ② bằng chứng: 2 hội thoại CỦA CHÍNH NGƯỜI ĐÓ, kèm HT-nnn và nguyên văn
  ③ câu mẫu DÙNG ĐƯỢC NGAY: 2 câu ✅ và 1 câu ⛔ đang dùng kèm lý do hỏng
     ★ SONG NGỮ EN/VI nếu người đó trực cả hai ngôn ngữ
  ④ cách đo ở kỳ sau: tiêu chí N nào, từ bao nhiêu % lên bao nhiêu %

VIẾT VIỆC THẾ NÀO:
  ⛔ "Cần chủ động hơn"
  ✅ "Sau khi khách im 30 phút (trong giờ), nhắn lại một câu hỏi về tình trạng"
  ⛔ "Chú ý múi giờ"
  ✅ "Khi hỏi giờ gọi, hỏi luôn múi giờ: 'what time works for you, and which
      time zone?'"
  ⛔ "Cần nắm thông tin quốc tế"
  ✅ "Câu đầu tiên sau lời chào: 'May I ask which country you're messaging from?'"
  ⛔ "Trả lời khách kỹ hơn về bảo hành"  ← ⛔ KHÔNG VIẾT: đang chờ T&C
★ Mỗi việc phải kiểm được bằng ctrl-F trong hội thoại kỳ sau.

PHẦN "KHÁCH CỦA BẠN LÀ AI":
  chân dung gặp nhiều nhất (mã + tên của kỳ này) · tầng · mã O/OQ cao nhất
  · RÀO CHỐT · CÂU HỎI NGẦM · ★ RÀNG BUỘC CHUYẾN ĐI của tệp đó
  · ba câu trả lời sẵn, ĐÚNG NGÔN NGỮ của họ (⛔ không chạm O-07, O-12, OQ-01, OQ-04)

★★ MỤC 6 CỦA ST-CN — "VIỆC KHÔNG PHẢI CỦA BẠN" — ⛔ KHÔNG ĐƯỢC BỎ
   Liệt kê những ô dữ liệu còn trống đang chặn hội thoại của chính người này,
   kèm AI ĐANG CẤP. Vì sao bắt buộc: trực kênh quốc tế mỗi ngày gặp những câu
   mình không có đáp án; không nói rõ ra thì người giỏi sẽ TỰ NGHĨ RA MỘT CON SỐ
   — và đó đúng là cách cờ đỏ CĐ-5 xuất hiện.

★ ST-TN phải có đủ: mục 5 (BẢY nhóm lỗi hệ, kèm ai cấp) và mục 6 (LỊCH TRỰC
  THEO MÚI GIỜ — việc của lịch, ⛔ không của người).
★ ST-ND phải có đủ: mục 5 (ô CHỜ DỮ KIỆN — ⛔ Content không nhận làm) và
  mục 6 (cờ pháp chế HAI TẦNG + dòng xác nhận R8).

⛔ KIỂM TRƯỚC KHI PHÁT:
  [ ] Sổ của người này có chứa tên/điểm/hội thoại của người khác không?
  [ ] Lỗi hệ có bị viết thành việc của nhân viên không? (chạy phép thử rào ③)
  [ ] Câu "Điểm dùng để phân việc kèm cặp…" có ở đầu mọi ST-CN không?
  [ ] ST-CN có mục 6 "việc không phải của bạn" chưa?
  [ ] Còn chỗ «agent điền» nào chưa viết không?
  [ ] Còn cờ 🔴 nào chưa gỡ ở BẤT KỲ TẦNG PHÁP LÝ nào không? R8 đã xác nhận chưa?
      (CỔNG 2 — id-K §9)

NHỊP PHÁT: trưởng nhóm trước → từng nhân viên bản RIÊNG → người làm nội dung
→ ★ Điều phối QT + Vận hành (bản trích mục việc hệ thống + lịch trực theo múi giờ).
⛔ Không phát ST-CN vào nhóm chat chung.
⛔ Không đính kèm nhiều ST-CN trong một file.
```
