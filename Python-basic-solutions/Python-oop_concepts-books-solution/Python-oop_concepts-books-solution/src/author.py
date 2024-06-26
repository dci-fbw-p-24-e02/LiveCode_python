from gender import Gender


class Author:
    def __init__(self, name: str, email: str, gender: Gender):
        self._name = name
        self._gender = gender
        self._email = email

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

    def get_gender(self) -> Gender:
        return self._gender

    def __str__(self):
        return (
            "Author["
            + "name="
            + self._name
            + ", email="
            + self._email
            + ", gender="
            + self._gender
            + "]"
        )
