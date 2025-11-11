"""Maintain a digital journal that balances structure and soul."""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class JournalEntry:
    """Represent a single journal entry."""

    timestamp: datetime
    mood: str
    gratitude: str
    reflection: str

    def format(self) -> str:
        """Return a formatted string for storage."""
        stamp = self.timestamp.strftime("%Y-%m-%d %H:%M")
        return (
            f"[{stamp}]\n"
            f"Mood: {self.mood}\n"
            f"Gratitude: {self.gratitude}\n"
            f"Reflection: {self.reflection}\n"
            "—" * 20 + "\n"
        )


def save_entry(entry: JournalEntry, path: Path) -> None:
    """Append the journal entry to the given file path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(entry.format())
    print(f"Entry saved to {path}.")


def show_recent_entries(path: Path, limit: int = 3) -> None:
    """Display the most recent entries, if available."""
    if not path.exists():
        print("No journal entries yet. Today can be the first one.")
        return

    with path.open(encoding="utf-8") as file:
        lines = file.readlines()

    separator = "—" * 20 + "\n"
    entries = "".join(lines).split(separator)
    recent = [entry for entry in entries if entry.strip()][-limit:]

    print("\nRecent reflections:\n")
    for entry in recent:
        print(entry.strip())
        print(separator)


def main() -> None:
    """Gather journal inputs and save them."""
    journal_path = Path("journal_entries.txt")

    mood = input("Mood word: ").strip()
    gratitude = input("Something you are grateful for: ").strip()
    reflection = input("Share a thought you want to remember: ").strip()

    entry = JournalEntry(
        timestamp=datetime.now(),
        mood=mood,
        gratitude=gratitude,
        reflection=reflection,
    )
    save_entry(entry, journal_path)

    view = input("Would you like to see recent entries? (y/n): ").strip().lower()
    if view == "y":
        show_recent_entries(journal_path)

    print("Close your eyes for a moment and let the words settle.")


if __name__ == "__main__":
    print("Welcome to your Digital Journal sanctuary.")
    main()

