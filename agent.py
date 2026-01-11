#!/usr/bin/env python3
"""
Simple Research Agent - Built with ConnectOnion
================================================

A straightforward agent that researches topics and provides summaries.
This demonstrates ConnectOnion's core concepts cleanly.

Author: Sreekar Reddy
"""

from connectonion import Agent, Memory, llm_do


# --- Tools (just functions!) ---


def search_topic(query: str) -> str:
    """
    Search for information on a topic.

    Args:
        query: What to search for

    Returns:
        Search results summary
    """
    # In production, this would call a real search API
    # For demo, we use llm_do to simulate intelligent search
    result = llm_do(
        f"Provide a brief, factual summary about: {query}. "
        f"Include 3-4 key points with recent developments.",
        model="co/gpt-4o-mini",
    )
    return result


def summarize(text: str, style: str = "brief") -> str:
    """
    Summarize text in a specific style.

    Args:
        text: Content to summarize
        style: 'brief', 'detailed', or 'bullets'

    Returns:
        Summarized content
    """
    style_prompts = {
        "brief": "Summarize in 2-3 sentences",
        "detailed": "Provide a comprehensive summary with context",
        "bullets": "Summarize as 5 bullet points",
    }

    prompt = style_prompts.get(style, style_prompts["brief"])

    return llm_do(f"{prompt}:\n\n{text}", model="co/gpt-4o-mini")


def save_note(topic: str, content: str) -> str:
    """
    Save research notes for later.

    Args:
        topic: Topic name (used as key)
        content: Notes to save

    Returns:
        Confirmation message
    """
    memory = Memory()
    memory.write_memory(topic.lower().replace(" ", "-"), content)
    return f"Saved notes on '{topic}'"


def get_notes(topic: str) -> str:
    """
    Retrieve saved notes on a topic.

    Args:
        topic: Topic to look up

    Returns:
        Saved notes or 'not found'
    """
    memory = Memory()
    return memory.read_memory(topic.lower().replace(" ", "-"))


# --- Create the Agent ---

agent = Agent(
    name="research-assistant",
    system_prompt="""You are a helpful research assistant. 

Your job is to:
1. Search for information when asked about a topic
2. Summarize findings clearly
3. Save important notes for later reference

Be concise and factual. Always search before answering questions about current topics.""",
    tools=[search_topic, summarize, save_note, get_notes],
    model="co/gpt-4o-mini",  # FREE via ConnectOnion
    max_iterations=5,  # Keep it simple
)


# --- Main ---

if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════════════╗
║  🧅 Simple Research Agent                         ║
║  Built with ConnectOnion by Sreekar Reddy         ║
╚═══════════════════════════════════════════════════╝
""")

    print("Examples:")
    print("  • 'What are AI agents?'")
    print("  • 'Summarize the latest in machine learning'")
    print("  • 'Save a note about Python'")
    print("  • Type 'quit' to exit\n")

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
