fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

counts = dict()
for line in fHand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

        # using get() to achieve the same result
        # counts[word] = counts.get(word, 0) + 1

print(counts)