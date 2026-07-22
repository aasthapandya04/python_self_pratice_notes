# Tuples 
# Tuples can be changed after creation. IMMUTABLE 

tup = (96, 33, 26, 45, 67, 89, 12, 34, 56, 78)
print(type(tup))
print(tup[5])

# Accessing elements in a tuple

print(tup[0:5])  # Slicing
print(tup[-6])   # negative indexing
print(tup[3])    #positive indexing
print(tup[4:9:2])
print(tup[2:])   # Slicing from index 2 to end
print(tup[:7])

# Manipulation of tuples 

countries = ('India', 'USA', 'UK', 'Canada', 'Australia')
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# Methods in Tuples

tuple1 = (1, 2, 3, 2, 4, 3, 2, 1, 1, 3, 2, 3,1,1)
res = list(tuple1)
res.append(5)
print(tuple(res))

result = tuple1.count(3)
print("The count of 3 in this tuple is:" , result )

result1 = tuple1.index(3)
print("The first occurence of 3 is :" , result1)

result2 = tuple1.index(3 , 4 , 8 )
print("From the given range first occurence of 3 is " , result2 )