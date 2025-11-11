"""Observe mutability by comparing lists and tuples with the same information."""

# A tuple holds memories like a scrapbook you do not wish to rearrange.
favorite_quotes = ("Growth is gentle", "Rest is productive", "Intuition is wisdom")

# A list is a journal you can keep editing.
daily_gratitudes = ["quiet mornings", "good conversation", "warm light"]

print("Treasured quotes (tuple):", favorite_quotes)
print("Gratitudes before update:", daily_gratitudes)

# Lists are comfortable with change.
daily_gratitudes.append("a page of notes that made sense")
print("Gratitudes after update:", daily_gratitudes)

# Try altering the tuple to feel the boundary. It will protect its structure.

