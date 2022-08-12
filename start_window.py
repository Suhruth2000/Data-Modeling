import sys
sys.settrace
from curses import window
from http import server
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
import time
import os
import database_details as db_window
class startupwindow(QMainWindow):

    def __init__(self):
        super().__init__()

        #Setting Title
        self.setWindowTitle("SETL Window")

        #Setting Geometry
        self.setGeometry(100,60,1000,800)

        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()

    def UiComponents(self):

        self.heading_label=QLabel(self)
        self.heading_label.setText('SETL')
        self.heading_label.setFont(QFont('Times',45))
        self.heading_label.adjustSize()
        self.heading_label.move(430,60)

        self.existing_xml=os.listdir('/Users/ayush/Documents/Data Modelling/configs')
        self.existing_xml.reverse()
        
        self.use_existing_list_box=QComboBox(self)
        self.use_existing_list_box.addItems(self.existing_xml)
        self.use_existing_list_box.setGeometry(350,150,300,100)

        self.use_existing_button=QPushButton(self)
        self.use_existing_button.setText('Use Existing Config')
        self.use_existing_button.setFont(QFont('Times',30))
        self.use_existing_button.clicked.connect(self.clickMethod_use_existing)
        self.use_existing_button.setGeometry(350,250,300,150)

        self.create_new_button=QPushButton(self)
        self.create_new_button.setText('Create New Config')
        self.create_new_button.setFont(QFont('Times',30))
        self.create_new_button.clicked.connect(self.clickMethod_create_new)
        self.create_new_button.setGeometry(350,500,300,200)




    def clickMethod_use_existing(self):
        self.close()

    def clickMethod_create_new(self):
        self.new_window = db_window.startupwindow()
        self.close()

if(__name__ == "__main__"):
    app=QApplication(sys.argv)
    window=startupwindow()
    app.exec_()