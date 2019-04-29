from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AirplaneSpec(Base):
    __tablename__ = 'airplane_spec'

    target_type_id = Column(Integer, comment='Идентификатор типа цели',primary_key=True)
    airplane_type = Column(Integer, comment='Тип самолета (1-Самолет СА, 2-Многоцелевой истребитель,'
                                            ' 3-Штурмовик, 4-Самолет-разведчик,5-Самолет РЭБ, 6-Самолет ДРЛО)')
    radius = Column(Float, comment='Тактический радиус полета, м')
    distance = Column(Float, comment='Дальность полета, м')
    min_load_distance = Column(Float, comment='Дальность полета с минимальной загрузкой, м')
    max_load_distance = Column(Float, comment='Дальность полета с максимальнойй загрузкой, м')
    flight_duration_time = Column(Float, comment='Продолжительность полета, с')
    cruise_velocity = Column(Float, comment='Крейсерская скорость, м/с')
    cruise_height = Column(Float, comment='Высота крейсерского полета, м')
    min_velocity = Column(Float, comment='Минимальная скорость полета, м/с')
    max_roll_angle = Column(Float, comment='Максимальный угол крена, рад.')
    max_on_height_velocity = Column(Float, comment='Максимальная скорость полета на высоте, м/с')
    max_near_ground_velocity = Column(Float, comment='Максимальная скорость полета у земли, м/с')
    patrol_velocity = Column(Float, comment='Скорость барражирования, м/с')
    min_height = Column(Float, comment='Минимальная высота полета, м')
    service_ceiling = Column(Float, comment='Практический потолок, м')
    max_take_off_weight = Column(Float, comment='Максимальная взлетная масса, кг')
    empty_weight = Column(Float, comment='Масса пустого, кг')
    fuel_capacity = Column(Float, comment='Масса топлива во внутренних баках, кг')
    max_load = Column(Float, comment='Максимальная боевая нагрузка, кг')
    engine_type = Column(Integer, comment='Тип силовой установки')
    engine_qty = Column(Integer, comment='Количетво двигателей')
    engine_thrust = Column(Float, comment='Тяга каждого двигателя, кг')
    max_normal_overload = Column(Float, comment='Максимальная нормальная перегрузка, g')
    max_transverse_overload = Column(Float, comment='Максимальная трансверсальная перегрузка, g')
    path_to_cdo = Column(String, comment='Путь к файлу зависимости коэффициентa '
                                         'лобового сопротивления при нулевом '
                                         'угле атаки в зависимости от числа Маха')
    path_to_cdi = Column(String, comment='Путь к файлу зависимости коэффициента '
                                         'лобового сопротивления в зависимости от числа Маха '
                                         'и коэффициента подъемной силы',)
    path_to_cl = Column(String, comment='Путь к файлу зависимости тяги двигателя '
                                        'на режиме "Максимал" в зависимости '
                                        'от высоты полета и числа Маха')
    path_to_maximal = Column(String, comment='Путь к файлу зависимости тяги двигателя'
                                             ' на режиме "Максимал" в зависимости'
                                             ' от высоты полета и числа Маха')


    def __init__(self, airplane_type=1, radius=1000, distance=1000,
                 min_load_distance=1000, max_load_distance=1000, flight_duration_time=9000,
                 cruise_velocity=300, cruise_height=5000, min_velocity=300, max_roll_angle=10,
                 max_on_height_velocity=500, max_near_ground_velocity=500, patrol_velocity=400,
                 min_height=500, service_ceiling=25000, max_take_off_weight=20000, empty_weight=15000,
                 fuel_capacity=5000, max_load=2000, engine_type=1, engine_qty=1, engine_thrust=1000,
                 max_normal_overload=0, max_transverse_overload=0, path_to_cdo='no way',
                 path_to_cdi='no way', path_to_cl='no way', path_to_maximal='no way'):
        self.airplane_type = airplane_type
        self.radius = radius
        self.distance = distance
        self.min_load_distance = min_load_distance
        self.max_load_distance = max_load_distance
        self.flight_duration_time = flight_duration_time
        self.cruise_velocity = cruise_velocity
        self.cruise_height = cruise_height
        self.min_velocity = min_velocity
        self.max_roll_angle = max_roll_angle
        self.max_on_height_velocity = max_on_height_velocity
        self.max_near_ground_velocity = max_near_ground_velocity
        self.patrol_velocity = patrol_velocity
        self.min_height = min_height
        self.service_ceiling = service_ceiling
        self.max_take_off_weight = max_take_off_weight
        self.empty_weight = empty_weight
        self.fuel_capacity = fuel_capacity
        self.max_load = max_load
        self.engine_type = engine_type
        self.engine_qty = engine_qty
        self.engine_thrust = engine_thrust
        self.max_normal_overload = max_normal_overload
        self.max_transverse_overload = max_transverse_overload
        self.path_to_cdo = path_to_cdo
        self.path_to_cdi = path_to_cdi
        self.path_to_cl = path_to_cl
        self.path_to_maximal = path_to_maximal

    def __repr__(self):
        return "<Самолет вероятного союзника(id'%s',type'%s',rad'%s')>" % (self.target_type_id, self.airplane_type, self.radius)

