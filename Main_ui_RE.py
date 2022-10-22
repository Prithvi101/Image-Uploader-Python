
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTreeWidgetItem ,QPushButton,QMessageBox, QLabel, QComboBox
from PyQt5.QtCore import QThread, QObject, Qt, pyqtSignal 
from PyQt5 import QtCore
import os
from PyQt5.QtGui import QIcon, QPixmap
from  datetime import *
from ConnectFtp import ConnectServer,GetuserData
import create_directory
import multiprocessing
from FileUpload import UploadFle , UploadAlbumdetails
import csv
from MainUi import Ui_MainWindow as MainUi
from loginui import Ui_MainWindow as Loginui
from regui import Ui_MainWindow as Regui
import sys
import hashlib
import json
from io import *
import tempfile
import ftplib
from urllib.request import urlopen

class ErrorWindow(QMessageBox):
    def __init__(self, parent=None):
        QMessageBox.__init__(self, parent)
        self.setWindowTitle("Example")

        self.addButton(QPushButton("Yes"), QMessageBox.YesRole )
        self.addButton(QPushButton("No"), QMessageBox.NoRole)
        self.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)


class WorkerThread(QThread):

        UpdatedProgress = pyqtSignal(int)
        CurrentStatusL = pyqtSignal(str)
        UploadedItemCount = pyqtSignal(int)
        UploadComplete = pyqtSignal()
        UploadAlready = pyqtSignal()
        UploadFailed = pyqtSignal()
     
        def __init__(self):
                QThread.__init__(self)
                self.text = "Connecting To Server..."
                self.UploadedItems = []
        
        def __del__(self):
                self.wait()

    
        def run(self):
                self.CurrentStatusL.emit("Connecting To Server...")
                self.CurrentStatusL.emit("Connected")
                create_directory.checkDateDir(UploadDate,ftp)
                self.CurrentStatusL.emit("Getting Ready....")
                create_directory.OrderDirectory(genOrderno,ftp)
                while True:
                        try:
                                Adetails = getAlbumDetails()
                                UploadAlbumdetails(self, Adetails, ftp)
                                self.CurrentStatusL.emit("Starting Upload...")
                                print(selectedImadgesList)
                                for fileNames in selectedImadgesList:
                                        self.CurrentStatusL.emit("Uploading :"+fileNames)
                                        self.UploadedItems.append(fileNames)
                                        self.UpdatedProgress.emit(0)
                                        self.UploadedItemCount.emit(len(self.UploadedItems))
                                        self.count = 0
                                        if UploadFle(self, fileNames , ftp ,self.UpdateCallback,selected_path) == True:
                                                self.UploadComplete.emit()
                                        elif UploadFle(self, fileNames , ftp ,self.UpdateCallback,selected_path) == False:
                                                self.UploadAlready.emit()
                                        elif UploadFle(self, fileNames , ftp ,self.UpdateCallback,selected_path) == 1:
                                                self.UploadFailed.emit()


                                        
                                
                                break
                        except ftplib.all_errors as e:
                                if e == "[WinError 10054] An existing connection was forcibly closed by the remote host":
                                        print("Connection Error")
                                else:
                                        print(e)

                        
                
                
        
        def UpdateCallback(self,block):
                self.count += 1
                self.UpdatedProgress.emit(self.count-1)

def getAlbumDetails():
        AlbDat = ({user_text:{"OrderNo":genOrderno,"details":{"product":product,"papertype":papertype,"papersize":papersize,"emboss":emboss,"name":name,"box":box,"bag":bag,"cover":cover}}})
        string = json.dumps(AlbDat)
        stored = json.loads(string)
        dump = json.dumps(stored,ensure_ascii=False).encode('utf8')
        return dump    
          
def showMsgBox():
        QMessageBox.information(None, "Done", "Album Uploaded")   
        
