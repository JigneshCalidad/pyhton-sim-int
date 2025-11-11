"""Use a class method to uphold shared values among instances."""


class CircleMember:
    """Represent someone participating in a supportive circle."""

    shared_values = ["empathy", "curiosity", "consent"]

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def values_statement(cls) -> str:
        """Speak on behalf of all members about what matters."""
        values = ", ".join(cls.shared_values)
        return f"Our circle honors {values}."


print(CircleMember.values_statement())
member = CircleMember("Noor")
print(f"{member.name} carries these values into each meeting.")

