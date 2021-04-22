import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

for line in fHand:
    line = line.rstrip()

    # Search for lines that starts with 'X-',
    # followed by zero or more characters (.*),
    # followed by a colon (:),
    # and then a 'space'.
    # After the 'space', we are looking for one or more characters
    # which are either a digit (0-9) or a period ([0-9.]+).
    # Note that inside the square brackets, the period matches
    # an actual period sign (.).
    # xFormat = "^X-.*: [0-9.]+"

    # Search for lines that starts with 'X',
    # followed by any non-whitespace characters and ':',
    # followed by a space and any number,
    # The number can include a decimal.
    xFormat = "^X\S*: [0-9.]+"
    if re.search(xFormat, line):
        print(line)