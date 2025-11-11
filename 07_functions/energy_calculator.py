"""Return the average energy investment across activities."""

def average_energy(*energy_blocks: int) -> float:
    """Compute the average of provided energy blocks, honoring pacing."""
    if not energy_blocks:
        return 0.0
    return sum(energy_blocks) / len(energy_blocks)


print("Average energy:", average_energy(20, 35, 25))
print("Average energy on softer days:", average_energy(10, 15))

