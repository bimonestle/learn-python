fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File", fName, "doesn't exist")
    exit()

count = 0
for line in fHand:
    # If the line starts with 'From:', the count will be 27
    if line.startswith("From"):
        count += 1
        words = line.split()
        print(words[1])

print("There were", count, "lines in the file", fName, "with From as the first word")