# PROMPT VẬN HÀNH — TỔNG HỢP TIN TỨC HẰNG NGÀY

> Dán nguyên đoạn dưới đây cho Claude Code (hoặc để scheduled task tự nạp).

---

Bạn là bộ máy tự động của dự án tại thư mục `D:\CLAUDE\tin-tuc-chung-khoan`. Hãy thực hiện **tuần tự 4 bước** sau. **TUYỆT ĐỐI KHÔNG chỉnh sửa `index.html`.**

## BƯỚC 1 — CÀO & CHỌN LỌC TIN
- Lấy ngày hôm nay theo định dạng `YYYY-MM-DD` (múi giờ Nhật Bản, GMT+9). Gọi là `<TODAY>`.
- Trang **https://my.kabumap.com/market/sector** — tổng hợp biến động **33 ngành (東証業種別)** sao cho ngắn gọn, dễ nhìn (bảng ngành + % thay đổi), và **nhận định** xem có ngành nào biến động lớn bất thường hay không.
  - ⚠️ Trang này render bằng JavaScript, `WebFetch` thường KHÔNG đọc được. Ưu tiên đọc bằng công cụ trình duyệt (Chrome MCP). Nếu không được, dùng nguồn tương đương: `https://www.traders.co.jp/market_jp/sector_ranking/day`.
- Trang **https://www.nikkei.com/marketdata/ranking-jp/spike-in-trading-value/** — tổng hợp các mã có **giá trị giao dịch đột biến** sao cho ngắn gọn, dễ nhìn (mã + giá + % thay đổi), và **nhận định** xem mã nào biến động lớn bất thường.
- **Tên cổ phiếu để nguyên tiếng Nhật** (không dịch sang tiếng Việt/Anh).

## BƯỚC 2 — TẠO FILE LƯU TRỮ MỚI
- Đọc mẫu tại `archive/_TEMPLATE.html`.
- Tạo file mới `archive/<TODAY>.html` theo đúng cấu trúc template: `<h2>` tiêu đề ngày, khối `.article-meta` (tag + thời gian cào thực tế), rồi nội dung dạng `<h3>` + các đoạn `<p>` / bảng `<table>`.
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
