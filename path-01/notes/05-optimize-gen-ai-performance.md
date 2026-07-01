# Module 5 — Optimize generative AI model performance with Microsoft Foundry

_Learning objectives:_
1. Apply prompt engineering techniques (system messages, few-shot, parameters)
2. Understand when and how to ground a model using RAG
3. Identify when fine-tuning improves behavioral consistency
4. Compare optimization strategies and when to combine them

---

## 1. Prompt Engineering

Three levers to tune model output without changing the model:

### System messages
- Set persona, tone, constraints, output format
- Evaluated on every call — cheapest optimization

### Few-shot learning
- Provide examples in the prompt (input → expected output)
- Works for format control and simple task definition
- Limited by context window size

### Model parameters
| Parameter | Effect |
|-----------|--------|
| `temperature` (0–2) | Lower = deterministic, Higher = creative |
| `top_p` | Nucleus sampling — alternative to temperature |
| `max_tokens` | Caps response length |
| `stop` sequences | Define when to stop generating |

---

## 2. RAG (Retrieval Augmented Generation)

Ground the model in your own data without retraining.

**Flow:** User query → search your data (vector/ keyword) → retrieve relevant chunks → inject into prompt → model answers from that context

| When to use RAG | When NOT to |
|-----------------|-------------|
| Need factual, up-to-date responses | Latency-critical (adds search time) |
| Large corpus you can't fit in a prompt | Model's training data already covers it |
| Data changes frequently | Simpler prompt engineering suffices |

---

## 3. Fine-tuning

Train a base model on your own examples for consistent behavior.

| Compare | Prompt Eng | RAG | Fine-tune |
|---------|-----------|-----|-----------|
| Cost | Near-zero | Moderate (vector search infra) | High (training compute) |
| Data needs | None | Domain docs | Labeled examples |
| Behavior change | Light | Factual grounding | Deep style/tone |
| Maintenance | Edit prompt | Update index | Retrain model |

**Rule of thumb:** Start with prompt engineering → add RAG if you need facts → fine-tune only if you need consistent behavioral patterns that prompting can't achieve.

---

## Your notes

```

```

