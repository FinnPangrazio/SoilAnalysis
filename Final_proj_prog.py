#Ask which group of data the person wants to see
Question = input("Do you plan to use land for; Vegetables and Fruits? Cereal Cropping? Ornamental Crops? or for Grazing?")
Answer = input(Question)

#Dictionary to define use for soil
vegdict = {"1":"Vegetable and Fruits",
           "2":"Cereal Cropping",
           "3":"Ornamental Crops",
           "4":"Grazing"}

#Create Soil Type class and innitialising the subgroup of 'purpose' 
class Soil_Type:
    def __init__(purpose):
    
#Categorise the soils and their primary use
if SUBSCRPT == 'Bleached_Ferric':
    purpose = '1'
elif SUBSCRPT == 'Bleached_Mottled':
    purpose = '4'
elif SUBSCRPT == 'Endohypersodic':
    purpose = '2'
elif SUBSCRPT == 'Hypercalcic':
    purpose = '2'
elif SUBSCRPT == 'Ferric':
    purpose = '1'
elif SUBSCRPT == 'Friable':
    purpose = '4'
elif SUBSCRPT == 'Humosesquic':
    purpose = '4'
elif SUBSCRPT == 'Mottled-mesatronic':
    purpose = '3'
elif SUBSCRPT == 'Mottled-sodic':
    purpose = '3'
elif SUBSCRPT == 'Mottled-subnatric':
    purpose = '3'
elif SUBSCRPT == 'Petrocalcic':
    purpose = '2'
elif SUBSCRPT == 'Petroferric':
    purpose = '2'
elif SUBSCRPT == 'Sandy topsoil':
    purpose = '1'
elif SUBSCRPT == 'Deep sandy topsoil (dunes and ri':
    purpose = '1'


#Print the number of values for each of the 4 categories
if Answer == "Vegetables and Fruits"
   print (vars(purpose:1))
elif Answer == "Cereal Cropping"
   print (vars(purpose:2))
elif Answer == "Ornamental Crops"
   print (vars(purpose:3))
elif Answer == "Grazing"
   print (vars(purpose:4))
