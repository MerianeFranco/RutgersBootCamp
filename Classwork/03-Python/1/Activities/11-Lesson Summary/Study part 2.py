x = 1
y = 10

# Checks if one value is equal to another
if x == 1:
    print("x is equal to 1")

# Checks if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")

# Checks if one value is less than another
if x < y:
    print("x is less than y")

# Checks if one value is greater than another
if y > x:
    print("y is greater than x")

# Checks if a value is less than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

# Checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned true")

# Checks if either of two conditions is met
if x < 45 or y < 5:
    print("One or more of the statements were true")

# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")

print("----------------------------------------------")
# Chapter 6
# 1.
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")


# 2.
x = 2
y = 10
if len("Dog") < x:
    print(f"Question 2 works! The name fit on the space of {x} characters")
else:
    print("Still missing out, add more characters")

# 3.
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print(f"GOT QUESTION 3! x^3 = {x**3} and y^2 = {y**2} ")
else:
    print("Oh good you can count")

# 4.
name = "Paul"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if name in group_one:
    print(f"{name} is in the first group at position {group_one.index(name)}")
elif name in group_two:
    print(f"{name}  is in group two at position {group_two.index(name)}" )
elif name in group_three:
    print(name + " is in group three")
else:
    print(name + " does not have a group")


# 5.
height = 51
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")

print("Lists----------------------------------------------")

# Create a variable and set it as an List
myList = ["Jacob", 25, "Ahmed", 80]
print(myList)

# Adds an element onto the end of a List
myList.append("Matt")
print(myList)

# Returns the index of the first object with a matching value
print(myList.index("Matt"))

# Changes a specified element within an List at the given index
myList[3] = 85
print(myList)

# Returns the length of the List
print(f" Lenght of the list {len(myList)}")

# Removes a specified object from an List
myList.remove("Matt")
print(myList)
print(len(myList))
# Removes the object at the index specified
myList.pop(0)
myList.pop(0)
print(myList)

# Creates a tuple, a sequence of immutable Python objects that cannot be changed
myTuple = ('Python', 100, 'VBA', False)
print(myTuple)

print("Loop Dee Loop-----------------------------------------")

run = "y"

while run == "y":
# Loop through a range of numbers (0 through 4)
    for x in range(5):
        print(x)

    print("-----------------------------------------")

    # Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
    for x in range(2, 7):
        print(x)

    print("----------------------------------------")

    # Iterate through letters in a string
    word = "Peace"
    for letter in word:
        print(letter)

    print("----------------------------------------")

    # Iterate through a list
    zoo = ["cow", "dog", "bee", "zebra"]
    for animal in zoo:
        print(animal)

    print("----------------------------------------")

    # Loop while a condition is being met

    print("Hi!")
    run = input("To run again. Enter 'y': ")
