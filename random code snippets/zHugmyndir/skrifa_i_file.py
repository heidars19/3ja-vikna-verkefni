
STAFF_HISTORY_HEADER = "Nafn,Kennitale,Starf,Flugvél,Dags,Destination"


def append_data_to_file(data_list, name_of_file, header="") :
    ''' Appends data to file, creates a new file if none exists, and adds a header. 
        Accepts a list with 1 line, name of file (without file extension) and a 
        header file (can skip if it's 100% the file exists already) '''

    data_string = ",".join(data_list) # Changes a list to comma seperated string

    with open(name_of_file + '.csv', 'a') as f:
        if f.tell() == 0: 
            # File is empty or we just created it, so we add a header
            f.write(header + '\n')
        f.write(data_string + '\n') # Append data to file





def main() :
    
    # Býr til lista til að testa hluti með
    staff_history_list = ["Sigurgeir Helgason","2001765459","Flugmaður","Boeing 747","01.11.19","New York"]

    # Kallar á fall sem skrifar út í skrá
    append_data_to_file(staff_history_list, staff_history_list[1] , STAFF_HISTORY_HEADER)
    return

main()
    
if __name__ == "__main__":
    main()
    