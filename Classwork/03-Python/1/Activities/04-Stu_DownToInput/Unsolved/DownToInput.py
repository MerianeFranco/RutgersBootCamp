# Take input of you and your neighbor
your_first_name = input("What is your name ")
neighbor_first_name = input("Neighbor first name ")
# Take how long each of you have been coding
your_code = int(input("How long have you been coding in months? "))
neighbor_code = int(input("How long have your neighbor been coding in months? "))
# Add total month
total_code_time = int(your_code) + int(neighbor_code)

# Print results
print (f"I'm {your_first_name} and my neighbor is {neighbor_first_name} ")
print (f"Together we are coding for  {total_code_time} months")