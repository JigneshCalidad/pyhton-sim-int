"""Illustrate inheritance by adapting a grounding ritual."""


class Ritual:
    """Base ritual with a shared outline."""

    def begin(self) -> None:
        print("Pause. Breathe. Arrive.")

    def reflect(self) -> None:
        print("Consider one insight that is asking to be heard.")

    def close(self) -> None:
        print("Thank yourself for this moment.")


class MorningRitual(Ritual):
    """Add morning-specific touches."""

    def reflect(self) -> None:
        print("Welcome the sunrise and set a gentle intention for the day.")


class EveningRitual(Ritual):
    """Add evening-specific touches."""

    def close(self) -> None:
        print("Release the day. Trust that rest will weave the lessons in.")


MorningRitual().begin()
MorningRitual().reflect()
MorningRitual().close()

print("---")

EveningRitual().begin()
EveningRitual().reflect()
EveningRitual().close()

