import csv
import fileinput

class DATA_API :
    ''' 
    Contains data layer functions:
        def append_data_to_file(data_to_append, name_of_file, header=""):
        def does_line_exists(filestream, fieldname, searchparam): 
        def open_file(filename):
        def read_filestream_into_list(filestream):
        def change_line_in_file(filename, line_to_replace, replace_with) :

    '''





    def __init__ (self, filename, header="") :
        self.header = header
        self.filename = filename





    def append_data_to_file(self, data_to_append):
        ''' 
        Appends data to file, creates a new file if none exists, and adds a header. 

        Accepts a list with 1 line, name of file and a 
        header file (can skip if it's 100% the file exists already) 
        '''
        if isinstance(data_to_append, list) : 
            data_string = ",".join(data_to_append) # Changes a list to comma seperated string
        else :
            data_string = data_to_append

        with open(self.filename, 'a') as f:
            if f.tell() == 0: 
                # File is empty or we just created it, so we add a header
                f.write(self.header + '\n')
            f.write(data_string + '\n') # Append data to file


    def does_line_exists(self, filestream, fieldname, searchparam): 
        ''' 
        Checks if line exists in a file, returns line number, or False if not found 
        '''
        reader = csv.DictReader(filestream, delimiter=',')
        for line_number, line in enumerate(reader): 
            if line[fieldname] == searchparam :
                return line_number+1 # Add 1 because this func doesn't count the header
        return False


    def open_file(self):
        ''' 
        Opens a file and returns a filestream, or None if error.
        Does not close the file!
        '''
        try :
            f =  open(self.filename, 'r')
            return f
        except :
            return None


    def read_filestream_into_list(self, filestream):
        '''
        Takes a filestream, returns a list with file contents.
        Closes the file after reading it.
        '''
        data_list = []
        for line in filestream :
            data_list.append(line.strip())
        filestream.close() # Closes file after grabbing data from it
        return data_list


    def change_line_in_file(self, line_to_replace, replace_with) :
        ''' 
        Replaces 1 line in a file. 

        line_to_replace can be a line number (int) or a complete line (str).
        When line_to_replace is a string, it can replace partial lines.
        '''
        
        if isinstance(line_to_replace, int) : # If line_to_replace is a line number (int)
            for i, line in enumerate(fileinput.FileInput(self.filename,inplace=1)) :
                if i == line_to_replace :
                    print(replace_with.strip())   # Strip to remove extra \n, cause print adds it anyways
                else :
                    print(line, end='')
        else :   # line_to_replace is a complete line (str)
            for line in fileinput.FileInput(self.filename,inplace=1):
                line = line.replace(line_to_replace,replace_with)
                print(line, end='')


        






    # def main() :

    # # Opens a file and reads it into a list
    #     # filename = 'Crew.csv'
    #     # filestream = open_file(filename)
    #     # file_list = read_filestream_into_list(filestream)
    #     # for lines in file_list :
    #     #     print(lines)


    # # Tests the change_line_in_file function
    # #    filename = 'Crew.csv'
    # #    line_number = 'inn í línu 4'
    # #    test_str = 'inn í línu 4, sem ég breyti núna' # 'Þetta setti ég inn í línu {}'.format(line_number)

    # #    change_line_in_file(filename, line_number, test_str)

    # #    print("Búinn!")


    #     return


    # if __name__ == "__main__":
    #     main()