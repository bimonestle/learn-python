import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened", fName)
    exit()

regex = input("Enter a regular expression: ")
count = 0
totRevNumb = 0
for line in fHand:
    line = line.rstrip()
    
    if re.search(regex, line):
        revNumb = re.findall("([0-9.]+)", line)
        if len(revNumb) > 0:
            # print(revNumb)
            count += 1
            revNumb = int(revNumb[0])
            totRevNumb += revNumb

average = int(totRevNumb / count)
print(average)