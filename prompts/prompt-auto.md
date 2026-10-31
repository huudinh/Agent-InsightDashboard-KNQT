# prompt-auto · chạy cả kỳ một phát

> Dán vào Claude/ChatGPT/Gemini đã nạp bộ não + 12 sổ tri thức. Đính kèm file hội thoại và file ads.
> ⚠ `AUTO` đi qua **hai cổng duyệt**: CỔNG 0 duyệt chân dung, CỔNG 1 duyệt ma trận. Nó dừng ở cả hai.
> ★ Và trước đó còn **CỔNG M**: không khai được tầng thị trường thì ⛔ không kết luận gì.

---

```
AUTO

KỲ: <tu> → <den>
FILE HỘI THOẠI: <tên file đính kèm>
FILE ADS (có cột `market`?): <tên file · có/không có cột market, hoặc "chưa có">
FILE GOOGLE ADS: chưa có
KỲ TRƯỚC: <tên file kết quả kỳ trước, hoặc "chưa có">
R8 — đủ điều kiện KCB cho người nước ngoài: <đã xác nhận / chưa>

CHẶNG 1 — chạy B1 → B3 theo id-A §3, rồi DỪNG ở CỔNG 0.

In ra đúng năm khối:

① CỠ MẪU
   đọc bao nhiêu · loại bao nhiêu · vì sao loại
   ★ + bao nhiêu HT là KHÁCH NỘI ĐỊA NHẮN LẠC vào kênh quốc tế (đã loại,
     ⛔ không xếp vào TT-B)

② ★ BẢNG THỊ TRƯỜNG — CỔNG M
   TT-A / TT-B / TT-C / TT-D / TT-0: số HT · % mẫu · ngôn ngữ chính · market
   + CĂN CỨ SUY từng nhóm (khai sẵn · khách tự nói · suy từ chữ · suy từ kênh)
   + bảng NGÔN NGỮ khách × ngôn ngữ nhân viên trả lời
   + bảng KÊNH (ghi rõ kênh nào ⛔ không truy được về chiến dịch)
   + bảng MÚI GIỜ: trong giờ / ngoài giờ 8–17 ICT · chờ TB · số HT mất quá 12h
   ⚠ TT-0 ≥ 20% mẫu → nói thẳng rằng mọi tỷ lệ bên dưới đọc với độ tin thấp,
     và chờ tôi xác nhận bảng này trước khi kết luận.

③ SÁU THẺ SỐ TỔNG
   hội thoại mới · bỏ sau 1 lượt · có cách liên hệ · trả lời tin đầu ≤5′ (trong giờ)
   · HOT/WARM chưa có liên hệ · ★ S4 CHƯA ĐÓNG
   mỗi thẻ kèm so kỳ trước (hoặc "⚠ chưa có mốc so sánh")

④ NGUYÊN LIỆU PHÁC HỌA
   cụm chữ khách tự nói — ★ TÁCH RIÊNG theo ngôn ngữ (đếm theo SỐ HỘI THOẠI)
   · phân bố chặng S1–S7 · phân bố bốn rào chốt · phân bố rào cản
   · 10 câu hỏi đầu đáng chú ý nhất, GIỮ NGUYÊN NGÔN NGỮ, đã ẩn danh, kèm HT-nnn

⑤ BẢN PHÁC HỌA CHÂN DUNG — ⏳ CHỜ DUYỆT
   2–7 chân dung, mỗi chân dung: mã · tên (CHỮ CỦA KHÁCH, nguyên ngôn ngữ)
   · họ là ai · NỖI SỢ · dấu hiệu nhận ra
   · ★ TẦNG CHÍNH · ★ RÀO CHỐT (đúng một trong SỢ/NGỜ/NGẠI/XA)
   · ★ RÀNG BUỘC CHUYẾN ĐI · hệ số giá trị đơn · HT-nnn làm bằng
   + số HT dự kiến rơi CD0, và nói rõ còn tách thêm được chân dung nào không
   + chân dung nào GIỮ NGUYÊN MÃ của kỳ trước vì cùng nỗi sợ
   ⛔ Không gán QT1–QT7 của Agent-AdsOptimize-Kangnam-QT.

⛔ DỪNG tại đây. ⛔ Không gán chân dung. ⛔ Không viết thẻ insight.
⛔ Không dựng ma trận. ⛔ Không chấm điểm cá nhân. ⛔ Không tự điền người duyệt.
Chờ tôi gõ DUYỆT CHÂN DUNG.
```

