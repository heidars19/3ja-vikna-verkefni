from LL.Airplanes import Airplane
from DB.DATA_API import *
import string

class AirplanesLL():

    def filter_available(self, all_planes):
        pass


    def filter_planes(planes_list=[], a_header=''):
        header = planes_list[0]
        a_header_index = int
        for index, value in enumerate(header):
            if value == a_header:
                a_header_index = index
            
        types = []
        
        for a_list in planes_list[1:]:
            if a_list[a_header_index] not in types:
                types.append(a_list[a_header_index])

        return types


    def get_airplane_list():        
        PlaneFilehandler = AirplaneFile()
        all_planes = PlaneFilehandler.start()
        all_planes_list = []
        for plane in all_planes:
            all_planes_list.append(plane.split(','))
        return all_planes_list


    def save_airplane(self, plane_id, plane_type, manufacturer, model, name, capacity):
        new_plane = Airplane(plane_id, plane_type, manufacturer, model, name, capacity)
        log_plain = AirplaneFile(data_to_append=str(new_plane))
        status = log_plain.start()
        return status


    def change_airplane(self, new_info):
        new_plane_id, new_plane_type, new_manufacturer, new_model, new_name, new_capacity = new_info
        line_in_db = AirplaneFile(fieldname="plane_id",searchparam=new_plane_id)
        
        if line_in_db == 0:
            return False, "Flugvél ekki til í gagnagrunni"
        if line_in_db == -1:
            return False, "Villa kom upp!"
        
        new_info_plane = Airplane(new_plane_id, new_plane_type, new_manufacturer, new_model, new_name, new_capacity)
        PlaneFilehandler = AirplaneFile(line_to_replace=line_in_db, replace_with=str(new_info_plane))
        status = PlaneFilehandler.start()        
        return status
    
