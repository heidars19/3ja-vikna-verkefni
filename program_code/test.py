from DB.DATA_API import *
import time
import datetime

def main ():
    #Append data to a file - check
    test = WorkTripFileOld(data_to_append="NA6839,LWK,KEF,2019-11-24T03:00:00,2019-11-24T05:00:00,TF-PGK,2907675667,1900769521,1811931544,1107951952,2509913418")
    test.start()

    # Reads a file and returns a list - check
    test = AirplaneFile()
    datalist = test.start()
    print(datalist)

    # Changes a line - check
    test = WorkTripFile(line_to_replace=8, replace_with="Þetta ætti að breyta línu 8")
    test.start()

    # Finds line number of a given search parameter - check
    test = StaffFile(fieldname="ssn", searchparam="3009907461")
    line_number = test.start()
    print("Ætti að skila línu númer 1: --> {}".format(line_number))

    # Change a line at a certain line number - check
    test = AirplaneFile(line_to_replace=4, replace_with="Þetta ætti að breyta línu 4")
    test.start()
    sleep(5)
    # Changes part of a line - check
    test = AirplaneFile(line_to_replace="Þetta ætti að breyta línu 4", replace_with="Núna breytt aftur" + datetime.date(isoformat()))
    test.start()



    return

if __name__ == "__main__":
    main()