#!/usr/bin/python2.6
#-*-encoding:utf-8-*-

import sys
'''
python2.6 quchong_zyp.py ./_input/old_zongbang ./_input/xinshouji_zongbang ./_input/mianfei_1 ./_input/mianfei_2 > output
python2.6 quchong_zyp.py ./_input/old_zongbang > output_c
'''
app_name_map = {}
def main():
    flag = 0
    for filepath in sys.argv:
        '''just for sys and Usage: python2.6 quchong_zyp.py file_list'''
        if flag == 0:
            flag = 1
            continue#just for argv[0]
        if flag == 1:
            '''the first article do more: add nwe topic to app_name_map and add the quchong topic'''
            ifp = file(filepath)
            for line in ifp:
                if not line:continue
                array = line.split("\t")
                app_name = array[0]
                #print app_name
                if app_name not in app_name_map:
                     #app_name_map[app_name] = set()#if first,then create a new set, and the set is none chongfu elements
                     app_name_map[app_name] = []#just use [] replace the set(),because the set is unique eles
                #app_name_map[app_name].add(line)# if the first or not, both add
                app_name_map[app_name].append(line)# [] is append in array tail
            ifp.close()
            flag = 4
        else:
            '''the last articles just add the new topic to app_name_map'''
            ifp = file(filepath)
            for line in ifp:
                if not line:continue
                arr = line.split("\t")
                app_name = arr[0]
                if app_name not in app_name_map:
                    #app_name_map[app_name] = set()#if first,then create a new set, and the set is none chongfu elements$
                    app_name_map[app_name] = []#just use [] replace the set(),because the set is unique eles$
                    #app_name_map[app_name].add(line)# if the first or not, both add$
                    app_name_map[app_name].append(line)# [] is append in array tail$
            #end for
            ifp.close()
    # end for
    # output the conbined result
    for app_name, app_set in app_name_map.items():
        if len(app_set) == 1:# just for output the chongfu eles
            continue
        for item in app_set:
            print item.strip()
        #print "
    #end for

if __name__ == '__main__':
    main()

