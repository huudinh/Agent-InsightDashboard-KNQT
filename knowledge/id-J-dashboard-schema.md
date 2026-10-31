# id-J · DASHBOARD & SCHEMA BÁO CÁO

> Dashboard là **một trang HTML cố định** đọc dữ liệu từ `data/*.json`. Mỗi kỳ chỉ sinh thêm một file JSON, ⛔ không sửa trang.
> Nhờ vậy link gửi cho sếp **không bao giờ đổi**, và xem lại được mọi kỳ cũ.
>
> ⚠️ Schema của bản này là `insight-dashboard-knqt/1` — ⛔ **không tương thích** với `insight-dashboard-kangnam/1` của bản nội địa. Hai dashboard, hai bộ dữ liệu, ⛔ không trộn file kỳ.

---

## 1. MƯỜI TAB *(nội địa: 9)*

| # | Tab | Trả lời câu |
|---|---|---|
| ① | **Phễu inbox** | Khách vào bao nhiêu, nóng tới đâu, rơi ở đâu và vì sao |
| ★ ② | **Thị trường & kênh** | Khách **ở đâu**, nhắn **ngôn ngữ gì**, qua **kênh nào**, vào **giờ nào** |
| ③ | **Chân dung & Insight** | Khách là ai, họ sợ gì, câu hỏi ngầm là gì. ⏳ Khoá lại khi chân dung chưa qua CỔNG 0 |
| ④ | ★ **Chấm điểm nhân viên** | Khối trực kênh đang yếu tiêu chí nào, ai cần kèm |
| ⑤ | **Marketing — Meta** | Chuỗi chi → CPM→CTR→CPI→CPL→CPB→**CPA-KHÁM**, cắt theo thị trường |
| ⑥ | **Marketing — Google Ads** | ⚠ chờ dữ liệu |
| ⑦ | **Ma trận ưu tiên** | Kỳ tới làm việc nào · ★ việc nào đang chờ dữ kiện |
| ⑧ | **Ngân hàng hook** | Viết gì, cho tầng nào, ngôn ngữ nào, format nào |
| ⑨ | **Sổ tay & việc cần xử lý** | Ai làm gì, hạn bao giờ, đo thế nào |
| ⑩ | **Ghi chú dữ liệu** | Mọi con số đến từ đâu, loại gì ra, vì sao |

★ **Tab ② là tab mới của bản quốc tế, và nó đứng thứ hai — ngay sau Phễu — là có chủ ý.** Người đọc phải thấy *khách ở đâu* trước khi đọc bất kỳ tỷ lệ nào (CỔNG M · `id-L` §2).

### Ba bố cục — ⛔ vẫn chỉ MỘT bản trang

Chọn bằng trường `bo_cuc` trong `data/index.json`:

| `bo_cuc` | Tên báo cáo | Tab | Thẻ số tổng |
|---|---|---|---|
| *(không khai)* · `day-du` | Khách quốc tế & chất lượng trực kênh | cả 10 | cả 6 |
| `insight` | **Insight khách quốc tế** — khách là ai · họ tắc ở đâu · kỳ tới làm nội dung gì | ① ② ③ ⑦ ⑧ | HT · bỏ 1 lượt · có liên hệ · HOT/WARM chưa liên hệ · **`S4` chưa đóng** |
| `truc-kenh` | **Chất lượng trực kênh** — khối yếu gì · ai cần kèm · việc nào của hệ thống | ④ ① ② ⑨ ⑩ | HT · trả lời lượt đầu · rơi do trực kênh · **ngoài giờ chờ >12h** · HOT/WARM chưa liên hệ |

```
⛔ Tách báo cáo KHÔNG được đẻ thêm một bản trang.
★ Thứ tự tab đi theo ĐÚNG thứ tự khai trong bố cục.
★ Tab ② có mặt trong CẢ BA bố cục — ⛔ không bố cục nào được bỏ nó.
⚠ Ba bố cục dùng CHUNG một file kỳ. Số liệu chỉ có một bản.
★ Bố cục bỏ tab ⑩ thì ghi chú dữ liệu chuyển lên ô gập đầu trang, ⛔ không biến mất.
```

### Đầu trang — luôn hiện, không nằm trong tab nào

