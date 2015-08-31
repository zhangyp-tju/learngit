from AppKit import NSScreen
from appscript import k
from app import application,reference
import window

class cls(application.cls,reference.cls):
    @property
    def isfullscreen(self):
        """return true if fullscreen"""
        if len(self.windows)>0:
            f=NSScreen.mainScreen().frame()
            w=self.windows.front
            return w.bounds==(
                f.origin.x,
                f.origin.y,
                f.size.width,
                f.size.height
            ) and w.zoomed==True
        return False

    def togglescreen(self):
        self.keystroke("f", using=[k.command_down,k.control_down])

    def fullscreen(self):
        """Enter fullscreen mode"""
        self.activate()
        if not self.isfullscreen:
            if len(self.windows)==0: # not work if len(windows)==0
                self.app.make(new=k.window)
            super(cls,self).fullscreen()
        return self

    @property
    def windows(self):
        return window.list(
            map(
                lambda w:window.cls(w),
                self.app.windows()
            ),
            ["uid"]
        )

    def open(self,url):
        """open/refresh url"""
        exists=False
        for w in self.windows:
            for t in w.tabs:
                if t.url==url:
                    exists=True
                    t.reload()
        if exists:
            return self
        if len(self.windows)>0:
            self.windows.front.tabs.new(url)
        else:
            self.windows.new(url)
        return self

    @property
    def version(self):
        """return Chrome version"""
        return self.app.version()