# Python object

class partyAnimal:
    x = 0

    # Using its ownself (an object) as a parameter
    def party(self):
        self.x += 1
        print("So far %d" % (self.x))

an = partyAnimal()
print(an)
print("So far %d" % (an.x))
an.party()
an.party()
an.party()
partyAnimal.party(an)