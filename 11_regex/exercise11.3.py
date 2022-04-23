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