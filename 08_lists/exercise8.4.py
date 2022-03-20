# Find all unique words in a file
# Shakespeare used over 20,000 words in his works. But how would you determine that?
# How would you produce the list of all the words that Shakespeare used?
# Would you download all his work, read it and track all unique words by hand?
# Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order,
# that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print("Cannot open file name %s" % fname)
    quit()

unique_words = list()
for line in fhand:
    line = line.rstrip()
    # print("Line:", line)
    words = line.split()
    # print('word:', words)

    for word in words:
        if word in unique_words:
            continue
        unique_words.append(word)

sorted_words = sorted(unique_words)
print("Sorted Words:", sorted_words)