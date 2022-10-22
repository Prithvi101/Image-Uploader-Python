import requests
import json
from io import*
from os import path

# with open("ServerDetails",encoding='utf-8', errors='ignore') as ServerDetails:      
#         h = json.load(ServerDetails,strict=False)
#         print(h["Username"])
#         print(h["Password"])
#         print(h["host"])

def ServerDetails():
        url = 'https://api.npoint.io/9bce046268cfd1febfea'
        r = requests.get(url, allow_redirects=False)
        # open("Server.json", 'wb').write(r.content)
        server = r.json()
        return server

        

ServerDetails()