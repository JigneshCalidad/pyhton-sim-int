"""Show how different prompts respond to the same request."""


class Prompt:
    def respond(self) -> str:
        raise NotImplementedError


class ReflectionPrompt(Prompt):
    def respond(self) -> str:
        return "What insight asked for your attention today?"


class ConnectionPrompt(Prompt):
    def respond(self) -> str:
        return "Who supported you recently, and how can you thank them?"


class FutureDreamPrompt(Prompt):
    def respond(self) -> str:
        return "Describe a future moment that feels both calm and exciting."


def invite(prompt: Prompt) -> None:
    print(prompt.respond())


for prompt in [ReflectionPrompt(), ConnectionPrompt(), FutureDreamPrompt()]:
    invite(prompt)

