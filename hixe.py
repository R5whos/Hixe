# -*- coding: utf-8 -*-

import sys
import os
import re
from http.server import HTTPServer, CGIHTTPRequestHandler

def LocalHost(port):
	print('Success run')
	os.system(f'start http://localhost:{port}/')
	server_address = ("", int(port))
	httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
	httpd.serve_forever()

class Hixe():
	def __init__(self, name):
		self.name = None
		

	def sites(*names, **sites):
		for name in names:
			try:

				f = open(name, 'r', encoding='utf-8')
				f.close()
			
			except:
				print(f'can`t find {name}')
				sys.exit()

		try:
			if sites['main']:
				pass
				#os.system(f'start {os.getcwd()}\\{sites["main"]}')

		except:
			try:
				os.system(f'start {os.getcwd()}\\index.html')
			except:
				os.system(f'start {os.getcwd()}\\{names[0]}')


		try:
			LocalHost(sites['lchost'])


		except Exception as e:
			pass







