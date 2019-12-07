from LL.Airplanes import *
from DB.DATA_API import *
from LL.LL_functions import *
import string

class AirplanesLL(LL_functions):

    #Útfærði þetta á sama hátt og hjá employee þar sem við notum save_object_to_DB function til að vista hvað sem er og unpökkum hér
    def create_airplane(self,airplane_identity):
        '''Creates a new airplane and saves to database'''
        
        new_plane = Airplanes(*airplane_identity, registration_date='')
        registration_str = new_plane.get_registration_str()
        
        print(registration_str)
        self.save_object_to_DB("airplane",registration_str)

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


    # def create_plane(self, plane_id, plane_type, manufacturer, model, name):
    #     new_plane = Airplane(plane_id, plane_type, manufacturer, model, name)
    #     log_plain = AirplaneFile(data_to_append=str(new_plane))
    #     status = log_plain.start()
    #     return status


    def change_airplane(self, new_info):
        new_id, new_plane_id, new_plane_type, new_manufacturer, new_model, new_name, registration_date = new_info
        
        new_dest = Airplanes(*new_info)
        registration_str = new_dest.get_changes_registration_str()

        return_value = self.change_object_in_DB("airplane", registration_str, new_id) # Bring 'id' seperately, so next function can find line number

        return return_value