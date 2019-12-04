import DB.DATA_API

def main ():
    # #Append data to a file - check
    # test = AirplaneFile(data_to_append="TF-EOC,NAFokker80,Fokker,F800,100")
    # test.run_me()

    # # Reads a file and returns a list - check
    # test = AirplaneFile()
    # datalist = test.run_me()
    # print(datalist)

    # # Changes a line - check
    # test = AirplaneFile(line_to_replace="TF-EOC,NAFokker80,Fokker,F800,100", replace_with="TF-EOD,NAFokker80,Fokker,F80,80")
    # test.run_me()

    # # Finds line number of a given search parameter - check
    # test = AirplaneFile(fieldname="planeID", searchparam="TF-EOD")
    # line_number = test.run_me()
    # print(line_number)

    # # Change a line at a certain line number - check
    # test = AirplaneFile(line_to_replace=4, replace_with="TF-BOD,NAFokker60,Fokker,F60,60")
    # test.run_me()

    # # Changes part of a line - check
    # test = AirplaneFile(line_to_replace="TF-BOD", replace_with="TF-EOB")
    # test.run_me()



    return

if __name__ == "__main__":
    main()