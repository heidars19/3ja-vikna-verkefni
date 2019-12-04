from DB.DATA_API import *

# -*- coding: cp1252 -*-

def main ():
    # #Append data to a file - check
    # test = DestinationFile(data_to_append="8,Longyearbyen,Svalbard,1:30:25,1.993,Þarmar Klámsson,632827365")
    # test.start()

    # # Reads a file and returns a list - check
    # test = AirplaneFile()
    # datalist = test.start()
    # print(datalist)

    # # Changes a line - check
    # test = WorkTripFile(line_to_replace=6, replace_with="Þetta ætti að breyta línu 6")
    # test.start()

    # # Finds line number of a given search parameter - check
    # test = StaffFile(fieldname="ssn", searchparam="3009907461")
    # line_number = test.start()
    # print("Ætti að skila línu númer 1: --> {}".format(line_number))

    # # Change a line at a certain line number - check
    # test = AirplaneFile(line_to_replace=4, replace_with="TF-BOD,NAFokker60,Fokker,F60,60")
    # test.start()

    # # Changes part of a line - check
    # test = AirplaneFile(line_to_replace="TF-BOD", replace_with="TF-EOB")
    # test.start()



    return

if __name__ == "__main__":
    main()