# Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are. Then you can use the in operator as a fast way
# to check whether a string is in the dictionary.

fName = input("Enter a file name: ")

try:
    fHand = open(fName)
except:
    print("No file name of %s" % fName)
    quit()

key_word = dict()
for line in fHand:
    line = line.strip()
    words = line.split()
    for word in words:

        # Immediately skip the duplicate words
        if not word in key_word:
            key_word[word] = "n/a"
        else:
            print("%s is already in the dictionary" % word)
            continue

# print(key_word)