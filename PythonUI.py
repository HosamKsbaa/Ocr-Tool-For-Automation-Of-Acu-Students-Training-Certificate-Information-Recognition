# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import execProg






class Ui_MainWindow(object):

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.clicked("Hellooo"))
        self.pushButton.setGeometry(QtCore.QRect(330, 270, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.lbl_printed = QtWidgets.QLabel(self.centralwidget)
        self.lbl_printed.setGeometry(QtCore.QRect(340, 170, 55, 16))
        self.lbl_printed.setObjectName("lbl_printed")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#Butto        
    def clicked(self, text):
        execProg()

    def updateNumberOfstudentsLabel(self, studentNumber):
        self.lbl_printed.setText(studentNumber)

            
        

        
        
    
            
        
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Button"))
        self.lbl_printed.setText(_translate("MainWindow", "TextLabel"))
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

