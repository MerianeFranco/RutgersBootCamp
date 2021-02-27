import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter

# Find the total number of matches wrestled

# Find the percentage of matches won

# Find the percentage of matches lost

# Find the percentage of matches drawn

# Print out the wrestler's name and their percentage stats

# Read in the CSV file

def percentage(wrestler_data):
    player = str(wrestler_data[0])
    wins = int(wrestler_data[1])
    losses = int(wrestler_data[2])
    draws = int(wrestler_data[3])

    games = wins + losses + draws

    winP = (wins/ games)*100
    lossesP = (losses/ games)*100
    drawP = (draws/ games)*100

    if lossesP > 50:
        type = "Jobber"

    else:
        type = "Superstar"

    print(f"Stats for {player}")
    print(f"WIN PERCENT: {winP}")
    print(f"LOSS PERCENT: {lossesP}")
    print(f"DRAW PERCENT: {drawP}")
    print(f"{player} is a {type}")


with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for letter in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check.upper() == letter[0].upper()):
            percentage(letter)
