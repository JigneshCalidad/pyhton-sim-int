"""Apply logical operators to decide on restorative actions."""

is_weekend = False
energy_reserve_high = True
friend_needs_support = True

offer_help = energy_reserve_high and friend_needs_support
plan_solo_time = (not friend_needs_support) or (not energy_reserve_high)

print("Offer help?", offer_help)
print("Plan solo time?", plan_solo_time)

# Notice how logical operators honor both empathy and boundaries.

