# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
# to find who has the most messages and print how many messages the person has.

fName = input("Enter a file name: ")
try:
    fHand = open(fName)
except:
    print("There is no %s" % fName)
    quit()

# Construct the dictionary of senders
senders = dict()
for line in fHand:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        sender = words[1]
        senders[sender] = senders.get(sender, 0) + 1

# Find the maximum occurence of senders
largest = 0
for sender in senders:
    if senders[sender] > largest:
        largest = senders[sender]
        senderMax = sender

print(senderMax, largest)