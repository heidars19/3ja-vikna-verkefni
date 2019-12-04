from DB.FileHandlr import FileHandlr

class AirplaneFile (FileHandlr) :
    ''' 
    Filehandler for airplane table.

    Airplane(data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None )    

    Usage:
    Call class constructor with variable name.
    Append data 
    MakeNewInstance = Airplane(data_to_append=data) 
    --data_to_append can be a list or a string
    
    Read data
    MakeNewInstance = Airplane() 
    --Empty constructor reads and returns a list
    
    Replace data
    Airplane(line_to_replace=data, replace_with=data)
    -- replace data with actual data
    
    Find data, returns line number, 0 if not found and -1 if error
    MakeNewInstance = Airplane(fieldname=data, searchparam=data1)
    -- Enter fieldname and data to make a search for a value
    
    
    Airplane(data_to_append=data) data_to_append can be a list or a string
    Call with variable names, for example: a = Airplane(data_to_append=data)
    
    '''

    def run_me(self) :
        if self.data_to_append :
            FileHandlr.append_data_to_file(self)
        
        elif self.line_to_replace : 
            FileHandlr.change_line_in_file(self)

        elif self.fieldname:
            self.line_number = FileHandlr.does_line_exists(self)
            return self.line_number

        else :
            FileHandlr.read_filestream_into_list(self)
            return self.data_list

        return


    def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None ) :

        self.filename = 'Aircraft.csv'
        self.header = 'plainID,plainType,manufacturer,model,capacity,'
        self.data_to_append = data_to_append
        self.fieldname = fieldname
        self.searchparam = searchparam
        self.line_to_replace = line_to_replace
        self.replace_with = replace_with
        self.filestream = None

        