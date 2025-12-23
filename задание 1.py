class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = []

    def get_full_name(self):
        return self.name + " " + self.surname
    
    def add_mark(self, mark):
        if 1 <= mark <= 5:
            self.marks.append(mark)
        else:
            print("оценка должна быть от 1 до 5")

    def get_average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks)/ len(self.marks)
    
if __name__ == "__main__":
    student = Student("Валя", "Зыкова")
    print(student.get_full_name())

    student.add_mark(4)
    student.add_mark(5)

    print(student.marks)
    print(student.get_average_mark())