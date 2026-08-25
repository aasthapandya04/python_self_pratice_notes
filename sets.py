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

# Methods in Sets

s1 = {1, 2, 65, 6, 11}
s2 = {11, 22, 33, 44, 55, 66, 88, 77}

# 1. union()
# all the values of both sets with common values one time
s3 = s1.union(s2)
print("Union of s1 and s2 = " , s3)

# 2. update()
s1.update(s2)
print("update method of elements of s1 from s2 , new s1 = " , s1)
print(s2)

# 3. intersection()
# on;y common values of both sets 
s5 = s1.intersection(s2)
print("intersection i.e. common items in both sets = " , s5)

# 4. intersection_update()
s1.intersection_update(s2)
print("intersection update" , s1)

# 5. symmetric_difference()
# all the values of both sets which not are common

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# 6. symmetric_difference_update()
cities2.symmetric_difference_update(cities)
print(cities)

# 7. difference()

cities4 = cities.difference(cities2)
print(cities4)

# 8. difference_update()
cities.difference_update(cities2)
print(cities)

# 9. isdisjoint()
print(cities.isdisjoint(cities2))

# 10. issubset()
print(cities.issubset(cities2))

# 11. issuperset()
print(cities.issuperset(cities2))

# 12. add()

name = {"Aastha", "Riya", "Ankita"}
name.add("Sakshi")
print(name)

# 13. update()
name2 = {"Riya", "Ankita", "Sakshi", "Aastha", "Pooja"}
name.update(name2)
print(name)

# 14. remove()
name.remove("Riya")
print(name)

# 15. pop()
item = name.pop()
print(item)  # it will remove any random item from set and return it

# 16. del kayword 
del name2

# 17. clear()
name.clear()
print(name)  # it will clear all items in set but an empty set will still exist

# 18. in keyword
if "Aastha" in name:
    print("Aastha is present in set")
else:
    print("Aastha is not present in set")