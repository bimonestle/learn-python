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