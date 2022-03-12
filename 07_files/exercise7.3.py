fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print("File cannot be opened", fname)

    if fname.find('.') == -1:
        print(fname.upper(), "- You've been punk'd!")

    quit()

lineCount = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("Subject:"):
        lineCount += 1


print("There are %d subject lines in %s." % (lineCount, fname))