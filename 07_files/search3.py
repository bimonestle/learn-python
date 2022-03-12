fname = input('Enter a file name: ')
fhand = open(fname)

for line in fhand:
    line = line.rstrip()

    # Skip 'uninteresting' line
    if not line.startswith('From:'):
        continue

    # Process the 'interesting' line
    print(line)