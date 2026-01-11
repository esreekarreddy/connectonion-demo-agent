# ConnectOnion Demo Agent

A minimal agent demonstrating ConnectOnion's core features.

**Author:** Sreekar Reddy  
**Framework:** ConnectOnion v0.6.2

## Quick Start

```bash
pip install connectonion
co auth                    # Get free credits
python agent.py
```

## Example Output

```
You: Tell me about AI agents

  [+] topic_overview: 2408ms
  [=] Done: 1 tools, 2 LLM calls

Agent: AI agents are software systems that can perceive their environment...
```

## Tools

| Tool | Type | What It Does |
|------|------|--------------|
| `topic_overview` | Function | LLM-generated overview of a topic (not web search) |
| `summarize` | Function | Condense text (brief/detailed/bullets) |
| `read_memory` | Memory | Retrieve saved notes |
| `write_memory` | Memory | Save notes |
| `list_memories` | Memory | List all saved keys |
| `search_memory` | Memory | Search saved content |

**Note:** 2 function tools + Memory instance (auto-discovers 4 methods) = 6 tools total.

## Features Demonstrated

| Feature | Description |
|---------|-------------|
| `Agent` | Core agent with function tools |
| `Memory` | Passed as tool, auto-discovers methods |
| `llm_do` | One-shot LLM calls inside tools |
| `plugins` | Custom metrics using `after_each_tool`, `on_complete` |
| `co/gpt-4o-mini` | Free credits via `co auth` |

## What I'd Build Next

```
┌───────────────────────────────────────────────┐
│               ORCHESTRATOR                    │
│          coordinates via connect()            │
└───────┬───────────────┬───────────────┬───────┘
        │               │               │
        ▼               ▼               ▼
  ┌──────────┐   ┌──────────┐   ┌──────────┐
  │RESEARCHER│   │ ANALYST  │   │  WRITER  │
  │  host()  │   │  host()  │   │  host()  │
  └──────────┘   └──────────┘   └──────────┘
```

| Feature | Purpose |
|---------|---------|
| `host(agent)` | Expose agent via HTTP, WebSocket, P2P |
| `connect(address)` | Connect to remote agents |
| `re_act` plugin | Built-in planning + reflection |

## Resources

- [Docs](https://docs.connectonion.com) · [Plugins](https://docs.connectonion.com/plugin) · [P2P](https://docs.connectonion.com/host) · [GitHub](https://github.com/openonion/connectonion)

---

*Built for [OpenOnion](https://openonion.ai) by Sreekar Reddy*
