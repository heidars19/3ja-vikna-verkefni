from DB.FileHandlr import FileHandlr

class AirplaneFile (FileHandlr) :
    ''' 
    Filehandler for airplane table.\n
\n
    class AirplaneFile(data_to_append: [string or list]..., fieldname: [string]..., searchparam: [string or integer], line_to_replace: [string]..., replace_with: [string]... )    \n
\n
    Usage:\n
    Call class constructor with variable name. \n
    Append data \n
    MakeNewInstance = AirplaneFile(data_to_append=...) \n
    \n 
    Read data\n
    MakeNewInstance = AirplaneFile() \n
    --Empty constructor reads and returns a list\n
    
    Replace data\n
    AirplaneFile(line_to_replace=..., replace_with=...)\n
    \n
    Find data, returns line number, 0 if not found and -1 if error\n
    MakeNewInstance = AirplaneFile(fieldname=..., searchparam=...)
    '''
    
    # def start(self) :
    #     if self._data_to_append :
    #         return_value = FileHandlr.find_next_id(self)
    #         if return_value <= 0 :
    #             return return_value
    #         FileHandlr.append_data_to_file(self)
        
    #     elif self._line_to_replace : 
    #         FileHandlr.change_line_in_file(self)

    #     elif self._fieldname:
    #         self._line_number = FileHandlr.does_line_exists(self)
    #         return self._line_number

    #     else :
    #         FileHandlr.read_filestream_into_list(self)
    #         return self._data_list

    #     return


    def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None ) :

        self._filename = FileHandlr.AIRPLANE_TABLE
        self._header = FileHandlr.AIRLPANE_TABLE_HEADER
        self._data_to_append = data_to_append
        self._fieldname = fieldname
        self._searchparam = searchparam
        self._line_to_replace = line_to_replace
        self._replace_with = replace_with
        self._filestream = None
        self._line_number = None
        self._data_list = None
        self._id = 0

        