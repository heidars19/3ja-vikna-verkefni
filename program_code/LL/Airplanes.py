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