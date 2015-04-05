import random
import timeit
import time
from CreatureClasses import *


class EcoSim():
    CreatureList = []
    DayCount = 0
    AirTemperature = 75
    FoodTimer = 0
    SexTimer = 0

    def __init__(self):
        print('EcoSim started on', time.strftime('%b %d, %Y at %I:%M:%S %p'))
        for count in range(0,16000):
            x = Microbe(self.DayCount)
            self.CreatureList.append(x)
        for count in range(0,400):
            x = SmallFish(self.DayCount)
            self.CreatureList.append(x)
        for count in range(0,40):
            x = BigFish(self.DayCount)
            self.CreatureList.append(x)
        for count in range(0,2):
            x = Human(self.DayCount)
            self.CreatureList.append(x)
        self.RunTwoMonths()

    def GetCreatureTally(self):
        TypeList = ['Microbe', 'Small Fish', 'Big Fish', 'Human']
        for cType in TypeList:
            cList = [c for c in self.CreatureList if c.CreatureType == cType]
            DiedCount = 0
            AliveCount = 0
            BornCount = 0
            for creature in cList:
                if creature.IsAlive == False:
                    if creature.DayOfDeath == self.DayCount:
                        DiedCount += 1
                    if creature.CauseOfDeath == 'Predation':
                        self.CreatureList.remove(creature)
                else:
                    AliveCount += 1
                    if creature.DayOfBirth == self.DayCount:
                        BornCount += 1
            print(DiedCount, 'deaths and', BornCount, 'births leaves', AliveCount, cType, 'creatures alive')

    def NextDay(self):
        self.DayCount = self.DayCount + 1
        for creature in self.CreatureList:
            creature.GetOlder()

    def RunTwoMonths(self):
        for count in range(0,61):
            LivingCreatureList = [c for c in self.CreatureList if c.IsAlive == True]
            if len(LivingCreatureList) > 0:
                print('Day', self.DayCount, 'summary:')
                self.FoodAndSex()
                print('Eating took', self.FoodTimer, 'sec')
                print('Sex took', self.SexTimer, 'sec')
                self.GetCreatureTally()
                self.NextDay()
            else:
                break

    def FoodAndSex(self):
        random.shuffle(self.CreatureList)
        self.FoodTimer = 0
        self.SexTimer = 0
        for creature in self.CreatureList:
            if creature.IsAlive == True:
                ft = timeit.Timer(lambda: self.EatSomething(creature))
                self.FoodTimer += ft.timeit(1)
            if creature.IsAlive == True:
                st = timeit.Timer(lambda: self.Reproduce(creature))
                self.SexTimer += st.timeit(1)
        
    def EatSomething(self, hungryCreature):
        PreyList = [p for p in self.CreatureList if p.CreatureType in hungryCreature.PreyCreatures and p.IsAlive == hungryCreature.PreysOnLivingCreatures and p.CauseOfDeath != 'Predation' and p != hungryCreature]
        while hungryCreature.IsHungry == True and len(PreyList) > 0:
            for creature in PreyList:
                if hungryCreature.IsHungry == True: 
                    DiceRoll = random.uniform(0, 1)
                    if DiceRoll <= creature.PredatorEvasionChance:
                        hungryCreature.Eat(creature.CaloriesProvided)
                        creature.Die('Predation')
                        PreyList.remove(creature)
                                      
                else:
                    break

    def Reproduce(self, hornyCreature):
        if hornyCreature.IsPregnant:
            if hornyCreature.Age >= hornyCreature.DayOfConception + hornyCreature.PregnancyDuration:
                hornyCreature.GiveBirth()
                if hornyCreature.CreatureType == 'Human':
                    self.CreatureList.append(Human(self.DayCount))
                elif hornyCreature.CreatureType == 'Big Fish':
                    self.CreatureList.append(BigFish(self.DayCount))
                elif hornyCreature.CreatureType == 'Small Fish':
                    self.CreatureList.append(SmallFish(self.DayCount))
                elif hornyCreature.CreatureType == 'Microbe':
                    self.CreatureList.append(Microbe(self.DayCount))
        else:
            if hornyCreature.Age >= hornyCreature.MinimumReproductiveAge:
                DiceRoll = random.uniform(0, 1)
                if DiceRoll <= hornyCreature.ReproductionChance:
                    hornyCreature.GetPregnant()
