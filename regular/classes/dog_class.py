class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def main():
        from regular.classes.dog_class import Dog
        dog1 = Dog("Buddy", 3)
        dog2 = Dog("Max", 5)

        print(dog1.bark())  # Output: Buddy says Woof!
        print(dog2.bark())  # Output: Max says Woof!

    if __name__ == "__main__":
        main()