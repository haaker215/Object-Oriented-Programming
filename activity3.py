class parrot:
    species = "Bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
ob1 = parrot("Olivia",10)
ob2 = parrot("Jack",20)
print(ob1.name)
print(ob1.age)
print(ob2.name)
print(ob2.age)
print(parrot.species)