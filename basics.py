print(5)
print("Aastha")
a = ("Yash")
print(a)

a,b = int(input("Enter first number: ")), int(input("Enter second number: "))
print(a,b)
x = a + b
print(x)

# Variables and datatypes in python 

a = 5
print(type(a))

b = 60.2
print(type(b))

c = 22j 
print(type(c))

d = {"Name": "Aastha", "age": 20}
print(type(d))  

e = True 
print(type(e))  

f = set("Aastha")
print(type(f))  
print("Set with string: ", f)

g = "HARRY"
print(type(g))

h = ["Aastha", "Yash", "Riya"]
print(type(h))
print(h[0])

i = ("Aastha", "Yash", "Riya")
print(type(i))
print(i[0],i[1])

# Calculator in python

# selection of operation

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#  Addition 
c = a + b
print("Addition of two numbers is: ", c)

# Subtraction
d = a - b
print("Subtraction of two numbers is: ", d)

# multiplication
e = a * b
print("Multiplication of two numbers is: ", e)

# division 
f = a / b
print("Division of two numbers is: ", f)


# typecasting in python
#  explicit typecasting

string = "11"
number= 7
string_number = int(string) # int mein convert ho gaya
sum =  string_number + number
print("Sum of string and number is: ", sum)

# implicit typecasting

a = 1.9
b =2
print(type(a))
print(type(b))
print("addition of a and b is: ", a + b)# result apne aap float m change ho kr aayega
print(type(a + b))

# slicing of strings 

fruit = "Mango"
print(fruit[0:3]) # 0 se 2 tak print hoga positive slicing 

# negaitve slicing 
name = 'Aastha'
print(name[-4:-2])

# methods and opreations in the string

# 1. uppercase
name = "Aastha" 
print(name .upper())

# 2. lowercase
print(name .lower())

# 3. rstrip
fruit = "!!!pinelapple!!!!!!!"
print(fruit .rstrip("!"))   
# sirf last wala strip hoga aage wala nhi

# 4. replace
str1 = "pineapple is my favourite. pineapple is a  fruit"
print(str1.replace("pineapple", "banana")) 

# 5. split
print(str1.split(" ")) # space ke basis pe split hoga

# 6. Capitalise
print(str1.capitalize()) # first letter capital hoga baki small

# 7.centre
print(str1.center(50))

# 8. count
print(str1.count("pineapple")) # count karega ki kitni baar aaya hai

# 9.endswith
print(str1.endswith("fruit"))
# check karega ki last mein fruit hai ya nhi if yes then true otherwise false

print(str1.endswith("to" , 4 ,10 )) # check karega ki 4 se 10 ke beech mein to hai ya nhi

# 10. startswith
print(str1.startswith("pineapple")) 
# check karega ki start mein pineapple hai ya nhi if yes then true otherwise false

# 11.find
print(str1.find("my")) # find karega ki my kaha pe hai
print(str1.find("iish")) # agar nhi hai to -1 return karega

# 12. index
# similar to find . but agar woh word nhi hai to error dega
# print(str1.index("iissh"))

# 13. isalnum
print(name.isalnum()) 

# 14. isalpha
print(name.isalpha())

# 15. isdecimal
num = "123"
print(num.isdecimal()) 

# 16. isdigit
print(num.isdigit()) 

# 17. islower
print(name.islower())

# 18. isupper
print(str1.isupper())

# 19.isprintable
print(str1.isprintable()) 

str2 = "Hello\nWorld"
print(str2.isprintable()) # false because of \n

# 20. isspace
space = "   "
print(space.isspace()) # true because only space is there

# 21. istitle
title = "Hello World"
print(title.istitle()) # true because first letter of each word is capital

# 22. swapcase
swapcase = "Hello World"
print(swapcase.swapcase()) # swapcase karega capital ko small aur small ko capital

# 23. title
myself = "Hii my name is Aastha"
print(myself.title()) # first letter of each word will be capital


