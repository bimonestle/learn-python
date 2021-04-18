# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter frequency varies between languages.
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string
from string import digits

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("Cannot open file", fName)
    exit()

counts = dict()
for line in fHand:
    line = line.rstrip()

    # Remove all punctuations from each line
    # line.translate(str.maketrans(fromstr, tostr, deletestr))
    # Replace the characters in 'fromstr'
    # with the character in the same position in 'tostr'
    # and delete all characters that are in 'deletestr'.
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split()

    print(words)
    for word in words:
        # Remove all digits from each word
        # word.maketrans(fromstr, tostr, deletestr)
        removeDigits = word.maketrans("", "", digits)

        # Each word which returns empty string, skip it
        # and convert it to lowercase
        if word.translate(removeDigits) == "":
            continue
        word = word.translate(removeDigits).lower()

        # Count each string in every word traversed
        for s in word:
            counts[s] = counts.get(s, 0) + 1

# Each letter and its counted frequency add it to a list
# and make its element as a tuple type by the order of frequency, letter
# in order for us abble to sort it descendingly
letterFreq = list()
for letter, freq in list(counts.items()):
    letterFreq.append((freq, letter))
letterFreq.sort(reverse=True)

# Reverse the order of the printed tuple
for lst in letterFreq:
    (freq, letter) = lst
    print(letter, freq)