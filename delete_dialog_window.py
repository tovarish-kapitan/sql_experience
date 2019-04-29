from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal
import sys

import delete_dialog
import plane_base

class DeleteDialogWindow(QtWidgets.QMainWindow, delete_dialog.Ui_MainWindow):
    set_base = pyqtSignal(bool)

    def __init__(self, pc, parent=None):
        super().__init__(parent)
        if pc is None:
            pass
        else:
            self.setupUi(self)
            self.pc = pc
            self.id_ = -1

    def id_slot(self):
        self.id_ = self.spinBox.value()

    def delete_slot(self):
        self.pc.delete_record(self.id_)
        self.set_base.emit(True)


if __name__ == '__main__':
    pc = plane_base.PlaneBase()
    #pc.clean_bd()
    app = QApplication(sys.argv)
    ddw = DeleteDialogWindow(pc)
    ddw.show()
    app.exec_()
