# Session 6 — The Thing That Changes Everything
## General Introduction to Agentic AI

**Duration:** 2–3 hours  
**the teacher's prep:** Anthropic API key ready. `pip install anthropic` done. Live demo of Claude/GPT agent prepared.

---

## 🎯 Goal

By the end of this session, Student understands:
- The arc from rule-based AI → ML → deep learning → LLMs → Agents
- What a Transformer is (conceptually)
- What makes an AI "agentic"
- How to call a real AI API from Python
- How to build a simple sports analyst agent

---

## 📖 the teacher's Narrative

### Hook

Live demo first. Before any explanation:

Open a terminal. Run a simple Claude API call:
```python
# Teacher runs this live, unexplained
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=300,
    messages=[{"role": "user", "content": 
               "Analyse Vinícius Jr's 2023/24 season in 3 sharp sentences."}]
)
print(response.content[0].text)
```

Let Student read the response. Then: *"That was 8 lines of Python calling an AI that understands football, statistics, and context. Let's understand how we got here."*

---

### The Arc — 70 Years in 20 Minutes

**1950s–1980s: Rule-Based AI**  
"If the player is in the penalty area AND the ball is in the air THEN head it."  
Programmers wrote every rule by hand. It worked for simple games (chess engines in 1997). Failed for anything messy and real. The world is too complicated to hand-code.

**1990s–2000s: Statistical Machine Learning**  
Instead of writing rules, feed the computer thousands of examples. It finds the patterns.  
Decision trees, support vector machines, random forests. Spam filters, credit scoring, early recommendation engines. Better — but limited by feature engineering (humans still deciding what to look at).

**2012: The Deep Learning Moment**  
AlexNet wins ImageNet by a huge margin using a Convolutional Neural Network. The model learns its own features — nobody told it what edges and shapes to look for. It figured it out from millions of images.  
*"The shift: humans stopped designing features. Models learned to design their own."*

**2017: "Attention Is All You Need"**  
Google researchers publish the Transformer architecture. Two key ideas:
1. **Attention mechanism** — the model learns which parts of the input to focus on for each output
2. **Parallel training** — unlike previous sequence models, Transformers train in parallel → can use GPUs → can scale

*"Before Transformers, 'Read this paragraph and answer a question' was hard for AI. After Transformers, it became the baseline."*

**2020–2022: GPT-3, ChatGPT**  
Scale the Transformer with billions of parameters and train on the entire internet.  
The emergent behaviour is shocking — the model can write code, explain concepts, do math, translate languages — without being explicitly trained on any of those tasks.  
ChatGPT: 1 million users in 5 days. 100 million in 2 months. Fastest product adoption in history.

**2024–2025: Agents**  
What makes a **chatbot**: ask a question → get an answer. One turn. Passive.  
What makes an **agent**: given a goal → plan → use tools → take actions → verify → iterate.

The four components of an agent:
1. **Reasoning** — thinks through a problem step by step
2. **Memory** — remembers context, previous steps, past interactions
3. **Tools** — can call external functions (search web, run code, query database)
4. **Action** — can take actions in the world (send email, book calendar, write file)

*"The transition from chatbot to agent is the same as the transition from a calculator to a programmer. One answers questions. The other gets things done."*

---

### How the API Works

Show the anatomy of a Claude API call:

```python
client.messages.create(
    model="claude-opus-4-7",      # Which model
    max_tokens=500,               # Maximum length of response
    system="You are...",          # The persona/instructions
    messages=[                    # The conversation so far
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."},  # Previous responses
        {"role": "user", "content": "..."},       # Latest message
    ]
)
```

*"The system prompt is the personality dial. The messages array is the memory. The model is the brain. That's the whole architecture."*

Show: change the system prompt from "sports analyst" to "harsh critic" to "tactical coach" — same question, completely different voice. The model is the same. The instructions changed.

---

## ⚡ Wow Moment

Show Student a multi-turn conversation with the sports analyst agent:
1. *"Analyse Bellingham's season"*
2. *"Compare him to Zidane at the same age"* (agent has memory — knows who "him" is)
3. *"What tactical system would get the best out of him?"*
4. *"Write a 3-tweet thread summarising this analysis"*

The agent maintains context across all four turns. It reasons, recalls, and adapts. That's agency.

Then: *"You're going to build this in 15 minutes."*

---

## 🔑 Key Concepts Checklist

- [ ] Rule-based AI — explicit if/then rules; brittle, doesn't scale
- [ ] Machine learning — learns patterns from examples
- [ ] Deep learning — learns its own features, not designed by humans
- [ ] Neural network — layers of matrix multiplications + activation functions
- [ ] Transformer — architecture that uses attention; basis of all modern LLMs
- [ ] Attention mechanism — model learns what to focus on for each output token
- [ ] LLM — Large Language Model; trained on massive text data
- [ ] System prompt — defines the AI's persona and instructions
- [ ] Agent — AI that reasons, uses tools, takes actions
- [ ] API — how your Python code talks to the AI model

---

## Teaching Notes for Teacher

- Start with the live demo — create the "wow" before the explanation. Don't explain first.
- The history section should feel like a story, not a lecture. Use the AI winter and the 2012 moment as dramatic beats.
- The system prompt experiment (changing persona) is essential. Student needs to feel the power of that dial.
- Keep the lab simple — 10-15 lines. The magic is in understanding what each line does, not in complexity.
- Best question: *"If you were building an AI agent for a football club, what would you have it do?"* — let him dream. Then show him he's 80% of the way to building it.
