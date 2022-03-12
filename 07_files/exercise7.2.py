fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

lineCount = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        lineCount += 1
        numbPos = line.find(': ')
        floatNumb = float(line[numbPos+2:])
        total += floatNumb

average = total/lineCount
print("Average spam confidence:", average)

# Test it on mbox-short.txt, mbox.txt