# Good Morning Sir 
# Ek aisa program jo greet karega user ko time ke according 
# Ismein python ki time module ka use karenge (time module is pre installed in python)

import time

timestamp = time.strftime("%H:%M:%S")
print("Current time : " , timestamp)

# getting the current time 

hour = int(time.strftime("%H"))
print("Hour : " , hour)
minutes = int(time.strftime("%M"))
print("Minutes : " , minutes)
seconds = int(time.strftime("%S"))
print("Seconds : " , seconds)

# Greet the user 

if(5 <= hour < 12 ):
    print("Hieee user!! \n\"Good Morning\"")
elif(12 <= hour < 17) :
    print("Hieee user!! \n\"Good Afternoon\"")
elif(17 <= hour <= 21) :
    print("Hieee user!! \n\"Good Evening\"")
else:
    print("Hieee user!! \n\"Good Night\"")

# Time ranges used:
# 5:00 AM – 11:59 AM → Good Morning
# 12:00 PM – 4:59 PM → Good Afternoon
# 5:00 PM – 8:59 PM → Good Evening
# 9:00 PM – 4:59 AM → Good Night

# This is a simple and standard way to complete the exercise using Python time module.








