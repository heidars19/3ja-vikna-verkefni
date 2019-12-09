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
        index_list = self.find_index_from_header(keyword, row_names)
        filtered_list = self.get_filtered_list_from_DB(keyword,index_list,date,match=False)

        row_names = ['arriving_at', 'captain' ,'copilot' ,'fsm' ,'fa1' ,'fa2']
        staff_index_list = self.find_index_from_header(keyword, row_names)
        destination_staffmember_list = self.filter_by_header_index(staff_index_list, filtered_list)
        return destination_staffmember_list

           



        

