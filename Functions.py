# Introduction to Functions

def greet(name):
    print(f"Hello, {name}!")

greet("Aswin")                             # This will print "Hello, Aswin!"

def add(a, b):
    return a + b

result = add(5, 3)                         # This will return 8
print(f"The sum of 5 and 3 is {result}.")  # This will print "The sum of 5 and 3 is 8."

# Built-in Functions

abs_value = abs(-10)  # This will return 10
print(f"The absolute value of -10 is {abs_value}.")  # This will print "The absolute value of -10 is 10."

print(bool(1))  # This will return True
print(bool(0))  # This will return False
print(bool(100)) # This will return True
print(bool(""))  # This will return False
print(bool("Hello"))  # This will return True
print(bool([]))  # This will return False

print(dir('hello')) # This will return a list of attributes and methods of the string object
print(help)

sent = "print('Hello')"
eval(sent)

def calculate_factorial(num):
    factorial = 1

    while num > 1:
        factorial *= num
        num -= 1
    
    return factorial

print(f"The factorial of 5 is {calculate_factorial(5)}.")  # This will print "The factorial of 5 is 120."