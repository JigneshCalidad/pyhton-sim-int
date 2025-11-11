"""Demonstrate encapsulation with gentle access to private reflections."""


class SoulJournal:
    """Hold reflections privately while offering mindful sharing."""

    def __init__(self) -> None:
        self._entries: list[str] = []

    def add_entry(self, note: str) -> None:
        """Protect the way entries are stored while adding a new note."""
        self._entries.append(note)

    def latest_entry(self) -> str:
        """Share only the most recent entry, honoring privacy."""
        if not self._entries:
            return "No reflections yet, and that is okay."
        return self._entries[-1]


journal = SoulJournal()
journal.add_entry("Today I learned that patience can be practiced in code.")
print(journal.latest_entry())

