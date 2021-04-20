import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

for line in fHand:
    line = line.rstrip()

    # Search the line that starts with "From:"
    # We will only match lines that start with the string "From:"
    if re.search("^From:", line):
        print(line)