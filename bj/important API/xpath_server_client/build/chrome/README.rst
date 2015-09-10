Installing
----------

::

    pip install chrome

Usage
-----

::

    from chrome import chrome
    chrome.activate()
    print chrome.frontmost
    >>> True
    chrome.open("http://www.github.com").fullscreen() # all methods return self
    if chrome.isfullscreen:
        chrome.normalscreen()
    for w in chrome.windows:
        print w.index,w.id,w.title,w.active_tab_index
        # w.bounds,w.presenting,w.closeable,w.zoomed,w.minimizable,w.resizable
        for t in w.tabs:
            print t.index,t.id,t.name,t.url,t.loading,t.active
            t.active=True # bring this tab to front
            t.reload()
            t.url="http://www.google.ru" # open google
            t.close() # close tab

    chrome.quit()
    print chrome.active
    >>> False

