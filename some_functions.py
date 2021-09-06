def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)    

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)   

def fibonacci_like(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 3    
    else:
        return fibonacci_like(n - 3) + fibonacci_like(n - 2) + fibonacci_like(2 - 1)   
