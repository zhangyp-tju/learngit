# -*- coding: utf-8 -*-
from os import isatty
from sys import stdout
from os.path import exists
from envoy import run

def osascript(applescript_or_file,flags=None):
    """osascript applescript code or file
    https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/osascript.1.html
    """
    if flags:
        flags="-s %s " % flags
    else:
        flags=""
    if exists(applescript_or_file):
        r=run("osascript %s %s" % (flags,applescript_or_file))
    else:
        r=run("osascript %s" % flags,applescript_or_file)
    if r.status_code==0:
        return r.std_out[:-1]
    else:
        raise Exception(r.std_err)

def sudo(command):
    """do shell "%s" with administrator privileges
    http://developer.apple.com/library/mac/#technotes/tn2065/_index.html"""
    if isatty(stdout.fileno()): # terminal
        cmd="sudo %s" % command
        r=run(cmd)
    else: # GUI
        escaped=command.replace('"','\\"')
        cmd='do shell script "%s" with administrator privileges' % escaped
        r=run("osascript",cmd)
    if r.status_code==0:
        return r.std_out
    else:
        raise Exception(r.std_err)