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

## Prompt vận hành hằng ngày
Xem mục "PROMPT VẬN HÀNH" trong README hội thoại / bên dưới để chạy 4 bước:
Cào tin → Tạo file archive → Cập nhật JSON → Push GitHub.
