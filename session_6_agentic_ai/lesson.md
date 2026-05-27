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

Google moved quickly. They acquired the AlexNet team for around $44 million, then bought DeepMind in 2014 for $500 million. DeepMind went on to build AlphaGo — the first AI to beat a world champion at Go, in 2016. Go has roughly 10^170 possible board positions, so brute-force search is impossible. AlphaGo used reinforcement learning combined with neural networks to develop intuition. It was a watershed moment. DeepMind then turned that same approach to biology: AlphaFold solved protein folding in 2020 — a problem that had stumped scientists for 50 years. Google's latest frontier model, Gemini, is their direct competitor to ChatGPT.

**2017: "Attention Is All You Need"**  
Google researchers publish the Transformer architecture. Two key ideas:
1. **Attention mechanism** — the model learns which parts of the input to focus on for each output
2. **Parallel training** — unlike previous sequence models, Transformers train in parallel → can use GPUs → can scale

*"Before Transformers, 'Read this paragraph and answer a question' was hard for AI. After Transformers, it became the baseline."*

**2020–2022: GPT-3, ChatGPT**  
Scale the Transformer with billions of parameters and train on the entire internet.  
The emergent behaviour is shocking — the model can write code, explain concepts, do math, translate languages — without being explicitly trained on any of those tasks.  
ChatGPT: 1 million users in 5 days. 100 million in 2 months. Fastest product adoption in history.

**Microsoft's $10 billion bet**  
In January 2023, Microsoft invested $10 billion in OpenAI — the company behind ChatGPT. They integrated GPT-4 into Bing, Office, and Windows. More importantly, they launched **GitHub Copilot** — an AI that writes code alongside you, trained on billions of lines of code from GitHub (which Microsoft acquired in 2018 for $7.5B). Within a year, over 1 million developers were using Copilot daily. It is the first mass-market AI tool that directly replaces a part of a software engineer's job.

*"Microsoft was written off in 2013. By 2024, they were the most valuable company in the world again — because of this bet."*

While Microsoft and OpenAI were building behind closed doors, Meta took the opposite approach. In 2023 they released LLaMA — Large Language Model Meta AI — as open-source. Unlike GPT-4, anyone could download and run it. That single decision changed the pace of the whole field: startups, researchers, and students gained access to a foundation model on par with what only the biggest labs had previously. LLaMA is why AI moved so fast in 2023 and 2024 — dozens of new models were built on top of it almost immediately.

Anthropic came from a different direction. Founded in 2021 by Dario Amodei and others who left OpenAI, they focused on AI safety from the start. They developed Constitutional AI — a training approach designed to make models helpful, harmless, and honest. Their model is Claude. The one running in the lab today.

**2024–2025: Agents**  
What makes a **chatbot**: ask a question → get an answer. One turn. Passive.  
What makes an **agent**: given a goal → plan → use tools → take actions → verify → iterate.

The four components of an agent:
1. **Reasoning** — thinks through a problem step by step
2. **Memory** — remembers context, previous steps, past interactions
3. **Tools** — can call external functions (search web, run code, query database)
4. **Action** — can take actions in the world (send email, book calendar, write file)

*"The transition from chatbot to agent is the same as the transition from a calculator to a programmer. One answers questions. The other gets things done."*

The earliest mass-market attempt at a voice AI agent was Amazon's Alexa, launched in 2014. It could answer questions, set timers, control smart home devices — each of those was an action triggered by language. The limitations were obvious: it couldn't reason across multiple steps and had no real memory of who you were. Today Amazon provides access to dozens of frontier models through AWS Bedrock, and AWS itself hosts a large share of the infrastructure that all AI companies run on. The shift from Alexa to today's agents is the shift from a scripted response system to genuine multi-step reasoning.

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

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** What was the key technological innovation in the 2017 "Attention Is All You Need" paper?
- A) A faster way to train decision trees
- B) The Transformer architecture, which uses attention and trains in parallel ✓
- C) A new programming language for AI
- D) The first neural network to beat humans at chess

