#   Conditional statements :-

age = int(input("Enter your age: "))
print("Your age is: ", age)

if (age >= 18):
    print("You are eligible to vote.")

else:
    print("You are not eligible to vote.")


# Conditional operators
# <= >= == != < > 

print(age >= 18)
print(age <= 18)
print(age == 18)
print(age != 18)
print(age < 18)
print(age > 18)

# elif

# program to check if a number is positive, negative or zero

num = int(input("Enter a number: "))
if (num > 0):
    print("The number is positive.")
elif (num < 0):
    print("The number is negative.")
elif (num <= -989):
    print("The number is a special number.")
else:
    print("The number is zero.")

# program to check the budget and apple price

appleprice = 10
budget  = 200
if (budget - appleprice > 50):
    print("Alexa add 1 kg to the cart .")

elif (budget - appleprice > 70):
    print("Its okay you can buy")

else:
    print("Alexa dont add 1 kg to the cart.")

# nested if else

num = int(input("Enter a number: "))

if (num < 0):
    print("The number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1 and 10.")
    elif(num > 10 and num <= 20):
        print("Number is between 11 and 20.")       
    else:
        print("Number is greater than 20.")
else:
    print("The number is zero.")         