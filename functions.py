def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def f2c(fahrenheit):
    if fahrenheit < -459.67:
        raise AssertionError("Farenheit is not valid")
    else:
        return multiply(subtract(fahrenheit, 32), 5 / 9) # <-- Fix this in step 7
