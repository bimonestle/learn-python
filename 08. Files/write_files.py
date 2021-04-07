fout = open('output.txt', 'w')
print(fout)

line1 = "This there's the wattle,\n"
fout.write(line1)

line2 = "the emblem of our land.\n"
fout.write(line2)

line3 = "Hello world!"
fout.write(line3)

fout.close()