class LoginThread(QThread):

        CurrentUserName = pyqtSignal(str)
        Loginstatus = pyqtSignal()
        Loginlable = pyqtSignal(str)
        DialogueSignal = pyqtSignal(str,str)
  
        def __init__(self):
                QThread.__init__(self)
                

        def __del__(self):
                
                self.wait()
                    
        def run(self):
                self.Loginlable.emit("Valaditing...")
                try:
                        
                        if userdat[user]["password"] == password:
                                userdata = ({"user":user_text},{"pass":password})
                                print("UI Started")
                                with open('Userdata.ini', 'w') as outfile:
                                        json.dump(userdata, outfile)
                                self.CurrentUserName.emit(user_text)
                                self.Loginlable.emit("Logging...")
                                self.Loginstatus.emit()

                        else:
                                self.DialogueSignal.emit('Error','Worng Password')
                                print("incorrect passwrod")
                                self.Loginlable.emit("Wrong Password")
                                return
                except:
                        self.DialogueSignal.emit('Error','User Not Found')
                        self.Loginlable.emit("User Not Found ")
                
        
class Controller:
        
    def __init__(self):
        
        pass
        

    def show_login(self):
        self.login = LoginWindow()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = Ui()
        self.login.close()
        self.window.show()


product = "Not Selected"
papertype = "Not Selected"
papersize = "Not Selected"
emboss = "Not Selected"
name =  "Not Selected"
box = "Not Selected"
bag = "Not Selected"
cover = "Not Selected"
UploadDate = "Error"
genOrderno = "Error"
ftp = "None"
        

