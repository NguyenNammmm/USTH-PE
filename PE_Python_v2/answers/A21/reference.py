import wx
def build_frame():
    frame=wx.Frame(None,title="PE wx",size=(420,360)); panel=wx.Panel(frame)
    sizer=wx.BoxSizer(wx.VERTICAL)
    text=wx.TextCtrl(panel,style=wx.TE_MULTILINE); sizer.Add(text,1,wx.EXPAND|wx.ALL,8)
    button=wx.Button(panel,label="Print"); sizer.Add(button,0,wx.ALL,8)
    button.Bind(wx.EVT_BUTTON,lambda event:text.AppendText("Clicked\n"))
    check=wx.CheckBox(panel,label="Reminder"); check.SetValue(False); sizer.Add(check,0,wx.ALL,8)
    radio=wx.RadioBox(panel,label="Level",choices=["Basic","Advanced"]); sizer.Add(radio,0,wx.ALL,8)
    group=wx.StaticBoxSizer(wx.VERTICAL,panel,"Info")
    group.Add(wx.StaticText(group.GetStaticBox(),label="Ready"),0,wx.ALL,8); sizer.Add(group,0,wx.EXPAND|wx.ALL,8)
    panel.SetSizer(sizer)
    bar=wx.MenuBar(); menu=wx.Menu(); item=menu.Append(wx.ID_EXIT,"Exit"); bar.Append(menu,"File"); frame.SetMenuBar(bar)
    frame.Bind(wx.EVT_MENU,lambda event:frame.Close(),item)
    return frame,dict(text=text,button=button,check=check,radio=radio)
if __name__=="__main__":
    app=wx.App(False); frame,_=build_frame(); frame.Show(); app.MainLoop()
