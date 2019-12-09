#import time
from datetime import datetime, timedelta

def get_date_n_time(work_trip_line):
    """Gets date and time from the DB and returns a list of ints"""
    """changes this 2019-12-06 23:07:18.704449 into this: [2019, 12, 6, 23, 7]"""

    wholelist = work_trip_line.strip().split(",") # splits the entry line
    """"Passa hér að neðan að ná í úr réttum dálk - þarf að breyta eftir header, ég notaði 5 en það verður ekki rétt á endanum"""
    date_n_time_string = str(wholelist[5]) # gets the timestamp
    date_n_time_list = date_n_time_string.split() # splits date and time numbers to list

    date_string = date_n_time_list[0] # isolates the date
    date_list = date_string.split("-") # splits the date

    time_string = date_n_time_list[1] # isolates the time
    time_list = time_string.split(":") # splits the time 

    date_n_time_final = [date_list[0], date_list[1], date_list[2], time_list[0], time_list[1]] # total list of numbers needed
    date_n_time_final = [int(i) for i in date_n_time_final] # comprehension to ints

    return date_n_time_final

filename = "Worktrips.csv"
filename2 = filename + ".bak"
filename3 = "Worktrips_old.csv"
with open(filename, 'r', encoding='utf-8') as readable:
    with open(filename2, 'w+', encoding='utf-8') as readable2:
        with open(filename3, 'a', encoding='utf-8') as readable3:
            now_time = datetime.now() # Gets currents timestamp
            for line in readable:
                # Muna að sleppa línu 1, header
                date_time_list = get_date_n_time(line) # sends the whole line to the function

                old_time = datetime(date_time_list[0], date_time_list[1], date_time_list[2], date_time_list[3], date_time_list[4]) #ints sent in the class
                
                old_time_plus_hour = old_time + timedelta(hours = 1) # Worktrip is over 1 hour after landing in Iceland
                
                if now_time > old_time_plus_hour:
                    readable3.write(line) # Archaves old worktrips
                else:
                    readable2.write(line) # Writes future worktrips into a new file

                """Nú er til .bak skrá sem þarf að yfirskrifa "Worktrips.csv" þeger keyrslu líkur"""   