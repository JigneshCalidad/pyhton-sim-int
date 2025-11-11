"""Explore instance methods that draw from object attributes."""


class ReflectionBuddy:
    """Hold space for meaningful check-ins."""

    def __init__(self, name: str, focus: str) -> None:
        self.name = name
        self.focus = focus

    def greet(self) -> None:
        """Share a greeting rooted in this buddy's focus."""
        print(f"{self.name} says: I'm here to explore {self.focus} with you.")


buddy = ReflectionBuddy("Lena", "creative sparks")
buddy.greet()

