
# Creates a variable with a string "Frankfurter"
title = "Frankfurter"

# Creates a variable with an integer 80
years = 80

# Creates a variable with the boolean value of True
expert_status = True

# Prints a statement adding the variable
print("Nick is a professional " + title)

# Convert the integer years into a string and prints
print("He has been coding for " + str(years) + " years")

# Converts a boolean into a string and prints
print("Expert status: " + str(expert_status))

# An f-string accepts all data types without conversion
print(f"Expert status: {expert_status}")

# Create a variable called 'name' that holds a string
name = "Vikas"

# Create a variable called 'country' that holds a string
country = "United States"

# Create a variable called 'age' that holds an integer
age = 25

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 15

# Calculate the daily wage for the user
daily_wage = hourly_wage * 8

# Create a variable called 'satisfied' that holds a boolean
satisfied = True

# Print out "Hello <name>!"
print("Hello " + name + "!")

# Print out what country the user entered
print("You live in " + country)

# Print out the user's age
print("You are " + str(age) + " years old")

# With an f-string, print out the daily wage that was calculated
print(f"You make {daily_wage} per day")

# With an f-string, print out whether the users were satisfied
print(f"Are you satisfied with your current wage? {satisfied}")


# Make a calculation 
print (f"Years * Money * 180 is equal to  {years *180* daily_wage} and this doesn't make any sense" )


#### Chap 3
# Collects the user's input for the prompt "What is your name?"
snack = input("What is your snack for today? ")

# Collects the user's input for the prompt "How old are you?" 
# and converts the string to an integer.
amount = int(input("How many do you have "))

# Collects the user's input for the prompt "Is input truthy?" 
# and converts it to a boolean. Note that non-zero,
#   non-empty objects are truth-y.
trueOrFalse = bool(input("Is the input truthy? "))

# Creates three print statements that to respond with the output.
print("My snack is " + str(snack))
print("I will eat " + str(amount) + " today.")
print("The input was converted to " + str(trueOrFalse))

# Take input of you and your neighbor
your_first_name = input("What is your name? ")
neighbor_first_name = input("What is your neighbor's name? ")

# Take how long each of you have been coding
months_you_coded = int(input("How many months have you been coding? "))
months_neighbor_coded = int(input("How many months has your neighbor been coding? "))

# Add total month
total_months_coded = int(months_you_coded) + int(months_neighbor_coded)

# Print results
print("I am " + your_first_name + " and my neighbor is " + neighbor_first_name)
#print("Together we have been coding for " + str(total_months_coded) + " months!")
print(f"Together we have been coding for   {months_you_coded + months_neighbor_coded}   months!")

