from DB.DATA_API import *

# 6.12 Allt virkar

def main ():

    # # Reads a file and returns a list - check
    # new_instance = WorkTripFile()
    # datalist = new_instance.start()
    # header = new_instance.get_header()
    # print(header)
    # print()
    # print(datalist)
    # print()
    
    # #Append data to a file - check
    # new_instance = WorkTripFile(data_to_append="NA5638,Keflavik,Longyearbyen,2019-12-20T06:45:00,2019-12-20T10:45:00,321321,321321,321323213211,321321321,3213213,321,321,321")
    # new_instance.start()
    
    # # Finds line number of a given search parameter - check
    # new_instance = WorkTripFile(fieldname="id", searchparam="22")
    # line_number = new_instance.start()
    # print("Ætti að skila línu númeri: --> {}".format(line_number))
    # print()
    
    # Changes a line - check
    new_instance = WorkTripFile(line_to_replace="31,NA5638,Keflavik,Longyearbyen,2019-12-20T06:45:00,2019-12-20T10:45:00,321321,321321,321323213211,321321321,3213213,321,321,321,2019-12-07 13:55:18.999874", replace_with="34,NA5638,Keflavik,Longyearbyen,2019-12-20T06:45:00,2019-12-20T10:45:00,321321,321321,321323213211,321321321,3213213,321,321,321,2019-12-07 13:55:26.679896")
    new_instance.start()   
    
    # # Change a line at a certain line number - check
    # new_instance = WorkTripFile(line_to_replace=6, replace_with="15,NA5638,Keflavik,Longyearbyen,2019-12-20T06:45:00,2019-12-20T10:45:00,321321,321321,321323213211,321321321,3213213,321,321,321")
    # new_instance.start()





    return

if __name__ == "__main__":
    main()