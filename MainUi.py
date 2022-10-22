# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1320, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1320, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1320, 720))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UploadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.UploadBtn.setGeometry(QtCore.QRect(1190, 630, 121, 51))
        self.UploadBtn.setStyleSheet("QPushButton:hover{\n"
"        background: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background-color:rgb(255, 85, 0);\n"
"        border:4px outset;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"        border-color: beige;\n"
"        color: rgb(255, 255, 255);\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}")
        self.UploadBtn.setObjectName("UploadBtn")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1321, 41))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.graphicsView.setObjectName("graphicsView")
        self.my_uploads = QtWidgets.QPushButton(self.centralwidget)
        self.my_uploads.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.my_uploads.setStyleSheet("QPushButton:hover{\n"
"        \n"
"        background-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        background: rgb(0, 170, 255);\n"
"        border:4px outset;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"        border-color: beige;\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.my_uploads.setObjectName("my_uploads")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 10, 101, 23))
        self.pushButton_3.setStyleSheet("QPushButton:hover{\n"
"        \n"
"        background-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        background: rgb(0, 170, 255);\n"
"        border:4px outset;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"        border-color: beige;\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 10, 61, 23))
        self.pushButton_4.setStyleSheet("QPushButton:hover{\n"
"        \n"
"        background-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        background: rgb(0, 170, 255);\n"
"        border:4px outset;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"        border-color: beige;\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 41, 61, 20))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(True)
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color:rgb(222, 222, 222);")
        self.label.setObjectName("label")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 40, 771, 31))
        self.graphicsView_2.setStyleSheet("background-color:rgb(222, 222, 222);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(160, 41, 201, 20))
        self.label_2.setStyleSheet("background-color:rgb(222, 222, 222);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 42, 101, 21))
        self.label_3.setStyleSheet("background-color:rgb(222, 222, 222);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 45, 191, 16))
        self.label_4.setStyleSheet("background-color:rgb(222, 222, 222);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 45, 71, 16))
        self.label_5.setStyleSheet("background-color:rgb(222, 222, 222);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 41, 171, 20))
        self.label_6.setStyleSheet("background-color:rgb(222, 222, 222);")
        self.label_6.setObjectName("label_6")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(0, 70, 771, 71))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(770, 40, 551, 101))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.UploadProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.UploadProgressBar.setGeometry(QtCore.QRect(510, 100, 241, 31))
        self.UploadProgressBar.setProperty("value", 24)
        self.UploadProgressBar.setObjectName("UploadProgressBar")
        self.RemainingD = QtWidgets.QLabel(self.centralwidget)
        self.RemainingD.setGeometry(QtCore.QRect(456, 100, 31, 20))
        self.RemainingD.setObjectName("RemainingD")
        self.UploadedD = QtWidgets.QLabel(self.centralwidget)
        self.UploadedD.setGeometry(QtCore.QRect(386, 100, 31, 20))
        self.UploadedD.setObjectName("UploadedD")
        self.TotalImagesSelectedDislpay = QtWidgets.QLabel(self.centralwidget)
        self.TotalImagesSelectedDislpay.setGeometry(QtCore.QRect(286, 100, 41, 20))
        self.TotalImagesSelectedDislpay.setObjectName("TotalImagesSelectedDislpay")
        self.OrderDateDisplay = QtWidgets.QLabel(self.centralwidget)
        self.OrderDateDisplay.setGeometry(QtCore.QRect(160, 100, 91, 20))
        self.OrderDateDisplay.setObjectName("OrderDateDisplay")
        self.OrderNoDisplay = QtWidgets.QLabel(self.centralwidget)
        self.OrderNoDisplay.setGeometry(QtCore.QRect(10, 95, 141, 31))
        self.OrderNoDisplay.setObjectName("OrderNoDisplay")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_5.setGeometry(QtCore.QRect(0, 140, 1321, 261))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 155, 111, 21))
        self.label_12.setObjectName("label_12")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_6.setGeometry(QtCore.QRect(10, 180, 321, 211))
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 200, 51, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 230, 51, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 260, 71, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 285, 71, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(30, 315, 71, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(30, 340, 47, 41))
        self.label_18.setObjectName("label_18")
        self.Product_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Product_2.setGeometry(QtCore.QRect(160, 230, 151, 22))
        self.Product_2.setObjectName("Product_2")
        self.ProductCat = QtWidgets.QComboBox(self.centralwidget)
        self.ProductCat.setGeometry(QtCore.QRect(160, 260, 151, 22))
        self.ProductCat.setObjectName("ProductCat")
        self.PaperSize = QtWidgets.QComboBox(self.centralwidget)
        self.PaperSize.setGeometry(QtCore.QRect(160, 290, 151, 22))
        self.PaperSize.setObjectName("PaperSize")
        self.PaperType = QtWidgets.QComboBox(self.centralwidget)
        self.PaperType.setGeometry(QtCore.QRect(160, 320, 151, 22))
        self.PaperType.setObjectName("PaperType")
        self.Emboss = QtWidgets.QComboBox(self.centralwidget)
        self.Emboss.setGeometry(QtCore.QRect(160, 350, 151, 22))
        self.Emboss.setObjectName("Emboss")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(350, 155, 111, 21))
        self.label_19.setObjectName("label_19")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_7.setGeometry(QtCore.QRect(350, 180, 341, 211))
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(370, 200, 71, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(370, 230, 47, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(370, 260, 47, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(370, 290, 47, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(370, 320, 47, 21))
        self.label_24.setObjectName("label_24")
        self.Type = QtWidgets.QComboBox(self.centralwidget)
        self.Type.setGeometry(QtCore.QRect(480, 230, 151, 22))
        self.Type.setObjectName("Type")
        self.Box = QtWidgets.QComboBox(self.centralwidget)
        self.Box.setGeometry(QtCore.QRect(480, 260, 151, 22))
        self.Box.setObjectName("Box")
        self.Bag = QtWidgets.QComboBox(self.centralwidget)
        self.Bag.setGeometry(QtCore.QRect(480, 290, 151, 22))
        self.Bag.setObjectName("Bag")
        self.CoverType = QtWidgets.QComboBox(self.centralwidget)
        self.CoverType.setGeometry(QtCore.QRect(480, 320, 151, 22))
        self.CoverType.setObjectName("CoverType")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_8.setGeometry(QtCore.QRect(0, 400, 1321, 301))
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 410, 581, 31))
        self.textEdit.setObjectName("textEdit")
        self.SelectFolder = QtWidgets.QPushButton(self.centralwidget)
        self.SelectFolder.setGeometry(QtCore.QRect(600, 410, 81, 31))
        self.SelectFolder.setObjectName("SelectFolder")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(720, 450, 291, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.ReviewChanges = QtWidgets.QTableWidget(self.centralwidget)
        self.ReviewChanges.setGeometry(QtCore.QRect(1020, 451, 281, 171))
        self.ReviewChanges.setObjectName("ReviewChanges")
        self.ReviewChanges.setColumnCount(0)
        self.ReviewChanges.setRowCount(0)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(790, 50, 171, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(1020, 425, 141, 21))
        self.label_26.setObjectName("label_26")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_9.setGeometry(QtCore.QRect(1045, 180, 261, 211))
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(1070, 190, 211, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(1070, 220, 201, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.graphicsView_10 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_10.setGeometry(QtCore.QRect(700, 180, 321, 211))
        self.graphicsView_10.setObjectName("graphicsView_10")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(710, 160, 47, 13))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(1050, 160, 47, 13))
        self.label_28.setObjectName("label_28")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(710, 190, 301, 171))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(920, 365, 91, 21))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.DeetailTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.DeetailTree.setGeometry(QtCore.QRect(10, 450, 671, 231))
        self.DeetailTree.setAlternatingRowColors(True)
        self.DeetailTree.setAllColumnsShowFocus(True)
        self.DeetailTree.setObjectName("DeetailTree")
        self.DeetailTree.headerItem().setText(0, "1")
        self.graphicsView_11 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_11.setGeometry(QtCore.QRect(360, 350, 321, 31))
        self.graphicsView_11.setStyleSheet("background-color:rgb(85, 170, 255);\n"
"border:4px outset;\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"border-color: beige;")
        self.graphicsView_11.setObjectName("graphicsView_11")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 350, 191, 31))
        self.label_7.setObjectName("label_7")
        self.TotalImagecount = QtWidgets.QLabel(self.centralwidget)
        self.TotalImagecount.setGeometry(QtCore.QRect(570, 360, 47, 13))
        self.TotalImagecount.setObjectName("TotalImagecount")
        self.ApplyChanges = QtWidgets.QPushButton(self.centralwidget)
        self.ApplyChanges.setGeometry(QtCore.QRect(1060, 630, 121, 51))
        self.ApplyChanges.setStyleSheet("QPushButton:hover{\n"
"        background: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background-color:rgb(255, 85, 0);\n"
"        border:4px outset;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"        border-color: beige;\n"
"        color: rgb(255, 255, 255);\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}")
        self.ApplyChanges.setObjectName("ApplyChanges")
        self.CurrentStatus = QtWidgets.QLabel(self.centralwidget)
        self.CurrentStatus.setGeometry(QtCore.QRect(510, 80, 221, 16))
        self.CurrentStatus.setText("")
        self.CurrentStatus.setObjectName("CurrentStatus")
        self.graphicsView_12 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_12.setGeometry(QtCore.QRect(0, 689, 1321, 31))
        self.graphicsView_12.setStyleSheet("background-color:rgb(0, 170, 255)")
        self.graphicsView_12.setObjectName("graphicsView_12")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 695, 101, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1040, 470, 47, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1040, 505, 71, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1040, 543, 71, 31))
        self.label_11.setObjectName("label_11")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(1040, 590, 47, 13))
        self.label_29.setObjectName("label_29")
        self.RVproduct = QtWidgets.QLabel(self.centralwidget)
        self.RVproduct.setGeometry(QtCore.QRect(1156, 470, 131, 21))
        self.RVproduct.setText("")
        self.RVproduct.setObjectName("RVproduct")
        self.RVpapertype = QtWidgets.QLabel(self.centralwidget)
        self.RVpapertype.setGeometry(QtCore.QRect(1156, 510, 131, 20))
        self.RVpapertype.setText("")
        self.RVpapertype.setObjectName("RVpapertype")
        self.RVpapersize = QtWidgets.QLabel(self.centralwidget)
        self.RVpapersize.setGeometry(QtCore.QRect(1156, 550, 131, 20))
        self.RVpapersize.setText("")
        self.RVpapersize.setObjectName("RVpapersize")
        self.RVemboss = QtWidgets.QLabel(self.centralwidget)
        self.RVemboss.setGeometry(QtCore.QRect(1156, 590, 121, 20))
        self.RVemboss.setText("")
        self.RVemboss.setObjectName("RVemboss")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(730, 420, 81, 20))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(720, 450, 291, 171))
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(1200, 10, 111, 21))
        self.label_32.setStyleSheet("background-color:rgb(85, 170, 255);\n"
"border:4px outset;\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"border-color: beige;")
        self.label_32.setObjectName("label_32")
        self.OrderNo = QtWidgets.QLineEdit(self.centralwidget)
        self.OrderNo.setGeometry(QtCore.QRect(160, 200, 151, 20))
        self.OrderNo.setReadOnly(True)
        self.OrderNo.setObjectName("OrderNo")
        self.AlbumName = QtWidgets.QLineEdit(self.centralwidget)
        self.AlbumName.setGeometry(QtCore.QRect(480, 200, 151, 20))
        self.AlbumName.setObjectName("AlbumName")
        self.graphicsView_8.raise_()
        self.graphicsView_5.raise_()
        self.graphicsView_2.raise_()
        self.UploadBtn.raise_()
        self.graphicsView.raise_()
        self.my_uploads.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.graphicsView_3.raise_()
        self.graphicsView_4.raise_()
        self.UploadProgressBar.raise_()
        self.RemainingD.raise_()
        self.UploadedD.raise_()
        self.TotalImagesSelectedDislpay.raise_()
        self.OrderDateDisplay.raise_()
        self.OrderNoDisplay.raise_()
        self.label_12.raise_()
        self.graphicsView_6.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.Product_2.raise_()
        self.ProductCat.raise_()
        self.PaperSize.raise_()
        self.PaperType.raise_()
        self.Emboss.raise_()
        self.label_19.raise_()
        self.graphicsView_7.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.Type.raise_()
        self.Box.raise_()
        self.Bag.raise_()
        self.CoverType.raise_()
        self.textEdit.raise_()
        self.SelectFolder.raise_()
        self.textBrowser.raise_()
        self.ReviewChanges.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.graphicsView_9.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.graphicsView_10.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.plainTextEdit_2.raise_()
        self.pushButton_5.raise_()
        self.DeetailTree.raise_()
        self.graphicsView_11.raise_()
        self.label_7.raise_()
        self.TotalImagecount.raise_()
        self.ApplyChanges.raise_()
        self.CurrentStatus.raise_()
        self.graphicsView_12.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_29.raise_()
        self.RVproduct.raise_()
        self.RVpapertype.raise_()
        self.RVpapersize.raise_()
        self.RVemboss.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.OrderNo.raise_()
        self.AlbumName.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UploadBtn.setText(_translate("MainWindow", "UPLOAD"))
        self.my_uploads.setStatusTip(_translate("MainWindow", "background-color:rgb(135, 157, 255)"))
        self.my_uploads.setText(_translate("MainWindow", "My Uploads"))
        self.pushButton_3.setText(_translate("MainWindow", "Upload Images"))
        self.pushButton_4.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Order No"))
        self.label_2.setText(_translate("MainWindow", "Order Date"))
        self.label_3.setText(_translate("MainWindow", "Total Selected"))
        self.label_4.setText(_translate("MainWindow", "Uploaded"))
        self.label_5.setText(_translate("MainWindow", "Remaining"))
        self.label_6.setText(_translate("MainWindow", "Progress"))
        self.RemainingD.setText(_translate("MainWindow", "0"))
        self.UploadedD.setText(_translate("MainWindow", "0"))
        self.TotalImagesSelectedDislpay.setText(_translate("MainWindow", "0"))
        self.OrderDateDisplay.setText(_translate("MainWindow", "00-00-00"))
        self.OrderNoDisplay.setText(_translate("MainWindow", "00000-000-000"))
        self.label_12.setText(_translate("MainWindow", "Photo Print Details"))
        self.label_13.setText(_translate("MainWindow", "Order No"))
        self.label_14.setText(_translate("MainWindow", "Product"))
        self.label_15.setText(_translate("MainWindow", "Product Cat"))
        self.label_16.setText(_translate("MainWindow", "Paper Size"))
        self.label_17.setText(_translate("MainWindow", "Paper Type"))
        self.label_18.setText(_translate("MainWindow", "Emboss"))
        self.label_19.setText(_translate("MainWindow", "Album Details"))
        self.label_20.setText(_translate("MainWindow", "Name"))
        self.label_21.setText(_translate("MainWindow", "Type"))
        self.label_22.setText(_translate("MainWindow", "Box"))
        self.label_23.setText(_translate("MainWindow", "Bag"))
        self.label_24.setText(_translate("MainWindow", "Cover"))
        self.SelectFolder.setText(_translate("MainWindow", "Select Folder"))
        self.label_25.setText(_translate("MainWindow", "Lab Account Details"))
        self.label_26.setText(_translate("MainWindow", "Review Changes"))
        self.checkBox.setText(_translate("MainWindow", "        Close Application After Upload"))
        self.checkBox_2.setText(_translate("MainWindow", "        Shut Down PC After Upload"))
        self.label_27.setText(_translate("MainWindow", "Note"))
        self.label_28.setText(_translate("MainWindow", "Extras"))
        self.pushButton_5.setText(_translate("MainWindow", "Apply Changes"))
        self.label_7.setText(_translate("MainWindow", "Total Images Selected        :"))
        self.TotalImagecount.setText(_translate("MainWindow", "00"))
        self.ApplyChanges.setText(_translate("MainWindow", "Apply Changes"))
        self.label_8.setText(_translate("MainWindow", "Connected...."))
        self.label_9.setText(_translate("MainWindow", "Product"))
        self.label_10.setText(_translate("MainWindow", "Paper Type"))
        self.label_11.setText(_translate("MainWindow", "Paper Size"))
        self.label_29.setText(_translate("MainWindow", "Emboss"))
        self.label_30.setText(_translate("MainWindow", "Preview"))
        self.label_32.setText(_translate("MainWindow", "Aynonumus"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

