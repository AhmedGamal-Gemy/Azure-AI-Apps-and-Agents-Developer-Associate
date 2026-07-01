# Exercise: City Explorer AI

Build an AI travel assistant that uses all four tool types to help users explore cities.

## Setup

- Use the **Azure OpenAI endpoint** with Entra ID auth (same pattern as Module 3)
- Model: `gpt-4.1` (or whatever you have deployed)
- Packages: `openai`, `azure-identity`
- Create a folder `city-explorer/` with your `.env` file and `city_explorer.py`

## Requirements

The assistant should handle these four kinds of user requests:

### 1. `web_search` — Current info

```
User: What's happening in Tokyo this weekend?
```

→ The model should search the web for current events in Tokyo and summarize them.

### 2. `file_search` — Local knowledge

Create a vector store and upload 2–3 text files (e.g., a mini guide about a city, restaurant tips, or your own notes about places you've visited).

```
User: Any good ramen spots in Shibuya?
```

→ The model should search the uploaded files and answer from that knowledge base.

### 3. `code_interpreter` — Calculations

```
User: If my budget is 200,000 yen, can I spend 5 days in Tokyo including a hotel at 15,000 yen/night?
```

→ The model should write and run Python code to calculate the budget breakdown and answer.

### 4. `function` — Custom tool

Define a custom function called `get_weather` that takes a `city` and `date` string parameter. For now, just return a mock response (hardcoded is fine — the point is the function-calling flow):

```
User: What's the weather like in Tokyo next Tuesday?
```

→ The model should call `get_weather("Tokyo", "next Tuesday")`, you handle the mock response, and the model formats the final answer.

## Code Structure

```python
# city_explorer.py — write this yourself!

# 1. Imports (openai, azure.identity, os)
# 2. Auth — token_provider with DefaultAzureCredential
# 3. Create OpenAI client
# 4. Create vector store + upload your files (for file_search)
# 5. Define get_weather function schema
# 6. Chat loop with all 4 tools in the tools list
# 7. Handle function call output (weather mock) and send it back
```

## Hints (only if stuck)

<details>
<summary>Hint 1 — tool definitions in the responses.create call</summary>

```python
tools=[
    {"type": "code_interpreter"},
    {"type": "web_search"},
    {
        "type": "file_search",
        "vector_store_ids": [vector_store.id]
    },
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the weather forecast for a city on a specific date",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"},
                "date": {"type": "string"}
            },
            "required": ["city", "date"]
        }
    }
]
```

</details>

<details>
<summary>Hint 2 — handling function calls</summary>

After the response, check if the model wants to call a function:

```python
if response.output[0].type == "function_call":
    # Call your mock function
    # Create a function_call_output message
    # Call responses.create again with the output
```

</details>

## Verify it works

Test all four scenarios above. The assistant should:
- Search the web for current Tokyo events
- Find ramen tips from your uploaded files
- Calculate a budget breakdown using Python code
- Tell you the weather (from your mock function)

## What you're practicing

| Tool | Skill |
|------|-------|
| `web_search` | Adding real-time grounding without any API setup |
| `file_search` | Vector stores + file upload for RAG-style answers |
| `code_interpreter` | Letting the model run code instead of guessing numbers |
| `function` | The function-calling round-trip (model calls → you handle → feed back) |
