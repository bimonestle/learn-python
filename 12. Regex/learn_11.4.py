import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

for line in fHand:
    line = line.rstrip()
    
    # Search for lines that start with 'From:' and
    # have an at sign
    if re.search("^From:.+@", line):
        print(line)

    # The search string "^From:.+@" will successfully match lines that start with "From:",
    # followed by one or more characters (.+),
    # followed by an 'at' sign.

    # It is good to think of the plus and asterisk characters as 'pushy'.
    # For example, the following string would match the last 'at' sign in the string
    # as shown below:
    # From: stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @iupui.edu

    # It is possible to tell an asterisk or plus sign
    # not to be so 'greedy' by adding another character.