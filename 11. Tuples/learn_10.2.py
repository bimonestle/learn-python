import string

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

counts = dict()
for line in fHand:

    # Strip all of the punctuation marks.
    line = line.translate(str.maketrans("", "", string.punctuation))

    line = line.lower()
    words = line.split()

    for word in words:
        # For each word found in the sentence, add 1 count.
        counts[word] = counts.get(word, 0) + 1

print(counts)

lst = list()
print(counts.items())

# Convert (dict_items type) items in counts dictionary to a list
listCounts = list(counts.items())

# Traverse the list of counts dictionary items
# for each of its key and value, 
# construct a list of (val, key) tuples
# and add them to 'lst' array based on its value
for key, value in listCounts:
    lst.append((value, key))

# Sort descendingly based on its occurence
lst.sort(reverse=True)

for key, val in lst:
    print(key, val)