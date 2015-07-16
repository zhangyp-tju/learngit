#coding=gbk
__author__ = "ouyuanbiao"

import sys
import json
import traceback


for line in sys.stdin:
    try:
        jo = json.loads(line.strip('\n'), encoding='gbk')
        if "channel" in jo:
            print jo["channel"].encode('gbk') + '\t' + line.strip('\n')
    except:
        traceback.print_exc()
        sys.stderr.write(line)
