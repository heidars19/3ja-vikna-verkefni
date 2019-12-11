from DB.DATA_API import *

# 6.12 Allt virkar


def main ():

    # # Reads a file and returns a list - check
    # new_instance = AirplaneFile()
    # datalist = new_instance.start()
    # header = new_instance.get_header()
    # print(header)
    # print()
    # print(datalist)
    # print()
    
    #Append data to a file - check
    new_instance = AirplaneFile(data_to_append="TF-EOC,NAFokker80,Fokker,800,Heiðar er Bestur")
    new_instance.start()
    
    # Finds line number of a given search parameter - check
    new_instance = AirplaneFile(fieldname="id", searchparam="3")
    line_number = new_instance.start()
    print("Ætti að skila línu númeri: --> {}".format(line_number))
    print()
    
    # # Changes a line - check
    # new_instance = AirplaneFile(line_to_replace='23,TF-EOC,NAFokker80,Fokker,F800,Heiðar er Bestur,100,2019-12-05 18:44:25.899155', replace_with="23,TF-BAD,NAFokker80,Fokker,F800,Heiðar er Bestur,100,2019-12-05 18:44:25.899155")
    # new_instance.start()    
    
    # # Change a line at a certain line number - check
    # new_instance = AirplaneFile(line_to_replace=22, replace_with="16,TF-EOC,NAFokker80,Fokker,F800,Heiðar er Bestur,100,2019-12-05 18:32:25.202619")
    # new_instance.start()


    return

if __name__ == "__main__":
    main()