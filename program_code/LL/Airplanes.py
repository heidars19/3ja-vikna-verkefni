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
        {PlaneFilehandler = AirplaneFile()
        all_planes = PlaneFilehandler.start()
        return all_planes

    def save_airplane(planeID, planeType, manufacturer, model, name, capacity):
        new_plain = Airplane(planeID, planeType, manufacturer, model, name, capacity)
        log_plain = AirplaneFile(data_to_append=str(new_plain))
        log_plain.start()

    def change_airplane(planeID, planeType, manufacturer, model, name, capacity):
        pass

    def change_employee(self,old_info,new_info):
            '''Checks if user is trying to change invalid information'''
            
            ssn,name,address,mobile,email,role,rank,licence = new_info.split(',')

            old_info = StaffFile(fieldname="ssn",searchparam=ssn)