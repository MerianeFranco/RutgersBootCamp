import os
import csv

udemy_csv = os.path.join("..", "Resources", "web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:

with open(udemy_csv, newline='',encoding = 'utf-8') as csvfile:
    csv.reader = csv.reader(csvfile, delimiter = ",")
    for row in csv.reader:
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])

        percent = round(int(row[6])/int(row[5]),2)
        review_percent.append(percent)

        new_length = row[9].split(" ")
        length.append(float(new_length[0]))
# Zip lists together
cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
