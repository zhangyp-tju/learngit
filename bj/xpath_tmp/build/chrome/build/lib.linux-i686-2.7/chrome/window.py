#!/usr/bin/env python
import __builtin__
import appscript
import app
import tab

class cls(app.reference.cls):
    # title
    # resizable
    # index
    # active_tab_index
    # visible
    # zoomed
    # minimizable
    # closeable
    # bounds
    # presenting

    @property
    def tabs(self):
        return tab.list(self,
            map(
                lambda c:tab.cls(self,c),
                self.reference.tabs()
            )
        )

    def open(self,url):
        """open/reload url in this window"""
        for t in self.tabs:
            if t.url==url:
                t.reload()
                return
        self.reference.tabs.end.make(new=appscript.k.tab).URL.set(url)
        return self

    def close(self):
        self.reference.close()

    def __eq__(self,w):
        return self.__class__==w.__class__ and self.id==w.id

    def __str__(self):
        return "<id %s, %s>" % (self.id,self.title)

    def __repr__(self):
        return self.__str__()

class list(app.list.cls):
    def new(self,url=None):
        """make and return new window"""
        r=appscript.app("Google Chrome").make(new=appscript.k.window)
        if url:
            cls(r).tabs.active.url=url
        return cls(r)

    @property
    def front(self):
        if len(self[:])>0:
            return self[:][0]