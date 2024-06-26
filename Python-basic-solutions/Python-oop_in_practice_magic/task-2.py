class SafeWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# with method to call the class
with SafeWriter("output.txt") as file:
    file.write("Hello, world!")
    
