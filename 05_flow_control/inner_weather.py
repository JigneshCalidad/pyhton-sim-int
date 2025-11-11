"""Translate inner weather into guidance using nested decisions."""

emotional_weather = "overcast"  # try "sunny", "overcast", "stormy"
time_available = 45

if emotional_weather == "sunny":
    print("You feel bright. Maybe start a new creative coding idea.")
elif emotional_weather == "overcast":
    if time_available >= 30:
        print("Choose a comforting tutorial and journal your insights afterward.")
    else:
        print("Take five minutes to breathe and jot down one gentle intention.")
else:
    print("Stormy moments need care. Close the laptop and nurture your heart.")

