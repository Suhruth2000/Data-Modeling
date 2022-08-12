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
import xml.etree.ElementTree as et
import source_window as sw
import database_details as db
import start_window as stw



class startupwindow(QMainWindow):

    transformation_details=[]

    def __init__(self, db_window, sw_window):
        super().__init__()

        self.sw_window = sw_window
        self.db_window = db_window

        self.name=db_window.user_name
        self.db_name=db_window.database_name
        self.password=db_window.password
        self.table_name=db_window.table_name

        self.mydb = mysql.connector.connect(user = self.name,
                               host = 'localhost',
                              database = self.db_name,
                              password = self.password)

        self.mycursor = self.mydb.cursor()

        #Setting Title
        self.setWindowTitle("Transformation Window")

        #Setting Geometry
        self.setGeometry(100,60,1000,800)

        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()

    def UiComponents(self):
        self.heading_label=QLabel(self)
        self.heading_label.setText("Transformations Tab")
        self.heading_label.setFont(QFont('Times',25))
        self.heading_label.adjustSize()
        self.heading_label.move(400,60)

        self.query="show columns from "+self.table_name+" in "+self.db_name

        self.mycursor.execute(self.query)
        self.table_schema=self.mycursor.fetchall()

        self.columns=[]
        for c in self.table_schema:
            self.columns.append(c[0])

        self.target_columns_label=QLabel(self)
        self.target_columns_label.setText('Target Columns')
        self.target_columns_label.setFont(QFont('Times',20))
        self.target_columns_label.adjustSize()
        self.target_columns_label.setGeometry(195,180,200,70)

        self.target_columns_drop=QComboBox(self)
        self.target_columns_drop.addItems(self.columns)
        self.target_columns_drop.setGeometry(185,230,200,70)

        self.transformation_type_label=QLabel(self)
        self.transformation_type_label.setText('Transformation Type')
        self.transformation_type_label.setFont(QFont('Times',20))
        self.transformation_type_label.adjustSize()
        self.transformation_type_label.setGeometry(430,180,200,70)

        self.transformation_type=QComboBox(self)
        self.transformation_type.addItems(['Numeric','Concat','Null','Conditional','VLookup','Date-Time','Date'])
        self.transformation_type.setGeometry(420,230,200,70)

        self.transformation_label=QLabel(self)
        self.transformation_label.setText('Transformation')
        self.transformation_label.setFont(QFont('Times',20))
        self.transformation_label.adjustSize()
        self.transformation_label.setGeometry(730,180,200,70)

        self.transformation=QLineEdit(self)
        self.transformation.setGeometry(650,240,300,40)

        self.add_transformation=QPushButton(self)
        self.add_transformation.setText('Add Transformation')
        self.add_transformation.clicked.connect(self.clickMethod_add)
        self.add_transformation.setGeometry(400,600,200,70)

        self.add_another_source=QPushButton(self)
        self.add_another_source.setText('Add Another Source')
        self.add_another_source.clicked.connect(self.clickMethod_add_source)
        self.add_another_source.setGeometry(100,600,200,70)

        self.source_column_list_label=QLabel(self)
        self.source_column_list_label.setText('Source Column List')
        self.source_column_list_label.setFont(QFont('Times',20))
        self.source_column_list_label.adjustSize()
        self.source_column_list_label.setGeometry(420,350,200,70)

        self.source_column_list_box=QComboBox(self)
        self.source_column_list_box.addItems(self.sw_window.source_column_list)
        self.source_column_list_box.setGeometry(400,400,200,70)

        self.save_config_label=QPushButton(self)
        self.save_config_label.setText("Save Config")
        self.save_config_label.clicked.connect(self.clickMethod_saved)
        self.save_config_label.setGeometry(700,600,200,70)





    def clickMethod_add(self):
        self.transformation_details.append([self.target_columns_drop.currentText(),
        self.transformation_type.currentText(),self.transformation.text()])

    def clickMethod_add_source(self):
        self.new_window=sw.startupwindow(self.db_window)
        self.close()
 
    def clickMethod_saved(self):
        print(self.transformation_details)
        self.back_window = stw.startupwindow()

        self.transformations_tag=et.Element("Transformations")

        for t in self.transformation_details:
            self.transformation_tag=et.SubElement(self.transformations_tag,"Transformation")

            self.target_column_tag=et.SubElement(self.transformation_tag,"Target Column Name")
            self.target_column_tag.text=t[0]

            self.transformation_type_tag=et.SubElement(self.transformation_tag,"Type")
            self.transformation_type_tag.text=t[1]

            self.transformation_formula_tag=et.SubElement(self.transformation_tag,"Formula")
            self.transformation_formula_tag.text=t[2]

        self.xmlstr=et.tostring(self.transformations_tag,encoding='utf8',method='xml')
        print(self.xmlstr)

        self.close()


        


if(__name__ == "__main__"):
    app=QApplication(sys.argv)
    #window=startupwindow(db.window)
    app.exec_()





