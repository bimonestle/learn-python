txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    # add each words and its length to array 't'
    t.append((len(word), word))

print(t)

# Sort descendingly based on length of word
t.sort(reverse=True)

print(t)
res = list()
for length, word in t:
    # add sorted word based on its length to array 'res'
    res.append(word)

print(res)