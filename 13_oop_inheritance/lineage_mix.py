"""Show how subclasses can extend behavior without losing their roots."""


class SupportMessage:
    """Provide a message of care."""

    def message(self) -> str:
        return "You are doing your best."


class EncouragingMessage(SupportMessage):
    """Add motivation to the base message."""

    def message(self) -> str:
        base = super().message()
        return f"{base} Keep leaning into courage."


class RestfulMessage(SupportMessage):
    """Invite rest, keeping the supportive core."""

    def message(self) -> str:
        base = super().message()
        return f"{base} Consider resting to refill your well."


print(EncouragingMessage().message())
print(RestfulMessage().message())

