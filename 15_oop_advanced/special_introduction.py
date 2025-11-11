"""Use special methods to give objects authentic introductions."""


class ReflectionCard:
    """A card that introduces itself warmly when printed."""

    def __init__(self, theme: str, prompt: str) -> None:
        self.theme = theme
        self.prompt = prompt

    def __str__(self) -> str:
        return f"[{self.theme}] {self.prompt}"


card = ReflectionCard("Courage", "Describe a moment you listened to intuition today.")
print(card)

