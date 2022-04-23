# Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines
# that matched the regular expression:

import re


fName = input("Enter a file name: ")

try:
    fHandle = open(fName)
except:
    print("No file named %s" % fName)
    quit()

regex = input("Enter a regular expression: ")

count = 0
for line in fHandle:
    line = line.rstrip()
    if re.search(regex, line):
        print(line)
        count += 1

print("%s had %d lines that matched %s" % (fName, count, regex))