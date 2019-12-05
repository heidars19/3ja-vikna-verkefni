class Airplane():
    def __init__(self, name, planeID, planeType, manufacturer, model, capacity) :
        self.name = name
        self.__planeID = planeID
        self.__planeType = planeType
        self.__model = model
        self.__manufacturer = manufacturer 	
        self.__capacity = capacity 

    def __repr__(self):
        return f'Aircraft({self.name}, {self.__planeID}, {self.__planeType}, {self.__manufacturer}, {self.__manufacturer})'

    def __str__():
        return f'{self.name}, {self.__planeID}, {self.__planeType}, {self.__manufacturer}, {self.__manufacturer}'