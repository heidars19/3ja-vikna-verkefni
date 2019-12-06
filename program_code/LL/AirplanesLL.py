from LL.Airplanes import Airplane
from DB.DATA_API import *
from LL.LL_functions import *
import string

class AirplanesLL(LL_functions):

    #Útfærði þetta á sama hátt og hjá employee þar sem við notum save_object_to_DB function til að vista hvað sem er og unpökkum hér
    def create_airplane(self,airplane_identity):
        '''Creates a new airplane and saves to database'''
        print (airplane_identity)
        _id,plane_id, plane_type, manufacturer, model, name  = airplane_identity
        new_plane = Airplane(_id,plane_id, plane_type, manufacturer, model, name, registration_date='')

        data_string = new_plane.registration()

        LL_functions.save_object_to_DB("airplane",data_string)

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

    def get_plane_list():        
        PlaneFilehandler = AirplaneFile()
        all_planes = PlaneFilehandler.start()
        all_planes_list = []
        for plane in all_planes:
            all_planes_list.append(plane.split(','))
        return all_planes_list


    # def create_plane(self, plane_id, plane_type, manufacturer, model, name, capacity):
    #     new_plane = Airplane(plane_id, plane_type, manufacturer, model, name, capacity)
    #     log_plain = AirplaneFile(data_to_append=str(new_plane))
    #     status = log_plain.start()
    #     return status


    def change_plane(self, new_info):
        new_plane_id, new_plane_type, new_manufacturer, new_model, new_name, new_capacity = new_info
        updated_plain = Airplane(new_plane_id, new_plane_type, new_manufacturer, new_model, new_name, new_capacity)
        
        line_in_db = AirplaneFile(fieldname="plane_id",searchparam=new_plane_id)

        PlaneFilehandler = AirplaneFile(line_to_replace=line_in_db, replace_with=str(updated_plane))
        PlaneFilehandler.start()
    
    