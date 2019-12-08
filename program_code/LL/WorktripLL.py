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
    

    def get_emp_dest_date(self,date):
        """
        Gets list of employees enrolled in a worktrip at specified date, and their destinations.\n
        Date format: YYYY-MM-DD
        """

        
        

