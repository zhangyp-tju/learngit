import __builtin__
import appscript
import app

class cls(app.reference.cls):
    window=None

    def __init__(self,window,reference):
        self.window=window
        self.reference=reference

    @property
    def active(self):
        """return True if tab is frontmost"""
        return self.window.active_tab_index==self.index

    @active.setter
    def active(self,v):
        """bring this tab to front"""
        if v:
            self.window.active_tab_index=True

    @property
    def index(self):
        """return index of this tab"""
        for i,t in enumerate(self.window.tabs):
            if t==self:
                return i+1
        raise ValueError("tab id %s not found" % self.id)

    def reload(self):
        self.reference.reload()
        return self

    @property
    def url(self):
        return self.reference.URL() 

    @url.setter
    def url(self,v):
        self.reference.URL.set(v) 

    def close(self):
        self.reference.close()

    def __eq__(self,t):
        return self.__class__==t.__class__ and self.id==t.id

    def __str__(self):
        return "<%s, %s>" % (self.id,self.url)

    def __repr__(self):
        return self.__str__()

class list(app.list.cls):
    window = None
    def __init__(self, window=None,data=[]):
        from window import cls
        if window:
            if not isinstance(window,cls):
                raise TypeError(""""
invalid window type %s. expected window.cls""" % window.__class__)
        if not issubclass(data.__class__,__builtin__.list):
            raise TypeError(""""
invalid data type %s. expected [tab.cls]""" % data.__class__)
        self.window=window
        super(type(self),self).__init__(data,["id","url"])


    @property
    def active(self):
        """return active tab"""
        for t in self[:]:
            if t.id==self.window.active_tab.id():
                return t

    def new(self,url=None):
        """make and return new tab"""
        r=self.window.reference.tabs.end.make(new=appscript.k.tab)
        if url:
            cls(self.window,r).url=url
        return cls(self.window,r)