from DB.DATA_API import *

def main ():

    # Keywords: employee, destination, airplane, worktrip, worktripold
    keyword = 'worktrip'

    data_api = DATA_API()

    data_api.set_data(keyword, data_to_append="TF-STH,NAFokkerF28,Fokker,F28,Narfi")
    # data_api.set_data(keyword, fieldname="plane_id", searchparam="TF-EOC")
    # data_api.set_data(keyword, line_to_replace='7,TF-EOC,NAFokker80,Fokker,F800,Heiðar,2019-12-05 21:23:08.227855', replace_with='7,TF-EOC,NAFokker80,Fokker,F800,Kiddi,2019-12-05 21:23:08.227855')
    # data_api.set_data(keyword, line_to_replace=12, replace_with='12,TF-STH,NAFokkerF28,Fokker,F28,Narfi,2019-12-05 21:23:08.227855')
    # data_api.set_data(keyword)
    # data_api.set_data(keyword, header=True)
    result = data_api.start()
    # result = data_api.start()
    print(result)









    return

if __name__ == "__main__":
    main()