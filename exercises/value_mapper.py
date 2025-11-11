"""Connect decisions to values using conditionals."""

decision = input("What decision are you contemplating? ")
primary_value = input("Which core value feels most relevant right now? ")

if primary_value.lower() == "empathy":
    print(f"Consider how {decision} might support someone's feelings—including yours.")
elif primary_value.lower() == "growth":
    print(f"How could {decision} stretch you gently toward growth?")
else:
    print(f"What would it look like if {decision} honored {primary_value}?")

# Reflection: Add more `elif` branches for your other values. Let the script be a mirror.

