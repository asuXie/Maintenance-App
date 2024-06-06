import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi


        
        


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        loadUi('AppWindow.ui', self)
        
