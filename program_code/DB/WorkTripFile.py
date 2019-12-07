from DB.FileHandlr import FileHandlr

class WorkTripFile (FileHandlr) :
    ''' 
    Filehandler for WorkTrip table.\n
    \n
    class WorkTripFile(data_to_append: [string or list]..., fieldname: [string]..., searchparam: [string or integer], line_to_replace: [string]..., replace_with: [string]... )    \n
    \n
    Usage:\n
    Call class constructor with variable name. \n
    Append data \n
    MakeNewInstance = WorkTripFile(data_to_append=...) \n
    \n 
    Read data\n
    MakeNewInstance = WorkTripFile() \n
    --Empty constructor reads and returns a list\n
    
    Replace data\n
    WorkTripFile(line_to_replace=..., replace_with=...)\n
    \n
    Find data, returns line number, 0 if not found and -1 if error\n
    MakeNewInstance = WorkTripFile(fieldname=..., searchparam=...)
    '''

    def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None ) :

        self._filename = FileHandlr.WORKTRIP_TABLE
        self._header = FileHandlr.WORKTRIP_TABLE_HEADER
        self._data_to_append = data_to_append
        self._fieldname = fieldname
        self._searchparam = searchparam
        self._line_to_replace = line_to_replace
        self._replace_with = replace_with
        self._filestream = None
        self._line_number = None
        self._data_list = None
        self._id = 0
