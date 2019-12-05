#from DB.DATA_API import * eigum ekki að tala beint við db
from DB.DATA_API import *
from LL.AirplanesLL import *
from LL.DestinationLL import *


#----------------------------------------------------------------------------------------------

#Airplanes
class LL_API():
    def get_airplane_types():
        all_planes = Airplane.get_airplane_list()
        filtered_planes = Airplane.filter_planes(all_planes, model)
        return filtered_planes

    def get_all_airplanes():
        all_planes = Airplane.get_all_planes()
        return all_planes

    def create_airplane(plane_id, plane_type, manufacturer, model, name, capacity):
        new_plain = Airplane(planeID, planeType, manufacturer, model, name, capacity)
        new_plain.save_airplane()
        
    



    



    

#if __name__ == "__main__":


    #main()



#new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
"""emp = create_employee("2501952149","Eyþór Óli Borgþórsson","Þingás 31","8453474","eythoroli95@gmail.com","Pilot","Copilot","Fokker232")

print(emp)"""