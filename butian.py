# -*- coding: utf-8 -*-
import sys    
import random
import requests
from bs4 import BeautifulSoup
from requests import exceptions 
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)    
sys.setdefaultencoding('utf8')

class butiansrc(): #定义爬取及处理

	def domain(self,result):   #对域名进行处理
		if 'www' in result:
			result=result.replace('www.','')
		if 'http://' in result:
			result=result.replace('http://','')
		if 'https://' in result:
			result=result.replace('https://','')
		if '/' in result:
			result=result.replace('/','')
		result=result+"\n"
		open('domain.txt','ab').write(result) # 保存全部域名

	def urlresult(self,url):
		result=''					    #对url进行爬取
		data={
	'Host': 'loudong.360.cn',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate',
	'Cookie': 'cookie'
		proxie=[{"http": "183.136.218.253:80"},{"http": "14.215.177.73:80"},{"http": "14.215.177.58:80"},{"http": "163.177.151.23:80"},{"http": "112.80.255.21:80"},{"http": "121.8.98.198:80"},{"http": "112.80.255.32:80"},{"http": "220.181.163.231:80"},{"http": "202.100.83.139:80"},{"http": "115.239.210.42:80"},{"http": "123.125.115.86:80"},{"http": "123.125.142.40:80"},{"http": "163.177.151.162:80"},{"http": "60.2.148.253:80"}]
		user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like GeckoChrome/22.0.1207.1 Safari/537.1","Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6","Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5","Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3","Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3","Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3","Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3","Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)Chrome/19.0.1061.0 Safari/536.3","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"]
		aproxie=proxie[random.randint(0,10)]
		data['User-Agent']=user_agent_list[random.randint(0,18)]
		try:
			getre=requests.get(url,headers=data,proxies = aproxie)
			soup = BeautifulSoup(getre.text,'html.parser')
			result=unicode(soup.find_all('input')[4]['value'])
		except:
			pass
		if result !='':
			self.domain(result)

class create(): #定义任务开始

	def __init__ (self,start_id,end_id):
		self.start_id=start_id
		self.end_id=end_id

	def url_list(self):
		urls=[]
		for i in range(self.start_id,self.end_id):
			url="http://butian.360.cn/Loo/submit?cid="+str(i)  #创建url列表
			urls.append(url)
		return urls

	def useing(self):
		url_list=self.url_list()
		pool=ThreadPool(20)
		pool.map(butianobj.urlresult,url_list)   #构建线程池
		pool.close()
		pool.join()
		

if __name__ == "__main__":  # start
	butianobj=butiansrc()
	print 'start-----------------'
	start=create(1,70000)   
	start.useing()
		
