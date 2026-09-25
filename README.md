# Starter Agent

This project creates a small, local AI-style agent scaffold that can be used as a starting point for more advanced workflows.

## Features

- Simple `Agent` class with a message loop
- Lightweight CLI entry point for quick testing
- Extensible structure for adding tools, planning, or memory

## Run the agent

```bash
python app.py "hello there"
```

You can also launch an interactive chat session:

```bash
python app.py
```

## Project structure

- `app.py` - CLI entry point
- `agent_app/agent.py` - agent logic
- `tests/test_agent.py` - basic validation examples

## Notes

This scaffold intentionally avoids external dependencies so it is easy to run in a fresh environment.
