fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print(fName, "File doesn't exist")
    exit()

count = 0
for line in fHand:
    words = line.split()
    # print("Debug:", words)

    # Guardian statement a bit stronger
    # if there is a word from as its first word and only one word in it
    if len(words) < 3 or words[0] != "From":
        continue
    
    print(words[2])