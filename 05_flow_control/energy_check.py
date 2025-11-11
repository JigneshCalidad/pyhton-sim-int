"""Use conditionals to suggest a supportive next step."""

energy_level = 6  # scale 1-10
deadline_near = False

if energy_level >= 7:
    print("Energy feels abundant. Consider diving into a learning flow.")
elif 4 <= energy_level < 7:
    if deadline_near:
        print("Energy is moderate and a deadline is near. Focus gently, then rest.")
    else:
        print("Maybe choose a light review session paired with restorative breaks.")
else:
    print("Energy is tender. Rest is a wise investment today.")

