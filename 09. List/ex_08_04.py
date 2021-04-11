# Find all unique words in a file

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print(fName, "File doesn't exist")
    exit()

unique = list()
print(unique)
for line in fHand:
    # print(line)

    words = line.split()
    for word in words:
        
        # If the word is already in the list of unique words, skip it.
        if word in unique:
            continue

        # If the word is not in the unique list, add it.
        unique.append(word)
        
unique.sort()
print(unique)
    