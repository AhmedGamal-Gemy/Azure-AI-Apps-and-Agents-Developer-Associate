# Path 01 — Develop Generative AI Apps in Azure

_Hours: 6h 52m_  
_Modules: 6_  
_Branch: `path/01-generative-ai-apps`_

## Modules completed
- [x] Module 1 — Plan and prepare to develop AI solutions on Azure (Foundry portal, projects, resources, tools, quotas)
- [x] Module 2 — Select, deploy, and evaluate Microsoft Foundry models
- [x] Module 3 — Develop a generative AI chat app with Microsoft Foundry
- [ ] Module 4 — Develop generative AI apps that use tools
- [ ] Module 5 — Optimize generative AI model performance
- [ ] Module 6 — Implement a responsible generative AI solution

## 3 things I learned

1. **Two SDKs, different jobs — and you can use both.** The **Foundry SDK** (AIProjectClient) gives you project-level features: agents, evaluations, tracing, dataset management, and Foundry direct models. The **OpenAI SDK** (OpenAI client) gives you maximum compatibility and portability. For chat apps you use the OpenAI SDK either way — the Foundry SDK's chat client is actually derived from the OpenAI SDK via `get_openai_client()`. You can mix both in one app: Foundry SDK for project stuff, OpenAI SDK for model inference.

2. **Three authentication patterns.** **API keys** — simplest but dangerous, should be in Azure Key Vault, not in code. **Environment variables** — `OPENAI_BASE_URL` + `OPENAI_API_KEY` gives you zero-config `OpenAI()`. **Microsoft Entra ID** — production path, using `DefaultAzureCredential` with a `get_bearer_token_provider`. The token provider pattern (`get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")`) works across both Foundry SDK and OpenAI SDK auth.

3. **Responses API is the new path, but manual chaining gives control.** The Responses API is stateful — it maintains conversation context across turns, works with Foundry direct models, and is Microsoft's recommended path for new development. ChatCompletions is still valid for portability. The lab exercise showed manual conversation chaining: build a `conversation_history` list, append assistant responses with `response.output`, and pass it all back on each turn. This gives you full control over what stays in context vs. what gets pruned for token limits.

## 1 question I still have

- **Is the Responses API stateful at the Azure side or stateless-client-side?** From the lab it looks like I'm still manually passing `conversation_history` — so the "stateful" claim seems to mean the API response format includes output items that I can thread back, not that there's a server-side session. Does the Responses API actually persist state somewhere, or is it just a differently shaped input/output format compared to ChatCompletions?
