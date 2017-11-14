#!/usr/bin/python3
#module
from urllib import request

def curl(url):
	return request.urlopen(url).read()
	
def run():
	ip = curl('https://raw.githubusercontent.com/lu0yeah/ddns/master/ip').decode()
	print(ip)
	
if __name__ == '__main__':
	run()