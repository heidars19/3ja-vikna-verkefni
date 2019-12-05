from DB.DATA_API import *

def main ():

    # Reads a file and returns a list - check
    new_instance = WorkTripFile()
    datalist = new_instance.start()
    header = new_instance.get_header()
    print(header)
    print()
    print(datalist)
    print()
    
    #Append data to a file - check
    new_instance = WorkTripFile(data_to_append="Kulusuk,Greenland,1:00:55,1.343,Hraði Brunann,328738975")
    new_instance.start()
    
    # Finds line number of a given search parameter - check
    new_instance = WorkTripFile(fieldname="id", searchparam="3")
    line_number = new_instance.start()
    print("Ætti að skila línu númeri: --> {}".format(line_number))
    print()
    
    # # Changes a line - check
    # new_instance = WorkTripFile(line_to_replace='Sessý,TEST,TEST,BAE,BAE', replace_with="TF-EOC,NAFokker80,Fokker,F800,Heiðar,100")
    # new_instance.start()    
    
    # # Change a line at a certain line number - check
    # new_instance = WorkTripFile(line_to_replace=3, replace_with="Þetta ætti að breyta línu 3")
    # new_instance.start()

    # # Changes part of a line - check
    # new_instance = WorkTripFile(line_to_replace="TF-OAS,NABAE146,BAE,146,Sessý,82", replace_with="TF-OAS,NABAE146,BAE,146,Sessý,182")
    # new_instance.start()



    return

if __name__ == "__main__":
    main()