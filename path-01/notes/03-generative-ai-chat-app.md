# Module 3 — Develop a generative AI chat app with Microsoft Foundry

_Learning objectives:_
1. Describe the process for creating a generative AI chat app with Microsoft Foundry
2. Use the Chat playground to explore models and generate code samples
3. Choose an endpoint, auth method, and client SDK
4. Use the Responses API to generate AI responses
5. Use the ChatCompletions API to generate AI responses

---

## Chat Playground

- Testing models interactively without writing code
- Try different system messages, parameters (temperature, max tokens)
- Generate code samples directly from the playground

_Key insight: the playground is not just for exploring — it generates the SDK code you'd need for that model config._

---

## Endpoint & SDK Choices

### Endpoint types

| Endpoint | When to use |
|----------|-------------|
| Azure OpenAI endpoint | OpenAI SDK native APIs (ChatCompletions) |
| Foundry project endpoint | Responses API, Foundry Agent service |

### Authentication

| Method | When |
|--------|------|
| **Key** (API key) | Dev/testing only |
| **Microsoft Entra ID** | Production — use `DefaultAzureCredential` |

### SDK

- OpenAI SDK (Python, C#) — `openai` package
- Install: `pip install openai`

---

## ChatCompletions API

- The traditional OpenAI API (`/chat/completions`)
- Well-established, widely used
- Python pattern:

```python
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=f"{os.getenv('AZURE_OPENAI_ENDPOINT')}/openai/deployments/{DEPLOYMENT_NAME}"
)

response = client.chat.completions.create(
    model=DEPLOYMENT_NAME,
    messages=[...]
)
```

---

## Responses API

- Newer API — increasingly superseding ChatCompletions
- More flexible response types (text, tool calls, etc.)
- Designed for agentic patterns, not just chat
- Same SDK, different client initialization

---

## Key Patterns

- **Conversation tracking** — passing message history for context
- **Streaming** — `stream=True` for token-by-token responses
- **Async** — `AsyncOpenAI` client for non-blocking calls

---

## Your notes

```

```
