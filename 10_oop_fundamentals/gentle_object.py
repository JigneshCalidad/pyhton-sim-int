"""Show how different objects can emerge from the same class blueprint."""


class ReflectionSession:
    """Invite a reflective pause with a theme and duration."""

    def __init__(self, theme: str, minutes: int) -> None:
        self.theme = theme
        self.minutes = minutes

    def summary(self) -> str:
        """Return a sentence capturing the session's essence."""
        return f"A {self.minutes}-minute pause focused on {self.theme}."


morning_session = ReflectionSession("gratitude", 10)
evening_session = ReflectionSession("integration", 15)

print(morning_session.summary())
print(evening_session.summary())

