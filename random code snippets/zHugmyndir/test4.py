import fileinput

def change_line_in_file() :
       
line_to_replace = "2013,1,1,517,515,2,830,819,11,UA,1545,N14228,EWR,IAH,227,1400,5,15,2013-01-01T05:00:00Z"
replace_with = "Hahaha, breytti linu"

for line in fileinput.FileInput("flights.csv",inplace=1):
   line = line.replace(line_to_replace,replace_with)
   print(line, end='')
   
