# Revise a previous program as follows: Read and parse the “From” lines and
# pull out the addresses from the line. Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the list in
# reverse order and print out the person who has the most commits.

fName = input("Enter file name: ")
try:
    fHandle = open(fName)
except:
    print("There is no file %s" % fName)
    quit()

senders = dict()
for line in fHandle:
    if not line.startswith("From "):
        continue
    line = line.rstrip()
    words = line.split()
    sender = words[1]
    senders[sender] = senders.get(sender, 0) + 1

# Sort the dictionary by value
lst = list()
for (key, val) in list(senders.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for (val, key) in lst[:1]:
    print(key, val)

# sortedSenders = dict()
# for (count, sender) in lst:
#     sortedSenders[sender] = sortedSenders.get(sender, 0) + count