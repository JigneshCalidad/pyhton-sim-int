"""Reflect on invitations using if/elif/else logic."""

invitation_type = "gathering"  # try "study_date", "solo_retreat"
energy_today = "soft"  # try "vibrant", "soft", "low"

if invitation_type == "gathering" and energy_today == "vibrant":
    print("Join the gathering. Your spark could brighten the room.")
elif invitation_type == "study_date" and energy_today in ("vibrant", "soft"):
    print("A study date could be grounding. Bring tea and curiosity.")
elif invitation_type == "solo_retreat":
    print("Honor your inner world today. A solo retreat sounds nourishing.")
else:
    print("It might be kind to decline and rest. Your peace matters.")

