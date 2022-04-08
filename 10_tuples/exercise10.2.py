fName = input("Enter file name: ")
try:
    fHandle = open(fName)
except:
    print("There is no file %s" % fName)
    quit()

hours = dict()
for line in fHandle:
    if not line.startswith("From "):
        continue
    line = line.rstrip()
    words = line.split()
    times = words[-2]
    time = times.split(":")
    hour = time[0]
    hours[hour] = hours.get(hour, 0) + 1

# sort by hour
hourList = list()
for (key, val) in list(hours.items()):
    hourList.append((key, val))

hourList.sort()
for (hour, count) in hourList:
    print(hour, count)