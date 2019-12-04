import DB.DATA_API

"""
planeID	planeType	manufacturer	model 	capacity 
"""

class Aircraft():
    def __init__(self, name, planeID, planeType, manufacturer, model, capacity) :
        self.name = name
        self.__planeID = planeID
        self.__planeType = planeType
        self.__manufacturer	model 	
        self.__capacity = capacity 

    def __repr__(self):
        Aircraft(f'{self.name}, {self.__planeID}, {self.__planeType}, {self.__manufacturer}, {self.__manufacturer})

    def __str__():
        return f'{self.name}, {self.__planeID}, {self.__planeType}, {self.__manufacturer}, {self.__manufacturer}'

    def ChangeInfo(self, new_name):
        current_register = f'{self.name}, {self.__planeID}, {self.__planeType}, {self.__manufacturer}, {self.__manufacturer}'
        new_register = ''
        return return ,  