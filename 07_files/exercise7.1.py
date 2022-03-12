# Exercise 1: Write a program to read through a file and
# print the contents of the file (line by line) all in upper case.

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

for line in fhand:
    line = line.strip()
    uppercased = line.upper()
    print(uppercased)