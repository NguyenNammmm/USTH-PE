# T10 - Người học tự viết unit test cho GUI

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import unittest
import tkinter as tk
from form_app import passed,build
class ThresholdTests(unittest.TestCase):
    def test_below(self): self.assertFalse(passed(4.9))
    def test_boundary(self): self.assertTrue(passed(5))
    def test_above(self): self.assertTrue(passed(8))
class FormTests(unittest.TestCase):
    def setUp(self):
        self.root=tk.Tk(); self.root.withdraw(); self.widgets=build(self.root)
    def tearDown(self): self.root.destroy()
    def test_button(self):
        self.widgets["entry"].insert(0,"5")
        self.widgets["button"].invoke()
        self.assertEqual(self.widgets["status"].cget("text"),"Dat")
if __name__=="__main__": unittest.main()
```

## Đáp án kiểm tra hiểu

1. Test passed(8)==True có bắt được mutant score>5 không?

Đáp án: Không, cần test đúng 5

- Có: Cả >=5 và >5 đều nhận 8.
- Không, cần test đúng 5: Đúng: test biên phân biệt hai chương trình.
- Chỉ cần thêm print: print không tự tạo assertion.

