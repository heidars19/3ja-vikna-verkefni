from DB.DATA_API import *

# 6.12 all virkar


def main ():

    # # Reads a file and returns a list - check
    # new_instance = DestinationFile()
    # datalist = new_instance.start()
    # header = new_instance.get_header()
    # print(header)
    # print()
    # print(datalist)
    # print()
    
    # #Append data to a file - check
    # new_instance = DestinationFile(data_to_append="Kulusuk,Greenland,1:00:55,1.343,Hraði Brunann,328738975")
    # new_instance.start()
    
    # # Finds line number of a given search parameter - check
    # new_instance = DestinationFile(fieldname="id", searchparam="3")
    # line_number = new_instance.start()
    # print("Ætti að skila línu númeri: --> {}".format(line_number))
    # print()
    
    # # Changes a line - check
    # new_instance = DestinationFile(line_to_replace='5,Tingwall,Shetland,1:15:15,1.445,Ulle Bjakk,712223566,Someairport,SomeRegistrationDate\n', replace_with="17,Kulusuk,Greenland,1:00:55,1.343,Hraði Brunann,328738975,2019-12-05 21:16:50.497635")
    # new_instance.start()    
    
    # # Change a line at a certain line number - check
    # new_instance = DestinationFile(line_to_replace=22, replace_with="19,Kulusuk,Greenland,1:00:55,1.343,Hraði Brunann,328738975,2019-12-05 21:18:09.381820")
    # new_instance.start()


    return

if __name__ == "__main__":
    main()