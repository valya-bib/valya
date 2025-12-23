class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def set_age(self, new_age):
        self.__age = new_age



person = Person("Валя", 18)

print("имя:", person.get_name())
print("возраст:", person.get_age())


person.set_name("Соня")
person.set_age(20)

print("имя:", person.get_name())
print("возраст:", person.get_age())