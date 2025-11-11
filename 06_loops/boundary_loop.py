"""Demonstrate breaking a loop when a boundary is reached."""

check_ins = ["energized", "steady", "tired", "worn out"]

for mood in check_ins:
    print(f"Current mood: {mood}")
    if mood == "tired":
        print("Time to pause. Breaking the loop to honor rest.")
        break

print("Loop complete. Boundaries respected, energy protected.")

