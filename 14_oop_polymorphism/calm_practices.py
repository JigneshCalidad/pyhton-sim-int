"""Demonstrate polymorphism with different calm-seeking practices."""


class CalmPractice:
    """Base practice inviting subclasses to define their calm."""

    def find_calm(self) -> str:
        raise NotImplementedError("Subclasses must share how they find calm.")


class BreathingPractice(CalmPractice):
    def find_calm(self) -> str:
        return "I count breaths and feel my chest soften."


class JournalingPractice(CalmPractice):
    def find_calm(self) -> str:
        return "I write honest words until my thoughts settle."


class NatureWalkPractice(CalmPractice):
    def find_calm(self) -> str:
        return "I walk among trees and let the wind organize my mind."


practices: list[CalmPractice] = [
    BreathingPractice(),
    JournalingPractice(),
    NatureWalkPractice(),
]

for practice in practices:
    print(practice.find_calm())

