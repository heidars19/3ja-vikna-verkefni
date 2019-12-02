import csv

def append_data_to_file(data_list, name_of_file, header=""):
    ''' Appends data to file, creates a new file if none exists, and adds a header. 
    Accepts a list with 1 line, name of file (without file extension) and a 
    header file (can skip if it's 100% the file exists already) '''

    data_string = ",".join(data_list) # Changes a list to comma seperated string

    with open(name_of_file, 'a') as f:
        if f.tell() == 0: 
            # File is empty or we just created it, so we add a header
            f.write(header + '\n')
        f.write(data_string + '\n') # Append data to file


def does_line_exists(filestream, fieldname, searchparam): 
    ''' Checks if line exists in a file, returns line number, or False if not found '''
    reader = csv.DictReader(filestream, delimiter=',')
    for line_number, line in enumerate(reader): 
        if line[fieldname] == searchparam :
            return line_number+1 # Add 1 because this func doesn't count the header
    return False


def open_file(filename):
    ''' Opens a file and returns a filestream, or None if error '''
    try :
        f =  open(filename, 'r')
        return f
    except :
        return None



#import fileinput

    # def change_line_in_file(filename, line_to_replace, replace_with) :
    #     ''' Replaces 1 line in a file '''
    #     for line in fileinput.FileInput(filename,inplace=1):
    #         line = line.replace(line_to_replace,replace_with)
    #         print(line, end='')
    
    
    
    






def main() :




    return


if __name__ == "__main__":
    main()