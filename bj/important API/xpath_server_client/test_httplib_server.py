#!/usr/bin/python2.6 
#coding=gbk

#import httplib
#
#
#conn = httplib.HTTPConnection("10.134.37.33:8889")
#data = {}
#data['account_openid'] = "oIWsFt0SU-lvLzXIOZPG7qTOp-P4" 
#data['zhu'] = "%E5%A8%B1%E4%B9%90"
#data2 = "account_openid=oIWsFt0SU-lvLzXIOZPG7qTOp-P4&zhu=%E5%A8%B1%E4%B9%90"
#res = conn.request('POST','/zhu_cong_account',data)
#print res
#print conn.getresponse().read()



#!/usr/bin/python
#coding=utf-8
 
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
 
import time
import cgi
import json 
starttime=time.time()
 
class MyHandler(BaseHTTPRequestHandler):
#	 '''Definition of the request handler.'''
	def _writeheaders(self,doc): # for do_GET
 
		if doc is None:
			self.send_response(404)
		else:
			self.send_response(200)
	 
	 
		self.send_header("Content-type","text/html")
		# self.send_header("Content-type", "application/json; charset=utf-8")
		self.end_headers()
	 
	def _set_header(self): # for do_POST
		self.send_response(200)
		self.send_header("Content-Type", "application/json; charset=utf-8")
		self.end_headers()

	def _getdoc(self,filename):
		'''Handle a request for a document,returning one of two different page as as appropriate.'''
		if filename == '/':
			return '''
				<html>
					<head>
						<title>Samlle Page</title>
						<script type="text/javascript">
							//alert("hello");
						</script>
					</head>
 
					<body>
						This is a sample page.You can also look at the
						<a href="stats.html">Server statistics</a>.
					</body>
				</html>
				'''
		elif filename == '/stats.html':
			return''' 
				<html>
					<head>
						<title>Statistics</title>
					</head>
 
					<body>
						this server has been running for %d seconds.
					</body>
				</html>
				'''%int(time.time()-starttime)
		else:
			return None
		 
	def do_HEAD(self):
		'''Handle a request for headers only'''
		print "do_HEAD: %s" %(self.path)
		doc=self._getdoc(self.path)
		self._writeheaders(doc)
 
	def do_GET(self):
		'''Handle a request for headers and body'''
		print "do_GET: Get path is:%s"%self.path
		doc=self._getdoc(self.path)
		self._writeheaders(doc)
		if doc is None:
			self.wfile.write('''
								<html>
									<head>
										<title>Not Found</title>
										<body>
											The requested document '%s' was not found.
										</body>
									</head>
								</html>
								'''%(self.path))
 
		else:
			self.wfile.write(doc)

	def inner_return_wrong(resp): # for do_POST returnings
			resp["status"] = -1
			resp["msg"] = "the post must be dict like:{\"mids\":[\"aaa\",\"bbb\"]}"
			resp_str = json.dumps(resp,ensure_ascii=False).encode("gbk")
			self.wfile.write(resp_str)
			return
		
	# compare with the do_GET method
	def do_POST(self):
		'''Handle a request for headers and body'''
		print "do_POST: POST path is:%s"%self.path
		self._set_header() 
		form = cgi.FieldStorage(
				fp = self.rfile, #fp:file pointer; default: sys.stdin(not used when the request method is GET)
				headers = self.headers, # header dictionary-like object; default:taken from environ as per CGI spec
				environ = {'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],} # environ	 :environment dictionary; default: os.environ
				)
		resp = {"status":0,"msg":"","result":{}}
		if form.getvalue("mids", None) is None:
			inner_return_wrong(resp)
		else:
			try:
				s = form.getvalue("mids")
				s = s.replace("'","\"")
				mid_list = json.loads(s)
			except:
				inner_return_wrong(resp)	 
			if not isinstance(mid_list,list):
				inner_return_wrong(resp)
			else:
				resp["status"] = 0
				resp["msg"] = ""
				print "server:***",mid_list# 仅仅是实例说明，打印了传递的参数；实际过程中，需要根据参数，查询数据库等发挥结果的，这里仅仅返回了测试数据
				result_test = {u"姓名":"yitian","sex":u"男女no","age":25}
				resp["result"] = result_test
				resp_str = json.dumps(resp,ensure_ascii=False).encode("gbk")
				# 不能用末尾的encode("gbk") (assii错误),也不能encoding="GBK"
				#result_test = {"name":"yitian","sex":"男","age":25}
				#result_test["sex"] = result_test["sex"].decode("GBK")
				#resp["result"] = result_test
				#resp_str = json.dumps(resp,encoding="GBK")
				self.wfile.write(resp_str) # self.wfile.write()返回response结果
				return


def start_test_server(ip,port):
	#Create the pbject and server requests
	serveaddr=(ip,port)
	httpd=HTTPServer(serveaddr,MyHandler)
	print "Time:%s Base serve is start add is %s port is %d"\
	%(starttime,serveaddr[0],serveaddr[1])
	httpd.serve_forever()
	# 启动服务两步：httpd = HTTPServer(ip,port,Handler) httpd.serve_forever()


# nohup python2.6 test_httplib.py &
if __name__ == "__main__":
	ip = '192.168.175.128'
	port = 8899
	start_test_server(ip,port)
	
	
	statistic_by_time(current_path)
	statistic_results_group_write(out_path)

