import random

class Creature():

    CreatureType = 'Creature'
    IsAlive = True
    Age = 0                             #measured in days
    DayOfBirth = 0
    NaturalLifespan = 0                 #measured in days
    StarvationTime = 0                  #measured in days
    AccidentalDeathChance = 0           #0-1 probability  
    PredatorEvasionChance = .5          #0-1 probability
    CauseOfDeath = ''
    DayOfDeath = -1
    
    IsPregnant = False
    PregnancyDuration = 0               #measured in days
    MinimumReproductiveAge = 0          #measured in days
    ReproductionChance = 0              #0-1 probability

    PreyCreatures = []                  #list of CreatureTypes that this CreatureType can eat
    PreysOnLivingCreatures = True

    def GetOlder(self):
        if self.IsAlive == True:
            self.StarvationTime = self.StarvationTime - 1
            self.Age = self.Age+1
            if self.StarvationTime <= 0:
                self.Die('Starvation')
            elif self.NaturalLifespan <= self.Age:
                self.Die('Old Age')
            else:
                DiceRoll = random.uniform(0, 1)
                if DiceRoll <= self.AccidentalDeathChance:
                    self.Die('Accident')

    def Die(self, cause):
        self.IsAlive = False
        self.CauseOfDeath = cause
        self.DayOfDeath = self.DayOfBirth + self.Age

    def Status(self):
        if self.Age == 0 and self.IsAlive == True:
            return self.CreatureType + ' born today!'
        elif self.Age == 0 and self.IsAlive == False and self.CauseOfDeath == 'Eaten':
            return self.CreatureType + ' was Eaten'
        elif self.Age == 0 and self.IsAlive == False:
            return self.CreatureType + ' died at birth'
        elif self.IsAlive:
            return self.CreatureType + ' still alive after ' + str(self.Age) + ' days'
        else:
            return self.CreatureType + ' died of ' + self.CauseOfDeath + ' after ' + str(self.Age) + ' days'

class Human(Creature):

    def __init__(self, day):
        self.CreatureType = 'Human'
        self.DayOfBirth = day
        self.NaturalLifespan = 22000
        self.StarvationTime = 4
        self.AccidentalDeathChance = .001

        self.PregnancyDuration = 300
        self.MinimumReproductiveAge = 6600
        self.ReproductionChance = .8

        self.PreyCreatures = ['Big Fish', 'Small Fish']

    def Eat(self):
        self.StarvationTime = 4

class BigFish(Creature):

    def __init__(self, day):
        self.CreatureType = 'Big Fish'
        self.DayOfBirth = day
        self.NaturalLifespan = 3700
        self.StarvationTime = 2
        self.AccidentalDeathChance = .01

        self.PregnancyDuration = 90
        self.MinimumReproductiveAge = 400
        self.ReproductionChance = .8

        self.PreyCreatures = ['Small Fish']

    def Eat(self):
        self.StarvationTime = 2

class SmallFish(Creature):

    def __init__(self, day):
        self.CreatureType = 'Small Fish'
        self.DayOfBirth = day
        self.NaturalLifespan = 2000
        self.StarvationTime = 2
        self.AccidentalDeathChance = .01

        self.PregnancyDuration = 50
        self.MinimumReproductiveAge = 200
        self.ReproductionChance = .8

        self.PreyCreatures = ['Microbe']

    def Eat(self):
        self.StarvationTime = 2

class Microbe(Creature):

    def __init__(self, day):
        self.CreatureType = 'Microbe'
        self.DayOfBirth = day
        self.NaturalLifespan = 100
        self.StarvationTime = 5
        self.AccidentalDeathChance = .01

        self.PregnancyDuration = 5
        self.MinimumReproductiveAge = 5
        self.ReproductionChance = .8

        self.PreyCreatures = ['Microbe', 'Small Fish', 'Big Fish', 'Human']
        self.PreysOnLivingCreatures = False

    def Eat(self):
        self.StarvationTime = 5
