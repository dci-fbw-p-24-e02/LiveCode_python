class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __gt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age > other.age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age

# Testing
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 30)

print(person1)  # Outputs: Alice, 30 years old
print(person2)  # Outputs: Bob, 25 years old
print("Is person1 older than person2?", person1 > person2)  # True
print("Is person1 the same age as person3?", person1 == person3)  # True
