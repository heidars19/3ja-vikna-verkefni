from DB.DATA_API import *
import string

ALL_TEST = ['TF-OAS,NABAE146,BAE,146,Sessý,82','TF-STH,NAFokkerF28,Fokker,F28,Finnur,65','TF-EOB,NAFokker100,Fokker,F100,Helgi,100']

def filter_available(all_planes):
    pass

def filter_planes(all_list, a_type):
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
        

    
    


def get_all_planes():
    plane_file_handler = AirplaneFile()
    all_planes = plane_file_handler.start()
    return all_planes

def register_to_database():
    pass

def change_register_in_database():
    pass


def test_main():
    all_plain_list = get_all_planes()
    print (all_plain_list)