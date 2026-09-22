# A18 - Dựng MySQL và thiết kế schema bằng Workbench

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```text
CREATE TABLE students(id VARCHAR(20) PRIMARY KEY,name VARCHAR(100) NOT NULL,dob DATE NOT NULL);
CREATE TABLE courses(id VARCHAR(20) PRIMARY KEY,name VARCHAR(100) NOT NULL,credits INT NOT NULL CHECK(credits>0));
CREATE TABLE marks(student_id VARCHAR(20),course_id VARCHAR(20),score DECIMAL(4,1) CHECK(score BETWEEN 0 AND 10),
  PRIMARY KEY(student_id,course_id),FOREIGN KEY(student_id) REFERENCES students(id),FOREIGN KEY(course_id) REFERENCES courses(id));
-- Python: dùng mysql.connector.connect với config từ biến môi trường, SELECT 1, đóng cursor và connection trong finally.
-- Workbench: tạo connection localhost, mở pe_lab, reverse engineer schema để xem hai FK và khóa kép.
```

## Đáp án kiểm tra hiểu

1. pip install mysql-connector-python có tự tạo MySQL server đang chạy không?

Đáp án: Không

- Có: Đó là driver client.
- Không: Đúng: server cần được cài/chạy riêng.
- Chỉ trên Windows: Vai trò package không đổi theo OS.

