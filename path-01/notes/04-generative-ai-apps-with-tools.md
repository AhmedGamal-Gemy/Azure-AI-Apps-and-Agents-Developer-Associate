# Module 4 — Develop generative AI apps that use tools

_Learning objectives:_
1. Describe the capabilities of generative AI tools
2. Use the `code_interpreter` tool to run code and analyze data
3. Use the `web_search` tool to retrieve real-time information from the internet
4. Use the `file_search` tool to access and analyze files
5. Use the `function` tool to run custom code

---

## What are tools?

Tools extend a model's capabilities beyond basic chat. Instead of just generating text, the model can:
- Run code and return results
- Search the web for real-time info
- Read and analyze uploaded files
- Call your own custom functions

Tools are listed in the `tools` parameter of the Responses API call. The model decides when to invoke them based on the user's prompt.

---

## Built-in Tools

### `code_interpreter`
- Model writes and executes Python code
- Useful for data analysis, math, visualization
- Returns code output as part of the response

### `web_search`
- Model searches the internet for current information
- Grounds responses in real-time data (news, weather, prices)
- No extra setup needed — just add the tool

### `file_search`
- Model searches uploaded documents via vector stores
- Requires creating a vector store and uploading files first
- Good for RAG-style queries over your own knowledge base
- Use `vector_store_ids` parameter to link to your store

### `function` (custom tool)
- Define your own function schema (name, description, parameters)
- Model outputs a function call — your app handles execution
- You send the result back to the model for final response
- Same pattern as OpenAI function calling

---

## Key Pattern

```python
response = openai_client.responses.create(
    model=model_deployment,
    instructions="...",
    input=input_text,
    previous_response_id=last_response_id,
    tools=[
        {
            "type": "file_search",
            "vector_store_ids": [vector_store.id]
        },
        {
            "type": "web_search"
        }
    ]
)
```

The model chooses which tool to call based on the input. You don't call tools directly — you define them and let the model decide.

---

## Your notes

```

```

