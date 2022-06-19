import random


class Enemy:
    damage = 5

    def __init__(self, name="joker", id=None, points=50):
        self.id = id
        self.name = name
        self.points = points

    def getAttacked(self, minusMoins):
        self.points = self.points - minusMoins
        if self.points <= 0:
            print(self.name, " am died")

    def go(self):
        print("I GO HHHHHHHHHH")

    def attack(self, person):
        print("I am attacking HHHHHHHH: ", person.name)
        person.getAttacked(Person.damage)


class Person:
    damage = 10

    def __init__(self, name="", id=None, points=200):
        self.id = id
        self.name = name
        self.points = points

    def getAttacked(self, minusMoins):
        self.points = self.points - minusMoins
        if self.points <= 0:
            print(self.name, " am died")

    def go(self):
        print(self.name, "  I go 1 m ")

    def attack(self, enemy: Enemy):
        print("Yes i am attacking ", enemy.name)
        enemy.getAttacked(Person.damage)


listEnemy = []
listPerson = []


def CreateGamer():
    for i in range(1, 4):
        listPerson.append(Person(name="Person" + str(i)))
    for i in range(1, 24):
        listEnemy.append(Enemy(name="Enemy" + str(i)))


def getRandamGamer(category):
    if category == 'ENEMY':
        return random.randint(0, len(listEnemy) - 1)
    elif category == 'HERO':
        return random.randint(0, len(listPerson) - 1)


def updateListDeadOfHeroAndEnemy():
    for person in listPerson:
        if person.points <= 0:
            listPerson.remove(person)

    for enemy in listEnemy:
        if enemy.points <= 0:
            listEnemy.remove(enemy)


CreateGamer()
while len(listPerson) > 0 and len(listEnemy) > 0:
    listEnemy[getRandamGamer('ENEMY')].attack(listPerson[getRandamGamer('HERO')])
    updateListDeadOfHeroAndEnemy()
    if len(listPerson) > 0 and len(listEnemy):
        listPerson[getRandamGamer('HERO')].attack(listEnemy[getRandamGamer('ENEMY')])
        updateListDeadOfHeroAndEnemy()
    if len(listPerson) > 0 and len(listEnemy):
        listPerson[getRandamGamer('HERO')].attack(listEnemy[getRandamGamer('ENEMY')])
        updateListDeadOfHeroAndEnemy()


if len(listPerson) > 0:
    print("The winner is Heros , this is the list")
    for person in listPerson:
        print(person.name, " : ", person.points)
else:
    print("The winner is Enemies , this is the list")
    for enemy in listEnemy:
        print(enemy.name, " : ", enemy.points)
