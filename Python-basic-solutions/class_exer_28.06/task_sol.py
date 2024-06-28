# Define the method_logger decorator to log method calls
def method_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Called {func.__name__} with {args[1:]} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Define the Grandparent class
class Grandparent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")

    def __str__(self):
        return f"Grandparent: {self.name}, aged {self.age}"

# Define the Parent class inheriting from Grandparent
class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.children = []

    def speak(self):
        super().speak()
        print(f"I have {len(self.children)} children.")

    def __add__(self, child_name):
        self.children.append(child_name)
        return self

    def __str__(self):
        return f"Parent: {self.name}, children count: {len(self.children)}"

# Define the Child class inheriting from Parent and Grandparent
class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name, age)
        self.__toys = []

    @method_logger
    def add_toy(self, toy):
        self.__toys.append(toy)
        print(f"Added toy: {toy}")

    def speak(self):
        super().speak()
        print(f"My favorite toy is {self.__toys[0]} if I have any.")

    def __len__(self):
        return len(self.__toys)

    def __str__(self):
        return f"Child: {self.name}, toys count: {len(self.__toys)}"

# Create instances 
grandparent = Grandparent("Gwen", 78)
parent = Parent("Laura", 50)
child = Child("Jack", 20)

parent + "Alice" + "Bob"  # Using __add__
child.add_toy("Teddy Bear")
child.add_toy("Lego Set")

print(grandparent)  # Using __str__
print(parent)        # Using __str__
print(child)         # Using __str__

parent.speak()
child.speak()
print(f"{child.name} has {len(child)} toys.")  # Using __len__

print(child.add_toy('Car' ))  # call add_toy and decorator
