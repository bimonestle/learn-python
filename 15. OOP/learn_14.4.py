# MULTIPLE INSTANCES

class partyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x += 1
        print(self.name, 'party count', self.x)


s = partyAnimal('Sally')
j = partyAnimal('Jim')

s.party()
j.party()
s.party()