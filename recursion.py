# Factorial 
# factorial(n) = n * factorial(n-1)

# 6! = 6*5*4*3*2*1
# and so on 

def factorial(n) :
    if(n==0 or n==1 ):
        return 1 
    else:
        return n * factorial(n-1) # same function called but with different arguments passed 

print(factorial(4))
print(factorial(8))
print(factorial(5))

# how the code will run :-
# 5* factorial (4) 
# 5* 4 * factorial (3) 
# 5* 4 * 3 *  factorial (2) 
# 5* 4 * 3 *  2 * factorial (1) 
# 5* 4 * 3 *  2 * 1 else ki jagah abb if m bhi enter karega 

# Fibonacci Series 

def fib(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return  1
    else :
        return fib(n - 1) + fib(n - 2)

print(fib(8))
print(fib(3))
print(fib(6))