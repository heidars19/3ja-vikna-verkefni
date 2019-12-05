#from DB.DATA_API import * eigum ekki að tala beint við db
from LL.Airplanes import *
from LL.Destination import *

#----------------------------------------------------------------------------------------------

#Airplanes
class LL_API():
    def get_airplane_types(self):
        all_planes = Airplane.get_airplane_list()
        filtered_planes = Airplane.filter_planes(all_planes, model)
        return filtered_planes

    def get_all_airplanes(self):
        all_planes = Airplane.get_all_planes()
        return all_planes

    def create_airplane(self, plane_id, plane_type, manufacturer, model, name, capacity):
        new_plain = Airplane(planeID, planeType, manufacturer, model, name, capacity)
        new_plain.save_airplane()

