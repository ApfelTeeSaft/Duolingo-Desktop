import wx
import wx.html2

class WebEmbedApp(wx.Frame):
    def __init__(self, parent, title):
        super(WebEmbedApp, self).__init__(parent, title=title, size=(800, 600))
        self.browser = wx.html2.WebView.New(self)
        self.browser.LoadURL("https://www.duolingo.com/")

        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = WebEmbedApp(None, "Duolingo Desktop made with ♥️ by apfelteesaft")
    app.MainLoop()