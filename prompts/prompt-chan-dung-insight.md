# prompt-chan-dung-insight · phác họa chân dung & đào sâu insight

> Dùng khi chỉ cần phần khách hàng, chưa cần chấm điểm hay ads. Đây là phần **đọc hiểu** — script không làm thay.
> Chạy **hai lượt**, vì **CỔNG 0** nằm giữa: lượt ① phác họa và xin duyệt, lượt ② gán và viết thẻ insight.
> ★ Và trước cả hai lượt là **CỔNG M**: chưa khai được tầng thị trường thì ⛔ chưa phác họa.

---

## Lượt ① — PHÁC HỌA, dừng ở CỔNG 0

```
PHÁC HỌA CHÂN DUNG QUỐC TẾ

FILE HỘI THOẠI: <tên file>
KỲ: <tu> → <den>
KỲ TRƯỚC: <tên file bản phác họa kỳ trước, hoặc "chưa có">

Theo id-C §1–2, làm đúng sáu việc:

① ★ KHAI THỊ TRƯỜNG TRƯỚC — CỔNG M
   Với từng hội thoại: tầng TT-A/B/C/D (hoặc TT-0) · market · ngôn ngữ · kênh
   · trong giờ / ngoài giờ 8–17 ICT, kèm CĂN CỨ SUY (id-B §3).
   ⛔ Ba cách suy SAI: suy từ dịch vụ khách hỏi · suy từ ngôn ngữ một mình ·
      suy từ tên thành phố Việt Nam trong câu (đó là NƠI MỔ, không phải NƠI KHÁCH Ở).
   ⚠ TT-0 ≥ 20% mẫu → in bảng ra và nói rõ: chưa biết khách ở đâu thì mọi kết
     luận sau đó đọc với độ tin thấp. Chờ tôi xác nhận.
   ⚠ Khách nội địa nhắn lạc (tiếng Việt, không nhắc gì đến ở nước ngoài / về
     nước / bay) → LOẠI khỏi mẫu, ⛔ KHÔNG xếp vào TT-B.

② GÁN TỪNG HỘI THOẠI — phần KHÔNG cần chân dung
   chặng S1–S7 (đọc CÂU HỎI ĐẦU TIÊN, ⛔ không đọc cả hội thoại; ★ nhận diện
   S4 TRƯỚC S5) · mã O · ★ mã OQ (quét TOÀN BỘ lời khách, không chỉ ba tin đầu)
   · ★ rào chốt (đúng một trong SỢ/NGỜ/NGẠI/XA) · mức nóng theo 5 tín hiệu
   · rào cản · vì sao rơi (ĐÚNG MỘT giá trị, có ba nhánh hệ thống)
   ⚠ Ô chân dung để TRỐNG ở bước này.

③ ĐỌC CHỮ CỦA KHÁCH
   Cụm chữ nào khách tự nói, lặp ở bao nhiêu HỘI THOẠI (⛔ không đếm số lần).
   ★ TÁCH RIÊNG theo ngôn ngữ — cụm tiếng Anh và cụm tiếng Việt là hai tệp khác nhau.
   ⛔ Cụm đông nhất chưa chắc là một chân dung: "rhinoplasty" là DỊCH VỤ,
      "in vietnam" là ĐIỂM ĐẾN — không phải nỗi sợ.

④ PHÁC HỌA CHÂN DUNG CỦA KỲ — 2–7 chân dung, mỗi chân dung một bảng:
   MÃ            — CD1, CD2, … ⛔ không dùng CD0 (mã dự trữ)
   TÊN           — NGUYÊN VĂN chữ của khách, giữ nguyên ngôn ngữ,
                   ⛔ không bằng tính từ, ⛔ không lấy tên dịch vụ, ⛔ không tên tầng
   HỌ LÀ AI      — họ vào từ nội dung nào, tin đầu họ gõ gì
   NỖI SỢ        — một nỗi sợ riêng. Hai nhóm cùng nỗi sợ là MỘT chân dung
   DẤU HIỆU      — cụm chữ để nhận ra; xếp chân dung HẸP trước, RỘNG sau
   ★ TẦNG        — tầng chính đứng trước. ⚠ Chân dung trải đều 3–4 tầng là
                   dấu hiệu phác họa chưa tới
   ★ RÀO CHỐT    — ĐÚNG MỘT trong SỢ · NGỜ · NGẠI · XA
   ★ RÀNG BUỘC CHUYẾN ĐI — cửa sổ thời gian · ở lại được bao lâu · đi một mình
                   hay có người đi cùng · có cần visa không
   HỆ SỐ         — 1 · 2 · 3 theo bảng giá công khai. ⚠ Áp LUẬT COMBO: dịch vụ
                   giá thấp cho TT-A/B/C tối đa hệ số 1
   TRÍCH         — ít nhất một HT-nnn làm bằng. ⛔ Không có trích = bịa = loại

   ⛔ KHÔNG gán QT1–QT7 của Agent-AdsOptimize-Kangnam-QT. Đó là khung mẫu dựng
      chiến dịch, chỉ dùng để ĐỐI CHIẾU sau CỔNG 0.

⑤ CÒN LẠI BAO NHIÊU
   Số HT không khớp dấu hiệu nào → rơi CD0.
   ≥15 HT rơi CD0 → nói rõ: tách thêm được một chân dung, hay nhóm này thật sự
   chưa kể gì. ⚠ CD0 đông thường đi kèm TT-0 đông — và cả hai cùng trỏ về MỘT
   việc: câu mở của trực kênh không hỏi khách đang ở đâu và đang gặp gì.

⑥ SO KỲ TRƯỚC
   Chân dung nào CÙNG NỖI SỢ với kỳ trước → GIỮ NGUYÊN MÃ cũ.
   ⚠ Với TT-B, mùa đổi thì nhóm đổi nhưng nỗi sợ không đổi → vẫn giữ mã.

⛔ DỪNG tại đây. ⛔ Không gán chân dung cho hội thoại. ⛔ Không viết thẻ insight.
⛔ Không dựng ma trận. ⛔ Không tự điền người duyệt.
Chờ tôi gõ DUYỆT CHÂN DUNG hoặc SỬA CD<n> <điều chỉnh>.
```

