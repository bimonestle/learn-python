import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

for line in fHand:
    line = line.rstrip()

    # ESCAPE CHARACTER
    # An expression to match the actual character we desired.
    # '\' indicate simply match a character by prefixing
    # that particular character 
    domFormat = "\@\S+[a-zA-Z]"
    domain = re.findall(domFormat, line)
    if len(domain) > 0:
        print(domain)