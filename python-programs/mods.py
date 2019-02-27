import datetime as dt
import csv
import math

print(dt.datetime.now())

# create a filename using the current date and time
filename = dt.datetime.strftime(dt.datetime.now(), "%d-%m-%y.csv")

# open the file with that filename
with open(filename, "w", newline='') as f:
    # enable csv writing to the file
    writer = csv.writer(f)
    # write a header row
    writer.writerow(["i", "j", "gcd"])
    # write the gcd for all (i,j) pairs from 0 to 100
    for i in range(100):
        for j in range(100):
            writer.writerow([i, j, math.gcd(i, j)])


# print(math.floor(1.23))
# print(math.factorial(4))
# print(math.gcd(10, 65))