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

new_trip=[d,r,t,e]

#list_of_options= Destinations + Restaurants + Transportations + Entertainments

def run_trip():
    day_trip = [destination,restaurant, transportation, entertainment]
    
    print(f'Destination:{day_trip[0]}')

    print(f'Restaurant: {day_trip[1]}')

    print(f'Transportation:{day_trip[2]}')

    print(f'Entertainment:{day_trip[3]}')

    user_input = input("Are you satisfied with your trip?")

    print(user_input)
        
    if user_input == "Y":
          print(f'Destination:{day_trip[0]}')

          print(f'Restaurant: {day_trip[1]}')

          print(f'Transportation:{day_trip[2]}')

          print(f'Entertainment:{day_trip[3]}')
          
            
              
    else:
        
        reselect_option()
        satisfied_trip()

    

    




def run_day_trip_generator():
    
    print("Oh no!")
    print("Lets Plan another getaway!")
    
    user_input = input("Are you ready for your next trip?")
    print(user_input)

    if user_input =="Y":
        print(f'Destination:{day_trip[0]}')

        print(f'Restaurant: {day_trip[1]}')

        print(f'Transportation:{day_trip[2]}')

        print(f'Entertainment:{day_trip[3]}')

    
    destination = random.choice(Destinations)

    restaurant = random.choice(Restaurants)

    transportation = random.choice(Transportations)

    entertainment = random.choice(Entertainments)

    day_trip = [destination,restaurant, transportation, entertainment]
    #new_trip = [d,r,t,e,]
    while True:
    
        print(f'Destination:{day_trip[0]}')

        print(f'Restaurant: {day_trip[1]}')

        print(f'Transportation:{day_trip[2]}')

        print(f'Entertainment:{day_trip[3]}')

        user_input = input("Are you satisfied with your trip?")

        print(user_input)
        if user_input == "Y":
            print_trip()
            break
        
        else:
               
            day_trip= reselect_option(day_trip)

           # new_trip =reselect_trip (new_tri
                #day_trip= reselect_option(day_trip)
          

def print_trip():

        print("")
        print("Here is your Day Trip!!")
        print(f'Destination:{destination}')
        print(f'Restaurant: {restaurant}')
        print(f'Transportation:{transportation}')
        print(f'Entertainment:{entertainment}')
        print("")
        print("Enjoy!!!")  
    

    

        

def reselect_option():
   
    
    while True:
        print("Oh no!")
        print("Lets Plan another trip!")
        user_input = input("Are you ready for your next trip?")
        print(user_input)

  
        if user_input=="Y":
            print_new_trip()
            
            break
            print(d)
            print(r)
            print(t)
            print(e)
        else:
            print(d)
            print(r)
            print(t)
            print(e)
            break 
    
           
def print_new_trip():

            print(d)
            print(r)
            print(t)
            print(e)

    

def reselect_trip():

    user_input = input("are")
    print(user_input)
    new_trip = [d,r,t,e,]

    print(f'New Destination:{d}')
    print(f'Restaurant: {r}')
    print(f'Transportation:{t}')
    print(f'Entertainment:{e}')
    print(new_trip)
    print("Enjoy!!!")  
   
        
def satisfied_trip():
    user_input= input("Are you satisfied with your new trip?")
    print(user_input)
    while True:
        if user_input == "Y": 
        
            print("Enjoy!")
            break
        
        else:
            reselect_option(d,r,t,e,)
        

    
        user_input= input("Are you satisfied with your new trip?")
        print(user_input)
        
        if user_input == "y":
                    print(d)
                    print(r)
                    print(t)
                    print(e)

        else:
            print()
           

run_trip()

