# INHERITANCE

from learnObject import partyAnimal

class cricketFan(partyAnimal):
    points = 0
    def six(self):
        self.points += 6
        self.party()
        print(self.name,"points", self.points)

s = partyAnimal('Sally')
s.party()
j = cricketFan('Jim')
j.party()
j.six()

print(dir(j))