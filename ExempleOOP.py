class Persone:
    def __init__(self , name , adresse):
        self.name = name
        self.adresse = adresse

    def describe(self):
        print(self.name , "at ", self.adresse)

class Shark:
    animal_type = "fish"
    location = "ocean"
    count = 0

    def __init__(self, name,  age= 10, category="A" , proprietaire:Persone = None):
        self.name = name
        self.age1 = age
        self.category = category
        self.proprietaire = proprietaire
        count = Shark.count +1

    def describe(self):
        print("Je suis un shark , my name is ", self.name, ".I am ", self.age1, " years old")
        if self.proprietaire is not None:
            print("Mon proprietaire est ",  self.proprietaire.name)
        else:
            print("I am alone")

    def swim(self):
        print("The shark is swimming.")

    def be_awesome(self):
        print("The shark is being awesome.")



s1 = Shark(name="Lach" )
s1.age1 = 20

s1.describe()

s2 = Shark(name="Jajj" )
s2.age1 = 13

s2.describe()

p1 = Persone(name="afellah" , adresse="El KLEA")
s1.proprietaire =p1
s1.describe()



