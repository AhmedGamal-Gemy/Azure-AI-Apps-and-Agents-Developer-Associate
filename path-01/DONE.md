# Path 01 — Develop Generative AI Apps in Azure

_Hours: 6h 52m_  
_Modules: 6_  
_Branch: `path/01-generative-ai-apps`_

## Modules completed
- [x] Module 1 — Plan and prepare to develop AI solutions on Azure (Foundry portal, projects, resources, tools, quotas)
- [ ] Module 2 — Select, deploy, and evaluate Microsoft Foundry models
- [ ] Module 3 — Develop a generative AI chat app with Microsoft Foundry
- [ ] Module 4 — Develop generative AI apps that use tools
- [ ] Module 5 — Optimize generative AI model performance
- [ ] Module 6 — Implement a responsible generative AI solution

## 3 things I learned

1. **The Azure AI hierarchy and the three endpoints.** A Foundry project runs inside a resource, which runs inside an Azure subscription. To connect from a client app you need three different endpoints: the **key** (key-based auth — only for dev/testing), the **project endpoint** (for Foundry-native APIs like the Foundry Agent service, and OpenAI models via the Responses API), and the **OpenAI endpoint** (for OpenAI's own APIs like Chat Completions). Production should use **Microsoft Entra ID** auth, not keys.

2. **Foundry Tools is the multimodal AI toolkit.** Five services cover the full surface: **Azure Language** (NER, sentiment, summarization, CLU/QA), **Azure Speech** (TTS, STT, real-time live speech for agents), **Azure Translator** (text translation across many languages), **Azure Document Intelligence** (prebuilt + custom models for forms/invoices/receipts), and **Azure Content Understanding** (multimodal — images, video, audio, docs in one pipeline).

3. **Quota + budget is an exam trap.** Free trial blocks most model deployments with TPM limits. The fix is switching to **PAYG** (you get $200 credit, so it stays free-ish) and adding a **budget alert** for safety. **Critical distinction: budget is an ALERT, not a hard cap** — it won't stop spend. For the exam, know the difference between quota (blocks deployment), budget (sends alert), and pricing tier (controls available SKUs and rate limits).

## 1 question I still have

- **How do I actually set up Microsoft Entra ID authentication for a Foundry project end-to-end?** The module said it's the production path, but didn't walk through assigning roles (e.g., Cognitive Services User, Azure AI Developer) to a managed identity or service principal and then using DefaultAzureCredential in the SDK. I'd like a concrete example for the exam's plan-and-manage domain (10–15%).
