import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

# Search for lines that starts with "F",
# followed by any 2 characters, followed by "m:"
for line in fHand:
    line = line.rstrip()
    if re.search("^F..m:", line):
        print(line)