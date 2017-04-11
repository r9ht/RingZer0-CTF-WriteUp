

import requests
import webbrowser
import hashlib
s = requests.session()

url = "https://ringzer0team.com/login"



payload = {'username':  'yourusername',
    'password': 'yourpassword'}


s.post('https://ringzer0team.com/login',payload)
r2 = s.get('https://ringzer0team.com/challenges/13')

#exact place where the hash is
hash = str(r2.text.split()[294])[:-3]

#sha512 hashing
hash_object = hashlib.sha512(str.encode(hash))
hex_dig = hash_object.hexdigest()
#flag get
r3 = s.get('https://ringzer0team.com/challenges/13/'+hex_dig)
print(r3.text)
#find the flag , ex : FLAG-mukgu5g2w932t2kx1nqnhhlhy4

