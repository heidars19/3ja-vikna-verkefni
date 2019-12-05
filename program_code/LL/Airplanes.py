from DB.DATA_API import *

class Airplane():
    def __init__(self, plane_id, plane_type, manufacturer, model, name, capacity) :
        self.planeID = plane_id
        self.planeType = plane_type
        self.manufacturer = manufacturer 	
        self.model = model
        self.name = name
        self.capacity = capacity 

    def __repr__(self):
        return f'Aircraft({self.planeID},{self.planeType},{self.name},{self.manufacturer},{self.model},{self.name},{self.capacity})'

    def __str__(self):
        return f'{self.planeID},{self.planeType},{self.name},{self.manufacturer},{self.model},{self.name},{self.capacity}'



        #====================================Functions==========================================#

    def filter_available(all_planes):
        pass

    def filter_airplanes(planes_list, a_type):
        header = ['plane_id', 'plane_type', 'manufacturer', 'model', 'name', 'capacity']
        type_input = None
        for index, value in enumerate(header):
            if value.lower() == a_type.lower():
                type_input = index
            
        types = []
        for list in planes_list:
            list = list.split(',')
            if list[index] not in types:
                types.append(list[3])
            
    def get_airplane_list():
        PlaneFilehandler = AirplaneFile()
        all_planes = PlaneFilehandler.start()
        all_planes_list = []
        for plane in all_planes:
            all_planes_list.append(plane.split(','))
        return all_planes_list

    def save_airplane(self):
        log_plain = AirplaneFile(data_to_append=str(self))
        status = log_plain.start()
        return status

    def change_airplane(self, new_info):
        new_plane_id, new_plane_type, new_manufacturer, new_model, new_name, new_capacity = new_info
        line_in_db = AirplaneFile(fieldname="plane_id",searchparam=new_plane_id)
        
        if line_in_db == 0:
            return False, "Flugvél ekki til í gagnagrunni"
        if line_in_db == -1:
            return False, "Villa kom upp!"
        
        new_info_plane = Airplane(new_plane_id, new_plane_type, new_manufacturer, new_model, new_name, new_capacity)
        PlaneFilehandler = AirplaneFile(line_to_replace=line_in_db, replace_with=str(new_info_plane))
        status = PlaneFilehandler.start()
        
        return status

def testmain():
    thelist = Airplane.get_airplane_list()
    print (thelist)