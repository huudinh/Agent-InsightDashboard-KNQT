# prompt-cham-diem · chấm điểm & phân loại nhân viên trực kênh quốc tế

> ⚠ Đọc `id-F` §1 và §7 trước khi dùng. Prompt này tạo ra một con số gắn với tên một con người.
> ★ Bản quốc tế có **27 tiêu chí** `N1.1`–`N7.6` và **10 cờ đỏ** — và có **bảy nhóm lỗi hệ** mà ⛔ không được trừ điểm người.

---

```
CHẤM ĐIỂM TRỰC KÊNH QUỐC TẾ

FILE HỘI THOẠI: <tên file>
KỲ: <tu> → <den>

Theo id-F, chấm hai tầng:

TẦNG 1 — từng hội thoại, 27 tiêu chí N1.1 … N7.6, mỗi tiêu chí ✓ / ✗ / —
   ✓ có bằng chứng trong hội thoại
   ✗ có bằng chứng là KHÔNG làm hoặc LÀM SAI — phải trích được nguyên văn
   — tình huống không phát sinh, HOẶC hệ thống chưa cấp dữ kiện,
     HOẶC tin đến NGOÀI GIỜ 8–17 ICT
   Điểm = (tổng điểm ✓) ÷ (tổng điểm các tiêu chí không phải "—") × 100

★ BỐN TIÊU CHÍ DỄ CHẤM SAI NHẤT CỦA BẢN QUỐC TẾ:
   N1.1 — chỉ tính tin đến TRONG 08:00–17:00 ICT. Ngoài giờ → "—", và phần
          dọn hộp thư ngoài giờ chấm ở N7.4 (trong 12h), ⛔ KHÔNG ở N1.1.
   N3.1 — giá ĐÃ CÔNG KHAI tại /price-list/ → né giá là LỖI NGƯỜI, ⛔ không
          còn là lỗi hệ (ngược hẳn bản nội địa). Ngoại lệ "—": dịch vụ khách
          hỏi không có trong bảng giá công khai.
   N4.2 — khách hỏi rào XA ("how many days") mà trả lời bằng GIÁ/ƯU ĐÃI = ✗.
   N7.6 — ⛔ KHÔNG đo "có biết số ngày hay không" (không ai biết, chưa ai cấp).
          Đo CÁCH XỬ LÝ: nói "bác sĩ xác nhận sau khám" + hẹn trả lời lại = ✓;
          tự nêu một con số = ✗ và là cờ đỏ CĐ-5; im lặng/lái sang giá = ✗.

TẦNG 2 — từng nhân viên
   Điểm = trung bình điểm các hội thoại của người đó
   Phân loại A ≥85 · B 70–84 · C 55–69 · D <55
   ⛔ Dưới 10 hội thoại: KHÔNG cho điểm tổng, KHÔNG phân loại. Ghi "chưa đủ mẫu".
   ⚠ Inbox quốc tế cỡ mẫu nhỏ là BÌNH THƯỜNG — ⛔ không hạ ngưỡng xuống 5 để
     "có bảng cho đẹp".
   Một cờ đỏ → trần 49 điểm cho hội thoại đó, và người đó ⛔ không được xếp loại A.

IN RA BẢY KHỐI:
① PHÂN BỐ        A/B/C/D + số người chưa đủ mẫu
② CHỈ SỐ ĐỘI     % đạt từng nhóm N1…N7 và từng tiêu chí
③ BẢNG CÁ NHÂN   tên · số HT · điểm · loại · tầng trực nhiều nhất · ngôn ngữ
                 · nhóm yếu nhất · nhóm mạnh nhất
                 ⛔ Khối này CHỈ vào sổ tay riêng và bản trưởng nhóm.
④ CỜ ĐỎ          mã · ai · HT-nnn · NGUYÊN VĂN câu nói · người xử lý đích danh
                 ★ Nêu riêng CĐ-5 · CĐ-7 · CĐ-9: ba cờ người ta cắm vào khi
                   ĐANG CỐ GIÚP KHÁCH → phải vào đào tạo, không chỉ vào sổ cá nhân.
⑤ ★ VIỆC HỆ THỐNG  các ô "—" do lỗi hệ, GOM THEO BẢY NHÓM của id-F §7 rào ③:
                 số ngày ở lại · T&C bảo hành · visa/thanh toán · người trực
                 ngôn ngữ · lịch trực theo múi giờ · dịch vụ ngoài bảng giá ·
                 privacy notice GDPR
                 — mỗi nhóm: số HT bị ảnh hưởng · AI CẤP · chặn mã nào
⑥ BA TIÊU CHÍ YẾU NHẤT CỦA KHỐI → nội dung đào tạo 15 phút kỳ sau
⑦ ★ CẮT THEO TẦNG  % đạt N4.2 và nhóm N7 theo TT-A/B/C/D (chỉ tầng ≥10 HT)
                 ⚠ Chênh lệch giữa các tầng thường là chênh lệch về DỮ KIỆN SẴN CÓ,
                   ⛔ không phải về năng lực.

BỐN RÀO AN TOÀN — kiểm lại trước khi trả lời:
① Mọi ✗ có HT-nnn + nguyên văn chưa? Không có thì đổi thành "—".
② ★ PHÉP THỬ RÀO ③ cho từng ô ✗: "nếu người giỏi nhất khối ngồi vào đúng hội
   thoại này, với đúng những gì hệ thống đang cấp, họ có làm được khác không?"
   Không → ô đó phải là "—".
③ "—" có bị cộng vào mẫu số không?
④ Có bảng xếp hạng cá nhân nào nằm ngoài sổ tay riêng không?

Chân mọi bảng điểm phải có câu:
"Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai."
```

---

## Chấm một người

```
CHẤM RIÊNG: <tên nhân viên>
Liệt kê từng hội thoại của người này: HT-nnn · tầng · ngôn ngữ · trong giờ/ngoài giờ ICT
· chân dung (bỏ trống nếu chưa qua CỔNG 0) · 27 ô ✓/✗/— · điểm
· câu đáng chú ý (một câu làm tốt, một câu làm hỏng, NGUYÊN VĂN, giữ nguyên ngôn ngữ).
★ Cuối bảng: liệt kê riêng những ô "—" do HỆ THỐNG, kèm ai cấp — đó là phần
sẽ vào mục 6 "việc không phải của bạn" trong sổ tay của người này.
```
