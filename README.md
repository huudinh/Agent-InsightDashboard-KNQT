# 🌏 Agent-InsightDashboard-KNQT

> **Agent đọc Insight khách QUỐC TẾ của Kangnam Korean Aesthetic Hospital.**
>
> Đọc **chính lời khách nói trên 7 kênh nhắn tin** cùng **số quảng cáo cắt theo thị trường**, rồi trả lời năm câu: **khách là ai · họ đang ở đâu · họ đang sợ gì · họ tắc ở đâu và vì ai · kỳ tới phải làm gì**.
>
> Đầu ra dùng được ngay: **dashboard 10 tab · ma trận ưu tiên · ngân hàng hook EN/VI · sổ tay thực thi riêng cho từng nhân viên**.

`v1.0` · 2026-10-31 · Claude / ChatGPT / Gemini / Claude Code

**Site phục vụ:** <https://kangnamaesthetichospital.com/> — ⛔ khác site nội địa.

Agent anh em: [`Agent-InsightDashboard-Kangnam`](../Agent-InsightDashboard-Kangnam/) *(insight nội địa)* · [`Agent-AdsOptimize-Kangnam-QT`](../Agent-AdsOptimize-Kangnam-QT/) *(từ khoá · ad · landing · GEO cho khách quốc tế)*

---

## ★ Một câu khiến bản này khác bản nội địa

> **Khách quốc tế quyết định HAI thứ, không phải một: *"có mổ không"* và *"có bay không"*.**

Bản nội địa hỏi *"khách rơi ở đâu"*. Bản này hỏi thêm một câu mà bản nội địa ⛔ không có:

```
Phép thử một hội thoại đã xong hay chưa:
  "Đọc hết hội thoại này, khách có đủ thông tin để mở app hàng không
   và chọn ngày bay chưa?"
Chưa → hội thoại CHƯA XONG, dù khách đã cho số, dù nhân viên rất lịch sự.
```

Chỗ đó là **chặng `S4` — lên kế hoạch chuyến đi**: chặng khách rụng nhiều nhất mà **gần như không ai đo**, vì nó xảy ra **sau khi lead đã vào CRM**. Agent này có một thẻ số riêng cho nó: **`S4 chưa đóng`**.

---

## Agent này làm gì

| Việc | Nghĩa |
|---|---|
| ★① **Khai tầng thị trường** | `TT-A` lân cận · `TT-B` **kiều bào** · `TT-C` phát triển · `TT-D` expat tại VN · `TT-0` chưa khai được. **CỔNG M:** không biết khách ở đâu thì ⛔ không kết luận gì |
| ② **Phác họa chân dung khách** | ⛔ Không có bộ chân dung dựng sẵn — mỗi kỳ phác họa 2–7 chân dung **từ chính hội thoại đưa vào**, người dùng duyệt ở **CỔNG 0**, rồi gán theo phễu **`S1–S7`** |
| ★③ **Đào sâu insight** | 12 mã `O` + **8 mã `OQ` chỉ có ở khách quốc tế** · **bốn rào chốt** `SỢ·NGỜ·NGẠI·XA` · câu hỏi ngầm · 5 tín hiệu nóng |
| ★④ **Chấm điểm nhân viên trực kênh** | 27 tiêu chí `N1.1–N7.6` · thang 100 · A/B/C/D · **10 cờ đỏ** · SLA **tính theo múi giờ** |
| ⑤ **Ma trận ưu tiên** | **4 khối**: Tăng HOT → ★ **MỞ CHẶNG `S4`** → Giảm COLD → Tối ưu WARM, + nhóm **⏸ chờ cấp dữ kiện** |
| ⑥ **Ngân hàng hook** | 7 loại × 16 format — ★ mỗi hook gắn **1 tầng + 1 ngôn ngữ**, và **format bị chặn theo tầng** |
| ⑦ **Sổ tay thực thi cá nhân hoá** | Một trang mỗi người: một việc, câu mẫu **song ngữ**, + ★ mục *"việc không phải của bạn"* |
| ⑧ **Dashboard 10 tab** | Trang HTML cố định, mỗi kỳ thêm một file JSON — **link không đổi** |

