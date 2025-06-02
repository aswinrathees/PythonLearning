# Introduction to Lists

# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets [].
# Oredered items can be accessed by their index.
# Lists can contain different data types, including strings, integers, and even other lists.
# Mutable, meaning you can change, add, or remove items after the list has been created.

shoppingList = ["Milk", "Eggs", "Bread", "Butter"]
print(shoppingList)
print(shoppingList[0])  # Accessing the first item
print(shoppingList[1])  # Accessing the second item 
print(shoppingList[2])  # Accessing the third item
print(shoppingList[3])  # Accessing the fourth item

print(shoppingList[0:2])  # Slicing the first two items
print(shoppingList[1:])   # Slicing from the second item to the end

shoppingList.append("Cheese")  # Adding an item to the end of the list
print(shoppingList)

shoppingList.insert(2, "Yogurt")  # Inserting an item at a specific position
print(shoppingList)

shoppingList.remove("Eggs")  # Removing an item by value
print(shoppingList)

del shoppingList[1]  # Deleting an item by index
print(shoppingList)
print(len(shoppingList))  # Getting the length of the list

shoppingList2 = ['Peanuts', 'Chips', 'Soda']

# Merging two lists
shoppingList.extend(shoppingList2)
print(shoppingList)                  # Printing the merged list

shoppingList.sort()                  # Sorting the list
print(shoppingList)                  # Printing the sorted list

shoppingList.reverse()               # Reversing the list
print(shoppingList)                  # Printing the reversed list

print(shoppingList + shoppingList2)  # Concatenating two lists
shoppingList.clear()                 # Clearing the list
print(shoppingList)                  # Printing the cleared list
print(shoppingList2*2)               # Printing the second list


listNumbers = [1, 2, 3, 4, 5]
# List Comprehension
print(min(listNumbers))              # Minimum value in the list
print(max(listNumbers))              # Maximum value in the list