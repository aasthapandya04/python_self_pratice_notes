# functions 

# Function to calculate mean

def calculategmean(a , b):
    gmean = (a * b) / (a + b)
    print(gmean)
a = 4
b = 5
calculategmean(a, b)

c = 10
d = 20
calculategmean(c, d)

# # even odd nikalne ke liye function

def evenodd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter a number: "))
evenodd(num)

# # Pass in a function

def gmean(a, b):
    return (a * b)/(a + b)

def evenodd(num):
    if num % 2 == 0:
       print("Even")
    else:
         print("Odd")

def percentage (a, b):
    pass

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
num = int(input("Enter a number: "))

print(gmean(a, b))
evenodd(num)


# # Arguments in function

# # 1. Default Arguments

def average (a=9 , b =1):
   print("The average is ", (a + b)/2)

average(10)

# 2. Keyword Arguments

def average (a=2 , b=10):
    print("The average is ", (a + b)/2)

average(b=20)
average(a=5, b=15)

# 3. Required Arguments

def average (a , b, c=9):
    print("The average is ", (a + b + c)/3)
    average(10, 20)   
    # here c is default argument and a, b are required arguments. If we don't pass c then it will take default value 9.

# 4. Variable Length Arguments

def average(*numbers):
    print(type(numbers))   # will show <class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average is ", sum/len(numbers))

average(10, 20, 30, 40, 50)

def name(**name):
    print(type(name))
    print("Hello, my name is", name["fname"], name["lname"])
    
name(fname="John", lname="Doe")

# Return statement in function

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average is ", sum/len(numbers))

    return sum/len(numbers)
c = average(10, 20, 30, 40, 50)
print("The average is ", c)