⛔ **Đây KHÔNG phải agent viết từ khoá / ad / landing quốc tế** *(`Agent-AdsOptimize-Kangnam-QT`)*, ⛔ **không phải agent đọc insight nội địa** *(`Agent-InsightDashboard-Kangnam`)*, ⛔ **không phải agent chấm cuộc gọi** *(`Agent-QC-Telesale`)*.

---

## Đầu vào → Đầu ra

```
① 100–300 hội thoại trên 7 kênh     ─┐              ┌─► ③ DASHBOARD 10 TAB
   (WhatsApp·Telegram·Viber·Line·     │              │
    Kakao·Zalo·Messenger)             │              ├─► ④ MA TRẬN ƯU TIÊN ← cổng duyệt
② Số ads ★ CÓ CỘT `market`          ─┼─►  AGENT  ───┼─► ⑤ NGÂN HÀNG HOOK EN/VI
③ Google Ads  🔴 chưa có            ─┘              ├─► ⑥ SỔ TAY từng nhân viên
                                                     ├─► ⑦ VIỆC CẦN XỬ LÝ (có tên người)
                                                     └─► ★⑧ DANH SÁCH ⏸ CHỜ CẤP DỮ KIỆN
```

---

## ★ Bảy thứ khác hẳn bản nội địa

Bản này **⛔ không phải bản dịch**. Cả bảy đều là thay đổi **logic**.

| # | Khác gì | Vì sao |
|---|---|---|
| ① | ★ **Thêm CỔNG M** — không có thị trường thì không kết luận | Cùng câu *"how much is rhinoplasty in Hanoi"*, người gõ từ Sydney và người gõ từ Hà Nội là **hai khách khác nhau, hai rào cản khác nhau, hai luật quảng cáo khác nhau**. Trộn rồi tính trung bình là ra một con số ⛔ không nói về ai cả |
| ② | **Phễu `5A` → `S1–S7`** | Thêm chặng `S4` *(kế hoạch chuyến đi)* và `S6` *(hậu phẫu từ xa)* — hai chỗ mất khách thật của du lịch y tế mà `5A` ⛔ không diễn đạt được |
| ③ | **Thêm 8 mã `OQ`** | Số ngày ở lại · ai lo khi về nước · ai trả phí chỉnh sửa · visa · thanh toán · phiên dịch · hậu cần · điều kiện văn hoá. ⚠️ **Sáu trong tám đang bị chặn vì thiếu dữ kiện gốc**, không vì nhân viên kém |
| ④ | **`N1`–`N6` → `N1`–`N7`**, SLA theo múi giờ | Giờ làm việc công bố là **08:00–17:00 ICT** = 20:00 Sydney · 10:00 London · 06:00 Los Angeles. Trả lời trong 5 phút lúc 3 giờ sáng ⛔ không phải việc của nhân viên — đó là việc của **lịch trực** |
| ⑤ | ★ **`N3.1` NGƯỢC HẲN** | Nội địa: giá chưa công khai → né giá là **lỗi hệ**. Quốc tế: giá **đã công khai** tại `/price-list/` → né giá là **lỗi người**. Và thêm `N3.2`: **phải nêu phụ phí quốc tế 10%** |
| ⑥ | **Pháp chế HAI TẦNG** | Luật Việt Nam **và** luật nước người xem *(AHPRA · ASA · FTC · GDPR · GCC)*. Một câu hợp lệ ở Việt Nam **vẫn có thể** bị cơ quan nước đích xử lý |
| ⑦ | **Thêm `CPA-KHÁM`, cửa sổ đo ≥8 tuần** | Độ trễ lead → đến khám của `TT-B`/`TT-C` là **4–12 tuần**. CPL rẻ trong kỳ mà không ai bay sang là **kỳ tệ**, không phải kỳ tốt |

---

## ★ Luật nặng nhất của bản này

```
⛔ TUYỆT ĐỐI KHÔNG NÊU SỐ NGÀY KHÁCH PHẢI Ở LẠI VIỆT NAM,
   HOẶC MỐC ĐƯỢC PHÉP BAY, BẰNG MỘT SỐ CỨNG.
```

