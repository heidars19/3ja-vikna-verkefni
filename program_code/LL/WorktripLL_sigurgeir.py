from LL.Worktrip import *
from DB.DATA_API import *
from LL.LL_functions import *
import string

class WorktripLL(LL_functions):

    def create_worktrip(self,worktrip_identity):
        """
        Creates a new worktrip and saves to database. \n
        worktrip_identity = ('',flight_number_out, flight_number_home,departing_from, arriving_at, departure, arrival, aircraft_id)
        """

        new_worktrip = Worktrip(*worktrip_identity)
        registration_str = new_worktrip.get_registration_str()

        return_value = self.save_object_to_DB("worktrip",registration_str)
        return return_value
    




    def get_emp_dest_date(self, keyword,date):
        """
        Gets list of employees enrolled in a worktrip at specified date, and the destinations.\n
        Date format: YYYY-MM-DD
        """

        row_names = ['departure','arrival']

        new_list = LL_functions()
        index_list = new_list.find_index_from_header(keyword, row_names)
        print ( index_list)
        filtered_list = new_list.get_filtered_list_from_DB(keyword,row_names,date,False)

        return filtered_list

           
#  def filter_planes(planes_list=[], a_header=''):
#         header = planes_list[0]
#         a_header_index = int
#         for index, value in enumerate(header):
#             if value == a_header:
#                 a_header_index = index
            
#         types = []
        
#         for a_list in planes_list[1:]:
#             if a_list[a_header_index] not in types:
#                 types.append(a_list[a_header_index])

        return types


        

