# A22 - Hai toolkit: chẩn đoán mainloop và trao đổi dữ liệu

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import sys,json,subprocess,threading,queue
from pathlib import Path
def main(kind,peer=False):
    child=None; inbox=queue.Queue()
    if peer:
        reader,writer=sys.stdin,sys.stdout
    else:
        other="wx" if kind=="tk" else "tk"
        child=subprocess.Popen([sys.executable,str(Path(__file__).resolve()),other,"--peer"],
            stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,encoding="utf8",bufsize=1)
        reader,writer=child.stdout,child.stdin
    def read_messages():
        for line in reader:
            try: inbox.put(json.loads(line))
            except ValueError: inbox.put({"type":"error","value":"Invalid JSON"})
        inbox.put({"type":"closed"})
    threading.Thread(target=read_messages,daemon=True).start()
    def send(message):
        try: writer.write(json.dumps(message,ensure_ascii=False)+"\n"); writer.flush()
        except (BrokenPipeError,OSError): inbox.put({"type":"closed"})
    def send_name(value): send({"type":"name","value":value})
    if kind=="tk":
        import tkinter as tk
        from tkinter import ttk
        root=tk.Tk(); root.title("Tk peer" if peer else "Tk host")
        entry=ttk.Entry(root); entry.pack(); status=ttk.Label(root,text="Ready"); status.pack()
        ttk.Button(root,text="Send",command=lambda:send_name(entry.get())).pack()
        closed=False
        def close():
            nonlocal closed
            if not closed: closed=True; send({"type":"quit"}); root.destroy()
        def poll():
            while not inbox.empty():
                message=inbox.get()
                if message.get("type")=="quit": close(); return
                status.configure(text="Received: "+str(message.get("value",message.get("type"))))
            if not closed: root.after(50,poll)
        root.protocol("WM_DELETE_WINDOW",close); root.after(50,poll); root.mainloop()
    else:
        import wx
        app=wx.App(False); frame=wx.Frame(None,title="wx peer" if peer else "wx host",size=(320,180))
        panel=wx.Panel(frame); box=wx.BoxSizer(wx.VERTICAL)
        entry=wx.TextCtrl(panel); status=wx.StaticText(panel,label="Ready"); button=wx.Button(panel,label="Send")
        for widget in (entry,status,button): box.Add(widget,0,wx.EXPAND|wx.ALL,8)
        panel.SetSizer(box); button.Bind(wx.EVT_BUTTON,lambda event:send_name(entry.GetValue()))
        timer=wx.Timer(frame)
        def close(event): timer.Stop(); send({"type":"quit"}); frame.Destroy()
        def poll(event):
            while not inbox.empty():
                message=inbox.get()
                if message.get("type")=="quit": frame.Close(); return
                status.SetLabel("Received: "+str(message.get("value",message.get("type"))))
        frame.Bind(wx.EVT_CLOSE,close); frame.Bind(wx.EVT_TIMER,poll,timer)
        timer.Start(50); frame.Show(); app.MainLoop()
    if child is not None:
        try: child.wait(timeout=1)
        except subprocess.TimeoutExpired: child.terminate(); child.wait(timeout=3)
        child.stdin.close(); child.stdout.close()
if __name__=="__main__": main(sys.argv[1],"--peer" in sys.argv)
```

## Đáp án kiểm tra hiểu

1. Chuyển cả wx GUI sang một thread nền có bảo đảm sửa được trên mọi OS không?

Đáp án: Không

- Có: GUI toolkit thường yêu cầu main thread.
- Không: Đúng: cần tôn trọng loop/thread của từng toolkit.
- Chỉ cần daemon=True: Daemon chỉ ảnh hưởng vòng đời thread.

