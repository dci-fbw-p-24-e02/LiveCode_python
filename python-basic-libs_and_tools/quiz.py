class MyContext:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_msg, traceback):
        print('And that is the end')
        if exc_type == IndexError:
            print(exc_type, 'suppressed by __exit__')
            return True

with MyContext():
    lst = [1,2]
    lst[0]

try:
    lst = [1,2]
    lst[0]
except IndexError as e:
    print(IndexError, ';suppressed by try/except')
finally:
    print('And that is the end')

