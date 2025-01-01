class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species


def make_sound():
    print("Woof!")


class Dog(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        print(self.name + ' ' + self.species + ' ' +'ГАФ!')


tom = Dog("Tom", 5, "Dog")
