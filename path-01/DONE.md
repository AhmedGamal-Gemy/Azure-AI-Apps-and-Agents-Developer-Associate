# Path 01 — Develop Generative AI Apps in Azure

_Hours: 6h 52m_  
_Modules: 6_  
_Branch: `path/01-generative-ai-apps`_

## Modules completed
- [x] Module 1 — Plan and prepare to develop AI solutions on Azure (Foundry portal, projects, resources, tools, quotas)
- [x] Module 2 — Select, deploy, and evaluate Microsoft Foundry models
- [x] Module 3 — Develop a generative AI chat app with Microsoft Foundry
- [x] Module 4 — Develop generative AI apps that use tools
- [ ] Module 5 — Optimize generative AI model performance
- [ ] Module 6 — Implement a responsible generative AI solution

## 3 things I learned

1. **Four tools, two tiers.** `web_search` and `code_interpreter` need zero setup — just add the type to the tools list. `file_search` requires a vector store + uploaded files first. `function` needs a schema definition and a round-trip handler on your side. The model decides which tool to invoke based on the prompt — you don't call them directly.

2. **file_search = vector stores + files.** Create a vector store (`client.vector_stores.create`), upload files with `upload_and_poll`, then reference the store ID in the tool definition. I uploaded PDF brochures and the model answered questions from them automatically. The vector store persists across sessions.

3. **Reusing the Module 3 client setup.** I imported the OpenAI client from my previous lab (`03-generative-ai-chat-app.py`) instead of rewriting auth — saved a lot of boilerplate. The pattern: put shared setup in one file, import it in each lab exercise.

## 1 question I still have

- **How does the `function` tool round-trip actually work in the Responses API?** I understand the schema part, but once the model returns `function_call`, do I call `responses.create` again with `function_call_output`, or is there a different API for submitting the result back? The exercise spec had it but I didn't implement it — I want to be clear on the flow before the exam.
