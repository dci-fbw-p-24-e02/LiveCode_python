## create  python file for every exercise 🎯


### Exercise 1: Advanced Operations for a Custom String Wrapper Class

- Objective:
Create a StringWrapper class that encapsulates a Python string and adds enhanced functionality using magic methods.

Tasks:

- Implement the __init__ method to initialize the string
- Implement the __str__ method to return the string itself
- Implement the __add__ method to allow concatenation of two StringWrapper instances or a StringWrapper with a Python string

- Implement the __eq__ method to compare equality between two StringWrapper instances or a StringWrapper and a Python string.




### Exercise 2: Implement a Safe File Writer Using Context Management
- Objective:
Create a SafeWriter class that uses context management to safely write to a file, ensuring that the file is always closed properly, even if an error occurs during writing.

Tasks:

- Implement the __init__ method to accept a filename.
- Implement the __enter__ method to open the file and return the file handle.
- Implement the __exit__ method to ensure the file is closed after writing.



### Exercise 3: Enhanced Person Class Using Magic Methods (very similar to first ex)

Objective:
Develop a Person class with enhanced functionalities using magic methods to handle string representation and comparison based on age.

Tasks:

- Initialization: Implement the __init__ method to accept name and age.
- String Representation: Implement the __str__ method to return a string format displaying the person's name and age.
- Greater Than: Implement the __gt__ method to compare two Person instances based on their age, determining which person is older.
- Equality: Implement the __eq__ method to check if two Person instances have the same age.
 
Testing:
Create several instances of Person and demonstrate comparisons using the implemented magic methods.






## Bonus Exercise 🤫☕😓

### Exercise: Implement a Detailed Log Writer using Context Management
* Objective:

* Develop a DetailedLogWriter class that uses context management to handle logging operations more comprehensively. This class should not only manage opening and closing log files but also annotate the logs with timestamps and error messages where necessary.

#### Tasks:

- Initialization: Implement the __init__ method to accept a filename for the log file.
- Enter Context: Implement the __enter__ method to open the log file in append mode. Upon entering the context, write an entry marking the start of a logging session with the current timestamp.
- Exit Context: Implement the __exit__ method to add a closing log entry with the current timestamp and close the log file. If an exception occurs during the log session, write an additional log entry detailing the type and message of the exception.
- Timestamping: Ensure that every log entry has a timestamp.
Error Handling: Specifically, manage any exceptions by logging them before closing the file

* Testing:

- Create a test case using the DetailedLogWriter class in a with block to write some entries.
- Simulate an error to see how the context manager handles logging the exception.
- Ensure that the log file correctly reflects the entries and any error information as expected.



⚡ Happy coding 