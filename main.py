import random 



                    #0           1             2          3
Destinations= ["Miami",  "New Orleans",  "New York",  "Seattle"]

Restaurants= ["Olive Garden", "The Cheesecake Factory", "Empanada Mamas", "Mama Shushi"]

Transportations= ["Bus", "Train", "Jet", "Scooter"]

Entertainments = ["Museum", "Bar", "Site-seeing", "Dancing"]




#def run_day_trip_generator(): 
    #print(f'Destination:{random.choice(Destinations)}')

    #print(f'Restaurant: {random.choice(Restaurants)}')

    #print(f'Transportation:{random.choice(Transportations)}')

    #print(f'Entertainment:{random.choice(Entertainments)}')
    
    #return run_day_trip_generator



#print(f'Destination:{random.choice(Destination_list)}')

#print(f'Restaurant: {random.choice(Restaurant_List)}')

#print(f'Transportation:{random.choice(Transportation_list)}')

#print(f'Entertainment:{random.choice(Entertainment_list)}')


#rand_int= random.randrange(0,4)
#print(f'Destination:{Destination_list[rand_int]}')

#rand_int= random.randrange(0,4)
#print(f'Restaurant:{Restaurant_List[rand_int]}')

#rand_int = random.randrange(0,4)
#print(f'Transportation:{Transportation_list[rand_int]}')

#rand_int= random.randrange(0,4)
#print(f'Entertainment:{Entertainment_list[rand_int]}')

   
   
def select_destination(Destination_list):
        select_destination = random.choice(Destination_list)
        return select_destination

Destination = select_destination(Destinations)
print(f'Destination:{Destination}')

def select_restuarant(Restuarant_list):
    select_restuarant = random.choice(Restuarant_list)
    return select_restuarant

Restaurant = select_restuarant(Restaurants)
print(f'Restaurant:{Restaurant}')


def select_transportation(transportation_list): 
    select_transportation = random.choice(transportation_list)
    return select_transportation 

transporation = select_transportation(Transportations)
print(f'Transportation:{transporation}')


def select_entertainment(entertainment_list):
    select_entertainment = random.choice(entertainment_list)
    return select_entertainment

Entertainment = select_entertainment(Entertainments)
print(f'Entertainment:{Entertainment}')

input("Are you satisfied with your trip? Y or N")

#  Pascal demo start
#  Pascal demo end

def re_select_option (Destination_list, Restuarant_list,transportation_list, entertainment_list):
    confirm_bool = True
    while confirm_bool:
        re_select_destination = random.choice(Destination_list)
        re_select_restuarant = random.choice(Restuarant_list)
        re_select_transportation = random.choice(transportation_list)
        re_select_entertainment = random.choice(entertainment_list)
        user_input= re_select_destination, re_select_restuarant, re_select_transportation, re_select_entertainment
        print(user_input)
        Destination = re_select_option(Destinations)
        Restaurant = re_select_option(Restaurants)
        Transportation = re_select_option(Transportations)
        Entertainment = re_select_option (Entertainments)
        if user_input == "N":
            print(input(f'Which option would you like to change?: {Destination}, {Restaurant}, {Transportation}, {Entertainment})'))
        else: confirm_bool = False 
        print(f'Here is your day Trip!: ')
       

    return re_select_option(Destination_list,Restuarant_list, transportation_list, entertainment_list)


         


#def re_select_option()

#Trips = Destination, Restaurant,transporation, Entertainment

#for Trip in Trips: 
    #confirm_bool = True 
    #while confirm_bool:
     #if User_input == "N":
       #print(input(f'Which option would you like to change Destination, Restaurant, transporation, Entertainment'))
    #else: 
        #print(f'Here is your Day Trip!:{Trips}')

#print()

#def select_trip(trip_lists):
    #confirm_bool =True 
   #while confirm_bool: 
       #select_trip = 
#user_input = input("Are you satisfied with your trip?! (Y/N)")
#if user_input =='N':
   #input(f'Which option would you like to change{Destination}, {Restaurant}, {transporation}, {Entertainment}')
#print()


#def select_destination(Destination_list):
    #confirm_bool = True
    #while confirm_bool:
        #selected_destination = random.choice(Destination_list)
        #user_input = input(f'Are you satisfied with your trip to{selected_destination}(Y/N)?')
        #if user_input == "N": 
           # pass 
        #return selected_destination


