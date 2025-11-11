"""See how subclasses inherit common structure but add nuance."""


class JournalEntry:
    """Base journal entry with title and body."""

    def __init__(self, title: str, body: str) -> None:
        self.title = title
        self.body = body

    def display(self) -> None:
        """Print the entry in a simple format."""
        print(f"# {self.title}\n{self.body}")


class GratitudeEntry(JournalEntry):
    """Add gratitude flair to the display."""

    def display(self) -> None:
        print(f"# {self.title} (gratitude focus)\n{self.body}\nThank you.")


class InsightEntry(JournalEntry):
    """Add a question at the end to invite deeper reflection."""

    def display(self) -> None:
        super().display()
        print("What new pattern do you notice here?")


GratitudeEntry("Morning Light", "The sun warmed the room and my heart.").display()
print()
InsightEntry("Coding Breakthrough", "I understood why functions soothe complexity.").display()

