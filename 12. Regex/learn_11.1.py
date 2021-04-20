import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

for line in fHand:
    line = line.rstrip()

    if re.search("From:", line):
        print(line)

    # The following code yield the same result as 
    # the one with rgex library above
    # linePos = line.find("From:")
    # if linePos > -1:
    #     print(line[linePos:])