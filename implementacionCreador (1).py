#pyuic5.exe -x p1.ui -o p1.py
import os
from PyQt5 import QtGui, QtCore
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
from CreadorDeArchivos import *

class Ui_CreadorArchivos(QtWidgets.QMainWindow,Ui_CreadorArchivos):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #-------------------------
        #-------------------------
        self.pushButton.clicked.connect(self.apply)
    def apply(self):
        name = self.lineEdit.text()
        text = self.lineEdit_2.text()
        number = self.spinBox.value()
        self.create(name, text, number)
    def create(self, name, text, number):
        address = "/home/oskar/Downloads/" + name + ".txt"
        f = open(address,'w')
        for i in range(0,number):
            f.write(text + "\n")
        f.close()
        self.analize(address)
    def analize(self, address):
        f = open(address,'r')
        x = ["a","e", "i", "o", "u"]
        vowels = 0
        consonants = 0
        while(True):
            line = f.readline()
            if line == "":
                break
            for j in line:
                if j in x:
                    vowels += 1
                elif j != "\n":
                    consonants += 1
        f.close()
        self.update(vowels, consonants)
    def update(self, vowels, consonants):
        self.textBrowser.setText(str(vowels))
        self.textBrowser_2.setText(str(consonants))
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_CreadorArchivos()
    window.show()
    app.exec_()
