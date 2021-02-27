# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):

    n = len(numbers) # number of values
    total = 0.0
    for i in numbers:
        total = total + i # add the value of number to total
    return total/n


# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))