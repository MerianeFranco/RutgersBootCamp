import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

# Open and read csv
with open(cereal_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ",")

    # read the reader row
    csv_header = next (csv_file)
    print (f"Header : {csv_header}")

    # read all the rows after the header
    for row in csv_reader:
        #convert row to float and compare to grams of fiber
        if float(row[7])>= 5:
            print (row)