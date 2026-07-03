# CLAUDE.md — Quy tắc vận hành dự án "Tin Tức Mỗi Ngày"

## Bối cảnh
Dự án tĩnh chạy trên GitHub Pages theo mô hình "Tĩnh nhưng chạy động".
**TUYỆT ĐỐI KHÔNG sửa `index.html`** trong quy trình hằng ngày.

## Quy tắc bất biến
- File nội dung đặt tên đúng chuẩn: `archive/YYYY-MM-DD.html`.
- File archive chỉ chứa **nội dung thô** (h2/h3/p/ul/table), KHÔNG có `<html>/<head>/<body>`.
- Dùng đúng class có sẵn: `.article-meta`, `.tag`, `.crawl-time`.
- Trong `database.json`: ngày **mới nhất luôn ở đầu** mảng `news_list`, định dạng `YYYY-MM-DD`.
- Không tạo trùng ngày. Nếu ngày đã tồn tại → ghi đè file, giữ nguyên JSON.
- **Tên cổ phiếu để nguyên tiếng Nhật**, không dịch.

## Nguồn cào tin
- `https://my.kabumap.com/market/sector` — biến động 33 ngành (JS-rendered, ưu tiên Chrome MCP; fallback `traders.co.jp/market_jp/sector_ranking/day`).
- `https://www.nikkei.com/marketdata/ranking-jp/spike-in-trading-value/` — mã có giá trị giao dịch đột biến.

## Biểu đồ cổ phiếu
- Dùng công cụ `tools/gen_spark.py` để sinh biểu đồ SVG (sparkline 1 tháng, dữ liệu Yahoo Finance) + link TradingView cho các mã biến động mạnh. KHÔNG viết SVG tay.
- Cú pháp: `python tools/gen_spark.py out.html "<mã>:<tên_JP>:<%>:<up|down>" ...`
- Chỉ số thị trường ở đầu trang (index.html) dùng widget TradingView mã feed OANDA free; cổ phiếu lẻ TSE bị khóa nên phải dùng biểu đồ SVG này.
- Trang có **dark mode** bật/tắt thủ công (nút góc phải masthead, lưu localStorage).

## Prompt vận hành hằng ngày
Xem file **`PROMPT-VAN-HANH.md`** — chạy 4 bước: Cào tin → Tạo file archive (kèm biểu đồ) → Cập nhật JSON → Push GitHub. Lịch tự động: **04:30 sáng hằng ngày (giờ Nhật GMT+9)**.
