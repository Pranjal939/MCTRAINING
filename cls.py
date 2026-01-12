class Person:
    def __init__(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g

    def display_info(self):

        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

    def is_adult(self):
        return self.age >= 18

p1 = Person("Pranjal", 19, "Female")
p1.display_info()
print("Is adult:", p1.is_adult())

class Student(Person):
    def __init__(self, n, a, g, c, p):
        super().__init__(n, a, g)
        self.college = c
        self.program = p

    def college_info(self):
        print