from LL.Worktrip import *
from DB.DATA_API import *
from LL.LL_functions import *
import string

class WorktripLL(LL_functions):

    #Útfærði þetta á sama hátt og hjá employee þar sem við notum save_object_to_DB function til að vista hvað sem er og unpökkum hér
    def create_worktrip(self,worktrip_identity):
        '''Creates a new airplane and saves to database'''
        
        departing_from, arriving_at, airplane_id, departure, arrival = worktrip_identity
        new_worktrip = Worktrip(departing_from, arriving_at, airplane_id, departure, arrival)

        self.save_object_to_DB("worktrip",str(new_worktrip))