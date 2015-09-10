#!/usr/bin/python
#coding=gbk

import sys

gov_set = set()

def filter_region():
    #gov_set = set()
    regex = "\t"
    err_cnt = 0
    city_pinyin = "市"
    gov_pinyin = "省"
    for line in sys.stdin:
        line = line.strip()
        if not line:
            err_cnt += 1
            continue
        cols = line.split(regex)
        try:
            #print city_pinyin,cols[2]
            if city_pinyin in cols[2] or gov_pinyin in cols[2]:
                continue
            gov_set.add(cols[2])
        except:
            err_cnt += 1
            continue
    print >> sys.stderr, "ERROR:%d" % (err_cnt)

def write_result():
    for gov in gov_set:
        print gov

def main():
    filter_region()
    write_result()

### cmd --- cat region_info.txt | python2.6 region_filter.py 1> region_dic
### cmd --- $1 | python2.6 region_filter.py 1> $2

if __name__ == "__main__":
    main()
