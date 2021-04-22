import re

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

for line in fHand:
    line = line.rstrip()

    # Search for line that starts with 'X',
    # followed by any non-whitespace characters and ':',
    # followed by a space and any number.
    # The number can include a decimal.
    # Then print the number if it's greater than zero.

    # When you add parentheses to the expression,
    # they are ignored when matching the string.
    # But when you use 'findall()', parentheses indicate that
    # while you want the whole expression to match,
    # you're only interested in extracting a portion of the substring
    # that matches the regular expression
    xDecimal = "^X\S*: ([0-9.]+)"
    decimal = re.findall(xDecimal, line)

    if len(decimal) > 0:
        print(decimal)