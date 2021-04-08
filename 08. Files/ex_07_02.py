fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File ",fName, " doesn't exist")
    exit()
count = 0
total = 0
for line in fHand:
    line = line.rstrip("\n")
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        dspamValPos = line.find(":") + 2
        dspamVal = float(line[dspamValPos:])
        total += dspamVal
        print("Line:", line, line[dspamValPos:], "Total:", total)
average = total / count
print("Count:", count)
print("Total:", total)
print("Average:", average)