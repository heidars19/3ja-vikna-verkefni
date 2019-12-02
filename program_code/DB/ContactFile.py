

class ContactFile :
    ''' Abstract class for filehandling '''

    def openFile(self, filename) :
        try :
            with open(filename, "r") as newfile :
                return newfile
        except :
            return None


    def __init__ (self, filename) :
        self.filestream = openFile(filename)



    def __str__ (self) :
        
        
        pass
