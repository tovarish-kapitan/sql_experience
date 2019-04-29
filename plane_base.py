from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

import airplane_spec


class PlaneBase:
    def __init__(self, path_to_db):
        self.Base = declarative_base()
        self.Session = sessionmaker()
        self.engine = create_engine(path_to_db)  #'sqlite:///foo.db'
        self.Session.configure(bind=self.engine)
        self.session = self.Session()
        self.Base.metadata.create_all(self.engine)
        self.plane_class = airplane_spec.AirplaneSpec

    def clean_bd(self):
        self.session.query(self.plane_class).delete()
        self.session.commit()

    def add_record(self, airplane_type=1, radius=1000, distance=1000,
                   min_load_distance=1000, max_load_distance=1000, flight_duration_time=9000,
                   cruise_velocity=300, cruise_height=5000, min_velocity=300, max_roll_angle=10,
                   max_on_height_velocity=500, max_near_ground_velocity=500, patrol_velocity=400,
                   min_height=500, service_ceiling=25000, max_take_off_weight=20000, empty_weight=15000,
                   fuel_capacity=5000, max_load=2000, engine_type=1, engine_qty=1, engine_thrust=1000,
                   max_normal_overload=0, max_transverse_overload=0, path_to_cdo='no way',
                   path_to_cdi='no way', path_to_cl='no way', path_to_maximal='no way'):
        plane = self.plane_class(airplane_type, radius, distance, min_load_distance,
                                 max_load_distance, flight_duration_time, cruise_velocity,
                                 cruise_height, min_velocity, max_roll_angle,
                                 max_on_height_velocity, max_near_ground_velocity, patrol_velocity,
                                 min_height, service_ceiling, max_take_off_weight, empty_weight,
                                 fuel_capacity, max_load, engine_type, engine_qty, engine_thrust,
                                 max_normal_overload, max_transverse_overload, path_to_cdo,
                                 path_to_cdi, path_to_cl, path_to_maximal)
        self.session.add(plane)
        self.session.commit()

    def save_changes(self, id_, airplane_type, radius, distance, min_load_distance,
                     max_load_distance, flight_duration_time, cruise_velocity,
                     cruise_height, min_velocity, max_roll_angle,
                     max_on_height_velocity, max_near_ground_velocity, patrol_velocity,
                     min_height, service_ceiling, max_take_off_weight, empty_weight,
                     fuel_capacity, max_load, engine_type, engine_qty, engine_thrust,
                     max_normal_overload, max_transverse_overload, path_to_cdo,
                     path_to_cdi, path_to_cl, path_to_maximal):
        our_plain = self.session.query(self.plane_class).filter_by(target_type_id=id_).first()
        if our_plain is None:
            pass
        else:
            our_plain.airplane_type = airplane_type
            our_plain.radius = radius
            our_plain.distance = distance
            our_plain.min_load_distance = min_load_distance
            our_plain.max_load_distance = max_load_distance
            our_plain.flight_duration_time = flight_duration_time
            our_plain.cruise_velocity = cruise_velocity
            our_plain.cruise_height = cruise_height
            our_plain.min_velocity = min_velocity
            our_plain.max_roll_angle = max_roll_angle
            our_plain.max_on_height_velocity = max_on_height_velocity
            our_plain.max_near_ground_velocity = max_near_ground_velocity
            our_plain.patrol_velocity = patrol_velocity
            our_plain.min_height = min_height
            our_plain.service_ceiling = service_ceiling
            our_plain.max_take_off_weight = max_take_off_weight
            our_plain.empty_weight = empty_weight
            our_plain.fuel_capacity = fuel_capacity
            our_plain.max_load = max_load
            our_plain.engine_type = engine_type
            our_plain.engine_qty = engine_qty
            our_plain.engine_thrust = engine_thrust
            our_plain.max_normal_overload = max_normal_overload
            our_plain.max_transverse_overload = max_transverse_overload
            our_plain.path_to_cdo = path_to_cdo
            our_plain.path_to_cdi = path_to_cdi
            our_plain.path_to_cl = path_to_cl
            our_plain.path_to_maximal = path_to_maximal
            self.session.commit()

    def attributes_dictionary(self, id_):
        our_plain = self.session.query(self.plane_class).filter_by(target_type_id=id_).first()
        if our_plain is None:
            return None
        else:
            #print(our_plain)
            dictionary = {'airplane_type': our_plain.airplane_type,
                          'radius': our_plain.radius,
                          'distance': our_plain.distance,
                          'min_load_distance': our_plain.min_load_distance,
                          'max_load_distance': our_plain.max_load_distance,
                          'flight_duration_time': our_plain.flight_duration_time,
                          'cruise_velocity': our_plain.cruise_velocity,
                          'cruise_height': our_plain.cruise_height,
                          'min_velocity': our_plain.min_velocity,
                          'max_roll_angle': our_plain.max_roll_angle,
                          'max_on_height_velocity': our_plain.max_on_height_velocity,
                          'max_near_ground_velocity': our_plain.max_near_ground_velocity,
                          'patrol_velocity': our_plain.patrol_velocity,
                          'min_height': our_plain.min_height,
                          'service_ceiling': our_plain.service_ceiling,
                          'max_take_off_weight': our_plain.max_take_off_weight,
                          'empty_weight': our_plain.empty_weight,
                          'fuel_capacity': our_plain.fuel_capacity,
                          'max_load': our_plain.max_load,
                          'engine_type': our_plain.engine_type,
                          'engine_qty': our_plain.engine_qty,
                          'engine_thrust': our_plain.engine_thrust,
                          'max_normal_overload': our_plain.max_normal_overload,
                          'max_transverse_overload': our_plain.max_transverse_overload,
                          'path_to_cdo': our_plain.path_to_cdo,
                          'path_to_cdi': our_plain.path_to_cdi,
                          'path_to_cl': our_plain.path_to_cl,
                          'path_to_maximal': our_plain.path_to_maximal}
            return dictionary

    def print_all(self):
        for instance in self.session.query(self.plane_class).order_by(self.plane_class.target_type_id):
            print(instance)

    def delete_record(self, id_):
        our_plain = self.session.query(self.plane_class).filter_by(target_type_id=id_).first()
        if our_plain is None:
            assert "wtf"
        else:
            self.session.query(self.plane_class).filter_by(target_type_id=id_).delete()
            self.session.commit()
