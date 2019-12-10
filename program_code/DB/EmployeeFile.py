from DB.FileHandlr import FileHandlr

class EmployeeFile (FileHandlr) :
    ''' 
    Filehandler for staff table.\n
    \n
    class EmployeeFile(data_to_append: [string or list]..., fieldname: [string]..., searchparam: [string or integer], line_to_replace: [string]..., replace_with: [string]... )    \n
    \n
    Usage:\n
    Call class constructor with variable name. \n
    Append data \n
    MakeNewInstance = EmployeeFile(data_to_append=...) \n
    \n 
    Read data\n
    MakeNewInstance = EmployeeFile() \n
    --Empty constructor reads and returns a list\n
    
    Replace data\n
    EmployeeFile(line_to_replace=..., replace_with=...)\n
    \n
    Find data, returns line number, 0 if not found and -1 if error\n
    MakeNewInstance = EmployeeFile(fieldname=..., searchparam=...)
    '''

    def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None, header=False ):
    
        self._filename = FileHandlr.STAFF_TABLE
        self._header = FileHandlr.STAFF_TABLE_HEADER
        self._data_to_append = data_to_append
        self._fieldname = fieldname
        self._searchparam = searchparam
        self._line_to_replace = line_to_replace
        self._replace_with = replace_with
        self._filestream = None
        self._line_number = None
        self._data_list = None
        self._id = 0
