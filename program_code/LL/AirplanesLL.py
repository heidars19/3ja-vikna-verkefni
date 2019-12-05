from DB.DATA_API import *
from LL.Airplanes import Airplane
import string

ALL_TEST = ['TF-OAS,NABAE146,BAE,146,Sessý,82','TF-STH,NAFokkerF28,Fokker,F28,Finnur,65','TF-EOB,NAFokker100,Fokker,F100,Helgi,100']

def filter_available(all_planes):
    pass

def filter_airplanes(all_list, a_type):
    header = ['plane_id', 'plane_type', 'manufacturer', 'model', 'name', 'capacity']
    type_input = None
    for index, value in enumerate(header):
        if value.lower() == a_type.lower():
            type_input = index
        

    types = []
    for list in all_list:
        list = list.split(',')
        if list[index] not in types:
            types.append(list[3])
        

    
    


def get_airplane_list():
    plane_file_handler = AirplaneFile()
    all_planes = plane_file_handler.start()
    return all_planes

def save_airplane(planeID, planeType, manufacturer, model, name, capacity):
    new_plain = Airplane(planeID, planeType, manufacturer, model, name, capacity)
    print (new_plain)
    log_plain = AirplaneFile(data_to_append=str(new_plain))
    log_plain.start()

def change_airplane():
    pass


def test_main():
    save_airplane('TEST,TEST,BAE,146,Sessý,82')