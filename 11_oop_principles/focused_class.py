"""Illustrate the single responsibility principle with a dedicated class."""


class MoodTracker:
    """Track current mood without taking on unrelated tasks."""

    def __init__(self, initial_mood: str) -> None:
        self._mood = initial_mood

    def update_mood(self, new_mood: str) -> None:
        """Change the mood with a simple, focused action."""
        self._mood = new_mood

    def describe(self) -> str:
        """Return a message about the current mood."""
        return f"Today feels {self._mood}."


tracker = MoodTracker("reflective")
print(tracker.describe())
tracker.update_mood("hopeful")
print(tracker.describe())

