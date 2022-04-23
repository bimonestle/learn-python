# Write a program to look for lines of the form:
# 'New Revision: 39772'

# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

import re


fName = input("Enter a file name: ")

try:
    fHand = open(fName)
except:
    print("No file named %s" % (fName))
    quit()

# regex = input("Enter a regular expression: ")

for line in fHand:
    line = line.rstrip()
    matches = re.findall('^New Revision: (\d+)',line)
    # matches = re.findall('^Details:.*rev=([0-9]+)',line)
    # matches = re.findall(regex,line)
    if len(matches) > 0:
        print(matches)