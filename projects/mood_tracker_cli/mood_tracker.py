"""A gentle CLI to record moods and notice patterns."""

from dataclasses import dataclass


@dataclass
class MoodEntry:
    """Represent one moment of emotional weather."""

    day: str
    mood: str
    note: str


def summarize(entries: list[MoodEntry]) -> None:
    """Print a compassionate summary of recorded moods."""
    if not entries:
        print("No entries yet. Each mood awaits your attention.")
        return

    print("\nSummary of the moods you shared:")
    unique_moods = {entry.mood for entry in entries}
    for mood in unique_moods:
        count = sum(1 for entry in entries if entry.mood == mood)
        print(f"- {mood}: noticed {count} time(s)")

    last_entry = entries[-1]
    print(f"\nLast note you offered: \"{last_entry.note}\" on {last_entry.day}")
    print("Take a breath and thank yourself for listening.")


def main() -> None:
    """Collect mood entries until the user chooses to stop."""
    entries: list[MoodEntry] = []

    while True:
        day = input("Day (e.g., Monday): ").strip()
        mood = input("Mood word: ").strip().lower()
        note = input("Short note: ").strip()
        entries.append(MoodEntry(day=day, mood=mood, note=note))

        keep_going = input("Add another entry? (y/n): ").strip().lower()
        if keep_going != "y":
            break

    summarize(entries)


if __name__ == "__main__":
    print("Welcome to the Mood Tracker. Trust whatever arises.")
    main()

