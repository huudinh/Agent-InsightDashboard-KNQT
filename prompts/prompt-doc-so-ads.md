# prompt-doc-so-ads · đọc số quảng cáo quốc tế & nối với hội thoại

---

```
ĐỌC SỐ ADS QUỐC TẾ

FILE ADS: <tên file>  ·  CÓ CỘT `market`? <có / không>
FILE GOOGLE ADS: chưa có
KỲ: <tu> → <den>  ·  KỲ TRƯỚC: <...>

Theo id-E, làm sáu việc:

① ★ KIỂM CƠ CẤU THỊ TRƯỜNG TRƯỚC MỌI KẾT LUẬN
   Chi theo từng market / tầng, và so với kỳ trước.
   ⚠ Chuyển chi từ KH sang AU thì CPM tăng, CPL tăng, mà KHÔNG có gì xấu đi —
     đó là một QUYẾT ĐỊNH NGÂN SÁCH, không phải một sự cố.
   ⛔ Thiếu cột `market` → ⛔ KHÔNG gán số cho tầng nào. Ghi "⚠ số ads chưa cắt
     theo thị trường — chỉ đọc được ở mức tổng" và đẩy "xin bản xuất có cột
     market" lên mục việc hệ thống.

② CHUỖI CHỈ SỐ — giữ ĐÚNG thứ tự
   Chi → CPM → CTR → CPI → CPL → CPB → ★ CPA-KHÁM (chi / khách ĐÃ ĐẾN KHÁM)
   Mỗi mắt xích ba thứ: giá trị · so MỤC TIÊU (TB 30 ngày của CHÍNH THỊ TRƯỜNG
   đó) · so KỲ TRƯỚC. Chưa có mốc → "⚠ chưa có mốc so sánh", ⛔ không tự đặt.
   Ngày dưới 3 kết quả → ⛔ không vẽ lên đường CPB/CPL.
   ★ TT-B/TT-C: độ trễ lead → khám là 4–12 TUẦN →
     · ⛔ không đánh giá trong cửa sổ ngắn hơn 8 tuần
     · ⛔ không đặt CPL của kỳ này cạnh CPA-KHÁM như thể chúng nói về cùng một tệp
     · ghi rõ: "CPL của kỳ này · CPA-KHÁM của tệp vào kỳ <cách đây 8–12 tuần>"

③ ★ PHÂN RÃ CPL
   CPL = (CPM/1000) ÷ (CTR × click→inbox% × inbox→lead%)
   Nói rõ thành phần nào xấu đi và đó là việc của ai:
     CTR giảm        → nội dung
     CPM tăng        → Adnet (tệp, bid, lịch) HOẶC ★ đổi cơ cấu thị trường
     click→inbox giảm→ kỹ thuật (điểm đến, lời chào) HOẶC ★ `geo_mode` sai
     inbox→lead giảm → TRỰC KÊNH HOẶC ★ MÚI GIỜ → chỉ ra bao nhiêu HT rơi và vì câu nào
   ⚠ Dấu hiệu `geo_mode` sai, đọc được từ HỘI THOẠI: chiến dịch khai TT-D (expat)
     mà inbox toàn khách hỏi "how many days" và "airport pickup". Phải nói ra.

④ CHẤM TỪNG NỘI DUNG 🟢🟡🔴
   🟢 CTR ≥ trung vị và CPL ≤ trung vị CỦA CÙNG THỊ TRƯỜNG → nhân bản
   🟡 một trong hai đạt → biến thể, đổi ĐÚNG MỘT biến
   🔴 + mã O/OQ vẫn cao → giữ ý, bỏ hook
   🔴 + mã thấp → bỏ hẳn
   ⛔ Không đổi ≥3 biến cùng lúc.
   ★ LUẬT PORT THỊ TRƯỜNG: nội dung 🟢 ở thị trường này ⛔ KHÔNG tự động 🟢 ở
     thị trường khác — khác bộ bằng chứng được phép dùng, khác cách đọc tiếng
     Anh, khác rào cản. Và ⛔ không dịch nội dung tiếng Việt sang EN rồi chạy.

⑤ NỐI HỘI THOẠI ↔ NỘI DUNG
   ★ Chỉ Messenger và click-to-WhatsApp (còn tham số) nối được. Telegram · Viber
   · Line · KakaoTalk · Zalo và WhatsApp khách tự nhắn → "nguồn: tự tìm / chưa
   truy được", ⛔ không chia đều lead của chúng cho các chiến dịch đang chạy.
   ★ IN RA `% inbox truy được về chiến dịch`. Dưới 50% thì mọi câu kiểu "nội dung
   X kéo được 12 inbox" chỉ đúng với phần truy được — phải ghi rõ như thế.
   Mỗi nội dung: market · chân dung · mã O/OQ khách hỏi · % bỏ sau 1 lượt
   · ★ cờ pháp chế THEO THỊ TRƯỜNG.
   Chiến dịch nhiều mẫu không tách được chi → bảng riêng, ⛔ không chia đều.

⑥ NGÂN SÁCH THEO CHẶNG
   % chi theo S1…S7. ★ Luật: S4 tối thiểu 15%, S3 tối thiểu 10%.
   ⚠ S4 chiếm tỷ lệ cao trong INBOX mà ngân sách S4 bằng 0 → ⛔ không phải tin
     xấu về nội dung, đó là CƠ HỘI LỚN NHẤT của kỳ: khách tự tìm tới chặng đó
     mà không ai mời.

⛔ Không so chéo CPL giữa hai thị trường, hoặc hai line khác nhau.
⛔ Không trộn "nhân viên chạy ads" với "nhân viên trực kênh".
⛔ Không trộn VND và USD trong một bảng.
```

---

## Khi Google Ads có dữ liệu

```
ĐỌC GOOGLE ADS
FILE: du-lieu/google-ads.csv

① Chuỗi CPC → CTR → CPL theo chiến dịch × THỊ TRƯỜNG, cùng khuôn với Meta.
② Bảng SEARCH TERM: truy vấn · ngôn ngữ · chi · click · chuyển đổi
   · MÃ O/OQ gán được · ★ CHẶNG S1–S7 · quyết định (giữ / phủ định / mở trang).
③ So kênh: cùng một mã, Meta tốn bao nhiêu và Google tốn bao nhiêu để ra 1 lead.
④ Truy vấn có người tìm mà chưa có trang EN trả lời
   → bàn giao Agent-AdsOptimize-Kangnam-QT (mode GEO-ANSWER).
⑤ ★ Tách riêng nhóm TRUY VẤN CHẶNG S4: "how many days in vietnam after
   rhinoplasty" · "english speaking surgeon hanoi" · "visa for medical treatment
   vietnam" — nhóm ít cạnh tranh nhất và ít ai trả lời nhất trong cả phễu.
```
