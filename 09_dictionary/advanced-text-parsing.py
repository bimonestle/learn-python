import string

fName = input("Enter a file name: ")
try:
    fHand = open(fName)
except:
    print("Cannot open file %s!" % fName)
    quit()

counts = dict()
for line in fHand:
    line = line.rstrip()
    mapTable = line.maketrans('','',string.punctuation) #remove any punctuation marks.
    line = line.translate(mapTable)
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)