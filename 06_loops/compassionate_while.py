"""Stay in a while loop until you feel ready to pause."""

breaths_taken = 0

while breaths_taken < 3:
    breaths_taken += 1
    print(f"Inhale... exhale... ({breaths_taken})")

print("Notice how the loop ended right when you chose enough calm.")

