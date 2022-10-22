import ftplib
import datetime
from ftplib import FTP
from datetime import *


def checkDateDir(DateUploaded,ftp):
        CurrentDate = DateUploaded
        ftpC = ftp
        #Get Folder Names
        files = [name[0] for name in ftpC.mlsd()]
        DirStatus = "Wating"
        for DateDir in files:
                if (DateDir == CurrentDate):
                        print("Dir Already Exist ......")
                        DirStatus = "exist"
                        print("dir Exist")
                         
        #Creating Dir                  
        if  (DirStatus == "exist"):
                ftp.cwd(CurrentDate) #Changing Current WorkSpace
        else:
                ftp.mkd(CurrentDate) #Creating Date Dir
                ftp.cwd(CurrentDate)

def OrderDirectory(OrderNo,ftp):
        ftpC = ftp
        CurrentUploads = [name[0] for name in ftpC.mlsd()]
        OrderDirStat = "0"
        print(CurrentUploads)
        for Orders in CurrentUploads:
                if (Orders == OrderNo):
                        OrderDirStat = "Dir Exist"
                         

        if (OrderDirStat == "Order Directory Exist"):
                ftpC.cwd(OrderNo)
        else:
                ftpC.mkd(OrderNo)
                ftpC.cwd(OrderNo)


        