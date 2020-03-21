#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:57:20 2020

@author: crmahesh
"""


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import urllib
import os
import os.path

from PyQt5.uic import loadUiType


ui,_ = loadUiType("main.ui")

class MainApp(QMainWindow, ui):
    
    
    
    def __init__(self, parent=None):
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.init_ui()
        self.handle_buttons()
        
    
    def init_ui(self):
        
        pass
    
    def handle_buttons(self):
        self.pushButton.clicked.connect(self.download)
        self.pushButton_2.clicked.connect(self.handle_browse)
        pass
    
    def handle_progress(self, blocknumber, blocksize, totalsize):
        readed_data = blocknumber  * blocksize
        total_data = totalsize
        
        if totalsize > 0:
            download_percentage = ( readed_data / total_data ) * 100
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()
        
    
    def handle_browse(self):
        save_location = QFileDialog.getSaveFileName(self, caption = "Save as", 
                                                    directory = ".", filter="All Files(*.*)")
        
        print(save_location)
        self.lineEdit_2.setText(str(save_location[0]))
    
    def download(self):
        print("Starting Download")
        
        download_url = self.lineEdit.text()
        
        
        save_location = self.lineEdit_2.text()
        
        
        if download_url == "" or save_location == "":
            QMessageBox.warning(self, "Data Error", "Provide a Valid URl or save Location")
        else:
            try:
                urllib.request.urlretrieve(download_url, save_location ,self.handle_progress)
            except:
                QMessageBox.warning(self, "Downloaded Error", "Proivde a valid URL or download Location.")
        
        QMessageBox.information(self, "Download Complete", "The file is downloaded.")
        
        
        self.progressBar.setValue(0)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        

    def save_browse(self):
        pass
        


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    
    window.show()
    app.exec_()
    

main()