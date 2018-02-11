# three lib for web application

# Requests：
# 	import requests
#   data = {'data1':'XXXXX', 'data2':'XXXXX'}
# 	response = requests.get(url, params=data)
# 	content = requests.get(url).content
# 	print "response headers:", response.headers
# 	print "content:", content
# Urllib2：
# 	import urllib2,urllib
#   data = urllib.urlencode(data)
#   full_url = url+"?"+data
# 	response = urllib2.urlopen(full_url)
# 	content = urllib2.urlopen(url).read()
# 	print "response headers:", response.headers
# 	print "content:", content
# Httplib2：
# 	import httplib2
# 	http = httplib2.Http()
# 	response_headers, content = http.request(url, 'GET')
# 	print "response headers:", response_headers
# 	print "content:", content

# post
# data = {'data1':'XXXXX', 'data2':'XXXXX'}
# Requests：data为dict，json
# 	import requests
# 	response = requests.post(url=url, data=data)
# Urllib2：data为string
# 	import urllib, urllib2
# 	data = urllib.urlencode(data)
# 	req = urllib2.Request(url=url, data=data)
# 	response = urllib2.urlopen(req)

# cookies login
# import requests
# requests_session = requests.session()
# response = requests_session.post(url=url_login, data=data)
# 若存在验证码，此时采用response = requests_session.post(url=url_login, data=data)是不行的，做法应该如下：
#
# response_captcha = requests_session.get(url=url_login, cookies=cookies)
# response1 = requests.get(url_login) # 未登陆
# ????response2 = requests_session.get(url_login) # 已登陆，因为之前拿到了Response Cookie！
# ????response3 = requests_session.get(url_results) # 已登陆，因为之前拿到了Response Cookie！

# 适用情况：限制IP地址情况，也可解决由于“频繁点击”而需要输入验证码登陆的情况。
#
# 这种情况最好的办法就是维护一个代理IP池，网上有很多免费的代理IP，良莠不齐，可以通过筛选找到能用的。对于“频繁点击”的情况，我们还可以通过限制爬虫访问网站的频率来避免被网站禁掉。
#
# proxies = {'http':'http://XX.XX.XX.XX:XXXX'}
# Requests：
# 	import requests
# 	response = requests.get(url=url, proxies=proxies)
# Urllib2：
# 	import urllib2
# 	proxy_support = urllib2.ProxyHandler(proxies)
# 	opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
# 	urllib2.install_opener(opener) # 安装opener，此后调用urlopen()时都会使用安装过的opener对象
# 	response = urllib2.urlopen(url)

# 有些网站会检查你是不是真的浏览器访问，还是机器自动访问的。这种情况，加上User-Agent，表明你是浏览器访问即可。有时还会检查是否带Referer信息还会检查你的Referer是否合法，一般再加上Referer。
#
# headers = {'User-Agent':'XXXXX'} # 伪装成浏览器访问，适用于拒绝爬虫的网站
# headers = {'Referer':'XXXXX'}
# headers = {'User-Agent':'XXXXX', 'Referer':'XXXXX'}
# Requests：
# 	response = requests.get(url=url, headers=headers)
# Urllib2：
# 	import urllib, urllib2
# 	req = urllib2.Request(url=url, headers=headers)
# 	response = urllib2.urlopen(req)


#  断线重连
# def multi_session(session, *arg):
# 	retryTimes = 20
# 	while retryTimes>0:
# 		try:
# 			return session.post(*arg)
# 		except:
# 			print '.',
# 			retryTimes -= 1
# 或者
#
# def multi_open(opener, *arg):
# 	retryTimes = 20
# 	while retryTimes>0:
# 		try:
# 			return opener.open(*arg)
# 		except:
# 			print '.',
# 			retryTimes -= 1
# 这样我们就可以使用multi_session或multi_open对爬虫抓取的session或opener进行保持。