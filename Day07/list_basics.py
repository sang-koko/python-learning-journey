# Program: List Basics
# Topics Covered:
# 1. Creating a list
# 2. Accessing elements
# 3. Updating elements
# 4. len() function
# 5. in operator

# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:")
print(fruits)

# Accessing elements
print("\nAccessing Elements:")
print("First Element:", fruits[0])
print("Second Element:", fruits[1])
print("Last Element:", fruits[-1])

# Updating an element
fruits[1] = "Grapes"

print("\nList After Updating:")
print(fruits)

# Finding the length of the list
print("\nNumber of Elements:", len(fruits))

# Checking if an element exists using 'in'
item = input("\nEnter a fruit to search: ")

if item in fruits:
    print(item, "is available in the list.")
else:
    print(item, "is not available in the list.")
