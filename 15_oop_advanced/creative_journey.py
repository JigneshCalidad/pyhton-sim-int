"""Explore composition by combining supportive companions."""


class Journal:
    """Hold reflections for the journey."""

    def write(self, note: str) -> str:
        return f"Journal entry saved: {note}"


class Mentor:
    """Offer gentle guidance."""

    def encourage(self) -> str:
        return "Mentor whispers: Trust your steady growth."


class Ritual:
    """Provide a grounding practice."""

    def begin(self) -> str:
        return "Light a candle, breathe deeply, and arrive."


class CreativeJourney:
    """Compose journal, mentor, and ritual into a supportive ecosystem."""

    def __init__(self) -> None:
        self.journal = Journal()
        self.mentor = Mentor()
        self.ritual = Ritual()

    def start(self) -> None:
        print(self.ritual.begin())
        print(self.mentor.encourage())
        print(self.journal.write("I am learning to merge intuition with logic."))


CreativeJourney().start()

