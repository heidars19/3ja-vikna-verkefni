from DB.FileHandlr import FileHandlr

class WorkTripFileOld (FileHandlr) :
    ''' 
    Filehandler for WorkTripOld table.\n
\n
    class WorkTripFileOld(data_to_append: [string or list]..., fieldname: [string]..., searchparam: [string or integer], line_to_replace: [string]..., replace_with: [string]... )    \n
\n
    Usage:\n
    Call class constructor with variable name. \n
    Append data \n
    MakeNewInstance = WorkTripFileOld(data_to_append=...) \n
    \n 
    Read data\n
    MakeNewInstance = WorkTripFileOld() \n
    --Empty constructor reads and returns a list\n
    
    Replace data\n
    WorkTripFileOld(line_to_replace=..., replace_with=...)\n
    \n
    Find data, returns line number, 0 if not found and -1 if error\n
    MakeNewInstance = WorkTripFileOld(fieldname=..., searchparam=...)
    '''
    
    def start(self) :
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

        self.filename = FileHandlr.WORKTRIP_OLD_TABLE
        self.header = FileHandlr.WORKTRIP_OLD_TABLE_HEADER
        self.data_to_append = data_to_append
        self.fieldname = fieldname
        self.searchparam = searchparam
        self.line_to_replace = line_to_replace
        self.replace_with = replace_with
        self.filestream = None
