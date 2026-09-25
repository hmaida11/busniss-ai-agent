from agent_app.agent import Agent


def test_agent_returns_greeting_response():
    agent = Agent(name="DemoAgent")
    response = agent.respond("hello")
    assert "DemoAgent" in response
    assert "hello" in response.lower()


def test_agent_handles_empty_input_gracefully():
    agent = Agent(name="DemoAgent")
    response = agent.respond("")
    assert "How can I help?" in response


def test_agent_helpfully_plans_tasks():
    agent = Agent(name="DemoAgent")
    response = agent.respond("help me make a plan for a project")
    assert "plan" in response.lower()
    assert "steps" in response.lower()
