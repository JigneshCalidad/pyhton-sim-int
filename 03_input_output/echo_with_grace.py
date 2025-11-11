"""Show how to reshape input into numbers for supportive feedback."""

minutes_today = input("How many mindful minutes did you gift yourself today? ")

# Convert the string to an integer if possible.
try:
    minutes_int = int(minutes_today)
    print(f"That is {minutes_int} minutes of intentional care. Beautiful.")
    print("If you add five more minutes tomorrow, how might that feel?")
except ValueError:
    print("Thank you for sharing. Even when numbers aren't exact, your effort matters.")

