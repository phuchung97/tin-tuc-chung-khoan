# 📰 Trang Cập Nhật Tin Tức Mỗi Ngày

Hệ thống tổng hợp tin tức **tự động hằng ngày**: cào dữ liệu → xử lý bằng AI →
sinh file tĩnh → đẩy lên **GitHub Pages** làm giao diện đọc báo.

Thiết kế theo mô hình **"Tĩnh nhưng chạy động"**: giao diện `index.html` cố định,
mỗi ngày chỉ thêm 1 file nội dung + cập nhật danh sách ngày trong `database.json`.

## 🗂️ Cấu trúc

| File / Thư mục | Vai trò |
|---|---|
| `index.html` | Trang chủ cố định (tạo 1 lần). Tự đọc `database.json` và nạp bài. |
| `database.json` | Danh sách các ngày có bài (`news_list`), mới nhất đứng đầu. |
| `archive/*.html` | Nội dung thô mỗi ngày, đặt tên `YYYY-MM-DD.html`. |
| `archive/_TEMPLATE.html` | Khung mẫu để tạo bài mới. |
| `.nojekyll` | Tắt Jekyll để GitHub Pages phục vụ file nguyên trạng. |
| `CLAUDE.md` | Quy tắc & prompt vận hành cho Claude Code. |

## 🔄 Luồng chạy hằng ngày

1. **Cào tin** từ các nguồn.
2. **Tạo** `archive/<hôm-nay>.html` từ template.
3. **Cập nhật** `database.json` — chèn ngày mới vào **đầu** `news_list`.
4. **Push** lên GitHub → GitHub Pages tự cập nhật.

## 🚀 Xem thử ở local

```bash
python -m http.server 8000
# mở http://localhost:8000
```

> Lưu ý: mở trực tiếp bằng `file://` sẽ không chạy do trình duyệt chặn `fetch()`.

---
Vận hành & phát triển bởi **Phuc Hung** ♥
