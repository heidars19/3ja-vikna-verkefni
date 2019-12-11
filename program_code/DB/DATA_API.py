from DB.FileHandlr import FileHandlr
from DB.AirplaneFile import AirplaneFile
from DB.EmployeeFile import EmployeeFile
from DB.DestinationFile import DestinationFile
from DB.WorkTripFile import WorkTripFile
from DB.WorkTripFileOld import WorkTripFileOld



class DATA_API:


    def __init__ (self, keyword='', data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None, header=False):
        self.set_data(keyword=keyword, data_to_append=data_to_append, fieldname=fieldname, searchparam=searchparam, line_to_replace=line_to_replace, replace_with=replace_with, header=header)
        return

    def set_data (self, keyword='', data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None, header=False):
        '''
        Resets DATA_API
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
            if self.keyword == "worktripold":
                new_instance.archive_old_worktrips()
            return_value = new_instance.read_filestream_into_list()
            return return_value

        return FileHandlr.UNKNOWN_ERROR

        return


    def file_type(self):

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