import csv
import datetime
import os

class FileHandlr :
    ''' 
    Abstract class for filehandling\n
    Contains all the functionality for the filehandlers.
    '''

    # Return constants
    WRONG_FORMAT = -5 # Value error
    FILENOTFOUND = -404
    UNKNOWN_ERROR = -1
    UNSUCCESSFUL = 0 # No error, but search yealded no results
    SUCCESS = 1 # For when you have no results to send back

    AIRPLANE_TABLE = "Data/Airplane.csv"
    AIRLPANE_TABLE_HEADER = 'id,plane_id,plane_type,manufacturer,capacity,name,registration_date'
    
    STAFF_TABLE = "Data/Employee.csv"
    STAFF_TABLE_HEADER = 'id,ssn,name,address,mobile,email,role,rank,licence,registration_date'
    
    DESTINATION_TABLE = "Data/Destinations.csv"
    DESTINATION_TABLE_HEADER = 'id,destination,country,flight_time,distance,contact,emerg_number,airport,destination_code,registration_date'
    
    WORKTRIP_TABLE = "Data/Worktrips.csv"
    WORKTRIP_TABLE_HEADER = 'id,flight_number_out,flight_number_home,departing_from,arriving_at,departure,arrival,aircraft_id,captain,copilot,fsm,fa1,fa2,staffing_status,registration_date'

    WORKTRIP_OLD_TABLE = "Data/Worktrips_old.csv"
    WORKTRIP_OLD_TABLE_HEADER = 'id,flight_number_out,flight_number_home,departing_from,arriving_at,departure,arrival,aircraft_id,captain,copilot,fsm,fa1,fa2,staffing_status,registration_date'
    
    
    def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None, header=False ) :
    
        self._filename = ''
        self._header = ''
        self._data_to_append = data_to_append
        self._fieldname = fieldname
        self._searchparam = searchparam
        self._line_to_replace = line_to_replace
        self._replace_with = replace_with
        self._filestream = None
        self._line_number = None
        self._id = 0
        self._header = header


    def start(self) :
        '''
        
        '''
        if self._data_to_append :
            return FileHandlr.append_data_to_file(self)
        
        elif self._line_to_replace : 
            return FileHandlr.change_line_in_file(self)

        elif self._fieldname:
            self._line_number = FileHandlr.does_line_exists(self)
            return self._line_number

        else :
            if str(type(self)) == "<class 'DB_Models.WorkTripFileOld.WorkTripFileOld'>":
                FileHandlr.archive_old_worktrips(self)
            return_value = FileHandlr.read_filestream_into_list(self)
            return return_value
        
        return FileHandlr.UNKNOWN_ERROR


    def remove_file(file_to_remove) :
        try :
            if os.path.exists(file_to_remove): # Checks if .bak file exists and removes it if it does
                try :
                    os.remove(file_to_remove)
                    return FileHandlr.SUCCESS # Success
                except:
                    return FileHandlr.UNKNOWN_ERROR
            else :
                FileHandlr.FILENOTFOUND
        except :
            return FileHandlr.UNKNOWN_ERROR


    def write_back(self, BACKUP_FILE) :
        try :
            with open(BACKUP_FILE, 'r', encoding='utf-8') as file_bak:
                with open(self._filename, 'w+', encoding='utf-8') as file_original:
                    for line in file_bak:
                        file_original.write(line)
        except :
            return FileHandlr.UNKNOWN_ERROR
        return FileHandlr.SUCCESS


    def archive_old_worktrips(self) :

        now_time = datetime.datetime.now() # Gets currents timestamp
        BACKUP_FILE = self._filename + ".bak"
        archive_filename = self._filename.split('.')
        ARCHIVE_FILE = archive_filename[0] + '_old.' + archive_filename[1]

        try :
            with open(self._filename, 'r', encoding='utf-8') as read_from_file:
                with open(BACKUP_FILE, 'w+', encoding='utf-8') as bak_file:
                    with open(ARCHIVE_FILE, 'a', encoding='utf-8') as archive_file:

                        list_line = []
                        for line in read_from_file :
                            list_line = line.strip().split(',')
                            if list_line[0] == 'id' : # If this is header line, jump to next iteration
                                bak_file.write(line) # Copies over header
                                continue
                            # list_line[5] should be the date column, change index number if not
                            try :
                                line_date = datetime.datetime.strptime(list_line[5], "%Y-%m-%d %H:%M")  # "%Y-%m-%d %H:%M:%S.%f" for full isoformat date
                            except ValueError :
                                # Date in file has wrong format
                                return FileHandlr.WRONG_FORMAT
                            if now_time > line_date + datetime.timedelta(hours = 1): # Worktrip is over 1 hour after landing in Iceland
                                archive_file.write(line) # Archives old worktrips
                            else:
                                bak_file.write(line) # Writes future worktrips into a new file 
        except FileNotFoundError:
            return FileHandlr.FILENOTFOUND 
        except :
            return FileHandlr.UNKNOWN_ERROR

        catch_return = self.write_back(BACKUP_FILE)  # Write back over original file
        if catch_return == FileHandlr.SUCCESS:
            return FileHandlr.remove_file(BACKUP_FILE)  # Remove backup file
        else :
            return catch_return



    def find_next_id(self, header_id='id'): 
        ''' 
        Finds the highest current id and sets self._id as that\n
        \n
        Returns id, 0 if empty file or error number on error
        '''
        self._filestream = self.open_file()

        try:
            self._id = 0
            reader = csv.DictReader(self._filestream, delimiter=',')
            for line in reader: 
                try: 
                    if int(line[header_id]) > self._id :
                        self._id = int(line[header_id])
                except: # empty database og a corrupt line/wrong format
                    continue
        except:
            # return FileHandlr.UNKNOWN_ERROR
            pass
        finally:
            try:
                self._filestream.close()
            except:
                pass
        
        if self._id >= 0 :
            self._id += 1 # Increases current highest id by 1
            return self._id 
        else :
            if self._filestream == FileHandlr.UNKNOWN_ERROR or self._filestream == FileHandlr.FILENOTFOUND:
                return self._filestream # Extend error from opening the file
            return FileHandlr.UNSUCCESSFUL # Empty file (or no id column)


    def get_header(self):
        ''' Returns headers of the file '''
        return self._header


    def append_data_to_file(self):
        ''' 
        Appends data to file, creates a new file if none exists, and adds a header. \n

        Accepts a list with 1 line or 1 string
        ''' 
        if isinstance(self._data_to_append, list) : 
            data_string = ",".join(self._data_to_append) # Changes a list to comma seperated string
        else :
            data_string = self._data_to_append
            
        # To prevent 'id' creation when adding a file into the archived WorkTripFileOld
        if not str(type(self)) == "<class 'DB_Models.WorkTripFileOld.WorkTripFileOld'>":
            return_value = FileHandlr.find_next_id(self)
            if return_value <= 0 : 
                return return_value # Extend error from find_next_id

        if self._id > 0 : # If line needs id, add it
            data_string = str(self._id) + ',' + data_string

        self._filestream = self.open_file('a')
        if self._filestream == FileHandlr.UNKNOWN_ERROR or self._filestream == FileHandlr.FILENOTFOUND:
            return self._filestream # Extend error from opening the file
        try :
            if self._filestream.tell() == 0: 
                # File is empty or we just created it, so we add a header
                self._filestream.write(self._header + '\n')
            self._filestream.write(data_string + ',' + str(datetime.datetime.now()) + '\n') # Append data to file
            return FileHandlr.SUCCESS
        except : # Unknown error
            return FileHandlr.UNKNOWN_ERROR


    def does_line_exists(self): 
        ''' 
        Checks if line exists in a file, returns line number, returns 0 if not found, returns -1 on error 
        '''
        self._filestream = self.open_file()

        try :
            if self._filestream <= 0 :
                return self._filestream # Extends the error

        except TypeError: # Filestream is not integer, so must be file object
            reader = csv.DictReader(self._filestream, delimiter=',')
            for line_number, line in enumerate(reader): 
                if line[self._fieldname] == self._searchparam : 
                    self._filestream.close()
                    return line_number + 1 # Add 1 because this func doesn't count the header
            self._filestream.close()
            return FileHandlr.UNSUCCESSFUL
    
        except : # Something else went wrong
            return FileHandlr.UNKNOWN_ERROR


    def open_file(self, mode='r'):
        ''' 
        Opens a file and returns a filestream\n
        Does not close the file!
        '''
        try :
            f =  open(self._filename, mode, encoding='UTF-8')
            return f
        except FileNotFoundError:
            return FileHandlr.FILENOTFOUND
        except :
            return FileHandlr.UNKNOWN_ERROR


    def read_filestream_into_list(self):
        '''
        Takes a filestream, returns a list with file contents.
        '''
        self._filestream = self.open_file()
        if self._filestream == FileHandlr.UNKNOWN_ERROR or self._filestream == FileHandlr.FILENOTFOUND:
            return self._filestream # Extend error from opening the file
        try :
            data_list = []
            for line in self._filestream :
                data_list.append(line.strip())
            self._filestream.close() # Closes file after grabbing data from it
            return data_list
        except : # Something went wrong
            self._filestream.close()
            return FileHandlr.UNKNOWN_ERROR


    def change_line_in_file(self):
        '''
        Changes a file
        '''
        # Reads a file 1 line at a time and writes each line immediately before reading second line
        # Writes changes into a new file at first, then overwrites original file
        # Then removes the temporary .bak file
        # Breaks loops on error before removing any file

        BACKUP_FILE = self._filename +".bak"
        try :
            with open(self._filename, 'r', encoding='utf-8') as file_original:
                with open(BACKUP_FILE, 'w+', encoding='utf-8') as file_bak:
                    if isinstance(self._line_to_replace, int) : # If line_to_replace is a line number (int)
                        for linenumber, line in enumerate(file_original): # Reads 1 file line by line into another file
                            if linenumber == self._line_to_replace :
                                file_bak.write(self._replace_with + '\n')
                            else :
                                file_bak.write(line)
                    else :
                        self._line_to_replace = self._line_to_replace + '\n' # Have to add newline, so we can accept normal strings

                        for line in file_original:
                            if line == self._line_to_replace :
                                file_bak.write(self._replace_with + '\n')
                            else :
                                file_bak.write(line)
        except :
            return FileHandlr.UNKNOWN_ERROR

        catch_return = self.write_back(BACKUP_FILE)  # Write back over original file
        if catch_return == FileHandlr.SUCCESS:
            return FileHandlr.remove_file(BACKUP_FILE)  # Remove backup file
        else :
            return catch_return



