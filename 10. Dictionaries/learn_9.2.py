import string

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

counts = dict()

# list of characters that python considers as punctuation marks
# print(string.punctuation)

for line in fHand:
    # get rid of whitespace at the end of the sentence
    line = line.rstrip()

    # line.translate(str.maketrans(fromstr, tostr, deletestr))
    # Replace the characters in 'fromstr'
    # with the character in the same position in 'tostr'
    # and delete all characters that are in 'deletestr'.
    # The 'fromstr' and 'tostr' can be empty strings and the 'deletestr' parameter can be omitted.
    # THE FOLLOWING LINE only deletes the punctuation marks inside the file,
    # and no changes from the previous strings to the new one
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Make the sentence become lowercase
    line = line.lower()
    
    # Form a collection of words by split the sentence by space
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

        # more succinct with get()
        # counts[word] = counts.get(counts[word], 0) + 1

print(counts)