```
Tiêu đề + chọn kỳ
▶ n lưu ý dữ liệu            (gập lại, mở ra xem)
★ dải TẦNG THỊ TRƯỜNG        TT-A · TT-B · TT-C · TT-D · TT-0  (số HT + %)
6 thẻ số tổng                (giá trị · so kỳ trước · so mốc gốc)
```

### Sáu thẻ số tổng

| Thẻ | Kiểu | Tốt là |
|---|---|---|
| `Hội thoại mới` | số | — |
| `Bỏ sau 1 lượt` | % | thấp |
| `Có liên hệ` | % | cao |
| `Trả lời tin đầu ≤5′ (trong giờ)` | % | cao |
| ★ `HOT/WARM chưa có liên hệ` | số | **thấp** |
| ★★ `S4 chưa đóng` | số | **thấp** — HT chạm rào `XA` mà bốn câu `id-D` §6.1 chưa được trả lời đủ |

★ **Thẻ `S4 chưa đóng` là thẻ số đặc trưng của bản quốc tế.** Nó đo đúng chỗ khách **đã muốn làm mà không bay được** — không có thẻ nào khác trong hệ đo được điều đó.

⚠️ Hai thẻ phụ bắt buộc hiện ở tab ② *(không nằm trong 6 thẻ chính)*: `% HT ngoài giờ 8–17 ICT` và `% HT ngoài giờ chờ >12h`.

⚠️ Tab ⑩ **không phải tab phụ**. Báo cáo không nói được số đến từ đâu thì không ai dám dùng để ra quyết định.

---

## 2. SCHEMA DỮ LIỆU — `insight-dashboard-knqt/1`

