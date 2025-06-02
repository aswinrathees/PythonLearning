# Introduction to Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# Dictionaries are created using curly braces {}.
# Keys must be unique and immutable (strings, numbers, or tuples).
# Values can be of any data type and can be duplicated.
# Dictionaries are unordered, meaning the items do not have a defined order.
# Mutable, meaning you can change, add, or remove items after the dictionary has been created.

students = {'Alice': 25, 'Bob': 22, 'Charlie': 23}
print(students)  # Printing the dictionary
print(students['Alice'])  # Accessing the value associated with the key 'Alice'
print(students['Bob'])  # Accessing the value associated with the key 'Bob'     
print(students['Charlie'])  # Accessing the value associated with the key 'Charlie'


del students['Alice']  # Deleting the key 'Alice' and its value
print(students)  # Printing the dictionary after deletion

students['David'] = 24  # Adding a new key-value pair
print(students)  # Printing the dictionary after adding a new key-value pair

students['Bob'] = 23  # Updating the value associated with the key 'Bob'
print(students)  # Printing the dictionary after updating the value