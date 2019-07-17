from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal
import sys
from sqlalchemy import create_engine


import plane_gui_wid
import plane_gui
import plane_base
import load_dialog_window
import add_dialog_window
import edit_dialog_window
import delete_dialog_window


#class PlaneGuiWindow(QtWidgets.QMainWindow, plane_gui_wid.Ui_MainWindow):
class PlaneGuiWindow(QtWidgets.QMainWindow, plane_gui_wid.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.base_path = 'sqlite:///foo.db'
        self.add_wind = None
        self.edit_wind = None
        self.delete_wind = None
        self.load_wind = None
        self.pb = None
        self.selected_row = None
        self.tableWidget.setHorizontalHeaderLabels(['id', 'airplane_type', 'radius', 'distance',
                                                    'min_load_distance', 'max_load_distance', 'flight_duration_time',
                                                    'cruise_velocity', 'cruise_height', 'min_velocity',
                                                    'max_roll_angle',
                                                    'max_on_height_velocity', 'max_near_ground_velocity',
                                                    'patrol_velocity',
                                                    'min_height', 'service_ceiling', 'max_take_off_weight',
                                                    'empty_weight',
                                                    'fuel_capacity', 'max_load', 'engine_type', 'engine_qty',
                                                    'engine_thrust',
                                                    'max_normal_overload', 'max_transverse_overload', 'path_to_cdo',
                                                    'path_to_cdi', 'path_to_cl', 'path_to_maximal'])

    #def add_slot(self):
    #    self.add_wind = add_dialog_window.AddDialogWindow(self.pb)
    #    self.add_wind.show()
    #    self.add_wind.set_base['bool'].connect(self.loadData)

    def add_slot(self):
        self.pb.add_record()
        self.load_data()

    def edit_slot(self):
        self.edit_wind = edit_dialog_window.EditDialogWindow(self.pb)
        self.edit_wind.show()
        self.edit_wind.set_base['bool'].connect(self.load_data)
        self.edit_wind.load_record()

    def delete_slot(self):
        self.delete_wind = delete_dialog_window.DeleteDialogWindow(self.pb)
        self.delete_wind.show()
        self.delete_wind.set_base['bool'].connect(self.load_data)

    def load_slot(self):
        self.load_wind = load_dialog_window.LoadDialogWindow(self.base_path)
        self.load_wind.show()
        self.load_wind.set_base['bool'].connect(self.setbase)

    def setbase(self):
        #self.load_wind.load_slot()
        self.pb = self.load_wind.p_b()
        self.load_data()

    def select_row(self, n):
        self.tableWidget.selectRow(n)
        id = int(self.tableWidget.item(n, 0).text())
        self.pb.set_selected_id(id)
        if self.edit_wind is not None:
            self.edit_wind.load_record()
        self.selected_row = n

    def load_data(self):
        engine = create_engine(self.base_path)
        connection = engine.connect()
        query = "SELECT * FROM airplane_spec"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,
                                         QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
        if self.selected_row is not None:
            self.tableWidget.selectRow(self.selected_row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pgw = PlaneGuiWindow()
    pgw.show()
    app.exec_()
