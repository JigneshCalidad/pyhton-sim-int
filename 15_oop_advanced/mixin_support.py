"""Share supportive abilities using a mixin."""


class EncouragementMixin:
    """Provide a shared encouragement method."""

    def encourage(self) -> str:
        return "Remember: progress is made of gentle repetitions."


class StudySession(EncouragementMixin):
    """A study session that inherits encouragement."""

    def plan(self) -> str:
        return "Schedule two focused blocks with soft breaks."


class ReflectionRetreat(EncouragementMixin):
    """A retreat that also offers encouragement."""

    def plan(self) -> str:
        return "Prepare a calm space with journals, tea, and ambient music."


for experience in (StudySession(), ReflectionRetreat()):
    print(experience.plan())
    print(experience.encourage())