```jsonc
{
  "schema": "insight-dashboard-knqt/1",
  "ky":   { "id","tu","den","tu_hien","den_hien","nhan","tao","nguon","crawl" },
  "chan": { "van_ban","het_han","con_hieu_luc" },
  "chi_phi": { "co_file": true, "co_cot_market": false, "nguon": "..." },
  "canh_bao": [ { "muc":"bad|warn", "text":"..." } ],
  "the_tong": [ { "id","nhan","gia_tri","kieu":"n|pct|s","tot":"cao|thap","phu" } ],
  "r8": { "xac_nhan": false, "ghi_chu": "[CHỜ CẤP: R8 — Pháp chế + Điều phối QT]" },

  "ket_luan": {
    "marketing":  [ { "viec","ly_do","so_huu","do_ky_sau","nhan":"da_do|gia_thuyet" } ],
    "truc_kenh":  [ ... ],
    "he_thong":   [ ... ],
    "cho_cap":    [ { "du_kien","ai_cap","so_ht","chan_ma" } ],   // ★ id-G §4
    "bu_quyet":   [ { "viec","chi_tiet" } ]
  },
  "theo_doi": [ { "bo_phan","viec","muc_tieu","ket_qua","dat":true|false|null,"lan" } ],

  "pheu": {
    "so_ht_phan_tich": 0,
    "nhiet": { "HOT":0,"WARM":0,"COLD":0 },
    "nhiet_x_lh": [ { "muc","chua","co" } ],
    "tin_hieu":   [ { "nhan","so" } ],              // 5 tín hiệu id-D §3
    "nguyen_nhan_roi": { "nội dung":0,"trực kênh":0,
                         "hệ thống — dữ kiện":0,"hệ thống — múi giờ":0,
                         "hệ thống — ngôn ngữ":0,"khách tự dừng":0,"không rơi":0 },
    "rao_can":    [ { "nhan","so" } ],
    "rao_chot":   { "SỢ":0,"NGỜ":0,"NGẠI":0,"XA":0 },            // ★ id-D §6
    "chang":      { "S1":0,"S2":0,"S3":0,"S4":0,"S5":0,"S6":0,"S7":0,"chưa rõ":0 },
    "ma_o":       [ { "ma","ten","so","pct","noi_dung_da_co","ket_luan" } ],
    "ma_oq":      [ { "ma","ten","so","pct","trang_thai_chan","ket_luan" } ],   // ★ 8 mã
    "s4_chua_dong": { "so":0, "cau": { "1_so_ngay":0,"2_ai_lo":0,
                                       "3_ai_tra_phi":0,"4_ngon_ngu":0 } },     // ★
    "chot_lich":  0,
    "van_de":     [ { "muc","tieu_de","nhan_do","so_lieu","de_xuat","so_huu","anh_huong" } ]
  },

  "thi_truong": {                                   // ★ tab ② — KHỐI MỚI
    "nguon_suy": { "khai_san":0,"khach_tu_noi":0,"suy_tu_chu":0,"suy_tu_kenh":0 },
    "tang":   [ { "tt","ten","ht","pct","hot","warm","cold","co_lh","pct_lh",
                  "roi_truc","ngon_ngu_chinh","market":["AU","NZ"] } ],  // + dòng TT-0
    "ngon_ngu": [ { "kh","nv","so" } ],              // ma trận ngôn ngữ khách × NV
    "kenh":   [ { "ten","ht","pct_lh","tra_loi_dau_phut","truy_duoc_ads":true } ],
    "mui_gio": { "trong_gio":0,"ngoai_gio":0,"pct_ngoai_gio":0,
                 "cho_tb_gio":null,"mat_qua_12h":0,
                 "theo_tang":[ { "tt","ngoai_gio","cho_tb_gio" } ] },
    "mua":    { "cua_so":"<mô tả cửa sổ mùa đang mở>","ghi_chu" }
  },

  "chan_dung": {
    "phac_hoa": { "trang_thai":"chua_phac_hoa|da_duyet","vi_sao","file",
                  "nguyen_lieu","so_chan_dung","duyet_boi","duyet_luc" },
    "tep":     [ { "cd","ten","ht","quan_sat","hot","warm","cold","co_lh",
                   "chot_lich","bo_1_luot","roi_truc","he_so",
                   "tt","ngon_ngu","rao_chot","rang_buoc_chuyen_di" } ],   // + CD0
    "insight": [ { "cd","ten","nhom","tt","ho_la_ai","insight","cau_hoi_ngam",
                   "tin_hieu_nong","rao_chot","huong_xu_ly","trich" } ],
    "co_hoi_win":    [ { "cd","ten","ht","lead_bo_lo","he_so","pct_lh","diem","hang",
                         "uu_tien","roi_truc","ghi_chu" } ],   // CD0 cuối, hang = null
    "cach_tinh_win": "công thức, viết ra để người đọc cãi được",
    "ma_tran_cd_s7": { "noi_dung": {...}, "hoi_thoai": {...} },  // hai bảng N×7
    "ma_tran_cd_tt": {...}                                      // ★ một bảng N×5
  },

  "nhan_vien": {
    "du_mau": true,
    "phan_bo": { "A":0,"B":0,"C":0,"D":0,"chua_du_mau":0 },
    "nhom":    [ { "ma":"N1","ten","diem_toi_da":15,"pct_dat":0,
                   "tieu_chi":[ { "ma":"N1.1","ten","diem":6,"dat":0,"chua":0,"khong_ap_dung":0 } ] } ],
    "ca_nhan": [ { "ten","ht","diem","loai","yeu_nhat","manh_nhat","co_do":[],
                   "tt_chinh","ngon_ngu" } ],         // ⛔ chỉ vào sổ tay riêng
    "theo_tang": [ { "tt","so_nv","diem_tb","ht" } ], // ★ id-F §8 mục ⑦
    "co_do":   [ { "ma":"CĐ-5","nguoi","ht","nguyen_van","nguoi_xu_ly" } ],
    "viec_he_thong": [ { "nhom","nguyen_nhan","so_ht","ai_cap","chan_ma" } ],  // ★ 7 nhóm
    "ghi_chu": "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai."
  },

  "meta": {                                          // tab ⑤ — trước gọi "facebook"
    "nguon","ky","ky_truoc","don_vi":"nghìn đ|USD",
    "chuoi": [ { "ma":"CHI|CPM|CTR|CPI|CPL|CPB|CPA_KHAM","nhan","gia_tri",
                 "muc_tieu","ky_truoc","kieu","tot","phu" } ],
    "theo_tang": [ { "tt","market","chi","inbox","lead","booking","den_kham",
                     "cpi","cpl","cpa_kham" } ],      // ★ cắt theo thị trường
    "cua_so_do": { "ngay":0, "du_8_tuan": false,
                   "ghi_chu":"⚠ TT-B/TT-C cần cửa sổ ≥8 tuần — id-E §1" },
    "truy_duoc": { "pct":0, "ghi_chu":"% inbox truy được về chiến dịch — id-E §6" },
    "noi_dung":  [ { "noi_dung","tt","ngon_ngu","danh_gia":"tot|giu|kem",
                     "tong":{...},"co_phap_che","nhan_xet" } ],
    "nhieu_mau": { "chien_dich":[ { "ten","chi" } ], "ghi_chu" },
    "van_de":    [ ... ]
  },

  "google": { "co_du_lieu": false, "ghi_chu": "⚠ chưa có dữ liệu Google Ads" },

  "ma_tran": {
    "trang_thai":"cho_duyet|da_duyet","duyet_boi","duyet_luc","cach_xep",
    "khoi": [ { "ma":"tang_hot|mo_s4|giam_cold|toi_uu_warm","ten","muc_tieu","tap_lead",
                "dong":[ { "cd","ten","tt","ht","lead","co_lh","he_so","diem","chang",
                           "cau_xa_chua_tl":[],"du_kien_du":true,"huong","chon","uu_tien" } ] } ],
    "sua_van_hanh": [ { "cd","ten","ht","truc","ly_do" } ],
    "cho_cap":      [ { "du_kien","ai_cap","so_ht","chan_ma" } ],     // ★ nhóm ⏸
    "quan_sat":     [ { "cd","ten","ht" } ]
  },

  "hook":   { "ghi_chu","dong": [ { "ma","khoi","cd","ten","tt","ngon_ngu","market",
                                    "chang","ma_o","rao","insight","hook","loai_hook",
                                    "fm":["L13","L16","L10"],"cta","truy_nguoc",
                                    "co_phap_che_vn","co_phap_che_market",
                                    "du_kien_du":true,"duyet" } ] },

  "so_tay": { "da_sinh": false, "so_ban": 0, "duong_dan": "out/so-tay/" },
  "viec":   [ { "so","viec","bo_phan","so_huu","han","do_the_nao","trang_thai" } ],
  "ghi_chu": [ "..." ],
  "truoc":   { "ky","the_tong","tep","noi_dung","chuoi","nhan_vien","thi_truong" },
  "moc_goc": { "ky","nguon","dong":[...] }
}
```

