# OBJECT LIFECYCLE

class partyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x += 1
        print("So far %d" % self.x)

    def __del__(self):
        print("I am destructed %d" % (self.x))

an = partyAnimal()
an.party()
an.party()
print("an contains", an)
an = 42
print("an contains", an)