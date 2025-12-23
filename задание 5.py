class Animal:
    def make_sound(self):
        return "животное издает звук"


class Dog(Animal):
    def make_sound(self):
        return "гав!"


class Cat(Animal):
    def make_sound(self):
        return "мяу!"


class Cow(Animal):
    def make_sound(self):
        return "муу!"


def zoo_concert(animals_list):
    for animal in animals_list:
        print(animal.make_sound())


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    cow = Cow()
    
    animals = [dog, cat, cow]
    
    print("концерт в зоопарке")
    zoo_concert(animals)