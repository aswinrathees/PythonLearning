# Introduction To Variables 

name = "Aswin"
print(name)

experience = 8
print(experience)

# Multiple assignment
name, experience = "Aswin", experience
print(name, experience)

aswinHome = ratheesHome = miniHome = "Chaithanya, Kochi"
print(aswinHome)

# Arithmetic operators
androidExperience = 3
iosExperience = 2

print(androidExperience + iosExperience)  # Addition
print(androidExperience - iosExperience)  # Subtraction
print(androidExperience * iosExperience)  # Multiplication
print(androidExperience / iosExperience)  # Division
print(androidExperience % iosExperience)  # Modulo Division

# Strings
firstName = "Aswin"
lastName = "Rathees"
print(firstName + " " + lastName)  # Concatenation

# String operations
greeting = "Hello, World! "
print(greeting)
print(greeting * 2)    # Repetition
print(len(greeting))   # Length of the string
print(greeting[0])     # First character
print(greeting[7:12])  # Slicing from index 7 to 11
print(greeting[0:])   # Slicing from index 1 to the end

# String Placeholders
name = "Aswin"
designation = "Software Engineer"
print("My name is %s and I am a %s." % (name, designation))  # Old style
print("My name is {} and I am a {}.".format(name, designation))  # New style
print(f"My name is {name} and I am a {designation}.")  # f-string

# Int and Float
name = "Aswin"
experience = 8
print("My name is %s and I have %d years of experience." % (name, experience))  # Old style
print("My name is {} and I have {} years of experience.".format(name, experience))  # New style

# Format
name = "Aswin"
print(f"My name is {name}")  # f-string