from DB.DATA_API import *


# Byrja efst í skjalinu:
data_api = DATA_API()

# Fá lista:
data_api.set_data(keyword)

# Bæta við línu (skrifar neðst í skránna):
data_api.set_data(keyword, data_to_append="Bætir þessu við neðst í skránna")

# Leita eftir sérstökum dálk
data_api.set_data(keyword, fieldname="id", searchparam="148")

# Skipta út línu, setja gömlu línuna eða línunúmer í line_to_replace
data_api.set_data(keyword, line_to_replace="Skiptir út þessari línu", replace_with="Setur þessa línu í staðinn")
data_api.set_data(keyword, line_to_replace=int, replace_with="Setur þessa línu í línu númer 'int'")

# Skilar header í skrá
data_api.set_data(keyword, header=True) 

possible_return_value = data_api.start() # Til að keyra breytingar niður í skrá





# # Fá lista:
# new_instance = WorkTripFileOld()

# # Bæta við línu (skrifar neðst í skránna):
# new_instance = WorkTripFileOld(data_to_append="Bætir þessu við neðst í skránna")

# # Leita eftir sérstökum dálk
# new_instance = WorkTripFileOld(fieldname="id", searchparam="148")

# # Skipta út línu, setja gömlu línuna eða línunúmer í line_to_replace
# new_instance = WorkTripFileOld(line_to_replace="Skiptir út þessari línu", replace_with="Setur þessa línu í staðinn")
# new_instance = WorkTripFileOld(line_to_replace=int, replace_with="Setur þessa línu í línu númer 'int'")


# get_header_line = new_instance.header() # Skilar header í skrá
# possible_return_value = new_instance.start()
