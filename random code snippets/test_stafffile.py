from DB.DATA_API import *

def main ():

    # Keywords: employee, destination, airplane, worktrip, worktripold
    keyword = 'employee'

    new_instance = DATA_API()

    new_instance.set_data(keyword, data_to_append="1234567890,Svanur Ketilsson,Hverfisbar,8453474,smurf@gmail.com,Pilot,Copilot,BOEING747")
    new_instance.set_data(keyword, fieldname="name", searchparam="Laddi")
    new_instance.set_data(keyword, line_to_replace='13,1234567890,Svanur Ketilsson,Hverfisbar,8453474,smurf@gmail.com,Pilot,Copilot,BOEING747,2019-12-07 18:31:40.430550', replace_with='13,1234567890,Jón Nonnason,Ármúla 6,8453474,pilot@gmail.com,Pilot,Captain,BOEING747,2019-12-07 18:31:40.430550')
    new_instance.set_data(keyword, line_to_replace=15, replace_with='15,8884449999,Fannar Guðmundsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Captain,Fokker232,2019-12-05 20:23:22.161232')
    new_instance.set_data(keyword)




    result = new_instance.start()
    print(result)



    # # Reads a file and returns a list - check
    # new_instance = EmployeeFile()
    # datalist = new_instance.start()
    # header = new_instance.get_header()
    # print(header)
    # print()
    # print(datalist)
    # print()
    
    # #Append data to a file - check
    # new_instance = EmployeeFile(data_to_append="1234567890,Svanur Ketilsson,Hverfisbar,8453474,smurf@gmail.com,Pilot,Copilot,BOEING747")
    # new_instance.start()
    
    # # Finds line number of a given search parameter - check
    # new_instance = EmployeeFile(fieldname="id", searchparam="3")
    # line_number = new_instance.start()
    # print("Ætti að skila línu númeri: --> {}".format(line_number))
    # print()
    
    # Changes a line - check
    # new_instance = EmployeeFile(line_to_replace='17,1234567890,Svanur Ketilsson,Hverfisbar,8453474,smurf@gmail.com,Pilot,Copilot,BOEING747,2019-12-07 19:24:35.183893', replace_with="17,1234567890,Ketil Svansson,Hverfisbar,8453474,smurf@gmail.com,Pilot,Copilot,BOEING747,2019-12-07 19:24:35.183893")
    # new_instance.start()    
    
    # # Change a line at a certain line number - check
    # new_instance = EmployeeFile(line_to_replace=15, replace_with="14,8884449999,Heiðar Sigurjónsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232,2019-12-05 20:23:22.161232")
    # new_instance.start()



    return

if __name__ == "__main__":
    main()