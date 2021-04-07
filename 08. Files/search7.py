fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File can't be opened:", fName)
    exit()
count = 0
for line in fHand:
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", fName)