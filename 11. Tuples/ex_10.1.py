# Revise a previous program as follows:
# Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.

# After all the data has been read,
# print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195


fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

senders = dict()
for line in fHand:
    line = line.rstrip()

    # Read and parse the "From " lines and
    # pull out the addresses from the line
    if line.startswith("From "):
        print(line)

        words = line.split()
        
        # count the numbers of messages from each person
        # using a dictionary
        emAddr = words[1]
        senders[emAddr] = senders.get(emAddr, 0) + 1

# print(senders)
sendersLst = list()

# Traverse a list of tuples(senders, counts)
# and append it to a list 'sendersLst'
for key, val in list(senders.items()):
    sendersLst.append((val, key))

# Sort the list in reverse order / descendingly
# and get the person who has the most commits
sendersLst.sort(reverse=True)
(a, b) = sendersLst[0]
print(b, a)