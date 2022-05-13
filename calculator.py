def add(a,b):
    answer=a+b
    return answer

def subtract(a,b):
    answer=a-b
    return answer

def multiply(a,b):
    answer=a*b
    return answer

def divide(a,b):
    answer=a/b
    return answer

def modulus(a,b):
    answer=a%b
    return answer

def intdivide(x,y):
    answer=x//y
    return answer

def exponent(x,y):
    answer=x**y
    return answer

def square(x):
    answer=x*x
    return answer

def cube(y):
    answer=y*y*y
    return answer

def factorial(x):
    factorial=1
    for number in range(1,x+1):
        factorial*=number
    return factorial
    
