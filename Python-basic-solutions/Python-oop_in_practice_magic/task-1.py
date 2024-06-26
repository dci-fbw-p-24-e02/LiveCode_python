class StringWrapper:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, StringWrapper):
            return StringWrapper(self.string + other.string)
        elif isinstance(other, str):
            return StringWrapper(self.string + other)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, StringWrapper):
            return self.string == other.string
        elif isinstance(other, str):
            return self.string == other
        return NotImplemented

# Test 
str1 = StringWrapper("hello")
str2 = StringWrapper(" world")
print("String 1:", str1)
print("String 2:", str2)
print("Concatenated String:", str1 + str2)
print("String 1 == 'hello':", str1 == "hello")