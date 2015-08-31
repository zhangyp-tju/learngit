Installing
----------

::

    pip install osascript

Usage
-----

::

    from osascript import osascript, sudo
    osascript('tell application "iTunes" to play')
    print osascript('return {1,2,3}',"h") # osascript flags
    >>> 1, 2, 3
    sudo("python setup.py install") # GUI if no terminal

`osascript(1) OS X Manual
Page <http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/osascript.1.html>`_
