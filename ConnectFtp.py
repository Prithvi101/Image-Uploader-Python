from ftplib import FTP
from contextlib import closing
import tempfile
from tempfile import NamedTemporaryFile
import json
import hashlib
from os import path
import requests
from io import*

def ConnectServer():
        for i in range(3):
                print("trying" + str(i))
                while True:
                        try:
                              
                                ServerDetails = getServerDetails() 
                                h = getServerDetails() 
                                print(h["Username"],h["Password"],h["host"])
                                Username = h["Username"]
                                Password = h["Password"]
                                ftp = FTP('')
                                ftp.connect(h["host"],timeout=5)
                                ftp.login(user=Username,passwd=Password)
                                print("Connected To Server")
                                return ftp
                        except:

                                getServerDetails()
                                continue
                break

                                


def getServerDetails():
        url = 'https://api.npoint.io/9bce046268cfd1febfea'
        r = requests.get(url, allow_redirects=False)
        # open("Server.json", 'wb').write(r.content)
        server = r.json()
        return server



         
def GetuserData():
        ftp = ConnectServer()
        #Get Folder Names
        files = [name[0] for name in ftp.mlsd()]
        DirStatus = "Wating"
        #Check If Dir Exist
        for UserDat in files:
                if (UserDat == "UserData"):
                        print("Dir Already Exist ......")
                        DirStatus = "exist"
                        print("dir Exist")
                
                        
                        
        #Creating Dir                  
        if  (DirStatus == "exist"):
                ftp.cwd("UserData") #Changing Current WorkSpace
                print("changed Current Working path")
        else:
                ftp.mkd("UserData") #Creating Date Dir
                ftp.cwd("UserData")
                print("Done")
        
        for i in range(3):
                print("trying" + str(i))
                while True:
                        try:
                                string = StringIO()
                                ftp.retrlines('RETR users.json',string.write)
                                return string
                        
                        except:
                        #QMessageBox.warning(None, "Error", "Registration Failed: Only users with super adm permissions")
                                userdata = hashlib.sha512(b"root").hexdigest()
                                p = hashlib.sha512(b'admin').hexdigest()
                                register_user = ({userdata:p})
                                print("i am here")
                                string = json.dumps(register_user)
                                stored = json.loads(string)
                                dump = json.dumps(stored,ensure_ascii=False).encode('utf8')
                                ftp.storbinary('STOR users.json', BytesIO(dump))
                                continue
                break






