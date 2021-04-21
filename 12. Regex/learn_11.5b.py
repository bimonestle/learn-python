import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

for line in fHand:
    line = line.rstrip()

    # Search for lines that have an at-sign between characters.
    # Which in result finds at least one substring that looks like
    # an email address
    x = re.findall("\S+@\S+", line)
    if len(x) > 0:
        print(x)