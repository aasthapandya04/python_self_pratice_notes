# Lists in python

marks = [90, 80, 70, 60, 50]
print(marks)
print(type(marks))

# Indexing of list 
print(marks[4])
print(marks[2])
print(marks[1])

lis1 = [1, 2, 3, 4, 5 , "Aastha" , "Rajesh" , 63 , 98]
print(lis1[5])

# positive indexing 

print(lis1[0])
print(lis1[1])
print(lis1[3])

# negative indexing

print(lis1[-1])
print(lis1[-4])

# positive to negative indexing

print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

# check whether an item exists in a list or not
# Use in Keyword 

Colors = ["Red", "Green", "Blue", "Yellow"]
if "Red" in Colors:
    print("Yes, 'Red' is present in the list of colors")
else:
    print("No, 'Red' is not present in the list of colors")

# Range of index 

print(Colors)
print(Colors[1:3])
print(Colors[:])
print(Colors[2:])
print(Colors[:3])
print(Colors[1:4:2])
# jump index = 2 doo doo jumps kar ke values dega 

# List Comprehension

lst3 = [33 , 44 , 55 , 66 , 77 , 88]
lst3 = [i for i in range(4)]
print(lst3)
lst3 = [i for i in range(4) if i%2==0]
print(lst3)

# List Methods in Python

list = [3, 55, 78 , 66, 36, 94 , 88 , 52 , 6]

# 1. Append Method
# adds an element at the end of the list

list.append(100)
print(list)

# 2. sort()

list.sort()  # increasing order sort 
list.sort(reverse=True)  # reverse order sort
print(list)

# 3. reverse()

list.reverse()  # reverse the original list
print(list)

# 4. index()

print(list.index(6))  # returns the index of the first occurrence of the specified value
print(list.index(88))

# 5. count()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
print(list1.count(1))  # returns the number of occurrences of the specified value
print(list1)

# 6.copy()

list2 = [1, 2, 3, 4, 5]
print(list2)

m = list2.copy()  # returns a copy of the specified list
m[0] = 0
print(list2)

# 7. insert()

list2.insert(0, 100)  # inserts an element at the specified position
print(list2)

# 8. extend()

k = [900, 1000, 1100]
list2.extend(k)  # adds the elements of a list (or any iterable), to the end of the current list
print(list2)


list4 = [33, 66, 99, 88, 77, 55, 44, 22]
m = k.copy()
k = m + list4
print(k)

list4.extend(m)
print(list4)

