from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal
import sys

import edit_dialog
import plane_base


class EditDialogWindow(QtWidgets.QMainWindow, edit_dialog.Ui_edit_dialog_window):
    airplane_type_set = pyqtSignal(int)
    radius_set = pyqtSignal(float)
    distance_set = pyqtSignal(float)
    min_load_distance_set = pyqtSignal(float)
    max_load_distance_set = pyqtSignal(float)
    flight_duration_time_set = pyqtSignal(float)
    cruise_velocity_set = pyqtSignal(float)
    cruise_height_set = pyqtSignal(float)
    min_velocity_set = pyqtSignal(float)
    max_roll_angle_set = pyqtSignal(float)
    max_on_height_velocity_set = pyqtSignal(float)
    max_near_ground_velocity_set = pyqtSignal(float)
    patrol_velocity_set = pyqtSignal(float)
    min_height_set = pyqtSignal(float)
    service_ceiling_set = pyqtSignal(float)
    max_take_off_weight_set = pyqtSignal(float)
    empty_weight_set = pyqtSignal(float)
    fuel_capacity_set = pyqtSignal(float)
    max_load_set = pyqtSignal(float)
    engine_type_set = pyqtSignal(int)
    engine_qty_set = pyqtSignal(int)
    engine_thrust_set = pyqtSignal(float)
    max_normal_overload_set = pyqtSignal(float)
    max_transverse_overload_set = pyqtSignal(float)
    path_to_cdo_set = pyqtSignal(str)
    path_to_cdi_set = pyqtSignal(str)
    path_to_cl_set = pyqtSignal(str)
    path_to_maximal_set = pyqtSignal(str)
    set_base = pyqtSignal(bool)

    def __init__(self, pb, parent=None):
        super().__init__(parent)
        if pb is None:
            pass
        else:
            self.setupUi(self)
            self.pb = pb
            self.id_ = self.pb.selected_id
            self.airplane_type = 0
            self.radius = 0
            self.distance = 0
            self.min_load_distance = 0
            self.max_load_distance = 0
            self.flight_duration_time = 0
            self.cruise_velocity = 0
            self.cruise_height = 0
            self.min_velocity = 0
            self.max_roll_angle = 0
            self.max_on_height_velocity = 0
            self.max_near_ground_velocity = 500
            self.patrol_velocity = 400
            self.min_height = 500
            self.service_ceiling = 25000
            self.max_take_off_weight = 20000
            self.empty_weight = 15000
            self.fuel_capacity = 5000
            self.max_load = 2000
            self.engine_type = 1
            self.engine_qty = 1
            self.engine_thrust = 1000
            self.max_normal_overload = 0
            self.max_transverse_overload = 0
            self.path_to_cdo = 'no way'
            self.path_to_cdi = 'no way'
            self.path_to_cl = 'no way'
            self.path_to_maximal = 'no way'

    def set_airplane_type(self):
        self.airplane_type = self.airplane_type_.value()

    def set_radius(self):
        self.radius = self.radius_.value()

    def set_distance(self):
        self.distance = self.distance_.value()

    def set_min_load_distance(self):
        self.min_load_distance = self.min_load_distance_.value()

    def set_max_load_distance(self):
        self.max_load_distance = self.max_load_distance_.value()

    def set_flight_duration_time(self):
        self.flight_duration_time = self.flight_duration_time_.value()

    def set_cruise_velocity(self):
        self.cruise_velocity = self.cruise_velocity_.value()

    def set_cruise_height(self):
        self.cruise_height = self.cruise_height_.value()

    def set_min_velocity(self):
        self.min_velocity = self.min_velocity_.value()

    def set_max_roll_angle(self):
        self.max_roll_angle = self.max_roll_angle_.value()

    def set_max_on_height_velocity(self):
        self.max_on_height_velocity = self.max_on_height_velocity_.value()

    def set_max_near_ground_velocity(self):
        self.max_near_ground_velocity = self.max_near_ground_velocity_.value()

    def set_patrol_velocity(self):
        self.patrol_velocity = self.patrol_velocity_.value()

    def set_min_height(self):
        self.min_height = self.min_height_.value()

    def set_service_ceiling(self):
        self.service_ceiling = self.service_ceiling_.value()

    def set_max_take_off_weight(self):
        self.max_take_off_weight = self.max_take_off_weight_.value()

    def set_empty_weight(self):
        self.empty_weight = self.empty_weight_.value()

    def set_fuel_capicity(self):
        self.fuel_capacity = self.fuel_capacity_.value()

    def set_max_load(self):
        self.max_load = self.max_load_.value()

    def set_engine_type(self):
        self.engine_type = self.engine_type_.value()

    def set_engine_qty(self):
        self.engine_qty = self.engine_qty_.value()

    def set_engine_thrust(self):
        self.engine_thrust = self.engine_thrust_.value()

    def set_max_normal_overload(self):
        self.max_normal_overload = self.max_normal_overload_.value()

    def set_max_transverse_overload(self):
        self.max_transverse_overload = self.max_transverse_overload_.value()

    def set_path_to_cdo(self):
        self.path_to_cdo = self.path_to_cdo_.text()

    def set_path_to_cdi(self):
        self.path_to_cdi = self.path_to_cdi_.text()

    def set_path_to_ci(self):
        self.path_to_cl = self.path_to_cl_.text()

    def set_path_to_maximal(self):
        self.path_to_maximal = self.path_to_maximal_.text()

    def save_changes(self):
        self.pb.save_changes(self.id_, self.airplane_type, self.radius, self.distance, self.min_load_distance,
                             self.max_load_distance, self.flight_duration_time, self.cruise_velocity,
                             self.cruise_height, self.min_velocity, self.max_roll_angle,
                             self.max_on_height_velocity, self.max_near_ground_velocity, self.patrol_velocity,
                             self.min_height, self.service_ceiling, self.max_take_off_weight, self.empty_weight,
                             self.fuel_capacity, self.max_load, self.engine_type, self.engine_qty, self.engine_thrust,
                             self.max_normal_overload, self.max_transverse_overload, self.path_to_cdo,
                             self.path_to_cdi, self.path_to_cl, self.path_to_maximal)
        self.set_base.emit(True)

    def load_record(self):
        #self.id_ = self.load_record_.value()
        self.id_ = self.pb.selected_id
        d = self.pb.attributes_dictionary(self.id_)
        if d is None:
            pass
        else:
            self.airplane_type = d['airplane_type']
            self.radius = d['radius']
            self.distance = d['distance']
            self.min_load_distance = d['min_load_distance']
            self.max_load_distance = d['max_load_distance']
            self.flight_duration_time = d['flight_duration_time']
            self.cruise_velocity = d['cruise_velocity']
            self.cruise_height = d['cruise_height']
            self.min_velocity = d['min_velocity']
            self.max_roll_angle = d['max_roll_angle']
            self.max_on_height_velocity = d['max_on_height_velocity']
            self.max_near_ground_velocity = d['max_near_ground_velocity']
            self.patrol_velocity = d['patrol_velocity']
            self.min_height = d['min_height']
            self.service_ceiling = d['service_ceiling']
            self.max_take_off_weight = d['max_take_off_weight']
            self.empty_weight = d['empty_weight']
            self.fuel_capacity = d['fuel_capacity']
            self.max_load = d['max_load']
            self.engine_type = d['engine_type']
            self.engine_qty = d['engine_qty']
            self.engine_thrust = d['engine_thrust']
            self.max_normal_overload = d['max_normal_overload']
            self.max_transverse_overload = d['max_transverse_overload']
            self.path_to_cdo = d['path_to_cdo']
            self.path_to_cdi = d['path_to_cdi']
            self.path_to_cl = d['path_to_cl']
            self.path_to_maximal = d['path_to_cdi']

            self.airplane_type_set.emit(self.airplane_type)
            self.radius_set.emit(self.radius)
            self.distance_set.emit(self.distance)
            self.min_load_distance_set.emit(self.min_load_distance)
            self.max_load_distance_set.emit(self.max_load_distance)
            self.flight_duration_time_set.emit(self.flight_duration_time)
            self.cruise_velocity_set.emit(self.cruise_velocity)
            self.cruise_height_set.emit(self.cruise_height)
            self.min_velocity_set.emit(self.min_velocity)
            self.max_roll_angle_set.emit(self.max_roll_angle)
            self.max_on_height_velocity_set.emit(self.max_on_height_velocity)
            self.max_near_ground_velocity_set.emit(self.max_near_ground_velocity)
            self.patrol_velocity_set.emit(self.patrol_velocity)
            self.min_height_set.emit(self.min_height)
            self.service_ceiling_set.emit(self.service_ceiling)
            self.max_take_off_weight_set.emit(self.max_take_off_weight)
            self.empty_weight_set.emit(self.empty_weight)
            self.fuel_capacity_set.emit(self.fuel_capacity)
            self.max_load_set.emit(self.max_load)
            self.engine_type_set.emit(self.engine_type)
            self.engine_qty_set.emit(self.engine_qty)
            self.engine_thrust_set.emit(self.engine_thrust)
            self.max_normal_overload_set.emit(self.max_normal_overload)
            self.max_transverse_overload_set.emit(self.max_transverse_overload)
            self.path_to_cdo_set.emit(self.path_to_cdo)
            self.path_to_cdi_set.emit(self.path_to_cdi)
            self.path_to_cl_set.emit(self.path_to_cl)
            self.path_to_maximal_set.emit(self.path_to_maximal)


if __name__ == '__main__':
    pb = plane_base.PlaneBase()
    #pb.clean_bd()
    app = QApplication(sys.argv)
    edw = EditDialogWindow(pb)
    edw.show()
    app.exec_()
    pb.print_all()