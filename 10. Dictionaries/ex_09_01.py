# Write a program that reads the words in words.txt and
# stores them as keys in a dictionary. It doesn’t matter what the values are.
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File doesn't exist")
    exit()

wordsKey = dict()
for line in fHand:
    words = line.split()
    for word in words:
        wordsKey[word] = ""
        # word in wordsKey
print(wordsKey)