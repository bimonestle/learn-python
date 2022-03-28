# Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print the dictionary.

fName = input("Enter a file name: ")
try:
    fHand = open(fName)
except:
    print("There is no %s" % fName)
    quit()

senders = dict()
for line in fHand:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        sender = words[1]
        senders[sender] = senders.get(sender, 0) + 1

print(senders)