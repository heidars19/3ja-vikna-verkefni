class Airplane():
    def __init__(self, plane_id, plane_type, manufacturer, model, name, capacity, registration_date='') :
        self.planeID = plane_id
        self.planeType = plane_type
        self.manufacturer = manufacturer 	
        self.model = model
        self.name = name
        self.capacity = capacity 
        self.registration_date = registration_date

    def __repr__(self):
        return f'Airplane({self.planeID},{self.planeType},{self.name},{self.manufacturer},{self.model},{self.name},{self.capacity})'

    def __str__(self):
        return f'{self.planeID},{self.planeType},{self.name},{self.manufacturer},{self.model},{self.name},{self.capacity}'



        #====================================Functions==========================================#


