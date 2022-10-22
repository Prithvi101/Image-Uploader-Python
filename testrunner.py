import requests
import json
from io import*




def ServerDetails():
        url = 'https://extendsclass.com/api/json-storage/bin/ebaaada'
        r = requests.get(url, allow_redirects=True)
        open("Server.json", 'wb').write(r.content)

