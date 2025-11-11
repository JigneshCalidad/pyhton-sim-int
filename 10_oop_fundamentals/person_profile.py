"""Introduce a simple Person class with meaningful attributes."""


class Person:
    """Represent someone with traits that tell a story."""

    def __init__(self, name: str, intention: str) -> None:
        self.name = name
        self.intention = intention

    def introduce(self) -> None:
        """Share how this person is moving through the day."""
        print(f"{self.name} is guided today by the intention to {self.intention}.")


friend = Person("Sage", "listen deeply")
friend.introduce()

