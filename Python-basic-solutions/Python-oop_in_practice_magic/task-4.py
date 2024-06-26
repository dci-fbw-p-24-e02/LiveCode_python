import datetime

class DetailedLogWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        self.file = open(self.filename, 'a')
        self.file.write(f"Log started on {self.start_time}\n")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.file.write(f"An error occurred: {exc_val}\n")
        self.file.write(f"Log closed on {datetime.datetime.now()}\n")
        self.file.close()
    
        return True
