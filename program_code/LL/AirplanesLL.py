<<<<<<< HEAD
from LL.Airplanes import *
from DB.DATA_API import *
from LL.LL_functions import *
import string

class AirplanesLL(LL_functions):

    def create_airplane(self,airplane_identity):
        """
        Creates a new employee and saves to database. \n
        airplane_identity = ('',plane_id, plane_type, manufacturer,model,name)
        """

        new_plane = Airplanes(*airplane_identity)
        registration_str = new_plane.get_registration_str()
        
        return_value = self.save_object_to_DB("airplane",registration_str)
        return return_value

    def change_airplane(self, changed_identity):
        """
        Changes information about airplane, except id or registration date.
        changed_identity = (id,plane_id, plane_type, manufacturer,model,name,registration_date)
        """

        changed_plane = Airplanes(*changed_identity)
        changed_str = changed_plane.get_changes_registration_str()
        return_value = self.change_object_in_DB("airplane", changed_str, changed_plane._id) # Bring 'id' seperately, so next function can find line number

        return return_value

        

    # def filter_available(self, all_planes):
    #     pass

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

    # def get_plane_list():        
    #     PlaneFilehandler = AirplaneFile()
    #     all_planes = PlaneFilehandler.start()
    #     all_planes_list = []
    #     for plane in all_planes:
    #         all_planes_list.append(plane.split(','))
    #     return all_planes_list


    # def create_plane(self, plane_id, plane_type, manufacturer, model, name):
    #     new_plane = Airplane(plane_id, plane_type, manufacturer, model, name)
    #     log_plain = AirplaneFile(data_to_append=str(new_plane))
    #     status = log_plain.start()
    #     return status

=======
from LL.Airplanes import *
from DB.DATA_API import *
from LL.LL_functions import *
import string

class AirplanesLL(LL_functions):

    def create_airplane(self,airplane_identity):
        """
        Creates a new employee and saves to database. \n
        airplane_identity = ('',plane_id, plane_type, manufacturer,model,name)
        """

        new_plane = Airplanes(*airplane_identity)
        registration_str = new_plane.get_registration_str()
        
        return_value = self.save_object_to_DB("airplane",registration_str)
        return return_value

    def change_airplane(self, changed_identity):
        """
        Changes information about airplane, except id or registration date.
        changed_identity = (id,plane_id, plane_type, manufacturer,model,name,registration_date)
        """

        changed_plane = Airplanes(*changed_identity)
        changed_str = changed_plane.get_changes_registration_str()
        return_value = self.change_object_in_DB("airplane", changed_str, changed_plane._id) # Bring 'id' seperately, so next function can find line number

        return return_value

    def get_plance_licence(self, keyword,date):
        """
        Gets list of plane types
        """
        searchparam = ""
        row_names = ['plane_type']
        match = False
        return_column = True

        new_list = LL_functions()
        filtered_list = list(set(new_list.get_filtered_list_from_DB(keyword,row_names, searchparam, match, return_column)))
        return filtered_list

    # def filter_planes(planes_list=[], a_header=''):
    #     header = planes_list[0]
    #     a_header_index = int
    #     for index, value in enumerate(header):
    #         if value == a_header:
    #             a_header_index = index
            
    #     types = []
        
    #     for a_list in planes_list[1:]:
    #         if a_list[a_header_index] not in types:
    #             types.append(a_list[a_header_index])

    #     return types

    # def get_plane_list():        
    #     PlaneFilehandler = AirplaneFile()
    #     all_planes = PlaneFilehandler.start()
    #     all_planes_list = []
    #     for plane in all_planes:
    #         all_planes_list.append(plane.split(','))
    #     return all_planes_list


    # def create_plane(self, plane_id, plane_type, manufacturer, model, name):
    #     new_plane = Airplane(plane_id, plane_type, manufacturer, model, name)
    #     log_plain = AirplaneFile(data_to_append=str(new_plane))
    #     status = log_plain.start()
    #     return status

>>>>>>> 96e14ad197cae6565070c566e998155ab0702624
