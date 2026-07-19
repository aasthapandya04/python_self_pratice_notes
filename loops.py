# for loops
# Number of iterations are known
# for loop is the most used loop in python

name = "John"
for i in name:
    print(i)


name = "Aastha"
for letter in name:
    print(letter)
    if(letter == 's'):
        print("Found the letter s")

colors = ["red", "green", "blue"]
for color in colors:
    print(color)
    for x in color:
        print(x)

# Range function

for a in range(5):
    print(a)
# 0 se 4 tak print karega

for k in range(1, 10):
    print(k+1) 
# 1 se 10 tak print karega

for m in range(1, 10, 2):
    print(m)
# increment by 2

# While loop
# number of iterations are not known

i = 0
while(i < 5):
    print(i)
    i = i + 1
print("loop ended")

# Decrementing Loop 

count = 5
while(count > 0):
    print(count)
    count = count - 1

# Else in while loop 

count = 5
while(count > 0):
    print(count)
    count = count - 1
else:
    print("Loop ended")

# Do While 
# Do While loop is not available in python 
# but we can simulate it using while loop

i = 0
while True:
    print(i)
    i = i + 1
    if(i % 100 == 0):
        break

# ismein error hai 
while True:
    number = int(input("Enter a number: "))
    print(number)
    if not number > 0:
        break

# error free code 

while True:
    try:
        number = int(input("Enter a number: "))
        print(number)

        if number <= 0:
            break
    except ValueError:
        print("Please enter a valid integer.")

# BREAK statement

for i in range(12):
    if(i==10):
        break
    print("5 X" , i+1 , "=", 5*(i+1))
print("Table completed")

# CONTINUE statement

for i in range(15):
    if(i==10):
        print("Skipping the iteration")
        continue
    print("5 X" , i+1 , "=", 5*(i+1))

# example :-

for i in range(1 , 101 , 1):
    print(i , end = " ")

    if(i == 50):
        break
    else:
        print("Mississipi")

print("Thank you")