#!/usr/bin/python3
#module
import requests
import github3
import time
#
username = 'lu0yeah'
password = 'ilku3328'
repo_name = 'ddns'
#
def login():
	gh = github3.login(username,password)
	repo = gh.repository('lu0yeah',repo_name)
	return repo
	
def get_ip():
	return requests.get('http://ipecho.net/plain').text
	
def run(ip=None,port=80):
	if ip==None:
		ip = get_ip()
	ip = ip + ':' + str(port)
	print('[*]ip: %s' % ip)
	repo = login()
	file = repo.contents('ip')
	print('[*]update ip to %s' % file.html_url)
	t = time.asctime(time.localtime())
	file.update('update: %s' % t,ip.encode())
	file = repo.contents('ip')
	print('[+]ip: %s' % file.decoded.decode())
	
if __name__=='__main__':
	run()
	