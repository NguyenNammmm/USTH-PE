# A23 - Bitmap lát nền trong wxPython

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import wx
class TiledPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent); self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.tile=wx.Bitmap(8,8); dc=wx.MemoryDC(self.tile)
        dc.SetBackground(wx.Brush("#eaf3f5")); dc.Clear()
        dc.SetPen(wx.TRANSPARENT_PEN); dc.SetBrush(wx.Brush("#087e86")); dc.DrawRectangle(0,0,4,4)
        dc.SelectObject(wx.NullBitmap)
        self.Bind(wx.EVT_PAINT,self.paint); self.Bind(wx.EVT_SIZE,self.resize)
        button=wx.Button(self,label="Quit",pos=(12,12)); button.Bind(wx.EVT_BUTTON,lambda event:parent.Close())
    def resize(self,event): self.Refresh(); event.Skip()
    def paint(self,event):
        dc=wx.AutoBufferedPaintDC(self); width,height=self.GetClientSize()
        for y in range(0,height,8):
            for x in range(0,width,8): dc.DrawBitmap(self.tile,x,y)
if __name__=="__main__":
    app=wx.App(False); frame=wx.Frame(None,title="Bitmap",size=(400,300)); TiledPanel(frame); frame.Show(); app.MainLoop()
```

## Đáp án kiểm tra hiểu

1. Vẽ bằng ClientDC một lần có bảo đảm nền còn sau khi bị cửa sổ khác che không?

Đáp án: Không, cần paint handler

- Có: OS có thể yêu cầu repaint sau đó.
- Không, cần paint handler: Đúng.
- Chỉ cần sleep: Sleep không lưu nội dung vẽ.

