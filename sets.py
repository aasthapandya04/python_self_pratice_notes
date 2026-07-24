# Sets are unordered collection of items 
# Key points to remember :-
# 1. Sets donot duplicate items 
# 2. Order of items can differ in output
# 3. Sets are unchangeable once made 

num = {2, 4, 6, 8, 9, 4, 8, 11} 
print(num)  # duplicate item can be seen in o/p

info = {"Aastha" , 20 , 5.9 , 8 , 20 , False}  # We can store different datatypes in sets
print(info) 
# order of items in sets may change so we can access set items using index

aastha = {}
print(type(aastha))   # type dict dega

harry = set()
print(type(harry))   # Now this is empty set and type o/p will be set

# Accesing items in sets 
# Use for loops . It will show all items 

for item in info :
    print(item)

