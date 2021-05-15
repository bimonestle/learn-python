# Classes as types

class partyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print("So far %d" % (self.x))

an = partyAnimal()
print("Type — ", type(an))
print("Dir — ", dir(an))

# From the 'dir' output, you can see that both
# 'x' attribute and 'party' method are
# available in the object
print("Type — ", type(an.x))
print("Type — ", type(an.party))