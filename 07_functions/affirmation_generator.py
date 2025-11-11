"""Return affirmations tailored to the learner's current mood."""

def affirmation(mood: str) -> str:
    """Offer a gentle affirmation based on mood."""
    mood = mood.lower()
    if mood == "hopeful":
        return "Hope is a compass—follow where it points today."
    if mood == "tired":
        return "Your worth is not measured by output. Rest is wise."
    if mood == "curious":
        return "Curiosity is a lantern. Let it light your exploration."
    return "You are doing enough. Keep breathing and noticing."


print(affirmation("curious"))
print(affirmation("tired"))

