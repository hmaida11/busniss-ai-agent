import sys

from agent_app.agent import Agent


def main() -> None:
    agent = Agent(name="DemoAgent")

    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
        print(agent.respond(message))
        return

    print(f"{agent.name} is ready. Type 'quit' to exit.")
    while True:
        try:
            user_input = input("You: ").strip()
        except EOFError:
            print()
            break

        if not user_input or user_input.lower() in {"quit", "exit", "q"}:
            print(f"{agent.name}: Goodbye! I’ll be here whenever you need me.")
            break

        print(agent.respond(user_input))


if __name__ == "__main__":
    main()
