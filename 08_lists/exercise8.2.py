# Figure out which line of the above program is still not properly guarded.
# See if you can construct a text file which causes the program to fail and
# then modify the program so that the line is properly guarded and test it
# to make sure it handles your new text file.

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print("Cannot open file name %s" % fname)
    quit()

for line in fhand:
    words = line.split()
    # print('Debug:', words)

    # Guardian Code
    if len(words) < 0 : continue
    # End of guardian code
    
    if words[0] != 'From' : continue
    print(words[2])