import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi

 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('LoginWindow.ui', self)
        self.loginButton.clicked.connect(self.loginFunction)
        

    def loginFunction(self):
        self.aWindow = AppWindow()
        widget.addWidget(self.aWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        
        