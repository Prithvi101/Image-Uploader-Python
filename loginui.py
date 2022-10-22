# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LoginBtn.setGeometry(QtCore.QRect(310, 260, 181, 41))
        self.LoginBtn.setStyleSheet("QPushButton:hover{\n"
"        background: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"        border: 1px solid #6593cf;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background-color:rgb(189, 189, 189);\n"
"        border:4px outset;\n"
"        border-width: 2px;\n"
"        border-radius: 15px;\n"
"        border-color: beige;\n"
"        color: rgb(255, 255, 255);\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}")
        self.LoginBtn.setObjectName("LoginBtn")
        self.RegBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RegBtn.setGeometry(QtCore.QRect(340, 340, 121, 31))
        self.RegBtn.setStyleSheet("QPushButton:hover{\n"
"        background: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"        border: 1px solid #6593cf;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background-color:rgb(255, 85, 0);\n"
"        border:4px outset;\n"
"        border-width: 2px;\n"
"        border-radius: 15px;\n"
"        border-color: beige;\n"
"        color: rgb(255, 255, 255);\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}")
        self.RegBtn.setObjectName("RegBtn")
        self.UserNameEN = QtWidgets.QLineEdit(self.centralwidget)
        self.UserNameEN.setGeometry(QtCore.QRect(332, 180, 141, 20))
        self.UserNameEN.setObjectName("UserNameEN")
        self.PasswordEN = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordEN.setGeometry(QtCore.QRect(330, 230, 141, 20))
        self.PasswordEN.setStyleSheet("")
        self.PasswordEN.setObjectName("PasswordEN")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 150, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 199, 81, 31))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 601, 381))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 241, 381))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 310, 141, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 171, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("UserAuth.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 171, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("tagline.jpg"))
        self.label_5.setObjectName("label_5")
        self.ConnectionStatus = QtWidgets.QLabel(self.centralwidget)
        self.ConnectionStatus.setGeometry(QtCore.QRect(20, 30, 201, 91))
        self.ConnectionStatus.setText("")
        self.ConnectionStatus.setObjectName("ConnectionStatus")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 191, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 300, 161, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 260, 161, 51))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 320, 131, 20))
        self.label_9.setObjectName("label_9")
        self.graphicsView.raise_()
        self.LoginBtn.raise_()
        self.RegBtn.raise_()
        self.UserNameEN.raise_()
        self.PasswordEN.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.graphicsView_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.ConnectionStatus.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoginBtn.setText(_translate("MainWindow", "    Login"))
        self.RegBtn.setText(_translate("MainWindow", "    Register Here!"))
        self.label.setText(_translate("MainWindow", "User Name"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "New Here ? Create Account"))
        self.label_6.setText(_translate("MainWindow", "For Any Quaries Regarding Software"))
        self.label_8.setText(_translate("MainWindow", "Email: Techbuster41@gmail.com"))
        self.label_9.setText(_translate("MainWindow", " Contact: 7887626393"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

