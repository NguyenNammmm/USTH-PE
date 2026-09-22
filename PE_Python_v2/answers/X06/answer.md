# X06 - PW9: ứng dụng quản lý điểm hoàn chỉnh bằng Tkinter

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```text
Domain: dùng Registry/Student/Course ở X02. Persistence: X03 load_pickle + X05 start_save. GUI: notebook bốn tab, Entry/Combobox readonly, callback kiểm tra đầu vào rồi gọi domain; report lấy Registry.ranking. Save chụp Registry, disable nút Save, poll Queue bằng after; ok bỏ dirty, error giữ dirty. Khi đang save khóa các thao tác sửa để trạng thái displayed và snapshot khớp; WM_DELETE_WINDOW lưu hoặc chờ. Startup load lỗi hiển thị thông báo và không cho autosave ghi đè file hỏng. Thư mục capstone_pw9 chứa reference triển khai đủ luồng.
```

## Đáp án kiểm tra hiểu

1. UI hiện điểm8 nhưng mở lại thành7 có được coi là hoàn thành không?

Đáp án: Không, luồng lưu/nạp chưa đúng

- Có vì UI đúng: Ứng dụng phải giữ dữ liệu qua phiên.
- Không, luồng lưu/nạp chưa đúng: Đúng: kiểm tra end-to-end gồm khởi động lại.
- Chỉ cần thêm animation: Animation không sửa persistence.

