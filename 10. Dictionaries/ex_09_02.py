# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print out the contents of your
# dictionary (order does not matter).

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

dates = dict()
count = 0
for line in fHand:
    line = line.rstrip()

    if line.startswith("From "):
        # print(line)
        words = line.split()

        # get the day from the particular line
        # and count it
        dates[words[2]] = dates.get(words[2], 0) + 1

print(dates)