

import requests
import webbrowser
import hashlib
import re
from bs4 import BeautifulSoup

s = requests.session()

url = "https://ringzer0team.com/login"



payload = {'username':  'yourusername',
    'password': 'yourpassword'}


s.post('https://ringzer0team.com/login',payload)
r2 = s.get('https://ringzer0team.com/challenges/32')

#find using regex's

data = re.findall('----- BEGIN MESSAGE -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END MESSAGE -----', r2.text, re.DOTALL)

#split it
data = data[0].split()

#first 5 elements will be used

num = int(data[0])

#find int the hex
hex_int = int(data[2], 16)
new_int = hex_int


#find int of the bin.
bin = int(data[4], 2)

eval_string = str(num) + data[1] + str(new_int) + data[3] + str(bin)
result = eval(eval_string)

#make get request to get the flag

r3 = s.get('https://ringzer0team.com/challenges/32/'+str(result))
#get find the flag

flag = re.findall('<div class="alert alert-info">(.*?)</div>', r3.text, re.DOTALL)

print(flag)