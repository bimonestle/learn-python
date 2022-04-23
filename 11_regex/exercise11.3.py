# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.


import re


fName = input("Enter a file name: ")

try:
    fHand = open(fName)
except:
    print("No file named %s" % (fName))
    quit()

# regex = input("Enter a regular expression: ")

total = 0
for line in fHand:
    line = line.rstrip()
    matches = re.findall('\d+',line)
    if len(matches) > 0:
        for num in matches:
            total += int(num)

print(total)