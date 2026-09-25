# Business AI Agent

A lightweight, extensible AI agent starter designed for business workflows such as planning, task assistance, brainstorming, and quick automation prototypes.

## Overview

This project provides a simple command-line agent that can respond to user prompts, support planning conversations, and serve as a base for more advanced AI-powered business tools.

## Features

- Simple conversational `Agent` class
- Task and project planning responses
- Interactive terminal mode
- Minimal dependency footprint
- Easy to extend with tools, memory, or LLM integrations

## Quick start

Run a single message:

```bash
python app.py "hello there"
```

Start an interactive session:

```bash
python app.py
```

Example inputs:

- hello
- help me make a plan for a project
- what can you do?
- quit

## Project structure

- `app.py` — CLI entry point
- `agent_app/agent.py` — agent logic and conversation flow
- `tests/test_agent.py` — validation tests
- `pyproject.toml` — Python project metadata

## Running tests

```bash
python -m pytest -q
```

## Notes

This project is intentionally simple and dependency-light so it can be used as a foundation for a larger business AI assistant.
