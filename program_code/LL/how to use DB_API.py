from DB.DATA_API import *


# Fá lista:
new_instance = WorkTripFileOld()

# Bæta við línu (skrifar neðst í skránna):
new_instance = WorkTripFileOld(data_to_append="Bætir þessu við neðst í skránna")

# Leita eftir sérstökum dálk
new_instance = WorkTripFileOld(fieldname="id", searchparam="148")

# Skipta út línu, setja gömlu línuna eða línunúmer í line_to_replace
new_instance = WorkTripFileOld(line_to_replace="Skiptir út þessari línu", replace_with="Setur þessa línu í staðinn")
new_instance = WorkTripFileOld(line_to_replace=int, replace_with="Setur þessa línu í línu númer 'int'")


get_header_line = new_instance.header() # Skilar header í skrá
possible_return_value = new_instance.start()
