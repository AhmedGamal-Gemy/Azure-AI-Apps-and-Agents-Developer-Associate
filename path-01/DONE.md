# Path 01 — Develop Generative AI Apps in Azure

_Hours: 6h 52m_  
_Modules: 6_  
_Branch: `path/01-generative-ai-apps`_

## Modules completed
- [x] Module 1 — Plan and prepare to develop AI solutions on Azure (Foundry portal, projects, resources, tools, quotas)
- [x] Module 2 — Select, deploy, and evaluate Microsoft Foundry models
- [ ] Module 3 — Develop a generative AI chat app with Microsoft Foundry
- [ ] Module 4 — Develop generative AI apps that use tools
- [ ] Module 5 — Optimize generative AI model performance
- [ ] Module 6 — Implement a responsible generative AI solution

## 3 things I learned

1. **Model benchmarks across four pillars.** Foundry gives you objective data to compare models by **quality** (BIG-Bench Hard, MMLU-Pro, MATH, HumanEval — normalized 0–1), **safety** (HarmBench ASR — lower is better for attack success, ToxiGen F1 — higher is better for hate speech detection, WMDP for dangerous knowledge awareness), **cost** (per 1M tokens, blended 3:1 input:output ratio), and **performance** (TTFT latency percentiles, GTPS/TTPS throughput). Scenario leaderboards let you filter by specific tasks like coding or groundedness.

2. **Three evaluation paradigms.** **Manual** covers subjective quality — interactive testing in the playground, structured human review (relevance, informativeness, engagement, accuracy, safety criteria), and user studies for real-world feedback. **AI-assisted metrics** use a GPT model to auto-rate groundedness, coherence, fluency, and safety dimensions (self-harm, hateful, violent, sexual, protected material, indirect attacks). **NLP metrics** like F1, BLEU, ROUGE give mathematical comparison against ground truth. You can bring your own dataset (JSONL/CSV), use existing data, or generate synthetic data.

3. **The evaluation flow drives iteration.** Run systematic assessments in the Foundry portal's **Build** tab → results tell you where to improve: prompt engineering, switching to a different model, adding RAG, or fine-tuning. There are specific evaluators for different scenarios (e.g., tool-calling evaluator for agent apps), and you can write custom evaluators. Low scores aren't failure — they tell you which lever to pull next.

## 1 question I still have

- **How do the deployment quota and content filter policies actually interact during deployment?** I know GlobalStandard gives the largest quota, but when I deploy I need to pick a content filter policy (Microsoft.DefaultV2, etc.), and I'm not sure how the policy selection affects throughput limits or which deployment types support custom content filters. Also, when would I pick DataZoneStandard vs GlobalStandard beyond data residency?
