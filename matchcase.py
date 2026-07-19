# Basic code 

x = int(input("Enter the value of x : "))
# x is the variable to match
match x :
    # if x is zero
    case 0 :
        print("x is zero")
    # case with if condition
    case 4 :
        print("Case is 4")
    case _ :
        print(x)

# match case mein if use kiya hai

x = int(input("Enter the value of x"))

match x :
    case 0 :
        print("x is zero")
    case 4 if x % 2 == 0 :
        print("Case x % 2 == 0 . case is 4")
    case _ if x < 10 :
        print("x is less than 10")
    case _:
        print(x)