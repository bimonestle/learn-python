fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    # exit()
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)