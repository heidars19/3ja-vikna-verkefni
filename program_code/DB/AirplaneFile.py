import FileHandlr
class AirplaneFile (FileHandlr) :
    ''' 
    Filehandler for airplane table.
    
    Call with variable names, for example: a = Airplane(data_to_append=data)
    
    '''

    def run_me() :
        if self.append :
            FileHandlr.append_data_to_file(self)
        
        elif self.fieldname:
            self.line_number = FileHandlr.does_line_exists(self)
            return self.line_number

        elif self.line_to_replace : 
            FileHandlr.change_line_in_file(self)

        else :
            FileHandlr.read_filestream_into_list(self)
            return self.data_list

        return


    def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None ) :

        self.filename = 'Aircraft.csv'
        self.header = 'plainID,plainType,manufacturer,model,capacity,'
        self.append = data_to_append
        self.fieldname = fieldname
        self.searchparam = searchparam
        self.line_to_replace = line_to_replace
        self.replace_with = replace_with


   