class Ui( QtWidgets.QMainWindow):
        switch_window = QtCore.pyqtSignal(str)
        def __init__(self, parent = None):
                super(Ui, self).__init__(parent) # Call the inherited classes __init__ method
                self.MainUi = MainUi()# Load the .ui file
                global selectedImadgesList 
                selectedImadgesList =[]
                global UploadDate,genOrderno
                self.x = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).replace(':','-', 4)
                genOrderno =  str(self.x.replace(' ','', 4))  
                UploadDate = str(date.today().strftime('%Y-%m-%d'))
                self.StartLoginWindow() # Show the GUI
        def restart (self):            
                #DO stuff before restarting here 
                global ftp
                ftp = ConnectServer() #Connect FTP
                self.MainUi = MainUi()# Load the .ui file
                global selectedImadgesList 
                selectedImadgesList =[]
                global UploadDate,genOrderno
                self.x = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).replace(':','-', 4)
                genOrderno =  str(self.x.replace(' ','', 4))  
                UploadDate = str(date.today().strftime('%Y-%m-%d'))
                self.StartLoginWindow() # Show the GUI
                # return QtCore.QCoreApplication.exit( EXIT_CODE_REBOOT )
        def StartLoginWindow(self):
            self.MainUi.setupUi(self)  #Setup UI
            self.MainUi.OrderNo.setText(genOrderno)#SettingOrderno
            self.MainUi.SelectFolder.clicked.connect(self.getDirectory)#Setting FolderSelection
            self.MainUi.DeetailTree.setColumnCount(3)
            self.MainUi.DeetailTree.setHeaderLabels(['Name','Path','Paper Size'])
            self.MainUi.DeetailTree.setColumnWidth(0, 200)  
            self.MainUi.DeetailTree.setColumnWidth(1, 400)  
            self.MainUi.DeetailTree.setColumnWidth(2, 100)

            self.MainUi.UploadBtn.clicked.connect(self.UploadBtnC)#Upload Button

            self.MainUi.UploadProgressBar.setValue(0)#Upload Progress

            #Apply Changes Button
            self.MainUi.ApplyChanges.clicked.connect(self.ApplyChange)

            #Set Lables
            self.MainUi.OrderNoDisplay.setText(genOrderno)
            self.MainUi.OrderDateDisplay.setText(UploadDate)

            #Combo Box Setup Photo Print Detail
            self.MainUi.Product_2.addItem("--Please Select--")
            self.MainUi.Product_2.addItem("Photo Book")

                
            self.MainUi.ProductCat.addItem("--Please Select--")
            self.MainUi.ProductCat.addItem("Photo Book") 

            self.MainUi.PaperSize.addItem("--Please Select--")
            self.MainUi.PaperSize.addItem("12x18")
            self.MainUi.PaperSize.addItem("12x24")
            self.MainUi.PaperSize.addItem("12x36")

               
            self.MainUi.PaperType.addItem("--Please Select--")
            self.MainUi.PaperType.addItem("HD Glossy")
            self.MainUi.PaperType.addItem("Glossy")
            self.MainUi.PaperType.addItem("Matt")
            self.MainUi.PaperType.addItem("Silk Matt")
            self.MainUi.PaperType.addItem("NTR Think(125)")
            self.MainUi.PaperType.addItem("NTR Thin(200)")
            self.MainUi.PaperType.addItem("Perl Metallic")

              
            self.MainUi.Emboss.addItem("--Please Select--")
            self.MainUi.Emboss.addItem("Plain")
            self.MainUi.Emboss.addItem("Metallic")
            self.MainUi.Emboss.addItem("Gold")


            #Combo Box Setup Album Detail
            self.MainUi.Type.addItem("--Please Select--")
            self.MainUi.Type.addItem("Print")
            self.MainUi.Type.addItem("Design")
            self.MainUi.Type.addItem("Print & Design")
      
            self.MainUi.Box.addItem("--Please Select--")
            self.MainUi.Box.addItem("Printed Box")

            
            self.MainUi.Bag.addItem("--Please Select--")
            self.MainUi.Bag.addItem("Printed Bag")

            
            self.MainUi.CoverType.addItem("--Please Select--")
            self.MainUi.CoverType.addItem("Photo Cover")
            self.MainUi.CoverType.addItem("Sparkle Cover")
            self.MainUi.CoverType.addItem("Fancy Cover")
            self.MainUi.DeetailTree.itemClicked.connect(self.onItemClicked)
            self.UpdateUserData()
            self.show()

        def UpdateUserData(self):
                with open("Userdata.ini") as data:
                                usData = json.load(data)
                                username = str(usData[0]["user"])
                                print(username)
                                self.MainUi.label_32.setText(username)

                
        def ApplyChange(self):
                global product,papertype,papersize,emboss,OrderNOc,name,box,bag,cover
                self.MainUi.TotalImagesSelectedDislpay.setText((str(len(selectedImadgesList))))
                product = self.MainUi.Product_2.currentText()
                papertype = self.MainUi.PaperType.currentText()
                papersize = self.MainUi.PaperSize.currentText()
                emboss = self.MainUi.Emboss.currentText()
                name = self.MainUi.AlbumName.text()
                box = self.MainUi.Box.currentText()
                bag = self.MainUi.Bag.currentText()
                cover = self.MainUi.CoverType.currentText()
                self.MainUi.RVproduct.setText(product)
                self.MainUi.RVpapertype.setText(papertype)
                self.MainUi.RVpapersize.setText(papersize)
                self.MainUi.RVemboss.setText(emboss)

    
        @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
        def onItemClicked(self, it, col):
                filename = (it.text(0))
                filepath = (it.text(1))
                imagePath = (filepath + "\\"+filename)
                pixmap = QPixmap(imagePath)
                pixmap4 = pixmap.scaled(291, 171, QtCore.Qt.KeepAspectRatio)
                self.MainUi.label_31.setPixmap(pixmap4)
                

        def getDirectory(self):
                #Folder Selection
                global Tfilelist
                selectedImadgesList.clear()
                path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
                if  path != '':
                        Tfilelist = os.listdir(path)
                        global selected_path
                        selected_path = str(path)
                        selectedImadgesList.clear()
                        self.getfiles(Tfilelist)
                        self.MainUi.TotalImagecount.setText((str(len(selectedImadgesList))))


        def getfiles(self,path):
                #Folder Selection
                selectedImadgesList.clear()
                self.MainUi.DeetailTree.clear()
                if len(path) > 0:
                        filelist = [fitcher for fitcher in path if fitcher.endswith(".jpg") ]
                        for Image in filelist:
                                selectedImadgesList.append(Image)
                                listWidgetItem = QtWidgets.QTreeWidgetItem(self.MainUi.DeetailTree) 
                                listWidgetItem.setText(0,Image)
                                listWidgetItem.setText(1,selected_path)
                                listWidgetItem.setText(2,"12X36")


        def ShowMessege(self):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Upload Finished")
                msgBox.setWindowTitle("Album Sucessfully Uploaded")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Abort)
                #msgBox.buttonClicked.connect(msgButtonClick)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                        self.restart()
                        print('OK clicked')
        
        def ShowMessegeFailed(self):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Upload Failed")
                msgBox.setWindowTitle("Album Falied To Uploaded")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                #msgBox.buttonClicked.connect(msgButtonClick)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                        print('OK clicked')

        def ShowMessegeAlready(self):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Upload Finished")
                msgBox.setWindowTitle("Album Already Uploaded")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                #msgBox.buttonClicked.connect(msgButtonClick)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                        print('OK clicked')

        def UploadBtnC(self):

                self.w_thread = WorkerThread()
                self.w_thread.UpdatedProgress.connect(self.setProgressBar)
                self.w_thread.CurrentStatusL.connect(self.updateCurrentStat)
                self.w_thread.UploadedItemCount.connect(self.TotalItemCount)
                self.w_thread.UploadComplete.connect(self.ShowMessege)
                self.w_thread.UploadAlready.connect(self.ShowMessegeAlready)
                self.w_thread.UploadFailed.connect(self.ShowMessegeFailed)
                self.w_thread.start()
                

        def setProgressBar(self, val):
                self.MainUi.UploadProgressBar.setValue(val)

        def updateCurrentStat(self, label_text):
                self.MainUi.CurrentStatus.setText(label_text)
    
        def TotalItemCount(self, label_text):
                self.MainUi.UploadedD.setText(str(label_text))
                self.MainUi.RemainingD.setText(str(len(selectedImadgesList) - label_text))
                self.MainUi.TotalImagesSelectedDislpay.setText(str(len(selectedImadgesList)))
    

