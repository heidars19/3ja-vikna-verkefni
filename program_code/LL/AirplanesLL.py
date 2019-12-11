from LL.Airplanes import *
from DB.DATA_API import *
from LL.LL_functions import *
import string

class AirplanesLL(LL_functions):

    def create_airplane(self,airplane_identity):
        """
        Creates new instance of airplane and saves to database. \n
        airplane_identity = ('',plane_id, plane_type, manufacturer,capacity,name)\n
        """
        new_plane = Airplanes(*airplane_identity)
        registration_str = new_plane.get_registration_str() #get string with registration attributes
        save_process = self.save_object_to_DB("airplane",registration_str)

        return save_process 

    def change_airplane(self, changed_identity):
        """
        Changes information about airplane, except id or registration date. \n
        changed_identity = (id,plane_id, plane_type, manufacturer,capacity,name,registration_date)
        """

        changed_plane = Airplanes(*changed_identity)
        changed_str = changed_plane.get_changes_registration_str() #get string with all attributes
        change_process = self.change_object_in_DB("airplane", changed_str, changed_plane._id) #_id so next function can find line to overwrite with changes

        return change_process

    def get_plane_licence(self):
        """
        Returns list of plane types representing licences.
        """

        row_names = ['plane_type']
        index_list = self.find_index_from_header('airplane', row_names) 

        filtered_list = list(set(self.get_filtered_list_from_DB('airplane',index_list, exact_match = False, return_column=True)))
        
        return filtered_list