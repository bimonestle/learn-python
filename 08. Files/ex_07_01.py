fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File ",fName, " doesn't exist")
    exit()
for line in fHand:
    line = line.rstrip("\n")
    line = line.upper()
    print(line)