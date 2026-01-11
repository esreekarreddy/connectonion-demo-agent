# 🧅 Research Agent - Built with ConnectOnion

A working AI research agent built with [ConnectOnion](https://connectonion.com), demonstrating the framework's core concepts.

**Author:** Sreekar Reddy  
**Framework:** ConnectOnion v0.6.2

---

## Quick Start

```bash
# Install
pip install connectonion

# Authenticate (FREE credits - no API key needed)
co auth

# Run
python agent.py
```

---

## What It Does

A research assistant with 4 tools:

| Tool | What It Does |
|------|--------------|
| `search_topic(query)` | Search for information using LLM |
| `summarize(text, style)` | Condense text (brief/detailed/bullets) |
| `save_note(topic, content)` | Persist notes using Memory |
| `get_notes(topic)` | Retrieve saved notes |

---

## Example

```
You: Future of AI Agents

Agent: The future of AI agents includes several key trends:

1. **Enhanced Personalization**: AI agents designed for 
   personalized experiences using advanced ML.

2. **Integration into Applications**: Customer service, 
   smart homes, business workflows.

3. **Ethical Focus**: Organizations adopting guidelines 
   for transparency and accountability.

4. **Collaborative AI**: Agents working alongside humans 
   in healthcare, finance, and creative industries.
```

---

## Key ConnectOnion Concepts Used

```python
from connectonion import Agent, Memory, llm_do

# 1. Agent with tools (functions become tools automatically)
agent = Agent(
    name="research-assistant",
    system_prompt="You are a helpful research assistant...",
    tools=[search_topic, summarize, save_note, get_notes],
    model="co/gpt-4o-mini"  # FREE via co auth
)

# 2. One-shot LLM calls inside tools
result = llm_do("Summarize this...", model="co/gpt-4o-mini")

# 3. Persistent memory
memory = Memory()
memory.write_memory("key", "value")  # Persists across sessions
```

---

## What I'd Build Next: Multi-Agent Research Team

If extending this, I'd leverage ConnectOnion's advanced features:

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     🎯 ORCHESTRATOR                          │
│              Coordinates via connect()                       │
└───────────┬─────────────────┬─────────────────┬─────────────┘
            │                 │                 │
            ▼                 ▼                 ▼
    ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
    │ 🔍 RESEARCHER │ │ 📊 ANALYST    │ │ ✍️ WRITER     │
    │  host()       │ │  host()       │ │  host()       │
    └───────────────┘ └───────────────┘ └───────────────┘
```

### Key Features I'd Use

| Feature | How I'd Use It |
|---------|----------------|
| **`connect(address)`** | Orchestrator calls remote specialist agents |
| **`host(agent)`** | Each specialist runs as a P2P service |
| **Plugin System** | Custom metrics plugin with event hooks |
| **`on_events`** | `after_llm`, `before_tools` for observability |
| **Memory** | Shared research findings across agents |

### Example: P2P Agent Communication

```python
from connectonion import Agent, connect, host

# Researcher agent (runs on one machine)
researcher = Agent("researcher", tools=[search, fetch_url])
host(researcher)  # Now accessible at 0x1234...

# Orchestrator connects remotely
researcher_remote = connect("0x1234...")
result = researcher_remote.input("Research AI agents")
```

### Example: Custom Plugin

```python
from connectonion import after_llm, on_complete

def log_performance(agent):
    trace = agent.current_session['trace'][-1]
    print(f"LLM call: {trace['duration_ms']}ms")

def task_done(agent):
    print("Task complete!")

metrics_plugin = [
    after_llm(log_performance),
    on_complete(task_done)
]

agent = Agent("monitored", tools=[...], plugins=[metrics_plugin])
```

### Why This Architecture

1. **Separation of Concerns** - Each agent does one thing well
2. **Scalability** - Agents can run on different machines
3. **P2P = No Central Server** - ConnectOnion's unique value prop
4. **Observability** - Plugins give full visibility into agent behavior

---

## Project Structure

```
connectonion-research-agent/
├── agent.py             # Working agent (~80 lines)
├── README.md            # This file
├── requirements.txt     # Dependencies
└── .gitignore           # Git config
```

---

## Resources

- [ConnectOnion Docs](https://docs.connectonion.com)
- [Quick Start](https://docs.connectonion.com/quickstart)
- [P2P Networking](https://docs.connectonion.com/connect)
- [Plugin System](https://docs.connectonion.com/plugin)
- [GitHub](https://github.com/openonion/connectonion)

---

*Built for [OpenOnion](https://openonion.ai) by Sreekar Reddy*
