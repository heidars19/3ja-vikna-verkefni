from DB.FileHandlr import FileHandlr

class EmployeeFile (FileHandlr) :
    ''' 

    '''

    def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None, header=False ):
        '''

        '''
        
        self._filename = FileHandlr.STAFF_TABLE
        self._header = FileHandlr.STAFF_TABLE_HEADER
        self._data_to_append = data_to_append
        self._fieldname = fieldname
        self._searchparam = searchparam
        self._line_to_replace = line_to_replace
        self._replace_with = replace_with
        self._filestream = None
        self._line_number = None
        self._id = 0
