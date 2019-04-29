from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal
import sys
import sqlite3

import plain_gui
import plane_base
import load_dialog_window
import add_dialog_window
import edit_dialog_window
import delete_dialog_window


class PlainGuiWindow(QtWidgets.QMainWindow, plain_gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.base_path = ''
        self.add_wind = None
        self.edit_wind = None
        self.delete_wind = None
        self.load_wind = None
        self.pc = None

    def add_slot(self):
        self.add_wind = add_dialog_window.AddDialogWindow(self.pc)
        self.add_wind.show()
        self.add_wind.set_base['bool'].connect(self.loadData)

    def edit_slot(self):
        self.edit_wind = edit_dialog_window.EditDialogWindow(self.pc)
        self.edit_wind.show()
        self.edit_wind.set_base['bool'].connect(self.loadData)

    def delete_slot(self):
        self.delete_wind = delete_dialog_window.DeleteDialogWindow(self.pc)
        self.delete_wind.show()
        self.delete_wind.set_base['bool'].connect(self.loadData)

    def load_slot(self):
        self.load_wind = load_dialog_window.LoadDialogWindow()
        self.load_wind.show()
        self.load_wind.set_base['bool'].connect(self.setbase)

    def setbase(self):
        self.pc = self.load_wind.pc
        self.loadData()

    def loadData(self):
        #####
        #####
        #####
        #path = self.load_wind.set_base_path()
        connection = sqlite3.connect('foo.db')
        query = "SELECT * FROM airplane_spec"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,
                                         QtWidgets.QTableWidgetItem(str(data)))
        connection.close()


if __name__ == '__main__':
    #pc.clean_bd()
    app = QApplication(sys.argv)
    pgw = PlainGuiWindow()
    pgw.show()
    #ldw.pc.print_all()
    app.exec_()
