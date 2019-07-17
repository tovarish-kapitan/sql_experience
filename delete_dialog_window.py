from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal
import sys

import delete_dialog
import plane_base

class DeleteDialogWindow(QtWidgets.QMainWindow, delete_dialog.Ui_MainWindow):
    set_base = pyqtSignal(bool)

    def __init__(self, pb, parent=None):
        super().__init__(parent)
        if pb is None:
            pass
        else:
            self.setupUi(self)
            self.pb = pb
            self.id_ = self.pb.selected_id

    def id_slot(self):
        self.id_ = self.pb.selected_id

    def delete_slot(self):
        self.pb.delete_record(self.id_)
        self.set_base.emit(True)
        self.close()


if __name__ == '__main__':
    pc = plane_base.PlaneBase()
    #pc.clean_bd()
    app = QApplication(sys.argv)
    ddw = DeleteDialogWindow(pc)
    ddw.show()
    app.exec_()
