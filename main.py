import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from windows import AppWindowViewmodel, LoginWindowViewmodel

 

        




app = QApplication(sys.argv)


widget = QtWidgets.QStackedWidget()

window = LoginWindowViewmodel.LoginWindowViewmodel(widget)
appWindow = AppWindowViewmodel.AppWindowViewmodel()

widget.addWidget(window)
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()

app.exec_()
