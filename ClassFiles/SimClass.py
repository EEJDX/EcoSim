import random
from CreatureClasses import *


class EcoSim():
    CreatureList = []
    DayCount = 0
    AirTemperature = 75

    def __init__(self):
        for count in range(0,400):
            x = Microbe(self.DayCount)
            self.CreatureList.append(x)
        for count in range(0,100):
            x = SmallFish(self.DayCount)
            self.CreatureList.append(x)
        for count in range(0,40):
            x = BigFish(self.DayCount)
            self.CreatureList.append(x)
        for count in range(0,5):
            x = Human(self.DayCount)
            self.CreatureList.append(x)
        self.RunOneWeek()

    def GetCreatureTally(self):
        for creature in self.CreatureList:
            if creature.IsAlive == False:
                if creature.DayOfDeath == self.DayCount:
                    print(creature.Status())
                elif creature.CauseOfDeath == 'Predation':
                    self.CreatureList.remove(creature)
            else:
                print(creature.Status())

    def NextDay(self):
        self.DayCount = self.DayCount + 1
        for creature in self.CreatureList:
            creature.GetOlder()

    def RunOneWeek(self):
        for count in range(0,7):
            print('Day', self.DayCount, 'summary:')
            self.FoodAndSex()
            self.NextDay()
            self.GetCreatureTally()

    def FoodAndSex(self):
        for creature in self.CreatureList:
            self.EatSomething(creature)
            self.Reproduce(creature)

    def EatSomething(self, hungryCreature):
        for creature in self.CreatureList:
            if creature != hungryCreature:
                if creature.CauseOfDeath != 'Predation':
                    if hungryCreature.IsAlive == True and creature.IsAlive == hungryCreature.PreysOnLivingCreatures:
                        if creature.CreatureType in hungryCreature.PreyCreatures:
                            print(hungryCreature.CreatureType, 'ate a', creature.CreatureType)
                            hungryCreature.Eat()
                            creature.Die('Predation')
                            return

    def Reproduce(self, hornyCreature):
        if hornyCreature.Age >= hornyCreature.MinimumReproductiveAge:
            DiceRoll = random.uniform(0, 1)
            if DiceRoll <= hornyCreature.ReproductionChance:
                #print('Two', hornyCreature.CreatureType, 'mated!')
                hornyCreature.IsPregnant = True
            else:
                return False
        else:
            return False
        
