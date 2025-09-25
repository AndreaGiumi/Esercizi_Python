class Animal:
    def __init__(self, name:str, legs:int):
        self.name = name
        self.legs = legs


    def setLeg(self, legs:int):
        self.legs = legs


    def getLegs(self):
        return self.legs
    


    def printInfo(self):
        print(f"{self.name}, {self.legs}")

cane = Animal("Leone", 4)
uccello = Animal("Pio", 2)
gatto = Animal("Miao", 7)



cane.setLeg(6)
uccello.setLeg(4)
gatto.setLeg(4)



print(cane.getLegs(), uccello.getLegs(), gatto.getLegs())



cane.printInfo()
uccello.printInfo()
gatto.printInfo()







# cane.leg = 5
# print(cane.leg)