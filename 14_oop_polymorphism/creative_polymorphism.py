"""Use polymorphism to highlight different creative expressions."""


class Painter:
    def express(self) -> str:
        return "Painting with watercolors to capture fleeting emotion."


class Writer:
    def express(self) -> str:
        return "Writing letters that explore layered truths."


class Musician:
    def express(self) -> str:
        return "Composing melodies that mirror inner tides."


def share_expression(artist) -> None:
    """Duck typing: trust that the artist can express themselves."""
    print(artist.express())


artists = [Painter(), Writer(), Musician()]
for artist in artists:
    share_expression(artist)

