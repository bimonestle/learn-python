# Rewrite the guardian code in the above example without two if statements.
# Instead, use a compound logical expression using the or logical operator
# with a single if statement.

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print("Cannot open file name %s" % fname)
    quit()

for line in fhand:
    words = line.split()
    # print('Debug:', words)

    if len(words) < 3 or words[0] != 'From':
        continue
    
    print(words[2])