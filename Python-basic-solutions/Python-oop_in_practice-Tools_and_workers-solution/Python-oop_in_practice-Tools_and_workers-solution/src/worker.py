from abc import ABC, abstractmethod
from tool import Laptop


class Worker(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        print(f"\n\n{self.name} starts working:")

    @abstractmethod
    def take_break(self, minutes):
        print(f"\n\n{self.name} takes {minutes} minutes break:")


class Programmer(Worker):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def __str__(self):
        return f"{self.name} codes with {self.language}"

    def work(self):
        super().work()
        print(f"The programmer is coding with {self.language}")

    def take_break(self, minutes):
        super().take_break(minutes)
        print("Programmer plays ninja fruit")


class Janitor(Worker):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

    def __str__(self):
        return f"{self.name} uses {self.tool}"

    def work(self):
        super().work()
        print(f"The janitor is working with {self.tool}")

    def take_break(self, minutes):
        super().take_break(minutes)
        print(f"Janitor {self.name} listens to music")





