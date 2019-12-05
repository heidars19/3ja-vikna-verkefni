class Destination():
    
    def __init__(self, destination,	country, id, flight_time, distance, contact, emergency_number):
        self.destination = destination
        self.country = country
        self.id	= id
        self.flight_time = flight_time
        self.distance = distance
        self.contact = contact
        self.emergency_number = emergency_number


    def __repr__(self):
        return f'Destination({self.destination}, {self.country}, {self.id}, {self.flight_time}, {self.distance}, {self.contact}, {self.emergency_number}')


    def __str__(self):
        return f'{self.destination},{self.country},{self.id},{self.flight_time},{self.distance},{self.contact},{self.emergency_number}'




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
        return all_planes

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

