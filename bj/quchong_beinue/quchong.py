#coding=utf-8
#!/usr/bin/python


print "Just for I/O test just for fun"

class File_RW:
	def __init__(self, src_file, des_file, pat):
		self.pat = pat
		try:
			self.fr = open(src_file,'rt')
			self.fw = open(des_file,'wt')
		except IOError:
			print "IOError:can\'t open this file\n"
	
	def __del__(self):
		self.fr.close()
		self.fw.close()
		#print "tttt"
	
	def read_write(self):
		#print "iiii"
		try:
			lines = self.fr.readlines()
			cnt = 0
			mylist = []
			for line in lines:
				if (line[-1] == '\n'):
					line = line[:-1]
					#print "have n"
				#print "test"
				#print line
				words = line.split(self.pat)
				#words = words[:-1]
				cp = 0
				for word in words:
					if cp == 0:
						cnt = cnt + 1
						if word in mylist:
							#print "repeat rows in line %d, context is %s" %(cnt, line)
							print word
							mylist[len(mylist):] = ['']
							break
						else:
							mylist[len(mylist):] = [word] 
							self.fw.write(word)
	#						cnt = cnt + 1
	#						print "**%s ** %d" % (word,cnt)
						
							cp = 1
					else:
						self.fw.write(',' + word)
				self.fw.write('\n')
		except IOError:
			print "IOError:can\'t not read from file"
	

src_file = "./old_zongbang"
des_file = "./new_zongbang"
pat = "\t"

if ( __name__ == "__main__"):
	frw = File_RW(src_file, des_file, pat)
	frw.read_write()