Đó là **mốc y khoa** *(ngày cắt chỉ · tái khám cuối · được phép bay)*, ⛔ không phải con số marketing. **Bay quá sớm sau phẫu thuật là rủi ro y khoa thật.**

→ Chưa có số → viết `[CHỜ CẤP: số ngày ở lại — Khoa Chuyên môn]` và trả lời bằng *"the surgeon confirms this at your assessment"*.

⚠️ Trong dữ liệu thử, nhân viên đã trả lời *"you can fly after 7 days"* — một câu nói ra vì **khách cần một con số để đặt vé**. Đó là cờ đỏ `CĐ-5`, và nó xuất hiện vì người ta **đang cố giúp khách**, không phải vì cẩu thả.

---

## Luật quan trọng thứ hai — phân rã CPL

```
CPL = (CPM/1000) ÷ ( CTR × click→inbox% × inbox→lead% )

⛔ KHÔNG KẾT LUẬN "CẦN LÀM THÊM NỘI DUNG" KHI THÀNH PHẦN XẤU ĐI KHÔNG PHẢI CTR.
★ VÀ KIỂM CƠ CẤU THỊ TRƯỜNG TRƯỚC CẢ BỐN THÀNH PHẦN.
```

| Thành phần xấu đi | Thật ra là việc của |
|---|---|
| **CTR** giảm | Nội dung |
| **CPM** tăng | Adnet — tệp, bid, lịch · ★ **hoặc đổi cơ cấu thị trường** |
| **click→inbox** giảm | Kỹ thuật — điểm đến, lời chào · ★ **hoặc `geo_mode` sai** |
| **inbox→lead** giảm | ★ **Trực kênh** — chứng minh bằng chính hội thoại · ★ **hoặc múi giờ** |

★ Chuyển chi từ `KH` sang `AU` thì CPM tăng, CPL tăng, mà **không có gì xấu đi cả** — đó là một **quyết định ngân sách**, không phải một sự cố.

---

## Cài đặt nhanh

| Nền tảng | Dán vào | File |
|---|---|---|
| **Claude Project** | Custom instructions | [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) |
| **ChatGPT Custom GPT** | Instructions *(trần 8.000 ký tự)* | [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md) · 7.998 ký tự |
| **Gemini Gem** | Chỉ dẫn | [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) |

Rồi nạp **12 file [`knowledge/`](knowledge/)** + **9 file [`prompts/`](prompts/)** vào Knowledge.
Nền tảng chỉ cho nạp ít file → dùng [`goi/GOP-tri-thuc.md`](goi/GOP-tri-thuc.md).

Chi tiết: [`doc/01-cai-dat.md`](doc/01-cai-dat.md) — có **8 câu smoke test**.

⛔ **Không nạp lẫn tri thức của bản nội địa vào cùng một Project.** Hai bản khác hệ chặng, khác luật hiển thị giá, khác số cơ sở.

---

## 12 sổ tri thức

