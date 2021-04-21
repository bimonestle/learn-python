import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

for line in fHand:
    line = line.rstrip()

    # Search for lines that have an 'at' sign between characters
    # The characters must be a letter or number
    # The following regex translation:
    # "look for substrings that starts with a single lowercase letter, uppercase letter,
    # or number[a-zA-Z0-9], followed by one or more non-blank characters (\S+),
    # followed by an 'at' sign, followed by one or more non-blank characters (\S+),
    # followed by a lowercase or uppercase letter."
    emailAdd = re.findall("[a-zA-Z0-9]\S+@\S+[a-zA-Z]", line)

    # followed by zero or more non-blank characters (\S*)
    # emailAdd = re.findall("[a-zA-Z0-9]\S*@\S*[a-zA-Z]")

    # Remember the '*' or '+' sign, applies to single character
    # immediately to the left of the '+' or '*'
    if len(emailAdd) > 0:
        print(emailAdd)