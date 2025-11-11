"""Log book reflections and optionally export them."""

from dataclasses import dataclass


@dataclass
class BookReflection:
    """Hold details about a book and what it offered you."""

    title: str
    author: str
    reflection: str


def export(reflections: list[BookReflection], path: str) -> None:
    """Export reflections to a text file."""
    with open(path, "w", encoding="utf-8") as file:
        for entry in reflections:
            file.write(f"{entry.title} by {entry.author}\n")
            file.write(f"Reflection: {entry.reflection}\n")
            file.write("-" * 40 + "\n")
    print(f"Reflections saved to {path}.")


def main() -> None:
    """Collect reflections until the learner chooses to stop."""
    reflections: list[BookReflection] = []

    while True:
        title = input("Book title: ").strip()
        author = input("Author: ").strip()
        reflection = input("What stayed with you? ").strip()
        reflections.append(BookReflection(title, author, reflection))

        another = input("Add another book? (y/n): ").strip().lower()
        if another != "y":
            break

    if reflections:
        save = input("Save reflections to a file? (y/n): ").strip().lower()
        if save == "y":
            filename = input("Filename (e.g., reflections.txt): ").strip()
            export(reflections, filename)

    print("Notice any themes across the stories you recorded. Let them simmer.")


if __name__ == "__main__":
    print("Welcome to the Book Reflection Log.")
    main()

