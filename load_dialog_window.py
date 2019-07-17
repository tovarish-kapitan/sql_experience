from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal
import sys

import load_dialog
import plane_base


class LoadDialogWindow(QtWidgets.QMainWindow, load_dialog.Ui_Dialog):
    set_base = pyqtSignal(bool)

    def __init__(self, path_to_db, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.path_to_db = path_to_db  #'sqlite:///foo.db'
        self.pb = plane_base.PlaneBase(self.path_to_db)

    def set_text_slot(self):
        self.path_to_db = self.lineEdit.text()

    def load_slot(self):
        self.set_base.emit(True)
        self.close()
        #self.set_base_path.emit(self.path_to_db)
        #return self.pb

    def p_b(self):
        return self.pb

    def set_base_path(self):
        return self.path_to_db


if __name__ == '__main__':
    #pc.clean_bd()
    app = QApplication(sys.argv)
    ldw = LoadDialogWindow()
    ldw.show()
    #ldw.pc.print_all()
    app.exec_()
