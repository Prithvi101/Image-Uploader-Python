# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg_ui.ui'
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(60, 320, 130, 40))
        self.Register.setStyleSheet("background-color:rgb(87, 137, 255);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-color: beige;\n"
" border-radius: 10px;")
        self.Register.setObjectName("Register")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(180, 230, 141, 20))
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(180, 260, 141, 20))
        self.Password.setStyleSheet("")
        self.Password.setObjectName("Password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 230, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 260, 111, 16))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 601, 381))
        self.graphicsView.setStyleSheet("background-color:rgb(223, 223, 223)")
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 60, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 90, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 140, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 170, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 200, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 290, 121, 16))
        self.label_8.setObjectName("label_8")
        self.PasswordCnf = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordCnf.setGeometry(QtCore.QRect(180, 290, 141, 20))
        self.PasswordCnf.setObjectName("PasswordCnf")
        self.MobileNo = QtWidgets.QLineEdit(self.centralwidget)
        self.MobileNo.setGeometry(QtCore.QRect(180, 200, 141, 20))
        self.MobileNo.setObjectName("MobileNo")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(180, 170, 141, 20))
        self.Email.setObjectName("Email")
        self.Pincode = QtWidgets.QLineEdit(self.centralwidget)
        self.Pincode.setGeometry(QtCore.QRect(180, 140, 141, 20))
        self.Pincode.setObjectName("Pincode")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(180, 60, 141, 20))
        self.Name.setObjectName("Name")
        self.Address = QtWidgets.QLineEdit(self.centralwidget)
        self.Address.setGeometry(QtCore.QRect(180, 90, 141, 41))
        self.Address.setObjectName("Address")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 322, 130, 40))
        self.pushButton.setStyleSheet("background-color:rgb(87, 137, 255);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-color: beige;\n"
" border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(340, 10, 256, 361))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView.raise_()
        self.Register.raise_()
        self.Username.raise_()
        self.Password.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.PasswordCnf.raise_()
        self.MobileNo.raise_()
        self.Email.raise_()
        self.Pincode.raise_()
        self.Name.raise_()
        self.Address.raise_()
        self.pushButton.raise_()
        self.graphicsView_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Register.setText(_translate("MainWindow", "Register !"))
        self.label.setText(_translate("MainWindow", "User Name                :"))
        self.label_2.setText(_translate("MainWindow", "Password                  :"))
        self.label_3.setText(_translate("MainWindow", "Name                       :"))
        self.label_4.setText(_translate("MainWindow", "Address                   :"))
        self.label_5.setText(_translate("MainWindow", "Pincode                    :"))
        self.label_6.setText(_translate("MainWindow", "Email                         :"))
        self.label_7.setText(_translate("MainWindow", "Mobile No                  :"))
        self.label_8.setText(_translate("MainWindow", "Confirm Password     :"))
        self.pushButton.setText(_translate("MainWindow", "Cancel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

