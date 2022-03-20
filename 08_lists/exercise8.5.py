# MINIMALIST EMAIL CLIENT
# Write a program to read through the mail box data and when you find line that
# starts with “From”, you will split the line into words using the split function.
# We are interested in who sent the message, which is the second word on the From line.

# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a count at the end.

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print("Cannot open file name %s" % fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        sender = words[1]
        count += 1
        print(sender)

print("There are '%d' lines in the '%s' file, with 'From ' as the first word" % (count, fname))