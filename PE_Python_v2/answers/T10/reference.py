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
