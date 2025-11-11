"""Track habits with compassionate summaries."""

from dataclasses import dataclass, field


@dataclass
class Habit:
    """Represent a habit and its daily check-ins."""

    name: str
    check_ins: list[bool] = field(default_factory=list)

    def record(self, completed: bool) -> None:
        """Record whether the habit was honored today."""
        self.check_ins.append(completed)

    def visualization(self) -> str:
        """Return a simple string showing progress."""
        symbols = ["✓" if done else "·" for done in self.check_ins]
        return "".join(symbols) or "No check-ins yet."


def main() -> None:
    """Guide the learner through tracking a few habits."""
    habit_names = input("List habits to track (comma separated): ").split(",")
    habits = [Habit(name.strip()) for name in habit_names if name.strip()]

    if not habits:
        print("No habits provided. Consider adding one nourishing practice.")
        return

    while True:
        for habit in habits:
            response = input(f"Did you honor '{habit.name}' today? (y/n): ").strip().lower()
            habit.record(response == "y")

        continue_tracking = input("Record another day? (y/n): ").strip().lower()
        if continue_tracking != "y":
            break

    print("\nHabit visualizations:")
    for habit in habits:
        print(f"{habit.name}: {habit.visualization()}")
    print("Remember: gaps are invitations, not failures.")


if __name__ == "__main__":
    print("Welcome to the Gentle Habit Tracker.")
    main()

