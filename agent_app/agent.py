class Agent:
    def __init__(self, name: str = "Agent") -> None:
        self.name = name
        self.history: list[str] = []

    def _build_plan_response(self, task: str) -> str:
        return (
            f"{self.name}: I can help build a plan for '{task}'. "
            "Here are the first steps: 1. Define the goal and constraints. "
            "2. Break the work into smaller deliverables. 3. Identify the first milestone "
            "and blockers. 4. Review progress and iterate."
        )

    def respond(self, user_input: str) -> str:
        cleaned = (user_input or "").strip()

        if not cleaned:
            return f"{self.name}: How can I help?"

        self.history.append(cleaned)
        message = cleaned.lower()

        if any(token in message for token in ("hello", "hi", "hey", "greetings")):
            return (
                f"{self.name}: Hello! I can help with planning, brainstorming, or quick answers."
            )

        if any(token in message for token in ("bye", "goodbye", "see you")):
            return f"{self.name}: Goodbye! I’ll be here when you need me again."

        if any(token in message for token in ("plan", "project", "task", "steps", "goal")):
            return self._build_plan_response(cleaned)

        if "help" in message or "?" in message:
            return (
                f"{self.name}: I can help with planning, summarizing, brainstorming, or quick answers. "
                "What would you like to do?"
            )

        return (
            f"{self.name}: I received '{cleaned}'. I can help plan, summarize, or brainstorm. "
            "What would you like to do next?"
        )