**Q2.** What is the difference between a chatbot and an AI agent?
- A) Chatbots are smarter than agents
- B) A chatbot answers one question at a time; an agent can plan, use tools, take actions, and iterate toward a goal ✓
- C) Agents only work for coding tasks
- D) There is no meaningful difference — they are the same thing

**Q3.** In the Claude API call from the session, what is the purpose of the `system` parameter?
- A) It tells the model which programming language to use
- B) It sets the maximum number of tokens
- C) It defines the AI's persona, role, and instructions ✓
- D) It stores the conversation history

**Q4.** In the sports analyst demo, why was the agent able to answer "Compare him to Zidane at the same age" without you saying who "him" was?

**Q5.** Why did rule-based AI (1950s–1980s) fail for complex real-world problems, even though it worked well for games like chess?

**Q6.** What was the "emergent behaviour" that surprised researchers when GPT-3 was scaled up with billions of parameters?
- A) It became much faster at running chess algorithms
- B) It learned to translate languages
- C) It could write code, explain concepts, do math, and translate — without being explicitly trained on those tasks ✓
- D) It could only write poetry

**Q7.** Name the four components that make an AI system an "agent" rather than a simple chatbot.

**Q8 (explain in your own words).** If you were designing an AI agent for a football club's scouting department, what four capabilities (aligned to the agent components from this session) would it need, and what would each one do?

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** B — The Transformer introduced the attention mechanism (allowing the model to learn which parts of input to focus on) and parallel training (enabling use of GPUs at scale), which is why it could be scaled to billions of parameters.

**Q2.** B — A chatbot is passive and stateless — one question, one answer. An agent is goal-directed: it reasons through a problem, uses external tools, takes actions in the world, and verifies results over multiple steps.

**Q3.** C — The system prompt is the personality and instruction dial. Changing it from "sports analyst" to "harsh critic" gives a completely different response to the same question, even though the model is identical.

**Q4.** The `messages` array stores the full conversation history. The agent can read back all previous turns and knows "him" refers to Bellingham, who was mentioned in the first message.

**Q5.** The real world has too many edge cases to hand-code. Chess has a defined set of rules and states; real-world language, images, and situations have near-infinite variation. No team of programmers can write enough if/then rules to cover it all.

**Q6.** C — When models were scaled to hundreds of billions of parameters, capabilities appeared that nobody designed for — including code writing, mathematical reasoning, and translation. This is called emergent behaviour.

**Q7.** The four components of an agent are: (1) Reasoning — thinks through a problem step by step; (2) Memory — stores context and past interactions; (3) Tools — can call external functions like web search or database queries; (4) Action — can take actions in the world such as sending emails or writing files.

**Q8.** Model answer: Reasoning — the agent analyses a player's stats and explains why they fit or don't fit the team's tactical system. Memory — it remembers which players were previously scouted and what was noted about them. Tools — it can query a stats database (like StatsBomb or Opta) or search for recent match footage. Action — it can draft a scouting report, add a player to a shortlist, or schedule a viewing trip on the coach's calendar.

---

## 📚 Research Materials

> 💡 **Start here:** Watch Andrej Karpathy's "Intro to Large Language Models" on YouTube — it is the clearest 1-hour explanation of how LLMs actually work, suitable for anyone who has done this session.

### 🎬 Films & Documentaries

