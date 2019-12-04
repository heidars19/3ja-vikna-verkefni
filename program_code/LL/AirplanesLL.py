import Airplanes
import string

ALL_TEST = ['TF-OAS,NABAE146,BAE,146,Sessý,82','TF-STH,NAFokkerF28,Fokker,F28,Finnur,65','TF-EOB,NAFokker100,Fokker,F100,Helgi,100']

def filter_available(all_planes):
    pass

def filter(all_list, a_type):
    header = ['planeID','planeType','manufacturer','model','name','capacity']
    type_input = None
    for index, value in enumerate(header):
        if value.lower() == a_type.lower():
            type_input = index
        

    types = []
    for list in all_list:
        list = list.split(',')
        if list[index] not in types:
            types.append(list[3])
        

    
    


def get_in_database():
    all_planes = AirplaneFile.start()
    return all_planes

def register_to_database():
    pass

def change_register_in_database():
    pass


filter(ALL_TEST, 'MOdEl')