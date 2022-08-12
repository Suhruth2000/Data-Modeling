from curses import window
from http import server
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
import sys
import time
import os
import target_window as tw
import source_window as sw

class startupwindow(QMainWindow):
    user_name=""
    database_name=""
    password=""
    table_name=""

    def __init__(self):
        super().__init__()

        #Setting Title
        self.setWindowTitle("Target Database Details Window")

        #Setting Geometry
        self.setGeometry(100,60,1000,800)

        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()

    def UiComponents(self):

        #Heading
        self.heading_label=QLabel(self)
        self.heading_label.setText("Target Database Details")
        self.heading_label.setFont(QFont('Times',25))
        self.heading_label.adjustSize()
        self.heading_label.move(380,60)

        #Server_Name
        self.server_name_label=QLabel(self)
        self.server_name_label.setText("User Name")
        self.server_name_label.setFont(QFont('Times',20))
        self.server_name_label.adjustSize()
        self.server_name_label.move(450,130)

        self.server_name_box=QLineEdit(self)
        self.server_name_box.setGeometry(400,170,200,40)


        #Login_ID
        self.login_id_label=QLabel(self)
        self.login_id_label.setText("Database Name")
        self.login_id_label.setFont(QFont('Times',20))
        self.login_id_label.adjustSize()
        self.login_id_label.move(440,270)

        self.login_id_box=QLineEdit(self)
        self.login_id_box.setGeometry(400,310,200,40)


        #Password
        self.password_label=QLabel(self)
        self.password_label.setText("Password")
        self.password_label.setFont(QFont('Times',20))
        self.password_label.adjustSize()
        self.password_label.move(460,400)

        self.password_box=QLineEdit(self)
        self.password_box.setGeometry(400,440,200,40)

        self.table_name_label=QLabel(self)
        self.table_name_label.setText("Table Name")
        self.table_name_label.setFont(QFont('TImes',20))
        self.table_name_label.adjustSize()
        self.table_name_label.move(440,540)

        self.table_name_box=QLineEdit(self)
        self.table_name_box.setGeometry(400,580,200,40)

        self.password_button=QPushButton(self)
        self.password_button.setText("Confirm")
        self.password_button.clicked.connect(self.clickMethod_password)
        self.password_button.move(450,650)


    def clickMethod_password(self):
        self.user_name=self.server_name_box.text()
        self.database_name=self.login_id_box.text()
        self.password=self.password_box.text()
        self.table_name=self.table_name_box.text()
        self.next_window = sw.startupwindow(self)
        self.close()

if(__name__ == "__main__"):
    app=QApplication(sys.argv)
    window=startupwindow()
    app.exec_()