---

## Lượt ② — sau khi tôi duyệt

```
DUYỆT CHÂN DUNG
```
hoặc
```
SỬA CD3 gộp vào CD1 — cùng nỗi sợ
```

Rồi:

```
GÁN & VIẾT INSIGHT

Theo id-C §3–6 và id-D, làm đúng chín việc:

① GÁN CHÂN DUNG cho từng hội thoại theo dấu hiệu ĐÃ DUYỆT
   ★ Tổng HT các chân dung + CD0 phải BẰNG ĐÚNG cỡ mẫu phân tích (luật ⑥).

② BẢNG CHÂN DUNG
   CD · tên · tầng · rào chốt · số HT · HOT/WARM/COLD · có liên hệ · % có liên hệ
   · chốt lịch · bỏ 1 lượt · rơi do trực kênh · ★ S4 chưa đóng   (+ dòng CD0)

③ BẢNG ĐẾM 12 MÃ O **và** ★ 8 MÃ OQ
   kể cả mã bằng 0. Tách riêng "(chưa nêu)" với "O-00".
   ★ Với mỗi mã OQ, ghi TRẠNG THÁI CHẶN (mã nào đang thiếu dữ kiện gốc).
   ⚠ Câu "how many days do I stay" là OQ-01, ⛔ KHÔNG phải O-09 — gán sai là
     xoá mất chặng S4 khỏi báo cáo mà tổng vẫn khớp.
   O-00 vượt 10% mẫu → BÁO LẠI để bổ sung từ điển, ⛔ đừng tự thêm mã.

④ ★ BẢNG BỐN RÀO CHỐT × TẦNG
   SỢ / NGỜ / NGẠI / XA theo TT-A/B/C/D.

⑤ ★ BẢNG S4 CHƯA ĐÓNG — bốn câu của rào XA (id-D §6.1)
   mỗi câu: bao nhiêu HT hỏi · bao nhiêu được trả lời đủ · còn lại là gì
   PHÉP THỬ: "đọc hết hội thoại này, khách có đủ thông tin để mở app hàng không
   và chọn ngày bay chưa?" Chưa → hội thoại chưa xong, dù khách đã cho số.

⑥ THẺ INSIGHT cho mỗi chân dung ≥5 HT, sáu ô:
   HỌ LÀ AI      — họ vào từ nội dung nào, ở tầng nào, tin đầu họ gõ gì
   INSIGHT       — điều họ đang tin / đang sợ, viết bằng chữ của họ
   CÂU HỎI NGẦM  — dịch câu họ gõ thành điều họ THẬT SỰ muốn biết
   TÍN HIỆU NÓNG — họ nóng lên khi nào (⚠ áp luật mùa cho cửa sổ chuyến đi)
   ★ RÀO CHỐT    — rào nào đang giữ họ lại, và bằng chứng nào gỡ được ở TẦNG ĐÓ
   HƯỚNG XỬ LÝ   — một việc cụ thể; ★ ghi rõ việc đó LÀM ĐƯỢC NGAY hay CHỜ DỮ KIỆN

⑦ TOP 10 CÂU CHÉP NGUYÊN VĂN
   câu hỏi đầu tiên hay nhất, GIỮ NGUYÊN NGÔN NGỮ, đã ẩn danh, kèm HT-nnn.

⑧ MA TRẬN CD × S7 — hai bảng N×7 (nội dung đang có · hội thoại trong kỳ)
   ★ XEM CỘT S4 TRƯỚC — đây là cột có nhiều ô ① nhất.
   + ★ MA TRẬN CD × TT — một bảng N×5.

⑨ NỬA TRỰC KÊNH TRẢ LỜI — insight tầng hai
   Điều gì trực kênh đang phải gõ tay nhiều lần mà đáng lẽ một trang EN làm?
   ★ Và điều gì họ KHÔNG trả lời được vì hệ thống chưa cấp — tách riêng.
   ⚠ Muốn thành điểm trừ nhân viên thì phải gắn tiêu chí N + HT-nnn theo id-F.

⛔ Ẩn danh 12 thứ (id-B §2) — gồm hộ chiếu · quốc tịch cá nhân · số hiệu chuyến
   bay · tên khách sạn.
⛔ Chân dung dưới 5 HT: không viết thẻ insight, chỉ ghi vào danh sách 👁 quan sát.
⛔ Không gộp hai chân dung có nỗi sợ khác nhau cho gọn bảng.
```
