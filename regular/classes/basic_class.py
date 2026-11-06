class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Initialize grade to the provided value

    def add_points(self, points):
        self.grade += points

ama = Student("Ama", 20, 85)
Kofi = Student("Kofi", 22, 90)

ama.add_points(10)  # Ama's grade is now 95
Kofi.add_points(5)  # Kofi's grade is now 95

print(ama.name, ama.age, ama.grade)  # Output: Ama 20 95
print(Kofi.name, Kofi.age, Kofi.grade)  # Output: Kofi 22 95