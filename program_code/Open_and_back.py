import datetime
import os

def convert_bytes(size_in_bytes):
    """
    This function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return "{:5.1f} {}".format(size_in_bytes, x)
        size_in_bytes /= 1024.0

def file_size(filename):
    """
    This function will return the file size
    """
    if os.path.isfile(filename):
        file_info = os.stat(filename)
        return convert_bytes(file_info.st_size)

def write_and_back(filename):
    filename2 = filename +".bak"

    start_time = datetime.datetime.now()
    print("Re-writing {}, size at: {}".format(filename, file_size(filename)))
    print("Starting at: {}".format(start_time))

    with open(filename, 'r', encoding='utf-8') as file_original:
        with open(filename2, 'w+', encoding='utf-8') as file_bak:
            for line in file_original:
                file_bak.write(line)

    with open(filename2, 'r', encoding='utf-8') as file_original:
        with open(filename, 'w+', encoding='utf-8') as file_bak:
            for line in file_original:
                file_bak.write(line)
    duration_time = datetime.datetime.now() - start_time
    print("Finished at: {}".format(datetime.datetime.now()))
    print("Duration at: {}".format(duration_time))
    print()

def whole_file_into_memory(filename) :
    filename2 = filename + ".bak"

    start_time = datetime.datetime.now()
    print("Re-writing {}, size at: {}".format(filename, file_size(filename)))
    print("Starting at: {}".format(start_time))

    origin_list = []
    with open(filename, 'r', encoding='utf-8') as file_original:
        for line in file_original :
            origin_list.append(line.strip())
    
    with open(filename2, 'w+', encoding='utf-8') as file_bak:
        for line in origin_list:
            file_bak.write(line)

    origin_list = []
    with open(filename2, 'r', encoding='utf-8') as file_bak:
        for line in file_bak :
            origin_list.append(line.strip())
    
    with open(filename, 'w+', encoding='utf-8') as file_original:
        for line in origin_list:
            file_original.write(line)

    duration_time = datetime.datetime.now() - start_time
    print("Finished at: {}".format(datetime.datetime.now()))
    print("Duration at: {}".format(duration_time))
    print()


# whole_file_into_memory("test0.1mb.csv")
# whole_file_into_memory("test1.0mb.csv")
# whole_file_into_memory("test4.2mb.csv")
# whole_file_into_memory("test111.3mb.csv")

write_and_back("test0.1mb.csv")
write_and_back("test1.0mb.csv")
write_and_back("test4.2mb.csv")
write_and_back("test111.3mb.csv")


'''
Speed tests reading and writing 1 line at a time:
Re-writing test1.0mb.csv, size at:   1.0 MB
Duration at: 0:00:00.020993

Re-writing test0.1mb.csv, size at:   2.8 MB
Duration at: 0:00:00.039985

Re-writing test4.2mb.csv, size at:   4.1 MB
Duration at: 0:00:00.056982

Re-writing test111.3mb.csv, size at: 101.5 MB
Duration at: 0:00:01.516860


Skifað í lista fyrst:
Re-writing test1.0mb.csv, size at:   1.0 MB
Duration at: 0:00:00.020989

Re-writing test0.1mb.csv, size at:   2.8 MB
Duration at: 0:00:00.042986

Re-writing test4.2mb.csv, size at:   4.1 MB
Duration at: 0:00:00.067976

Re-writing test111.3mb.csv, size at: 101.5 MB
Duration at: 0:00:01.594281
'''