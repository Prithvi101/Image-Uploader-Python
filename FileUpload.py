
from ConnectFtp import ConnectServer
import chilkat
import ftplib
import os
from io import *
import time




def UploadFle(self, fileName, ftp,callback , paths):
        tries = 0
        global done
        done = False
        File = paths + "//" + fileName
        print(File)
        LocalSize = os.path.getsize(File)
        while tries < 50 and not done:
                try:
                        tries += 1
                        print(tries)
                        with ftp as ftp:
                                files_list = ftp.nlst()
                                print(files_list)
                                if fileName in files_list:
                                        FtpSize = ftp.size(fileName)
                                        LocalSize = os.path.getsize(File)
                                        block_size = int(LocalSize/100)
                                        if LocalSize == FtpSize:
                                                print("Already Uploaded....")
                                                done = True
                                                return False
                                                break
                                        else:
                                                print("Reuploading...")
                                                with open(File,'rb') as fileU:
                                                        ftp.storbinary('STOR ' + fileName, fileU,blocksize=block_size,callback=callback)
                                                return 1
                                        break
                                else:
                                        LocalSize = os.path.getsize(File)
                                        print(LocalSize)
                                        block_size = int(LocalSize/100)
                                        with open(File,'rb') as fileU:
                                                ftp.storbinary('STOR ' + fileName, fileU,blocksize=block_size,callback=callback)
                                                print("file Uploaded")
                                        return True
                                break     

                except (ftplib.all_errors) as e:
                        print(e)
                        print("connection died, trying again")
                        time.sleep(5)      






               
def UploadAlbumdetails(self, fileName, ftp):
        print("processe Run")
        # ftp.storbinary('STOR ' + "AlbumDat.json", BytesIO(fileName))


        
                

