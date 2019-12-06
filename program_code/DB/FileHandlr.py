import csv
import fileinput
import datetime
import os

class FileHandlr :
    ''' Abstract class for filehandling '''

    AIRPLANE_TABLE = "Data/Airplane.csv"
    AIRLPANE_TABLE_HEADER = 'id,plane_id,plane_type,manufacturer,model,name,capacity,registration_date'
    
    STAFF_TABLE = "Data/Crew.csv"
    STAFF_TABLE_HEADER = 'id,ssn,name,address,mobile,email,role,rank,licence,registration_date'
    
    DESTINATION_TABLE = "Data/Destinations.csv"
    DESTINATION_TABLE_HEADER = 'id,destination,country,flight_time,distance,contact,emerg_number,airport,registration_date'
    
    WORKTRIP_TABLE = "Data/Worktrips.csv"
    WORKTRIP_TABLE_HEADER = 'id,flight_number_out,flight_number_home,departing_from,arriving_at,departure,arrival,aircraft_id,captain,copilot,fsm,fa1,fa2,registration_date'

    WORKTRIP_OLD_TABLE = "Data/Worktrips_old.csv"
    WORKTRIP_OLD_TABLE_HEADER = 'id,flight_number_out,flight_number_home,departing_from,arriving_at,departure,arrival,aircraft_id,captain,copilot,fsm,fa1,fa2,registration_date'
    
    def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None ) :
    
        self._filename = ''
        self._header = ''
        self._data_to_append = data_to_append
        self._fieldname = fieldname
        self._searchparam = searchparam
        self._line_to_replace = line_to_replace
        self._replace_with = replace_with
        self._filestream = None
        self._line_number = None
        self._data_list = None
        self._id = 0
        
        
    def find_id(self): 
        ''' 
        Finds the line number of a given id and returns it\n
        \n
        Returns -1 on error, 0 if empty file
        '''
        self._filestream = self.open_file()
        if not self._filestream :
            return -1 # Error opening file

        reader = csv.DictReader(self._filestream, delimiter=',')
        for linenumber, line in enumerate(reader):
            if int(line['id']) == self._searchparam :
                self._line_number = linenumber + 1 # Add 1 because this func doesn't count the header
                break
        self._filestream.close()
        
        if self._line_number > 0 :
            return self._line_number 
        else :
            return 0 # Empty file
        

    def find_next_id(self): 
        ''' 
        Finds the highest current id and sets self._id as that\n
        \n
        Returns -1 on error, 0 if empty file
        '''
        self._filestream = self.open_file()
        if not self._filestream :
            return -1 # Error opening file

        reader = csv.DictReader(self._filestream, delimiter=',')
        for line in reader: 
            if int(line['id']) > self._id :
                self._id = int(line['id'])
        self._filestream.close()
        
        if self._id > 0 :
            self._id += 1 # Increases current highest id by 1
            return self._id 
        else :
            return 0 # Empty file


    def get_header(self):
        ''' Returns headers of the file '''
        return self._header


    def append_data_to_file(self):
        ''' 
        Appends data to file, creates a new file if none exists, and adds a header. 

        Accepts a list with 1 line or 1 string
        '''
        
            
        if isinstance(self._data_to_append, list) : 
            data_string = ",".join(self._data_to_append) # Changes a list to comma seperated string
        else :
            data_string = self._data_to_append
            
        if self._id > 0 : # If line needs id, add it
            data_string = str(self._id) + ',' + data_string

        with open(self._filename, 'a', encoding='utf-8') as f:
            if f.tell() == 0: 
                # File is empty or we just created it, so we add a header
                f.write(self._header + '\n')
            f.write(data_string + ',' + str(datetime.datetime.now()) + '\n') # Append data to file


    def does_line_exists(self): 
        ''' 
        Checks if line exists in a file, returns line number, returns 0 if not found, returns -1 on error 
        '''
        self._filestream = self.open_file()
        if not self._filestream :
            return -1 # Error opening file

        reader = csv.DictReader(self._filestream, delimiter=',')
        
        for line_number, line in enumerate(reader): 
            if line[self._fieldname] == self._searchparam :
                self._filestream.close()
                return line_number+1 # Add 1 because this func doesn't count the header
        self._filestream.close()
        return 0


    def open_file(self):
        ''' 
        Opens a file and returns a filestream, or None if error.
        Does not close the file!
        '''
        try :
            f =  open(self._filename, 'r', encoding='UTF-8')
            return f
        except :
            return None


    def read_filestream_into_list(self):
        '''
        Takes a filestream, returns a list with file contents.
        Closes the file after reading it.
        '''
        self._filestream = self.open_file()
        if not self._filestream:
            return None
        data_list = []
        for line in self._filestream :
            data_list.append(line.strip())
        self._filestream.close() # Closes file after grabbing data from it
        self._data_list = data_list


    def change_line_in_file(self):
        filename2 = self._filename +".bak"

        with open(self._filename, 'r', encoding='utf-8') as file_original:
            with open(filename2, 'w+', encoding='utf-8') as file_bak:
                if isinstance(self._line_to_replace, int) : # If line_to_replace is a line number (int)
                    for linenumber, line in enumerate(file_original): # Reads 1 file line by line into another file
                        if linenumber == self._line_to_replace :
                            file_bak.write(self._replace_with + '\n')
                        else :
                            file_bak.write(line)
                else :
                    self._line_to_replace = self._line_to_replace + '\n' # Have to add newline, so LL we can accept normal strings

                    for line in file_original:
                        if line == self._line_to_replace :
                            file_bak.write(self._replace_with + '\n')
                        else :
                            file_bak.write(line)


        with open(filename2, 'r', encoding='utf-8') as file_bak:
            with open(self._filename, 'w+', encoding='utf-8') as file_original:
                for line in file_bak:
                    file_original.write(line)
        
        if os.path.exists(filename2): # Checks if .bak file exists and removes it if it does
            os.remove(filename2)

