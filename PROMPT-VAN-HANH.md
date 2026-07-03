# PROMPT VẬN HÀNH — TỔNG HỢP TIN TỨC HẰNG NGÀY

> Dán nguyên đoạn dưới đây cho Claude Code (hoặc để scheduled task tự nạp).

---

Bạn là bộ máy tự động của dự án tại thư mục `D:\CLAUDE\tin-tuc-chung-khoan`. Hãy thực hiện **tuần tự 4 bước** sau. **TUYỆT ĐỐI KHÔNG chỉnh sửa `index.html`.**

## BƯỚC 1 — CÀO & CHỌN LỌC TIN
> Chỉ dùng **WebFetch** để cào tin (không dùng Chrome/trình duyệt) → chạy hoàn toàn tự động, không phát sinh hỏi quyền.

- Lấy ngày hôm nay theo định dạng `YYYY-MM-DD` (múi giờ Nhật Bản, GMT+9). Gọi là `<TODAY>`.
- **Biến động ngành:** WebFetch trang `https://www.traders.co.jp/market_jp/sector_ranking/day` — tổng hợp biến động **33 ngành (東証業種別)** sao cho ngắn gọn, dễ nhìn (bảng ngành + % thay đổi), và **nhận định** ngành nào biến động lớn bất thường.
  - (Nguồn gốc `my.kabumap.com/market/sector` render JS nên `WebFetch` không đọc được → dùng Traders Web tương đương.)
- **Cổ phiếu đột biến:** WebFetch trang `https://www.nikkei.com/marketdata/ranking-jp/spike-in-trading-value/` — tổng hợp các mã có **giá trị giao dịch đột biến** sao cho ngắn gọn, dễ nhìn (mã + giá + % thay đổi), và **nhận định** mã nào biến động lớn bất thường.
- **Tên cổ phiếu để nguyên tiếng Nhật** (không dịch sang tiếng Việt/Anh).

## BƯỚC 2 — TẠO FILE LƯU TRỮ MỚI
- Đọc mẫu tại `archive/_TEMPLATE.html`.
- Tạo file mới `archive/<TODAY>.html` theo đúng cấu trúc template: `<h2>` tiêu đề ngày, khối `.article-meta` (tag + thời gian cập nhật thực tế), rồi nội dung dạng `<h3>` + các đoạn `<p>` / bảng `<table>`.
- **Biểu đồ cho phần "Cổ phiếu có giá trị giao dịch đột biến (Nikkei)":** chọn 3–4 mã biến động mạnh nhất, sinh biểu đồ bằng công cụ (KHÔNG viết SVG tay):
  ```
  python tools/gen_spark.py <file_tam>.html "<mã>:<tên_JP>:<%thay_đổi>:<up|down>" ...
  ```
  Ví dụ: `python tools/gen_spark.py chart.html "4812:電通総研:+14,71%:up" "9793:ダイセキ:-6,45%:down"`.
  Sau đó dán khối `<div class="spark-grid">…</div>` sinh ra vào ngay dưới phần 2 (dưới câu "📊 Biểu đồ các mã biến động mạnh"). Công cụ tự lấy giá 1 tháng từ Yahoo Finance và kèm link TradingView cho từng mã.
- **Chỉ chứa nội dung thô**, không thêm `<html>/<head>/<body>`. Nếu file ngày `<TODAY>` đã tồn tại thì **ghi đè**.

## BƯỚC 3 — CẬP NHẬT DATABASE.JSON
- Đọc `database.json`. Nếu `<TODAY>` **chưa** có trong mảng `news_list`, chèn vào **vị trí đầu tiên** (`unshift`). Nếu đã có thì giữ nguyên (không tạo trùng).
- Giữ định dạng JSON hợp lệ, thụt lề 2 khoảng trắng.

## BƯỚC 4 — ĐẨY LÊN GITHUB
- `git add archive/<TODAY>.html database.json`
- Commit message: `Cập nhật bản tin ngày <TODAY>`
- `git push` lên nhánh `main`.
- Xác nhận push thành công. GitHub Pages tự cập nhật sau 1–2 phút.

**RÀNG BUỘC:** Nếu bất kỳ bước nào lỗi (không cào được tin, git push fail…), **dừng lại và báo cáo rõ lỗi**, không tự ý sửa `index.html` hay xóa dữ liệu cũ. Cuối cùng in tóm tắt: số tin đã đăng, tên file tạo, trạng thái push.
