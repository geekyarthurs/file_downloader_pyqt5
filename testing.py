#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:22:41 2020

@author: crmahesh
"""


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello")
        self.setMinimumSize(400,300)
        
        
        
        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self) 
        impMenu.addAction(impAct)
        
        newAct = QAction('New', self)        
        
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        
        self.email = QLineEdit(self)
        self.email.setGeometry(100,100,200,30)
        self.email.setPlaceholderText("Email")
        self.email.show()
        
        self.password = QLineEdit(self)
        self.password.setGeometry(100,150,200,30)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.show()
        
        
        self.button = QPushButton(self)
        self.button.setText("Login")
        self.button.setGeometry(150,220,100,30)
        self.button.clicked.connect(self.login)
        
        
    def login(self):
        email = self.email.text()
        password = self.password.text()
        
        if email == "" or password == "":
            QMessageBox.warning(self, "Invalid Credentials", "Please Provide Complete Name and Password" )
        else:
            
            self.email.hide()
            self.password.hide()
            self.button.hide()
            
            label = QLabel(self)
            label.setText("<h1>Welcome to Facebook</h1>")
            self.setStyleSheet('background: black')
            label.setStyleSheet('color: white')
            label.setAlignment(Qt.AlignCenter)
            label.show()
            self.setCentralWidget(label)
        
    
    
    
app = QApplication([])
w = window()
w.show()
app.exec()