#!/usr/bin/python2.6

import sys

app_name_map = {}
def main():
	ifp = file(sys.argv[1])
	for line in ifp:
		if not line:continue
		array = line.split("\t")
		app_name = array[0]
		if not app_name_map.has_key(app_name):
			app_name_map[app_name] = set()
		app_name_map[app_name].add(line)
	ifp.close()
	#delete the chongfu line and add the line when the app_name is not appead in the first file
	ifp2 = file(sys.argv[2])
	for line in ifp2:
		if not line:continue
		array = line.split("\t")
		app_name = array[0]
		if not app_name_map.has_key(app_name):
			app_name_map[app_name] = set()
			app_name_map[app_name].add(line)
	ifp2.close()

	ifp3 = file(sys.argv[3])
	for line in ifp3:
		if not line:continue
		array = line.split("\t")
		app_name = array[0]
		if not app_name_map.has_key(app_name):
			app_name_map[app_name] = set()
			app_name_map[app_name].add(line)
	ifp3.close()
	ifp4 = file(sys.argv[4])
	for line in ifp4:
		if not line:continue
		array = line.split("\t")
		app_name = array[0]
		if not app_name_map.has_key(app_name):
			app_name_map[app_name] = set()
			app_name_map[app_name].add(line)
	ifp4.close()


    # output the conbined result
	for app_name, app_set in app_name_map.items():
		#if len(app_set) == 1:
			#continue
		for item in app_set:
			print item.strip()
		#print ""

if __name__ == '__main__':
	main()
