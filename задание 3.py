class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_info(self):
        return self.brand + " " + self.model
    
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def get_info(self):
        return "автомобиль " + super().get_info() + ", " + str(self.num_doors) + " двери"

class Bicycle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def get_info(self):
        return " велосипед " + super().get_info() + ", тип: " + self.type


if __name__ == "__main__":
    car = Car("Toyota", "RAV4", 4)      
    bicycle = Bicycle("Giant", "Escape", "городской")

    print("инф. об автомобиле: ", car.get_info())
    print("инф. о велосипеде: ", bicycle.get_info())