★ **Năm khối mới so với bản nội địa:** `thi_truong` · `pheu.ma_oq` · `pheu.s4_chua_dong` · `pheu.rao_chot` · `ma_tran.cho_cap`. Thêm `r8`, `meta.theo_tang`, `meta.cua_so_do`, `meta.truy_duoc`, `nhan_vien.theo_tang`.
⚠️ Khối `facebook` của bản nội địa đổi tên thành **`meta`** — ⛔ không đọc chéo hai schema.

---

## 3. NĂM LUẬT HIỂN THỊ *(nội địa: bốn)*

```
① KHÔNG CÓ SỐ thì hiện "—", ⛔ không hiện 0.
   0 nghĩa là đã đo và bằng không. "—" nghĩa là chưa đo.
   Cùng luật đó cho CHÂN DUNG: `tep` rỗng thì tab ③ hiện một ô khoá
   "⏳ chân dung chưa được phác họa" kèm lý do.

② MỌI SO SÁNH ghi rõ so với cái gì:
   "▲ 2,1 điểm so kỳ trước"  ·  "mốc gốc 42,7% · ▼ 3,2 điểm"
   Chưa có mốc → "⚠ chưa có mốc so sánh".

③ TIỀN: VND quy về NGHÌN ĐỒNG; bản xuất USD thì GIỮ USD.
   ⛔ Không trộn hai đơn vị trong một bảng. Ghi đơn vị ở đầu bảng.

④ TÊN NHÂN VIÊN ⛔ không xuất hiện trong tab ④ ở dạng bảng xếp hạng.
   Tab ④ hiện: phân bố A/B/C/D · % đạt từng tiêu chí · cờ đỏ (có tên, vì cần
   người xử) · việc hệ thống. Bảng điểm có tên chỉ nằm trong sổ tay riêng.

⑤ ★ MỌI TỶ LỆ PHẢI CẮT ĐƯỢC THEO TẦNG.
   Một con số trung bình toàn kỳ ⛔ không được đứng một mình: luôn kèm dòng
   phân rã TT-A/B/C/D. Tầng dưới 10 HT hiện "⚠ MẪU NHỎ", ⛔ không hiện tỷ lệ.
   Và: TT-0 ≥ 20% → dải tầng ở đầu trang tô cảnh báo, kèm câu
   "chưa biết khách ở đâu — mọi tỷ lệ bên dưới đọc với độ tin thấp".
```

