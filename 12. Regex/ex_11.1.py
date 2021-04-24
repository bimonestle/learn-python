import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened", fName)
    exit()

regex = input("Enter a regullar expression: ")
count = 0
for line in fHand:
    # line = line.rstrip()

    if re.search(regex, line):
        count += 1
        # print(line)

print(fName, "had %d lines that matched %s" %(count, regex))