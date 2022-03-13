fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Cannot open file %s' % fname)
    quit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])