# Introduction To Conditional statements
# Relational operators >, <, >=, <=, ==, !=
# Logical operators and, or, not

age = 18
if age > 17:
    print("You are an adult")  # This will be printed
else:
    print("You are a minor")  # This will not be printed

# Nested if, Logical operators and, or, not
if age > 18:
    print("You are an adult")
elif age == 18:
    print("You are exactly 18 years old")  # This will not be printed
elif age < 18 and age > 13:
    print("You are a teenager")  # This will not be printed
elif age < 13 and age > 0:
    print("You are a kid")
else:
    print("You are a baby")

if age <= 18 or age > 60:
    print("You are either a minor or a senior citizen")  # This will be printed


