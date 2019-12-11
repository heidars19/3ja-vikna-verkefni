from DB.DATA_API import *

# 6.12 Allt virkar

def main ():

    #Reads a file and returns a list - check
    new_instance = WorkTripFileOld()
    datalist = new_instance.start()
    header = new_instance.get_header()
    print(header)
    print()
    print(datalist)
    print()
    
    # #Append data to a file - check
    # new_instance = WorkTripFileOld(data_to_append="152,NA1914,LYR,KEF,2019-11-28T11:25:00,2019-11-28T15:25:00,TF-LNQ,2907675667,2211658134,1405853585,1103647756,1103912131,321321")
    # new_instance.start()
    
    # # Finds line number of a an id - check
    # new_instance = WorkTripFileOld(searchparam=148)
    # line_number = new_instance.start()
    # print("Ætti að skila línu númeri: --> {}".format(line_number))
    # print()

    # # Finds line number of a given search parameter - check
    # new_instance = WorkTripFileOld(fieldname="id", searchparam="148")
    # line_number = new_instance.start()
    # print("Ætti að skila línu númeri: --> {}".format(line_number))
    # print()
    
    # # Changes a line - check
    # new_instance = WorkTripFileOld(line_to_replace='150,NA5717,KEF,LYR,2019-11-30T05:23:00,2019-11-30T09:23:00,TF-IZE,2706838569,2410876598,909862878,1501681497,2807755841', replace_with="152,NA5717,KEF,LYR,2019-11-30T05:23:00,2019-11-30T09:23:00,TF-IZE,2706838569,2410876598,909862878,1501681497,2807755841")
    # new_instance.start()    
    
    # # Change a line at a certain line number - check
    # new_instance = WorkTripFileOld(line_to_replace=29, replace_with="149,NA1914,LYR,KEF,2019-11-28T11:25:00,2019-11-28T15:25:00,TF-LNQ,2907675667,2211658134,1405853585,1103647756,1103912131")
    # new_instance.start()



    return

if __name__ == "__main__":
    main()