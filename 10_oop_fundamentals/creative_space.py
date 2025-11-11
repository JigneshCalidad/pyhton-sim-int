"""Model a creative space with attributes and a gentle method."""


class CreativeSpace:
    """Describe a space that nurtures ideas."""

    def __init__(self, location: str, has_natural_light: bool, favorite_items: list[str]) -> None:
        self.location = location
        self.has_natural_light = has_natural_light
        self.favorite_items = favorite_items

    def describe(self) -> None:
        """Print a soothing description of the space."""
        light = "sunlit" if self.has_natural_light else "cozy lamplight"
        items = ", ".join(self.favorite_items)
        print(f"In the {self.location}, {light} filters through treasured items: {items}.")


studio = CreativeSpace("study nook", True, ["journals", "plants", "soft music"])
studio.describe()

