from curses import window
from http import server
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
import sys
import time
import os
import database_details as db
import target_window as tw
import pandas as pd

class startupwindow(QMainWindow):
    source_details=[]
    source_column_list=[]

    def __init__(self, database_window):

        self.db_window = database_window
        super().__init__()

        #Setting Title
        self.setWindowTitle("Source Window")

        #Setting Geometry
        self.setGeometry(100,60,1000,800)

        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()

    def UiComponents(self):
        self.heading_label=QLabel(self)
        self.heading_label.setText("Source File Details")
        self.heading_label.setFont(QFont('Times',25))
        self.heading_label.adjustSize()
        self.heading_label.move(380,40)


        self.source_type_label=QLabel(self)
        self.source_type_label.setText("Select Source File Type")
        self.source_type_label.setFont(QFont('Times',20))
        self.source_type_label.adjustSize()
        self.source_type_label.move(390,100)

        self.source_type_combo_box=QComboBox(self)
        self.source_type_list=['Xlsx','CSV','SQL']
        self.source_type_combo_box.addItems(self.source_type_list)
        self.source_type_combo_box.setGeometry(385,130,200,70)


        self.source_path_label=QLabel(self)
        self.source_path_label.setText("Enter Source File Path (For CSV and Xlsx File)")
        self.source_path_label.setFont(QFont('Times',20))
        self.source_path_label.adjustSize()
        self.source_path_label.move(350,220)

        self.source_path=QLineEdit(self)
        self.source_path.setGeometry(390,270,200,40)

        self.server_name_label=QLabel(self)
        self.server_name_label.setText("User Name(For SQL File)")
        self.server_name_label.setFont(QFont('Times',20))
        self.server_name_label.adjustSize()
        self.server_name_label.move(370,320)

        self.server_name_box=QLineEdit(self)
        self.server_name_box.setGeometry(390,370,200,40)

        self.login_id_label=QLabel(self)
        self.login_id_label.setText("Database Name(For SQL File)")
        self.login_id_label.setFont(QFont('Times',20))
        self.login_id_label.adjustSize()
        self.login_id_label.move(370,420)

        self.login_id_box=QLineEdit(self)
        self.login_id_box.setGeometry(390,470,200,40)

        self.password_label=QLabel(self)
        self.password_label.setText("Password(For SQL File)")
        self.password_label.setFont(QFont('Times',20))
        self.password_label.adjustSize()
        self.password_label.move(380,520)

        self.password_box=QLineEdit(self)
        self.password_box.setGeometry(390,570,200,40)

        self.table_name_label=QLabel(self)
        self.table_name_label.setText("Table Name(For SQL File)")
        self.table_name_label.setFont(QFont('TImes',20))
        self.table_name_label.adjustSize()
        self.table_name_label.move(380,620)

        self.table_name_box=QLineEdit(self)
        self.table_name_box.setGeometry(390,670,200,40)

        self.source_path_confirm=QPushButton(self)
        self.source_path_confirm.setText('Confirm')
        self.source_path_confirm.clicked.connect(self.clickMethod_pconfirm)
        self.source_path_confirm.move(440,720)
        
        

    def clickMethod_pconfirm(self):
        self.source_details.append(self.source_type_combo_box.currentText())
        if(self.source_details[0]=='CSV'):
            self.source_details.append(self.source_path.text())
            data=pd.read_csv(self.source_details[1])
            self.source_column_list=list(data.columns)
        elif(self.source_details[0]=='Xlsx'):
            self.source_details.append(self.source_path.text())
            data=pd.read_excel(self.source_details[1])
            self.source_column_list=list(data.columns)
        else:
            self.source_details.append(self.server_name_box.text())
            self.source_details.append(self.login_id_box.text())
            self.source_details.append(self.password_box.text())
            self.source_details.append(self.table_name_box.text())
            self.mydb=mysql.connector.connect(user=self.source_details[1],
                                              host='localhost',database=self.source_details[2],
                                              password=self.source_details[3])
            self.mycursor = self.mydb.cursor()
            self.query="show columns from "+self.source_details[4]+" in "+self.source_details[2]

            self.mycursor.execute(self.query)
            self.table_schema=self.mycursor.fetchall()

            for c in self.table_schema:
                self.source_column_list.append(c[0])
        
        
        self.new_window = tw.startupwindow(self.db_window, self)

        self.close()

if(__name__ == "__main__"):
    app=QApplication(sys.argv)
    #window=startupwindow(db.window)
    app.exec_()