---

## 4. KHỐI "VIỆC CẦN XỬ LÝ" — CUỐI TRANG

| Cột | Ghi chú |
|---|---|
| `#` | Số thứ tự |
| `Việc` | Viết như hành động |
| `Bộ phận` | Marketing · Trực kênh · Hệ thống · **Điều phối QT** · **Khoa Chuyên môn** · **Pháp chế** · BU |
| `Sở hữu` | ★ **Tên người thật.** Việc không có tên là việc không ai làm |
| `Hạn` | |
| `Đo thế nào` | Chỉ số cụ thể của kỳ sau |
| `Trạng thái` | mới · đang làm · đạt · chưa đạt · ★ `⏸ chờ cấp dữ kiện` |

★ Việc **chưa đạt 2 kỳ liên tiếp** → tự động gắn cờ `2 kỳ — đẩy BU`.
★★ Việc `⏸ chờ cấp dữ kiện` **chưa đạt 2 kỳ** → gắn cờ `🔴 CHẶN KÉO DÀI` và đưa lên **đầu trang**, không để cuối trang. Một ô dữ liệu trống hai kỳ liền đang chặn nhiều lead hơn mọi việc nội dung trong danh sách.

---

## 5. THEO DÕI VIỆC KỲ TRƯỚC

Mỗi kỳ mở đầu bằng việc **chấm lại việc kỳ trước**: đạt / chưa đạt / chưa đo.

⛔ Báo cáo không theo dõi việc kỳ trước là báo cáo bắt đầu lại từ đầu mỗi kỳ.

⚠️ **Với `TT-B`/`TT-C`, một việc marketing ⛔ không được chấm "chưa đạt" sau một kỳ 2 tuần** — độ trễ 4–12 tuần (`id-E` §1). Ghi `⏳ chưa đủ cửa sổ đo`.

---

## 6. TỰ KIỂM SỔ NÀY

- [ ] File JSON có `schema` đúng `insight-dashboard-knqt/1` không?
- [ ] Tổng các cột có khớp `so_ht_phan_tich` không? Bảng chân dung đã **cộng cả `CD0`**, bảng tầng đã **cộng cả `TT-0`** chưa?
- [ ] ★ Tab ② có đủ **bốn bảng cắt** của `id-L` §8 chưa?
- [ ] ★ Dải tầng ở đầu trang có hiện không? `TT-0` ≥ 20% có tô cảnh báo không?
- [ ] ★ Thẻ `S4 chưa đóng` có trong 6 thẻ số tổng không?
- [ ] ★ Có tỷ lệ nào đứng một mình, không kèm phân rã theo tầng không?
- [ ] ★ Tầng dưới 10 HT có hiện tỷ lệ thay vì `⚠ MẪU NHỎ` không?
- [ ] `chan_dung.phac_hoa.duyet_boi` có tên người thật chưa?
- [ ] Ô chưa đo có hiện `—` thay vì `0` không?
- [ ] Có bảng nào trộn VND và USD không?
- [ ] Tab ④ có bảng xếp hạng có tên lọt ra không?
- [ ] ★ Khối `viec_he_thong` có gom theo **bảy nhóm** và ghi **ai cấp** chưa?
- [ ] ★ Có dòng `⏸ chờ cấp dữ kiện` nào quá 2 kỳ mà chưa gắn `🔴 CHẶN KÉO DÀI` không?
- [ ] ★ `r8.xac_nhan` có được in ra không?
- [ ] Tab ⑩ có đủ: nguồn · đã loại gì · vì sao loại không?
