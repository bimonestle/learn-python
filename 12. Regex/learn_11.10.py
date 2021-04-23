import re

def findHour():
    fName = input("Enter file name: ")

    try:
        fHand = open(fName)
    except:
        print("File cannot be opened:", fName)
        exit()
    
    for line in fHand:
        line = line.rstrip()

        # Search for lines that start with From and a character
        # followed by a two digit number between 00 and 99 followed by ':'
        # Then print the number if it is greater than zero

        # Search for line that starts with 'From ',
        # followed by any number of characters (.*),
        # followed by a space,
        # followed by a two digits [0-9][0-9]
        # and surround those two digits with parentheses
        # to pull out the digits which we look for,
        # and followed by a colon character
        hourFormat = "^From .* ([0-9][0-9]):"
        hour = re.findall(hourFormat, line)
        if len(hour) > 0:
            print(hour)

findHour()