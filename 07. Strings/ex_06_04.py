# There is a string method called count that is similar to the function in the previous exercise.
# Read the documentation of this method at: https://docs.python.org/library/stdtypes.html#string-methods
# Write an invocation that counts the number of times the letter a occurs in “banana”.

def countLetter(word, letter):
    count = 0
    for alphabet in word:
        if alphabet == letter:
            count += 1
    print(count, "of " + letter)

word = input("Enter word: ")
letter = input("Enter letter: ")
countLetter(word, letter)

letterCount = word.count(letter)
print(letterCount)