| Title | Year | What to watch for |
|---|---|---|
| [iHuman](https://www.imdb.com/title/tt9271672/) | 2019 | Norwegian documentary; covers AI surveillance, data power, and the social consequences of machine intelligence |
| [AlphaGo](https://www.alphagodocumentary.com/) | 2017 | DeepMind's AlphaGo beats world champion Lee Sedol — a pivotal moment showing AI surpassing human expertise |
| [The Social Dilemma](https://www.thesocialdilemma.com/) | 2020 | Former tech insiders explain how recommendation algorithms (a form of agentic AI) shape behaviour at scale |
| [Ex Machina](https://www.imdb.com/title/tt0470752/) | 2014 | Fiction, but a thought-provoking exploration of what it means for an AI to reason, deceive, and act autonomously |

### 📺 YouTube

| Channel | Video | Link |
|---|---|---|
| Andrej Karpathy | Intro to Large Language Models | [youtube.com/watch?v=zjkBMFhNj_g](https://www.youtube.com/watch?v=zjkBMFhNj_g) |
| 3Blue1Brown | But what is a GPT? Visual intro to transformers | [youtube.com/watch?v=wjZofJX0v4M](https://www.youtube.com/watch?v=wjZofJX0v4M) |
| Andrej Karpathy | Let's build GPT: from scratch, in code, spelled out | [youtube.com/watch?v=kCc8FmEb1nY](https://www.youtube.com/watch?v=kCc8FmEb1nY) |
| Two Minute Papers | GPT-4 & Large Language Models Explained | *search "Two Minute Papers GPT-4 explained"* |
| Anthropic | Claude and Constitutional AI — Building Safe AI Systems | *search "Anthropic Claude Constitutional AI YouTube"* |
| AI Explained | How AI Agents Work (AutoGPT, LangChain, and beyond) | *search "AI Explained agents AutoGPT LangChain"* |

### 📖 Books

| Title | Author | Level | What it covers | Free |
|---|---|---|---|---|
| *The Alignment Problem* | Brian Christian | Easy | How AI systems learn human values (and fail to) — readable narrative for non-specialists | — |
| *Human Compatible* | Stuart Russell | Medium | Berkeley AI professor argues the current approach to AI is dangerous and proposes a new paradigm | — |
| *Attention Is All You Need* (paper) | Vaswani et al. | Medium | The original 2017 transformer paper — surprisingly readable; the foundation of every modern LLM | [Free →](https://arxiv.org/abs/1706.03762) |
| *Deep Learning* | Goodfellow, Bengio & Courville | Hard | The standard graduate-level textbook; free online at deeplearningbook.org | [Free →](http://deeplearningbook.org) |
| *The Coming Wave* | Mustafa Suleyman | Easy | Co-founder of DeepMind on why the AI wave is different from any previous technology shift | — |

### 🌐 Articles & Interactive Resources

| Resource | Link | What it covers |
|---|---|---|
| The Illustrated Transformer (Jay Alammar) | [jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/) | The best visual walkthrough of how attention and transformers work — no maths required |
| Anthropic's Claude API Docs | [docs.anthropic.com](https://docs.anthropic.com) | Official documentation; includes prompt engineering guide and API quickstart |
| OpenAI Prompt Engineering Guide | [platform.openai.com/docs/guides/prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering) | Official best practices for writing effective prompts |
| LangChain Documentation | [python.langchain.com](https://python.langchain.com) | The most widely used framework for building agentic LLM workflows |
| Hugging Face Course | [huggingface.co/learn/nlp-course](https://huggingface.co/learn/nlp-course/chapter1/1) | Free hands-on course covering transformers, tokenisation, and fine-tuning |

### 🔗 People to Look Up

- **Geoffrey Hinton** — "Godfather of deep learning"; won the 2024 Nobel Prize in Physics for his work on neural networks; recently left Google to speak freely about AI risks
- **Ilya Sutskever** — Co-founder of OpenAI and key architect of GPT; later founded Safe Superintelligence (SSI)
- **Andrej Karpathy** — Former Tesla AI Director and OpenAI researcher; his YouTube lectures are the gold standard for understanding LLMs from first principles
- **Sam Altman** — CEO of OpenAI; central figure in the commercialisation of large language models and the ChatGPT era
- **Demis Hassabis** — Co-founder and CEO of Google DeepMind; built AlphaGo, AlphaFold, and Gemini; 2024 Nobel Prize in Chemistry co-winner
- **Yann LeCun** — Chief AI Scientist at Meta; pioneer of convolutional neural networks; a prominent sceptic of current LLM approaches to AGI
