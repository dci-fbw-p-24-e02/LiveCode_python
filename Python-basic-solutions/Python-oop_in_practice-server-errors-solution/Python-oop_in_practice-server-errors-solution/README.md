# Class Polymorphism

## Task
Create 3 classes:
* **OK**: Represents OK code error 200.
* **NotFound**: Represents Not Found code error 404.
* **ServerError**: Represents Server Error code 500.

- [X] In each of the class, add attributes for the error code and the error message.
> **Solution:**
> 
> Define those attributes in the **\__init\__** method of each class.

- [x] Create a function **status(error_object)** That displays the error code and the error message of an object of any of the three classes above.
> **Solution:**
> 
> If the attributes have the same name in all three classes, it's enough to print them. The function **status(error_object)** will work with either type of error_object thanks to the polymorphism

-[X] Write a **main.py** to test your code: Create an object of each class, and run the function **status(error_object)** on them.


> The idea of this exercise is to see polymorphism in action:
> 
> The function **status(error_object)** changes its behaviour depending on the type (class) of the object it runs on.