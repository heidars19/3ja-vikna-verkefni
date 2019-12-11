from DB.DATA_API import *
import datetime

def main ():

    new_ = AirplaneFile()
    header = new_.get_header()
    print(header)
    print()
    
    #Append data to a file - check
    new_instance = AirplaneFile(data_to_append="TF-EOC,NAFokker80,Fokker,F800,Heiðar er Bestur,100")
    new_instance.start()

    # Reads a file and returns a list - check
    new_instance = AirplaneFile()
    datalist = new_instance.start()
    print(datalist)
    print()
    
    # Changes a line - check
    new_instance = AirplaneFile(line_to_replace='Sessý,TEST,TEST,BAE,BAE', replace_with="TF-EOC,NAFokker80,Fokker,F800,Heiðar,100")
    new_instance.start()

    # Finds line number of a given search parameter - check
    new_instance = AirplaneFile(fieldname="planeID", searchparam="TF-OAS")
    line_number = new_instance.start()
    print("Ætti að skila línu númeri: --> {}".format(line_number))
    print()
    
    # # Change a line at a certain line number - check
    # new_instance = AirplaneFile(line_to_replace=3, replace_with="Þetta ætti að breyta línu 3")
    # new_instance.start()

    # # Changes part of a line - check
    # new_instance = AirplaneFile(line_to_replace="TF-OAS,NABAE146,BAE,146,Sessý,82", replace_with="TF-OAS,NABAE146,BAE,146,Sessý,182")
    # new_instance.start()



    return

if __name__ == "__main__":
    main()