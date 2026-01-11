#!/usr/bin/env python3
"""ConnectOnion Demo Agent. Author: Sreekar Reddy"""

from connectonion import Agent, Memory, llm_do, after_each_tool, on_complete


def log_tool_execution(agent):
    trace = agent.current_session["trace"][-1]
    if trace["type"] == "tool_execution":
        tool_name = trace["tool_name"]
        timing = trace["timing"]
        status = trace.get("status", "success")
        icon = "+" if status == "success" else "x"
        print(f"  [{icon}] {tool_name}: {timing:.0f}ms")


def log_completion(agent):
    trace = agent.current_session["trace"]
    tool_count = sum(1 for t in trace if t["type"] == "tool_execution")
    llm_count = sum(1 for t in trace if t["type"] == "llm_call")
    print(f"  [=] Done: {tool_count} tools, {llm_count} LLM calls")


metrics_plugin = [after_each_tool(log_tool_execution), on_complete(log_completion)]


def topic_overview(query: str) -> str:
    """Generate an LLM-based overview of a topic (not web search). Returns key points."""
    result = llm_do(
        f"Provide a concise overview about: {query}. Include 3-4 key points.",
        model="co/gpt-4o-mini",
    )
    return result


def summarize(text: str, style: str = "brief") -> str:
    """Summarize text. Style: 'brief' (2-3 sentences), 'detailed', or 'bullets' (5 points)."""
    style_prompts = {
        "brief": "Summarize in 2-3 sentences",
        "detailed": "Provide a comprehensive summary with context",
        "bullets": "Summarize as 5 bullet points",
    }
    prompt = style_prompts.get(style, style_prompts["brief"])
    return llm_do(f"{prompt}:\n\n{text}", model="co/gpt-4o-mini")


memory = Memory()

agent = Agent(
    name="demo-agent",
    system_prompt="prompt.md",
    tools=[topic_overview, summarize, memory],
    model="co/gpt-4o-mini",
    max_iterations=5,
    plugins=[metrics_plugin],  # type: ignore[arg-type]
)


if __name__ == "__main__":
    print(
        """
+===================================================+
|  ConnectOnion Demo Agent                          |
|  Built by Sreekar Reddy                           |
+===================================================+
"""
    )

    print("Examples:")
    print("  - 'Tell me about AI agents'")
    print("  - 'Summarize: <paste text here>'")
    print("  - 'Save a note about Python'")
    print("  - Type 'quit' to exit\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            response = agent.input(user_input)
            print(f"\nAgent: {response}\n")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
