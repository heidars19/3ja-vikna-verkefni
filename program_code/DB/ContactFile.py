class ContactFile :
    
    ''' Abstract class for filehandling '''
    
    def openFile(filename) :
        with open(filename, "r") as newfile :
            return newfile
    
    def __init__ (self, filename) :
        filestream = openFile(filename)
        
    
    
    
    
    
    
    
    pass