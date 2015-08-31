#coding=gbk
import os, sys, string
import json
import hashlib
import time
import urllib
import traceback
import threading
import xpath as XPATH
from datetime import datetime
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class TestHTTPHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.resp = {}
		path = self.path
		try:
			if "?" not in path:
				self.resp["status"] = 0
				self.response()
				return
			else:
				self.resp["status"] = 1
			path = path[path.find("?") + 1 :]
			parts = path.split('&')
			param_map = {}
			for part in parts:
				param = part.split('=')
				if len(param) < 2:
					continue
				key = param[0]
				value = urllib.unquote(param[1]).decode('utf8').encode('gbk')
				param_map[key] = value
			url = param_map['url']
			xpath = param_map['xpath']
			charset = param_map['charset']
			r = XPATH.test(url, xpath, charset)
			self.resp["content"] = r
		except Exception, e:
			self.resp["status"] = 0
			self.resp["msg"] = e.message
			traceback.print_exc()
		self.response()
		#for item in collection.find():
			#print hehe
	def response(self):
		self.protocal_version = 'HTTP/1.1'
		self.send_response(200)
		#解决跨域问题
		self.send_header("Access-Control-Allow-Origin", "*")
		#self.send_header("Welcome", "Contect")
		self.end_headers()
		resp = json.dumps(self.resp, encoding='gbk')
		self.wfile.write(resp)



def start_server(port):
	http_server = HTTPServer(('10.11.195.140', int(port)), TestHTTPHandler)
	http_server.serve_forever() #设置一直监听并接收请求其中，IP为给localhost设定的访问地址
start_server(8899)