---

## Sau khi xem bản phác họa

```
DUYỆT CHÂN DUNG
```
hoặc
```
SỬA CD<n> <điều chỉnh>
```

Rồi agent chạy chặng 2:

```
CHẶNG 2 — chạy B3' → B5, rồi DỪNG ở CỔNG 1.

In ra đúng năm khối:

⑥ BẢNG CHÂN DUNG ĐÃ DUYỆT (+ dòng CD0)
   HT · tầng · rào chốt · HOT/WARM/COLD · có liên hệ · % có liên hệ · chốt lịch
   · bỏ 1 lượt · rơi do trực kênh · ★ S4 chưa đóng
   ★ Tổng HT + CD0 phải BẰNG ĐÚNG cỡ mẫu phân tích
   + thẻ insight cho mỗi chân dung ≥5 HT (họ là ai · insight · câu hỏi ngầm ·
     tín hiệu nóng · rào chốt · hướng xử lý) — viết bằng CHỮ CỦA KHÁCH
   + ma trận CD×S7 hai bảng N×7 — ★ XEM CỘT S4 TRƯỚC, đánh dấu ô ① và ô ③
   + ★ ma trận CD×TT một bảng N×5

⑦ ★ BẢNG S4 CHƯA ĐÓNG
   với từng câu của rào XA (số ngày ở lại · ai lo khi về · ai trả phí sửa · ngôn ngữ):
   bao nhiêu HT hỏi · bao nhiêu HT được trả lời đủ · còn lại là gì
   ⚠ Nói rõ câu nào ⛔ KHÔNG AI TRẢ LỜI ĐƯỢC vì thiếu dữ kiện gốc.

⑧ BA VẤN ĐỀ CỐT LÕI
   xếp theo SỐ HỘI THOẠI BỊ ẢNH HƯỞNG, mỗi vấn đề: mức · số liệu · đề xuất · ai làm
   ★ Mỗi vấn đề phải nói rõ nó là lỗi NỘI DUNG · TRỰC KÊNH · hay HỆ THỐNG
     (dữ kiện / múi giờ / ngôn ngữ).

⑨ CHUỖI CHỈ SỐ ADS (nếu có file)
   Chi → CPM → CTR → CPI → CPL → CPB → ★ CPA-KHÁM, mỗi mắt xích kèm mục tiêu + kỳ trước
   ★ + bảng cắt theo THỊ TRƯỜNG. Thiếu cột `market` → ⛔ không gán cho tầng nào.
   ⛔ Phân rã CPL TRƯỚC khi kết luận, và ★ kiểm CƠ CẤU THỊ TRƯỜNG trước cả bốn
      thành phần. Nếu thành phần hỏng không phải CTR thì nói thẳng "kỳ này
      không phải vấn đề nội dung".
   ⚠ TT-B/TT-C: ⛔ không kết luận trong cửa sổ ngắn hơn 8 tuần.

⑩ MA TRẬN ƯU TIÊN — BỐN khối, đúng thứ tự:
   ① Tăng HOT → ★② MỞ CHẶNG S4 → ③ Giảm COLD → ④ Tối ưu WARM
   + nhóm 🔧 sửa vận hành trước
   + ★ nhóm ⏸ CHỜ CẤP DỮ KIỆN (ghi ai cấp + chặn bao nhiêu HT + chặn mã nào)
   + nhóm 👁 quan sát
   ★ Mỗi ô khai ĐÚNG MỘT TẦNG.
   TRẠNG THÁI: ⏳ CHỜ DUYỆT

⛔ DỪNG tại đây. ⛔ Không viết hook. ⛔ Không sinh sổ tay. ⛔ Không chấm điểm cá nhân.
Chờ tôi gõ DUYỆT.
```

---

## Sau khi xem ma trận

```
DUYỆT
```
hoặc
```
SỬA <mã ô> <hướng mới>
```

Rồi agent chạy tiếp B6 → B8: chấm điểm `N1–N7` · sinh dashboard JSON · ngân hàng hook (có tầng + ngôn ngữ) · sổ tay từng người (có mục *"việc không phải của bạn"*) · soát **CỔNG 2 hai tầng pháp lý** + in dòng xác nhận **`R8`**.
