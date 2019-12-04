from DB.DATA_API import *


def main ():
    #Append data to a file - check
    test = WorkTripFileOld(data_to_append="NA6839,LWK,KEF,2019-11-24T03:00:00,2019-11-24T05:00:00,TF-PGK,2907675667,1900769521,1811931544,1107951952,2509913418")
    test.start()

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