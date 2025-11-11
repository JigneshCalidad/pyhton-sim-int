"""Use abstraction to reveal only what someone needs to feel supported."""


class SupportCircle:
    """Offer support without exposing the intricate logistics."""

    def __init__(self) -> None:
        self._listeners = ["Avery", "Kai", "Mira"]

    def request_listener(self) -> str:
        """Return a supportive name without sharing internal details."""
        if not self._listeners:
            return "The circle is resting today; try again tomorrow."
        return f"{self._listeners[0]} is available to listen."


circle = SupportCircle()
print(circle.request_listener())

