# Number Chain

#Chain up the numbers

## Instructions

#* Using a while loop, ask the user "How many numbers?", then print out a chain of ascending numbers, starting at 0.
m = "y"
y=0
while m == "y" :
    chain = int(input("how many numbers in the chain?"))

    chain = chain + y

    for x in range (y,chain):
        print (x)
        y = x+1


    # After the results have printed ask the user if they would like to continue.

#  * If "y", restart the process, starting at 0 again.

#  * If "n", exit the chain.

more = input("to continue press y")

## Bonus

#* Rather than just displaying numbers constantly starting at 0, have the numbers begin at the end of the previous chain.
