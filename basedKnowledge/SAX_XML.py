#coding=utf-8
#!/usr/bin/python

import xml.sax
# 继承语法 class 派生类名（基类名）：//... 基类名写作括号里，基本类是在类定义的时候，在元组之中指明的。     
class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self, print_path):
      try:
		self.fwrite = open(print_path,'wt')
      except IOError:
		print "Error:can\'t find this file\n"
      self.fwrite.write("******just for fun******\n")
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # 元素开始事件处理
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "movie":
         print "*****Movie*****"
         self.fwrite.write("****iMovie*****\n")
         title = attributes["title"]
         print "Title:", title
         self.fwrite.write("Title: " + title + "\n")

   # 元素结束事件处理
   def endElement(self, tag):
      if self.CurrentData == "type":
         print "Type:", self.type
      elif self.CurrentData == "format":
         print "Format:", self.format
      elif self.CurrentData == "year":
         print "Year:", self.year
      elif self.CurrentData == "rating":
         print "Rating:", self.rating
      elif self.CurrentData == "stars":
         print "Stars:", self.stars
      elif self.CurrentData == "description":
         print "Description:", self.description
      self.CurrentData = ""

   # 内容事件处理
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content

   def fileclose(self):
		self.fwrite.close()
  
xml_path = "./movies.xml"
print_result = "result.txt"

if ( __name__ == "__main__"):
   
   # 创建一个 XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # 重写 ContextHandler
   Handler = MovieHandler(print_result)
   parser.setContentHandler( Handler )
   
   parser.parse(xml_path)
   Handler.fwrite.write("$$$$end$$$$\n")
   Handler.fileclose()
#   Handler.fwrite.write("test close")
   
# the following is just for fun
print "\n****the following is just for fun\n"
def foo(bar=[]):        # bar是可选参数，如果没有指明的话，默认值是[]
	bar.append("MKY");    # 但是这行可是有问题的，走着瞧…
	return bar;
print foo()
print foo()

odd = lambda x : bool(x % 2)
nums = [n for n in range(10)]
nums[:] = [n for n in nums if not odd(n)]  # 啊，这多优美
print nums
