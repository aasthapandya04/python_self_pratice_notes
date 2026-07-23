# String Formatting in python

letter = "Hi my name is {} and I am from {}"
letter = "Hi my name is {1} and I am from {0}"
# indexing . india would be print in 1st bracket and name in second . 
# Output - Hi my name is India and I am from Aastha
name = "Aastha"
country = "India"
print(letter.format(name, country))

# f strings

print(f"My name is {name} and i am from {country}")
# directly we can add variables 

price = 49.022140
txt = f"For only for {price:.2f} dollars"
print(txt)
# .2f - sirf 2 decimal places tak karega 

print(f"{2*30}")

# doc strings
# remeber - write it just below the function

def square(n):     # function
    '''Takes a number and does the square of it ''' # doc string that gives definition of function
    print(n**2)
square(5)
print(square.__doc__)
# doc string can be access using doc attribute