# Extended Family Dynamics with Hybrid Inheritance

## Objective
Learn how to create classes where one class can get features from two other classes, and explore how decorators and encapsulation can enhance our code.

## Classes Overview

### Grandparent
- **Properties:** `name` (the grandparent's name), `age` (how old they are)
- **Methods:**
  - `speak()`: Makes the grandparent say hello and tell their name.
  - `__str__()`: Shows a text representation of the grandparent.

### Parent (inherits from Grandparent)
- **Additional Properties:** `children` (names of the parent's children)
- **Methods:**
  - `speak()`: Lets the parent talk about themselves and mention how many children they have.
  - `__add__(child_name)`: Lets you add a new child's name to the parent's list of children by using the plus sign (+).

### Child (inherits from both Grandparent and Parent)
- **Additional Properties:** `toys` (list of the child's toys)
- **Special Features:**
  - Uses features from both the `Grandparent` and the `Parent`.
  - Shows how one class can inherit features from two other classes.

## Learning Points

- **Multiple Inheritance:** The Child class gets features from both the Grandparent and Parent classes.
- **Decorators and Encapsulation:**
  - Use a simple decorator to log method calls.
  - Demonstrate encapsulation by making certain properties private and manipulating them through methods.

## Tasks

1. **Create Instances:** Make examples of each class and show how they can use their methods and properties.
2. **Add Children:** Use the `__add__` method to add names to the parent's list of children.
3. **Count Toys:** Use the `__len__` method to find out how many toys the child has.
4. **Show Multiple Inheritance in Action:** Explain how the Child class can do things that both a grandparent and a parent can do.
5. **Implement a Decorator:** Create a decorator that logs each time a method is called, including method name and any arguments passed.
6. **Encapsulate a Property:** Make the `toys` list in the `Child` class private and provide a method to add toys, ensuring the list cannot be modified directly from outside the class.

