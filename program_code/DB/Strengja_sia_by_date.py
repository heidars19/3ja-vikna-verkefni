def date_filtering(db_list, date, list_index=-1):

    """Filtering strings that contain selected date from list of strings into new list"""
    
    new_list = []

    for i in range(len(db_list)):
        temp_list = db_list[i].split(",")
        if date in temp_list[list_index]:
            new_list.append(db_list[i])
            
    if new_list == []:
        return 0
    else:
        return new_list


"""testkóði hér að neðan"""
db_list = [\
"1,NA5633,Keflavik,Longyearbyen,2019-12-06 23:07:18.704449,2019-12-06 23:07:18.704449,2019-12-06 23:07:18.704449,321321,321321321,321321321,3213213,321,321,321,",\
"2,NA5638,Keflavik,Longyearbyen,2020-12-06 23:07:18.704449,2019-12-06 23:07:18.704449,2019-12-06 23:07:18.704449,321321,321321321,321321321,3213213,321,321,321,",\
"8,NA5631,Longyearbyen,Keflavik,2020-12-06 23:07:18.704449,2019-12-06 23:07:18.704449,2019-12-06 23:07:18.704449,321321,321321321,321321321,3213213,321,321,321,"\
]
date = "2020-12-06"
list_index = 4

test_date_filtering = date_filtering(db_list, date, list_index)

print (test_date_filtering)