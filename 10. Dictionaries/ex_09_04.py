# Add code to the previous program (exercise 9.3) to figure out
# who has the most messages in the file. After all the data has been read and
# the dictionary has been created, look through the dictionary using a maximum loop
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages and
# print how many messages the person has.

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

senders = dict()
count = 0
for line in fHand:
    line = line.rstrip()

    if line.startswith("From "):
        # print(line)
        words = line.split()

        # Get the sender from the particular line and count it.
        # The longer version to get the result.
        # if words[1] not in senders:
        #     senders[words[1]] = 1
        # else:
        #     senders[words[1]] += 1

        # The more succinct alternative
        senders[words[1]] = senders.get(words[1], 0) + 1

mostMsg = max(senders.values())
for key in senders:
    if senders[key] == mostMsg:
        print(key, mostMsg)