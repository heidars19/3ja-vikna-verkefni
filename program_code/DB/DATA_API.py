from DB.FileHandlr import FileHandlr
from DB_Models.AirplaneFile import AirplaneFile
from DB_Models.EmployeeFile import EmployeeFile
from DB_Models.DestinationFile import DestinationFile
from DB_Models.WorkTripFile import WorkTripFile
from DB_Models.WorkTripFileOld import WorkTripFileOld


class DATA_API:
    '''
    API for file handlers.\n
    class DATA_API(keyword: [string]..., data_to_append: [string or list]..., fieldname: [string]..., searchparam: [string or integer], line_to_replace: [string]..., replace_with: [string]..., header: [Bool]... ) :   \n
    \n
    Decides what FileHandlr function to run, based on given arguments.
    First run set_data() to prepare for action, then start() to complete it.
    Can only remember 1 set_sata() at a time.\n
            
    # You should only need 1 instance: 
    data_api = DATA_API()\n

    # Get a list: 
    data_api.set_data(keyword): keywords = 'employee', 'airplane', 'destionation', 'worktrip', 'worktripold' \n

    # Append line: 
    data_api.set_data(keyword, data_to_append="Bætir þessu við neðst í skránna")\n

    # Search by column: 
    data_api.set_data(keyword, fieldname="id", searchparam="148")\n

    # Replace a line by line-number or a matching previous line: \n
    data_api.set_data(keyword, line_to_replace="Skiptir út þessari línu", replace_with="Setur þessa línu í staðinn")\n
    data_api.set_data(keyword, line_to_replace=int, replace_with="Setur þessa línu í línu númer 'int'")\n

    # Runs the command prepared above: 
    data_api.set_data(keyword, header=True) \n

    possible_return_value = data_api.start() 
    '''

    def __init__ (self, keyword='', data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None, header=False):
        '''
        Calls set_sata() to handle initialization
        '''
        self.set_data(keyword=keyword, data_to_append=data_to_append, fieldname=fieldname, searchparam=searchparam, line_to_replace=line_to_replace, replace_with=replace_with, header=header)
        return


    def set_data (self, keyword='', data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None, header=False):
        '''
        Resets DATA_API\n
        Sets given arguments and resets all others.
        '''
        self.keyword = keyword
        self.data_to_append = data_to_append
        self.fieldname = fieldname
        self.searchparam = searchparam
        self.line_to_replace = line_to_replace
        self.replace_with = replace_with
        self.header = header 
        return


    def start(self):
        '''
        Performs actions for the class.
        '''
        filename = self.file_type()
        new_instance = filename(data_to_append=self.data_to_append, fieldname=self.fieldname, searchparam=self.searchparam, line_to_replace=self.line_to_replace, replace_with=self.replace_with, header=self.header )
        if self.header :
            return new_instance.get_header()

        if self.data_to_append :
            return new_instance.append_data_to_file()
        
        elif self.line_to_replace : 
            return new_instance.change_line_in_file()

        elif self.fieldname:
            self.line_number = new_instance.does_line_exists()
            return self.line_number

        else :
            if self.keyword == "worktrip":
                new_instance.archive_old_worktrips()
            return_value = new_instance.read_filestream_into_list()
            return return_value

        return FileHandlr.UNKNOWN_ERROR

        return


    def file_type(self):
        '''
        Uses the 'self.keyword' to get filename, so classes can be initialized with that name.
        '''

        file_type = ""

        if self.keyword == "employee":
            file_type = EmployeeFile

        elif self.keyword == "destination":
            file_type = DestinationFile

        elif self.keyword == "airplane":
            file_type = AirplaneFile

        elif self.keyword == "worktrip":
            file_type = WorkTripFile

        elif self.keyword == "worktripold":
            file_type = WorkTripFileOld

        else:
            return f"There is no such object type as {keyword}. Change keyword - should be string."

        return file_type
