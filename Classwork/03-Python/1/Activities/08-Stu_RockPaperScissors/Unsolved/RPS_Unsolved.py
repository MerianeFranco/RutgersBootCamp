# Incorporate the random library
import random



# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
print (f"User selected {user_choice} and Computer selected {computer_choice}")
if (user_choice == computer_choice):
    print ("Game tied")
elif(computer_choice == "p" and user_choice == "r"):
    print ("You won")
elif(computer_choice == "p" and user_choice == "s"):
    print ("Computer won")
elif(computer_choice == "s" and user_choice == "p"):
    print ("Computer won")
elif(computer_choice == "s" and user_choice == "r"):
    print ("You won")
elif(computer_choice == "r" and user_choice == "s"):
    print ("Computer won")
else:
    print ("You won")
   