| Sổ | Nội dung |
|---|---|
| [`id-A`](knowledge/id-A-vai-tro-quy-trinh.md) | Vai trò · 8 bước · **bốn cổng chặn** · AUTO · ngưỡng mẫu |
| [`id-B`](knowledge/id-B-doc-dau-vao.md) | Ba dòng đầu vào · 7 kênh · ★ **suy tầng thị trường** · ẩn danh **12 thứ** |
| ★★ [`id-C`](knowledge/id-C-chan-dung-s7.md) | **Phác họa chân dung · CỔNG 0** × **phễu `S1–S7`** · ma trận lỗ hổng |
| ★★ [`id-D`](knowledge/id-D-dao-sau-insight.md) | 12 mã `O` + **8 mã `OQ`** · 5 tín hiệu nóng · **bốn rào chốt · bốn câu của rào `XA`** |
| ★ [`id-E`](knowledge/id-E-to-chuc-ads-chi-so.md) | Tổ chức ads quốc tế · **`CPA-KHÁM`** · phân rã CPL · ngân sách `S3`/`S4` · luật port thị trường |
| ★★ [`id-F`](knowledge/id-F-cham-diem-nhan-vien.md) | Tiêu chí `N1–N7` · A/B/C/D · **10 cờ đỏ** · **4 rào an toàn** · **bảy nhóm lỗi hệ** |
| ★ [`id-G`](knowledge/id-G-ma-tran-uu-tien.md) | Ma trận **4 khối** · luật combo · nhóm **⏸ chờ cấp dữ kiện** |
| [`id-H`](knowledge/id-H-ngan-hang-hook.md) | Hook 7 loại × 16 format · **giới hạn format theo tầng** · cụm hook `S4` |
| ★ [`id-I`](knowledge/id-I-so-tay-thuc-thi.md) | Sổ tay thực thi · luật một việc · **mục *"việc không phải của bạn"*** |
| [`id-J`](knowledge/id-J-dashboard-schema.md) | Dashboard **10 tab** · schema `insight-dashboard-knqt/1` · **5 luật hiển thị** |
| ★★ [`id-K`](knowledge/id-K-module-knqt-phap-che.md) | **Module KNQT** · 2 cơ sở · giá công khai · **pháp chế hai tầng** · rào `R8` |
| ★★ [`id-L`](knowledge/id-L-thi-truong-ngon-ngu-mui-gio.md) | **Tầng thị trường · ngôn ngữ · múi giờ · kênh** — sổ lõi, ⛔ không có ở bản nội địa |

★ **Đổi thương hiệu → thay đúng [`id-K`](knowledge/id-K-module-knqt-phap-che.md), ⛔ không sửa lõi `id-A`…`id-J`, `id-L`.**

---

## Dòng lệnh

```bash
# đọc hội thoại → tầng thị trường · chặng S1–S7 · mã O + OQ · nhiệt · vì sao rơi · chấm N1–N7
python tools/id.py doc du-lieu/hoi-thoai.md --ky "19-25/10"

# CỔNG 0 — phác họa chân dung
python tools/id.py chan-dung --ky "19-25/10" --mau
python tools/id.py chan-dung --ky "19-25/10" --kiem
python tools/id.py chan-dung --ky "19-25/10" --duyet "<tên người>"   # ★ người dùng gõ

# đọc số quảng cáo — ★ cần cột `market`
python tools/id.py ads du-lieu/ads-quoc-te.csv --ky "19-25/10"

# gộp thành JSON cho dashboard
python tools/id.py bao-cao --ky "19-25/10"

# sinh khung sổ tay từng người (sau khi ma trận đã duyệt)
python tools/so_tay.py --ky "19-25/10"

# xem dashboard
cd dashboard && python -m http.server 8080
```

Chạy thử ngay bằng file mẫu: `template/MAU_hoi-thoai.md` + `template/MAU_ads-quoc-te.csv`.
Chi tiết: [`doc/02-cau-lenh.md`](doc/02-cau-lenh.md) · Kết quả mẫu thật: [`doc/03-output-mau.md`](doc/03-output-mau.md)

> ⚠️ Script làm phần **đếm được**. Phần **đọc hiểu** — insight, câu hỏi ngầm, hướng nội dung, câu mẫu trong sổ tay, và **mọi phán đoán pháp chế hai tầng** — là việc của agent. Script để lại `«agent điền: …»` đúng chỗ cần người.

---

## 9 prompt mẫu

| Prompt | Dùng khi |
|---|---|
| [`prompt-auto.md`](prompts/prompt-auto.md) | Chạy cả kỳ một phát, dừng ở cổng duyệt |
| ★ [`prompt-thi-truong-mui-gio.md`](prompts/prompt-thi-truong-mui-gio.md) | **CỔNG M** — khách ở đâu · ngôn ngữ · kênh · múi giờ |
| ★ [`prompt-chan-dung-insight.md`](prompts/prompt-chan-dung-insight.md) | Chỉ cần phần khách hàng |
| ★ [`prompt-cham-diem.md`](prompts/prompt-cham-diem.md) | Chấm & phân loại trực kênh |
| [`prompt-doc-so-ads.md`](prompts/prompt-doc-so-ads.md) | Đọc số ads & nối với hội thoại |
| [`prompt-ma-tran.md`](prompts/prompt-ma-tran.md) | Dựng ma trận ưu tiên (cổng 1) |
| [`prompt-hook.md`](prompts/prompt-hook.md) | Viết ngân hàng hook (sau cổng 1) |
| ★ [`prompt-so-tay.md`](prompts/prompt-so-tay.md) | Viết sổ tay từng người |
| ★ [`prompt-phap-che.md`](prompts/prompt-phap-che.md) | Soát cổng 2 — **hai tầng pháp lý** |

