fName = input("Enter file name: ")
if fName.endswith(".txt") == False:
        print(fName.upper(), "TO YOU - You've been punk'd!")
else:
    try:
        fHand = open(fName)
    except:
        print("File", fName, "doesn't exist")
        exit()

    print(fHand)