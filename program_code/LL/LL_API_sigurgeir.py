#from DB.DATA_API import * eigum ekki að tala beint við db
from DB.DATA_API import *
from LL.AirplanesLL import *
from LL.DestinationLL import *


#----------------------------------------------------------------------------------------------

#Airplanes
class LL_API():
    def get_airplane_types():
        all_planes = AirplanesLL.get_plane_list()
        filtered_planes = AirplanesLL.filter_planes(all_planes, 'model')
        return filtered_planes

    def get_all_airplanes():
        all_planes = AirplanesLL.get_plane_list()
        return all_planes

    def create_airplane(self, plane_id, plane_type, manufacturer, model, name, capacity):
        new_register = AirplanesLL()
        status = new_register.create_airplane(plane_id, plane_type, manufacturer, model, name, capacity)
        
    def change_airplane():
        pass




#-----------------------------------------Destinations----------------------------------------#

    def get_all_destinations():
        all_destinations = DestinationLL.get_destination_list()
        print (all_destinations)

    def create_destination(self, id,destination,country,flight_time,distance,contact,emerg_number,airport):
        new_register = DestinationLL()
        status = new_register.create_destination(id, destination, country, flight_time, distance, contact, emerg_number, airport)




def testmain():
    new = LL_API()
    new.create_destination('1','Longyearbyen','Svalbard','1:30:25','1.993','Þarmar Klámsson','632827365', 'Vik')