---

## Mười hai luật bất biến

| # | Luật | Vì sao |
|---|---|---|
| ① | **Truy ngược** — mọi insight, hook, điểm trừ phải chỉ về `HT-nnn` hoặc một con số | Không truy ngược được = bịa |
| ★② | **Không có thị trường thì không kết luận** | Trung bình của bốn tầng là con số không nói về ai |
| ③ | **Phân rã CPL trước khi kết luận** | CPL tăng vì CPM mà đổi hook là chữa nhầm bệnh |
| ★④ | **Cửa sổ đo ≥8 tuần** với `TT-B`/`TT-C` | Độ trễ lead → khám là 4–12 tuần |
| ⑤ | **Một lần chấm** — một hội thoại chấm đúng một lần | |
| ⑥ | **Tổng phải khớp** cỡ mẫu — cộng cả `CD0` và `TT-0` | |
| ⑦ | **Ngưỡng mẫu** — <10 HT không kết luận · <10 HT/người hoặc /tầng không kết luận riêng | ⚠️ Inbox quốc tế cỡ mẫu nhỏ là bình thường, ⛔ không nới ngưỡng cho đẹp bảng |
| ⑧ | **`—` không phải `✗`** | |
| ★⑨ | **Lỗi hệ không trừ điểm người — BẢY NHÓM** | *Phép thử: "người giỏi nhất khối, với đúng những gì hệ thống đang cấp, có làm khác được không?"* |
| ⑩ | **Điểm để kèm cặp, không để kỷ luật** | ⛔ Không có bảng xếp hạng cá nhân ngoài sổ tay riêng |
| ⑪ | **Chưa đo hiện `—`, không hiện `0`** · chưa có mốc thì ghi `⚠`, ⛔ không tự đặt hệ số | |
| ★⑫ | **Ẩn danh 12 thứ** — thêm hộ chiếu · quốc tịch cá nhân · số hiệu chuyến bay · tên khách sạn | ⛔ Và không nạp ảnh khách/hộ chiếu/hồ sơ bệnh án vào bất kỳ công cụ AI nào |

---

## ⛔ Tuyệt đối không

- ⛔ **Nêu số ngày ở lại hoặc mốc được phép bay bằng số cứng** — mốc y khoa, rủi ro thật
- ⛔ **Dùng chữ *"lifetime"*** hoặc nêu bất kỳ thời hạn bảo hành — site đang ghi *lifetime warranty* mà chưa có T&C
- ⛔ **Nêu giá mà bỏ dòng phụ phí quốc tế 10%** — bom niềm tin ở quầy thanh toán
- ⛔ **So sánh giá với một quốc gia hoặc cơ sở có tên**
- ⛔ **Nói *"board certified"*** hoặc gắn claim hội–hiệp hội ở mức thương hiệu
- ⛔ **Gắn chức danh/số năm bác sĩ** chưa qua bốn cổng của `id-K` §3④; ⛔ không làm tròn *"nearly 20"* thành *"20+"*
- ⛔ **Testimonial kết quả lâm sàng hoặc before–after cho `TT-C`** (AU/UK/EU/US/GCC)
- ⛔ **Before–after cơ thể / ngôn từ về cân nặng** — mọi tầng, mọi thị trường
- ⛔ **Nhắc 5 viện thẩm mỹ tỉnh** cho khách quốc tế — các cơ sở đó không làm đại phẫu
- ⛔ **Đưa ra kết luận pháp lý** — chỉ nêu cơ quan phải tra, gắn cờ, đề xuất câu hạ rủi ro
- ⛔ **Dịch hook nội địa sang tiếng Anh** · ⛔ viết hook `TT-B` bằng tiếng Anh
- ⛔ **Trộn** `nhân viên chạy ads` với `nhân viên trực kênh`
- ⛔ **Phát bản còn cờ 🔴 ở bất kỳ tầng pháp lý nào, hoặc khi `R8` chưa xác nhận**