def register_user(users):
   ftp.storbinary('STOR UserData/users.json', BytesIO(users))

userdat = "none"
user_text = "none"
user = "none"
password = "none"
class LoginWindow(QtWidgets.QMainWindow,Loginui,Regui):

        switch_window = QtCore.pyqtSignal()
        connectionstat = pyqtSignal(str)
        

                

        def __init__(self, parent = None):
                super(LoginWindow, self).__init__(parent)
                self.loginWindow = Loginui()# Load the .ui file
                self.regWindow = Regui()
                self.MainUi = MainUi()# Load the .ui file

                global ftp
                ftp = ConnectServer() #Connect FTP
                global selectedImadgesList 
                selectedImadgesList =[]
                


                global UploadDate,genOrderno
                self.x = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).replace(':','-', 4)
                genOrderno =  str(self.x.replace(' ','', 4))  
                UploadDate = str(date.today().strftime('%Y-%m-%d'))
                
                self.StartLoginWindow()

        def StartLoginWindow(self):
                self.loginWindow.setupUi(self) 
                if os.path.exists("Userdata.ini"):
                        with open("Userdata.ini") as data:
                                usData = json.load(data)
                                username = str(usData[0]["user"])
                                print(username)
                                self.loginWindow.UserNameEN.setText(username)
                #asdf 
                self.loginWindow.LoginBtn.clicked.connect(self.login)
                self.loginWindow.RegBtn.clicked.connect(self.StartRegWindow)
               
                self.UpdateLoginLable("Connecting..")
               
                self.show()

        def login(self):
                global userdat, user_text, user, password
                userdat = json.loads(GetuserData().getvalue())
                user_text = self.loginWindow.UserNameEN.text()
                user = hashlib.sha512(self.loginWindow.UserNameEN.text().encode()).hexdigest()
                password =  hashlib.sha512(self.loginWindow.PasswordEN.text().encode()).hexdigest()
                self.Login_therad = LoginThread()
                self.Login_therad.Loginstatus.connect(self.StartMainUi)
                self.Login_therad.Loginlable.connect(self.UpdateLoginLable)
                self.Login_therad.CurrentUserName.connect(self.updateusername)
                self.Login_therad.DialogueSignal.connect(self.ShowDialogue)
                self.Login_therad.start()


        def ShowDialogue(self, Error, password ):
                QMessageBox.information(self, Error, password)


        def updateusername(self, label_text):
                #self.MainUi.CurrentStatus.setText(label_text) 
                print(label_text)

        def UpdateLoginLable(self, labletext):
                self.loginWindow.ConnectionStatus.setText(labletext)
                print(labletext)

        def StartMainUi(self):
                self.switch_window.emit() # Create an instance of our class
        

        def StartRegWindow(self,user):
                self.regWindow.setupUi(self)  
                self.usernameR = self.regWindow.Username.text()
                self.passcnfrmR = self.regWindow.Password.text()
                self.nameR = self.regWindow.Name.text()
                self.emailR = self.regWindow.Email.text()
                self.mobnoR = self.regWindow.MobileNo.text()
                self.pincodeR = self.regWindow.Pincode.text()
                self.regWindow.Register.clicked.connect(self.RregisterUser)
                self.regWindow.pushButton.clicked.connect(self.StartLoginWindow)
                self.show()



        def RregisterUser(self):
                users= json.loads(GetuserData().getvalue())
                if self.regWindow.Username.text() != "" or self.regWindow.Password.text() != "":
                        user = hashlib.sha512(self.regWindow.Username.text().encode()).hexdigest()
                        password = hashlib.sha512(self.regWindow.Password.text().encode()).hexdigest()
                        passcheck = self.regWindow.Password.text()
                        email = self.regWindow.Email.text()
                        name = self.regWindow.Name.text()
                        mobno = self.regWindow.MobileNo.text()
                        add = self.regWindow.Address.text()
                        pincode = self.regWindow.Pincode.text()
                        cnfpass = self.regWindow.PasswordCnf.text()

                        if user not in users:
                                if passcheck == cnfpass:
                                        users.update({user:{"password":password,"details":{"email":email,"name":name,"mob":mobno,"add":add,"pincode":pincode}}})
                                        dump = json.dumps(users).encode('utf8')
                                        register_user(dump)
                                        QMessageBox.information(self, "Regestered", "Successfully Registered User")
                                        self.StartLoginWindow()
                                else:
                                          QMessageBox.warning(self, "Password Not Matched", "Please Re-enter the password")

                        else:
                                QMessageBox.warning(self, "Registration Error", "User Already Regestered")
                                self.regWindow.Username.setText("")
                                self.regWindow.Password.setText("")

                       
                else:
                        QMessageBox.critical(self, "Error", "Main Fields Cannot Be Empty")
                        self.regWindow.Username.setText("")
                        self.regWindow.Password.setText("")
                return




        @QtCore.pyqtSlot(str)
        def updateLogStat(self, label_text):
                self.loginWindow.ConnectionStatus.setText(label_text)
        

class Error(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Connection Error'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.question(self, 'Error', "Please Check Your Internet Connection", QMessageBox.Abort)
        if buttonReply == QMessageBox.Abort:
            print('Aborted clicked.')
            QtCore.QCoreApplication.instance().quit()
            #QtCore.QCoreApplication.instance().quit
        else:
            print('No clicked.')

        #self.show()


def log():
        app = QtWidgets.QApplication(sys.argv)
        controller = Controller()
        controller.show_login()
        sys.exit(app.exec_())

def error():
        app = QtWidgets.QApplication(sys.argv)
        ex = Error()
        sys.exit(app.exec_())  




def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        stri = "https://www.google.co.in"
        data = urlopen(stri)
        print("connected")
        return True
    except :
        print("Not connected")
        return False


def start_app():
        if is_connected() == True :
                log()
        elif is_connected() == False :
                print("executing")
                error()
    
               
      
    


if __name__ == '__main__':
        print("application Started")
        start_app()

