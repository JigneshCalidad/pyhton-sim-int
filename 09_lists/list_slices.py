"""Use slicing to revisit portions of a list gently."""

week_reflections = [
    "Monday: noticed resilience",
    "Tuesday: practiced boundaries",
    "Wednesday: nurtured creativity",
    "Thursday: embraced rest",
    "Friday: celebrated progress",
]

midweek = week_reflections[1:4]
print("Midweek focus:")
for entry in midweek:
    print(entry)

print("Every other day reminder:", week_reflections[::2])

