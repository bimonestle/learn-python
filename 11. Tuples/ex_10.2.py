# This program counts the distribution
# of the hour of the day for each of the messages.
# You can pull the hour from the “From” line
# by finding the time string and then splitting that string
# into parts using the colon character.
# 
# Once you have accumulated the counts for each hour,
# print out the counts, one per line, sorted by hour as shown below.

# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

tm = dict()
for line in fHand:
    line = line.rstrip()

    # Read and parse the "From " line
    if line.startswith("From "):
        words = line.split()

        # Finding the time string from the line
        time = words[len(words) - 2]
        time = time.split(":")

        # Finding the hour from the time string
        hour = time[0]
        # hour = int(hour)

        # Count the occurences of each hour
        tm[hour] = tm.get(hour, 0) + 1

# print(tm)

hourLst = list()

# traverse the list of hours and its occurences from the list
# and append it to a new list 'hourLst'
for hour, occ in list(tm.items()):
    hourLst.append((hour, occ))

# Sort the list of hours ascendingly
hourLst.sort()
for lst in hourLst:
    (a, b) = lst
    print(a, b)