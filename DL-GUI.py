import wx
import wx.html2 as webview

class WebApp(wx.Frame):
    def __init__(self, parent, title):
        super(WebApp, self).__init__(parent, title=title, size=(800, 600))

        self.panel = wx.Panel(self)

        # Create a webview widget
        self.webview = webview.WebView.New(self.panel)
        self.webview.LoadURL("https://www.duolingo.com/")

        # Arrange the webview in a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.webview, 1, wx.EXPAND | wx.ALL, 10)
        self.panel.SetSizerAndFit(sizer)

        self.fullscreen = False  # Track the fullscreen state

        # Bind the Escape key event to the toggle_fullscreen method
        self.Bind(wx.EVT_KEY_DOWN, self.on_key_down)

        self.Show()

    def on_key_down(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.toggle_fullscreen()

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.ShowFullScreen(True)
        else:
            self.ShowFullScreen(False)

if __name__ == "__main__":
    app = wx.App(False)
    frame = WebApp(None, "Web Application")
    
    # Set focus to the frame to capture key events
    frame.SetFocus()

    app.MainLoop()
