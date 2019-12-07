from DB.DATA_API import *

def main ():

    # Reads a file and returns a list - check
    new_instance = EmployeeFile()
    datalist = new_instance.start()
    header = new_instance.get_header()
    print(header)
    print()
    print(datalist)
    print()
    
    #Append data to a file - check
    new_instance = EmployeeFile(data_to_append="1234567890,Svanur Ketilsson,Hverfisbar,8453474,smurf@gmail.com,Pilot,Copilot,BOEING747")
    new_instance.start()
    
    # # Finds line number of a given search parameter - check
    # new_instance = EmployeeFile(fieldname="id", searchparam="3")
    # line_number = new_instance.start()
    # print("Ætti að skila línu númeri: --> {}".format(line_number))
    # print()
    
    # # Changes a line - check
    # new_instance = EmployeeFile(line_to_replace='6,1234567890,Gunni Jónsson,Hverfisbar,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232,2019-12-05 20:49:51.086720', replace_with="6,1234567890,Nonni Jónsson,Hverfisbar,8453474,eythoroli95@gmail.com,Pilot,Copilot,Jumbo201,2019-12-05 20:49:51.086720")
    # new_instance.start()    
    
    # # Change a line at a certain line number - check
    # new_instance = EmployeeFile(line_to_replace=3, replace_with="3,8884449999,Heiðar Sigurjónsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232,2019-12-05 20:23:22.161232")
    # new_instance.start()



    return

if __name__ == "__main__":
    main()