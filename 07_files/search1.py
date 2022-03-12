fname = input('Enter a file name: ')
fhand = open(fname)

count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)