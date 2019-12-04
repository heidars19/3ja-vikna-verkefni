import csv
import fileinput

class FileHandlr :
    ''' Abstract class for filehandling '''



    def append_data_to_file(self):
        ''' 
        Appends data to file, creates a new file if none exists, and adds a header. 

        Accepts a list with 1 line, name of file and a 
        header file (can skip if it's 100% the file exists already) 
        '''
        if isinstance(self.data_to_append, list) : 
            data_string = ",".join(self.data_to_append) # Changes a list to comma seperated string
        else :
            data_string = self.data_to_append

        with open(self.filename, 'a') as f:
            if f.tell() == 0: 
                # File is empty or we just created it, so we add a header
                f.write(self.header + '\n')
            f.write(data_string + '\n') # Append data to file


    def does_line_exists(self): 
        ''' 
        Checks if line exists in a file, returns line number, returns 0 if not found, returns -1 on error 
        '''

        self.filestream = open_file(self)
        if not self.filestream :
            return -1 # Error opening file

        reader = csv.DictReader(self.filestream, delimiter=',')
        self.filestream.close_file()

        for line_number, line in enumerate(reader): 
            if line[self.fieldname] == self.searchparam :
                return line_number+1 # Add 1 because this func doesn't count the header
        return 0


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


    def read_filestream_into_list(self):
        '''
        Takes a filestream, returns a list with file contents.
        Closes the file after reading it.
        '''
        data_list = []
        for line in self.filestream :
            data_list.append(line.strip())
        self.filestream.close() # Closes file after grabbing data from it
        self.data_list = data_list



    def change_line_in_file(self) :
        ''' 
        Replaces 1 line in a file. 

        line_to_replace can be a line number (int) or a complete line (str).
        When line_to_replace is a string, it can replace partial lines.
        '''
        
        if isinstance(self.line_to_replace, int) : # If line_to_replace is a line number (int)
            for i, line in enumerate(fileinput.FileInput(self.filename,inplace=1)) :
                if i == self.line_to_replace :
                    print(self.replace_with.strip())   # Strip to remove extra \n, cause print adds it anyways
                else :
                    print(line, end='')
        else :   # line_to_replace is a complete line (str)
            for line in fileinput.FileInput(self.filename,inplace=1):
                line = line.replace(self.line_to_replace,self.replace_with)
                print(line, end='')


    def __init__ (self, filename) :
        



    def __str__ (self) :
        
        
        pass
