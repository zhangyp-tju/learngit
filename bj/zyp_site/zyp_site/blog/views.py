#!/usr/bin/python
#-*-encoding:utf-8-*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from conn_mongodb import*

'''
# Author: zyp
# Written: Jun 17,2015
# Modified: Jun 17,2015
# Purpse: just for test
'''
# Create your views here.

def index(request):
	params = {}
	params["name"] = "zyp"
	params["age"] = 1
	params["eles"] = ["java","python","c++"]
	res_list = conn_test()
	params["res_list"] = res_list
	print res_list
	return render_to_response("index.html",params,context_instance=RequestContext(request))
