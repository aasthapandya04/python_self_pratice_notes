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