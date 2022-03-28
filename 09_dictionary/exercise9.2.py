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