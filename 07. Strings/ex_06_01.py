# Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards

fruit = "banana"
lastIndex = len(fruit) - 1
while lastIndex >= 0:
    letter = fruit[lastIndex]
    print(letter)
    lastIndex -= 1