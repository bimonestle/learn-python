import re

def findRevNumb():
    fName = input("Enter file name: ")

    try:
        fHand = open(fName)
    except:
        print("File cannot be opened:", fName)
        exit()

    for line in fHand:
        line = line.rstrip()

        # Search for lines that start with 'Details: rev='
        # followed by numbers and '.'
        # Then print the number if it is greater than zero

        # We are looking for line that starts with 'Details:',
        # followed by any number of characters (.*),
        # followed by 'rev='
        # and then by one or more digits
        # We want to find lines that match the entire expression,
        # but we only want to extract the integers at the end of the line.
        # So we surround [0-9.]+ with parentheses ().
        revNumb = "^Details:.*rev=([0-9.]+)"
        numb = re.findall(revNumb, line)
        if len(numb) > 0:
            print(numb)

findRevNumb()