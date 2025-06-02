# Introduction to For Loops

fruits = ["Apple", "Banana", "Cherry", "Date"]
numbers = (2, 4, 6, 8, 10)

for fruit in fruits:
    print(fruit)  # This will print each fruit in the list

for number in numbers:
    print(number)  # This will print each number in the tuple

for i in range(1, 10):
    print(i)  # This will print numbers from 1 to 9

for i in range(1, 10, 2):
    print(i)  # This will print odd numbers from 1 to 9

for i in range(10, 0, -1):
    print(i)  # This will print numbers from 10 to 1 in reverse order

# Nested for loop
for i in range(0, 5):  # Outer loop
    for j in range(0, 3):  # Inner loop
        print(i*j)  # This will print the values of i and j