---

## 🔴 Đang bị chặn — cần cấp để mở

| # | Thứ còn thiếu | Ai cấp | Chặn gì |
|---|---|---|---|
| ★① | **Số ngày ở lại Việt Nam** theo 7 dịch vụ | **Khoa Chuyên môn** | 🔴 Mã `OQ-01` · tiêu chí `N7.6` · cờ `CĐ-5` · mọi hook chặng `S4` |
| ② | **T&C bảo hành bằng văn bản** *(gồm "ai trả chi phí bay nếu phải chỉnh sửa")* | Pháp chế + Vận hành | 🔴 `O-07` · `OQ-04` · cờ `CĐ-2` |
| ③ | **`R8`** — đủ điều kiện KCB cho người nước ngoài | Pháp chế + Điều phối QT | 🔴 **Toàn bộ** site EN và mọi chiến dịch |
| ④ | **Lịch trực theo múi giờ** cho `TT-C` *(UK/EU/US)* | Vận hành + Điều phối QT | 🔴 Mọi ô SLA ngoài giờ |
| ⑤ | **Một dòng dùng chung cho cả hai site** về claim hội–hiệp hội | Pháp chế | 🔴 Cờ `CĐ-4` |
| ⑥ | **Privacy notice đạt GDPR** | Pháp chế | 🔴 `L12` — mọi lead EU/UK |
| ⑦ | **Visa · thanh toán quốc tế · ngôn ngữ phiên dịch** | Điều phối QT | 🟠 `OQ-03` · `OQ-05` · `OQ-06` |
| ⑧ | **Bản xuất ads có cột `market`** | Khối Ads | 🟠 ⛔ không gán được số cho tầng nào |
| ⑨ | **Mốc mục tiêu TB 30 ngày theo từng thị trường** | Khối Ads | 🟠 Mọi chỉ số ghi `⚠ chưa có mốc so sánh` |
| ⑩ | **Dữ liệu Google Ads** | Khối Ads | 🟠 Tab ⑥ trống — khung đọc đã dựng sẵn |
| ⑪ | **Mẫu sổ tay thực thi chính thức** | Người dùng | 🟠 Khuôn `ST-CN` hiện là bản dựng tạm |

⚠️ **Mục ① cấp bách nhất, và nó khác về bản chất với các mục còn lại:** thiếu nó thì khách **không đặt được vé** — và lead không đặt vé thì ⛔ không bao giờ thành ca. Trong hội thoại thử đã có nhân viên **tự nghĩ ra một con số**. Đó không phải lỗi thái độ, đó là **một ô dữ liệu trống**.

---

## Cây thư mục

```
Agent-InsightDashboard-KNQT/
├── SYSTEM-PROMPT.md          bộ não đầy đủ
├── SYSTEM-PROMPT-NGAN.md     bản ≤8.000 ký tự cho ChatGPT
├── knowledge/                12 sổ id-A … id-L
├── prompts/                  9 prompt mẫu
├── goi/GOP-tri-thuc.md       bản gộp (sinh tự động)
├── template/                 MAU_hoi-thoai.md · MAU_ads-quoc-te.csv
├── tools/                    id.py · so_tay.py · tu_dien.json (song ngữ)
│                             gop-tham-khao.py · dem-ngan.py
│                             trang-huong-dan.py + huong-dan.json → huong-dan.html
├── dashboard/                index.html (cố định) + data/*.json (mỗi kỳ một file)
├── doc/                      cài đặt · dòng lệnh · output mẫu · changelog
└── out/                      kết quả — ⛔ KHÔNG commit
```

⛔ `out/`, `du-lieu/`, `dashboard/data/`, file hội thoại gốc, ảnh khách — [`.gitignore`](.gitignore) đã chặn.
