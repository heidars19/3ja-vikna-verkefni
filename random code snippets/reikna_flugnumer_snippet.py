

# Constants representing index in worktrip list
DEST_CODE_INDEX = 0
DEST_ID_INDEX = 0
WORKTRIP_DATE_INDEX = 0
FLIGHT_ID_OUT = 0
FLIGHT_ID_HOME = 0


def add_flightnumbers (destination_code, work_list) :
    '''  
    Final process of flight codes. Injects them into worktrip list,\n
    then writes lines into database.
    '''
    result_list = []
    for i, element in enumerate(work_list, step=2) :
        flight_id_out = FLUGFELAG + destination_code + str(i)
        flight_id_home = FLUGFELAG + destination_code + str(i+1)
        element[FLIGHT_ID_OUT] = flight_id_out
        element[FLIGHT_ID_HOME] = flight_id_home
        if int(element[0]) > 0 : # Overwrite lines in database
            new_instance = WorkTripFileOld(fieldname="id", searchparam=element[0])
            line_number = new_instance.start()
            new_instance = WorkTripFileOld(line_to_replace=line_number, replace_with=element)
            line_number = new_instance.start()
        else :  # Append a new line into database
            new_instance = WorkTripFileOld(data_to_append=element)
            line_number = new_instance.start()


def process_list_by_index(working_list, data_filter, element_index) :
    ''' 
    Collects elements of a list with where 'data_filter' corresponds to 'element_index'\n
    Returns a list
    '''
    new_list = []
    for element in working_list :
        if data_filter == element[element_index] :
            new_list.append(element)
    return new_list

    
def process_list(incoming_list, id_num="0"):
    ''' 
    Finds an element of a list with id == 'id_num'\n
    Returns a list
    ''' 
    for element in incoming_list:
        if element[0] == id_num :
            return element[DEST_CODE_INDEX]   # When id is found, return the destination_code 
    return 0 # Didn't find, or error
    

def register_worktrip(worktrip) :
    '''  
    Registers a worktrip and calculates the flight number. Re-arranges previous flight-numbers\n
    if needed    
    '''
    destination_id = worktrip[DEST_ID_INDEX] 
    worktrip_date = worktrip[WORKTRIP_DATE_INDEX] 

    FLUGFELAG = "NA"
    
    # destination_code   
    destination_list = get_updated_list_from_DB("Destination")     #  Gets list from database
    destination_code = process_list(destination_list, destination_id)   # Gets destination_code from a list            
    
    
    #------------------- Last number in flightnumber -----------------------------#

    worktrip_full_list = []
    worktrip_full_list = get_updated_list_from_DB("Worktrips")   # Fá lista
    workingy_list = process_list_by_index(worktrip_full_list, worktrip_date, WORKTRIP_DATE_INDEX) # Filters list by date
    same_day_list = process_list_by_index(workingy_list, destination_id, DEST_ID_INDEX) # Filters list by destination
    
    if len(same_day_list) == 0 :
        worktrip_number = 0 # No other trips this day, so write directly to DB
        new_instance = WorkTripFileOld(data_to_append=element)
        line_number = new_instance.start()      
    else :        
        # fleiri ferðir þennan dag
        same_day_list.append(worktrip) # Add current worktrip to the list from DB
        
        work_list = sorted(same_day_list, key = lambda x: x[-1]) # Sort by last element (maybe???)
        add_flightnumbers(destination_code, work_list)  # Processes flight number and injects them into list, write in database
    return 
    
                