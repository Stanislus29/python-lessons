from dog_class import Dog
def main():
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)

    print(dog1.bark())  # Output: Buddy says Woof!
    print(dog2.bark())  # Output: Max says Woof!

if __name__ == "__main__":
    main()