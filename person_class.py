class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.city = input("Enter your city: ")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

# Create an instance of the Person class and display the information
person = Person()
person.display_info()
