import random 

                    #0           1             2          3
Destinations= ["Miami",  "New Orleans",  "New York",  "Seattle"]

Restaurants= ["Olive Garden", "The Cheesecake Factory", "Empanada Mamas", "Mama Shushi"]

Transportations= ["Bus", "Train", "Jet", "Scooter"]

Entertainments = ["Museum", "Bar", "Site-seeing", "Dancing"]

destination = random.choice(Destinations)

restaurant = random.choice(Restaurants)

transportation = random.choice(Transportations)

entertainment = random.choice(Entertainments)

d = random.choice(Destinations)
r= random.choice(Restaurants)
t= random.choice(Transportations)
e= random.choice(Entertainments)

def run_day_trip_generator():
    day_trip=[destination,restaurant,transportation,entertainment]
    trip=[d,r,t,e]
 
    while True:
        print(f'Destination:{day_trip[0]}')
        print(f'Restaurant:{day_trip[1]}')
        print(f'Transportation:{day_trip[2]}')
        print(f'Entertainment:{day_trip[3]}')

        user_input = input("Are you satisfied with your trip?")
        print(user_input)

        if user_input =="Y":
            print_trip(trip)
            break 

        else:
           reselect_option(trip)
           run_day_trip_generator()
           

def print_trip(day_trip):
    day_trip=[destination,restaurant,transportation, entertainment]
    print("Here is your Day Trip!")
    print("")
    print(f'Destination:{day_trip[0]}')
    print(f'Restaurant:{day_trip[1]}')
    print(f'Transportation:{day_trip[2]}')
    print(f'Entertainment:{day_trip[3]}')
    print("ENJOY!!")


def reselect_option(trip):
    
    d = random.choice(Destinations)
    r= random.choice(Restaurants)
    t= random.choice(Transportations)
    e= random.choice(Entertainments)
    while True:    
        print("Oh no!")
        print("Lets Plan another trip!")
        user_input = input("Which option would you like to change? destination, restuarant, transportation, entertainment")
        print(user_input)
    
        if user_input == "destination":
            d=random.choice(Destinations)
            print(d)
            return [d,trip[1],trip[2],trip[3]]
        elif user_input == "restaurant":
              r= random.choice(Restaurants)
              print(r)
              return 
        elif user_input =="transportation":
            t= random.choice(Transportations)
            print(t)
            return
        elif user_input == "entertainment":
             e= random.choice(Entertainments)
             print(e)
             return
        else: 
            new_trip(trip)

def satisfied_new_trip():
    while True: 
        user_input=input("Are you satisfied with your new option?")
        print(user_input)
    
        if user_input =="N":
            new_trip()
            
       
        else: 
            reselect_option()
def new_trip(trip):
    print(d)
    print(r)
    print(t)
    print(e)
    return trip 


run_day_trip_generator()
