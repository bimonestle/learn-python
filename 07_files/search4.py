fname = input('Enter a file name: ')
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)