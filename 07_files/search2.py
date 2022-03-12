fname = input('Enter a file name: ')
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)