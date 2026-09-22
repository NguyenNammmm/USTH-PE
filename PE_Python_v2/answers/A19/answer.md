# A19 - MySQL INSERT, UPDATE, DELETE và transaction

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
class Students:
    def __init__(self,connection): self.connection=connection
    def write(self,sql,params):
        cursor=self.connection.cursor()
        try:
            cursor.execute(sql,params); count=cursor.rowcount; self.connection.commit(); return count
        except Exception:
            self.connection.rollback(); raise
        finally: cursor.close()
    def add(self,sid,name,dob):
        return self.write("INSERT INTO students(id,name,dob) VALUES (%s,%s,%s)",(sid,name,dob))
    def rename(self,sid,name):
        return self.write("UPDATE students SET name=%s WHERE id=%s",(name,sid))
    def delete(self,sid):
        return self.write("DELETE FROM students WHERE id=%s",(sid,))
    def all(self):
        cursor=self.connection.cursor()
        try:
            cursor.execute("SELECT id,name,dob FROM students ORDER BY id"); return cursor.fetchall()
        finally: cursor.close()
```

## Đáp án kiểm tra hiểu

1. DELETE FROM students thiếu WHERE làm gì?

Đáp án: Xóa mọi dòng phù hợp quyền/ràng buộc

- Xóa một dòng đầu: Không có giới hạn một dòng.
- Xóa mọi dòng phù hợp quyền/ràng buộc: Đúng: WHERE xác định phạm vi.
- Chỉ xóa schema: DROP TABLE mới bỏ bảng.

