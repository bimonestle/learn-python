# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and
# keep a running count of each of the days of the week. At the end of the program
# print out the contents of your dictionary (order does not matter).

fName = input("Enter a file name: ")
try:
    fHand = open(fName)
except:
    print("There is no %s" % fName)
    quit()

days = dict()
for line in fHand:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        day = words[2]
        days[day] = days.get(day, 0) + 1

print(days)