from LL.Worktrip import *
from DB.DATA_API import *
from LL.LL_functions import *
import string

class WorktripLL(LL_functions):

    #Útfærði þetta á sama hátt og hjá employee þar sem við notum save_object_to_DB function til að vista hvað sem er og unpökkum hér
    def create_worktrip(self,worktrip_identity):
        '''Creates new worktrip and saves to database'''
        
        departing_from, arriving_at, airplane_id, departure, arrival = worktrip_identity
        new_worktrip = Worktrip(departing_from, arriving_at, airplane_id, departure, arrival)

        self.save_object_to_DB("worktrip",str(new_worktrip))


    def staffing(self, changed_identity):
        staffed_worktrip = Worktrip(*staffing_info)
        staffed_str = staffed_worktrip.get_

    def change_employee(self,changed_identity):
        """
        Changes information about employee, except ssn, name or degistration date.
        changed_identity = (id,ssn,name,address,mobile,email,role,rank,licence,registration_date)
        """

        changed_emp = Employee(*changed_identity)
        changed_str = changed_emp.get_changes_registration_str()
    
        return_value = self.change_object_in_DB("employee", changed_str, changed_emp._id)  # Bring 'id' seperately, so next function can find line number
        return return_value
    
