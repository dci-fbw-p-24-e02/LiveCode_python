from author import Author


class Book:
    def __init__(self, name: str, author: Author, price: float, qty: int = 0):
        self._name = name
        self._author = author
        self._price = price
        self._qty = qty

    def get_name(self) -> str:
        return self._name

    def get_author(self) -> Author:
        return self._author

    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float):
        self._price = price

    def get_qty(self) -> int:
        return self._qty

    def set_qty(self, qty: int):
        self._qty = qty

    def __str__(self) -> str:
        return (
            "Book["
            + "name="
            + self._name
            + ", author="
            + str(self._author)
            + ", price="
            + str(self._price)
            + ", qty="
            + str(self._qty)
            + "]"
        )

    def get_author_name(self) -> str:
        return self.get_author().get_name()

    def get_author_email(self) -> str:
        return self.get_author().get_email()
