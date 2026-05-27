# Session 1.1 — What's Actually Inside the Box
## Building Blocks: CPU → GPU

**Duration:** 2–3 hours  
**the teacher's prep:** Pull up a die shot of Apple M3 chip. Have the half-adder code ready.

---

## 🎯 Goal

By the end of this session, Student understands:
- How binary and transistors form the base of all computing
- How a CPU works: fetch, decode, execute
- Why GPUs exist and why they power AI
- How to simulate logic gates in Python (first real code!)

---

## 📖 the teacher's Narrative

### Hook
*"There are 19 billion transistors in an Apple M3 chip. Each one is 3 nanometres wide. A human hair is 80,000 nanometres wide. How is that even possible — and what does it actually DO?"*

---

### The Transistor — Everything Starts Here

A transistor is a switch. It has two states: ON (1) and OFF (0).  
That's it. That's the whole foundation.

Stack enough switches together and you can represent any number in binary.  
Stack enough numbers together and you can represent any instruction.  
Stack enough instructions together and you can run Instagram.

*"Every photo, every video, every AI response — it's all just transistors switching on and off, billions of times per second."*

**Binary — the language of switches:**

| Decimal | Binary |
|---------|--------|
| 0       | 0000   |
| 1       | 0001   |
| 2       | 0010   |
| 5       | 0101   |
| 10      | 1010   |

Ask Student: *"Why do computers use binary and not decimal?"*  
Answer: Because transistors have two states (on/off), not ten. Physics decided.

---

### Stacking Bits → Representing Any Instruction

The leap from "switches" to "running Instagram" is not magic. Walk Student through it step by step.

**One bit — two possibilities:**
```
0  →  off
1  →  on
```

**Two bits — four possibilities:**
```
00  01  10  11
 0   1   2   3
```

**Eight bits (1 byte) — 256 possibilities:**
```
0000 0000  →   0
0000 0001  →   1
0000 0010  →   2
   ...
1111 1111  →  255
```

Eight bits can encode every letter, digit, and punctuation mark (this is ASCII). But here's the key insight:

> **The CPU doesn't care that `0000 0010` means 2. It just sees a pattern. You can decide the pattern means anything.**

CPU designers call this an **instruction set**. They pick patterns and assign meanings:

```
0000 0001  →  ADD
0000 0010  →  SUBTRACT
0000 0011  →  LOAD from memory
0000 0100  →  STORE to memory
0000 0101  →  JUMP to line X
```

**Now stack more bits to add detail.** A real instruction isn't just "ADD" — it needs to say *which* numbers to add and *where* to put the result:

```
OPCODE      REGISTER 1   REGISTER 2   RESULT
0000 0001   0010         0011         0100
  ADD       reg 2        reg 3     → reg 4
```

Show Student this actual ARM instruction (the CPU inside every iPhone and Android):

```
1110 0000 1000 0001 0000 0000 0000 0010
```

Decoded:
```
1110        →  always execute
0000 1000   →  ADD
0001        →  destination: register 1
0000        →  first operand: register 0
0000 0010   →  second operand: register 2
```

**It says:** `register1 = register0 + register2`

32 switches. That is a complete instruction.

*"Every program ever written — Instagram, FIFA, GPT-4 — eventually becomes millions of these 32-bit patterns, executed one at a time, 3 billion times per second. The magic isn't in the bits. It's in the agreed meaning humans gave to each pattern when they designed the chip."*

---

### Logic Gates — Three Gates Rule Everything

Three logical operations underlie all computing:

- **AND** — both inputs must be 1 → output is 1
- **OR** — at least one input is 1 → output is 1  
- **NOT** — flip the input (0→1, 1→0)

*"Every decision your computer makes — every if/else in every app ever built — reduces to these three operations."*

Show the truth tables. Let Student verify a few rows mentally.

---

### From Gates to CPU

Chain logic gates together → arithmetic circuits (adders, subtractors)  
Chain arithmetic circuits → ALU (Arithmetic Logic Unit)  
Add control logic + registers + memory connections → CPU

**The fetch-decode-execute cycle:**
1. **Fetch** — Get the next instruction from memory
2. **Decode** — Figure out what it means
3. **Execute** — Do it (add these numbers, store this value, jump to this address)

A modern CPU does this billions of times per second (clock speed = GHz = billion cycles per second).

*Analogy:* A chef reading a recipe (fetch), understanding a step (decode), then chopping the onion (execute). A CPU chef does this 3 billion times a second.

---

### Memory Hierarchy

Not all memory is equal. Speed and cost trade off:

```
Registers     → Fastest, tiny (bytes)         — inside the CPU
Cache (L1/L2) → Very fast, small (MB)         — on the chip
RAM           → Fast, medium (GB)             — separate chips
SSD/HDD       → Slow, large (TB)              — your storage
```

*"When you open a file, it moves from SSD → RAM → Cache → CPU registers. Each step gets faster and smaller. The CPU only works on what's in registers."*

---

### CPU vs GPU — The Basketball Analogy

**CPU = One brilliant player**  
A CPU has 8–16 powerful cores. Each can handle any complex task. It's like LeBron — can do everything, adapts to any situation, incredibly capable.

**GPU = A full team running a play**  
A GPU has thousands of small cores (NVIDIA H100: 16,896 cores). Each is simple, but they all work in parallel. It's like 11 footballers executing a set play simultaneously.

*"Training an AI model means multiplying massive matrices — millions of numbers times millions of numbers, thousands of times. You need every player on the pitch doing their job at once. You need the GPU."*

Show: GPT-4 was trained on ~25,000 NVIDIA A100 GPUs running for months.  
Show: NVIDIA's market cap went from $300B to $3T between 2022 and 2024. That's the GPU bet paying off.

---

## ⚡ Wow Moment

Show the electron microscope image of an Apple M3 chip die shot.  
Each little square is a functional unit. The whole chip is smaller than your thumbnail.

Then show this: *"The COVID-19 virus is about 100 nanometres. The transistors on this chip are 3 nanometres. The chip has 19 billion of them."*

Let that land for a second.

Then: *"Let's build one. Not 19 billion. Just three."*

---

## 🔑 Key Concepts Checklist

- [ ] Transistor — a silicon on/off switch; the base unit of computing
- [ ] Binary — base-2 number system (only 0 and 1)
- [ ] Instruction set — agreed patterns of bits that mean specific operations (ADD, LOAD, JUMP...)
- [ ] Opcode — the part of an instruction that names the operation
- [ ] Logic gates — AND, OR, NOT — the three basic operations
- [ ] ALU — Arithmetic Logic Unit — the part of CPU that does math
- [ ] CPU — the brain; fetch-decode-execute cycle
- [ ] Clock speed — how many cycles per second (GHz)
- [ ] Memory hierarchy — registers → cache → RAM → storage
- [ ] GPU — thousands of simple parallel cores; built for matrix math
- [ ] Why AI needs GPUs — parallel matrix operations at scale

---

## Teaching Notes for Teacher

- Don't get lost in CPU microarchitecture. Keep it to: transistor → gate → ALU → CPU → done.
- The basketball/football analogy for CPU vs GPU always lands. Use it.
- The lab (logic gates in Python) is the student's first real Python code. Go slow. Explain every line.
- It's fine if he doesn't fully get binary arithmetic — the concept of "two states = on/off" is enough for now.

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** A transistor has two states. What are they, and why does this force computers to use binary rather than decimal?
- A) Hot and cold — binary maps to temperature readings in early hardware
- B) On (1) and off (0) — a switch with two states can only represent two values, so base-2 is the natural number system ✓
- C) Positive and negative — transistors use electrical polarity to encode digits
- D) Fast and slow — clock speed variations create binary timing signals

**Q2.** What is the output of an AND gate when one input is 1 and the other is 0? What about an OR gate with the same inputs? Explain what physical meaning these operations have in a circuit.

**Q3.** A 32-bit ARM instruction encodes several pieces of information in a single pattern. What is an "opcode" and what role does it play within that instruction?
- A) The opcode is the destination register — it says where the result should be stored
- B) The opcode is the portion of the instruction that identifies which operation to perform (e.g. ADD, LOAD, JUMP) ✓
- C) The opcode is a checksum that verifies the instruction wasn't corrupted in memory
- D) The opcode is the clock signal that triggers instruction execution

**Q4.** Describe the fetch-decode-execute cycle in your own words. Use a real-world analogy other than the chef one from the lesson.

**Q5.** Put the following memory types in order from fastest to slowest: RAM, SSD, CPU registers, L1 Cache.
- A) SSD → RAM → L1 Cache → CPU registers
- B) RAM → L1 Cache → CPU registers → SSD
- C) CPU registers → L1 Cache → RAM → SSD ✓
- D) L1 Cache → CPU registers → RAM → SSD

**Q6.** The session compares a CPU to LeBron James and a GPU to a football team running a set play. In one or two sentences, explain why training an AI model specifically requires a GPU rather than a very fast CPU.

**Q7.** How many unique values can be represented with 8 bits (1 byte)? Show your reasoning.
- A) 8
- B) 16
- C) 128
- D) 256 ✓

**Q8.** NVIDIA's market cap grew from roughly $300 billion to $3 trillion between 2022 and 2024. Connecting this to what you learned about CPUs and GPUs: what single insight explains why NVIDIA became so valuable so quickly?

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** B — A transistor is physically either conducting current (on = 1) or not (off = 0). Because it has exactly two states, binary is the only number system that maps directly to the hardware. Decimal would require ten distinct voltage levels per transistor — physically impractical.

**Q2.** AND gate output: 0 (both inputs must be 1 for the output to be 1). OR gate output: 1 (at least one input being 1 is enough). Physically, AND is like two switches in series — both must be closed for current to flow; OR is like two switches in parallel — either being closed completes the circuit.

**Q3.** B — The opcode is the sub-pattern of bits that the CPU's decoder reads to identify the operation. In the ARM example from the lesson, `0000 1000` decoded to ADD. Without the opcode, the CPU wouldn't know whether to add, store, jump, or do anything else.

**Q4.** Accept any clear analogy. Example: a waiter (fetch) reads a table's order from their notepad, figures out what the kitchen needs to prepare (decode), then calls the order through to the kitchen (execute). The CPU does this billions of times per second — the waiter does it for every dish of every meal.

**Q5.** C — Registers are inside the CPU itself and operate at CPU speed. L1 Cache is on the chip but slightly slower. RAM is a separate chip, accessed over a bus. SSDs are storage devices — orders of magnitude slower than any of the above.

**Q6.** Training AI involves multiplying enormous matrices — millions of numbers against millions of numbers, repeated thousands of times. A GPU has thousands of simple cores that do these multiplications simultaneously in parallel. A CPU's 8–16 powerful cores would have to do them sequentially, taking orders of magnitude longer.

**Q7.** D — 2⁸ = 256. Each additional bit doubles the number of possible patterns: 1 bit = 2, 2 bits = 4, 4 bits = 16, 8 bits = 256.

**Q8.** The explosive growth of AI (especially large language models and image generation) requires massive parallel matrix computation, which GPUs are purpose-built for. NVIDIA was already the dominant GPU manufacturer, so every AI lab in the world became a NVIDIA customer almost overnight. The AI boom was a GPU boom — and NVIDIA had a near-monopoly on the hardware.

---

## 📚 Research Materials

> 💡 **Start here:** Watch the "How a CPU Works" video by In One Lesson — it walks through fetch-decode-execute with clear visuals in under 25 minutes and makes everything in this session click.

### 🎬 Films & Documentaries

| Title | Year | What to Watch For |
|-------|------|-------------------|
| *Revolution OS* | 2001 | How open-source software grew from the same hardware foundations covered here; features real engineers discussing low-level computing |
| *General Magic* | 2018 | Fascinating portrait of early Silicon Valley engineers grappling with hardware miniaturisation — the human story behind Moore's Law |
| *iHuman* | 2019 | Norwegian documentary on AI's rise; good context for why GPUs became so important to the modern world |

### 📺 YouTube

| Video / Channel | Link | Why Watch |
|-----------------|------|-----------|
| "How a CPU Works" — In One Lesson | https://www.youtube.com/watch?v=cNN_tTXABUA | Best visual walkthrough of fetch-decode-execute for beginners |
| "How Do Computers Add Numbers?" — Branch Education | https://www.youtube.com/watch?v=VBDoT8o4q00 | Stunning 3D animation showing transistors → logic gates → adders |
| "How Does a GPU Work?" — Branch Education | https://www.youtube.com/watch?v=h9Z4oGN89MU | Explains GPU parallelism with clear visuals; directly extends the CPU vs GPU section |
| "Moore's Law Is Ending" — Real Engineering | https://www.youtube.com/watch?v=rtI5wRyHpTg | Why transistor shrinkage is hitting physical limits and what comes next |
| "The von Neumann Architecture" — Computerphile | *search "von Neumann architecture Computerphile"* | University of Nottingham professors explain the architecture that every modern computer is still based on |

### 📖 Books

| Title | Author | Level | Covers |
|-------|--------|-------|--------|
| *But How Do It Know?* | J. Clark Scott | Easy | How a simple computer is built from scratch — transistors to CPU, written for complete beginners |
| *Code: The Hidden Language of Computer Hardware and Software* | Charles Petzold | Easy–Medium | The gold-standard accessible book on how computers work; builds from Morse code to a working CPU |
| *The Elements of Computing Systems* (Nand to Tetris) | Nisan & Schocken | Medium | Hands-on: you build a working computer from NAND gates up; the companion to the free online course |
| *In the Plex* | Steven Levy | Easy | Inside Google's computing infrastructure; excellent context for why hardware choices matter at scale |
| *The Innovators* | Walter Isaacson | Easy | Narrative history of computing from Ada Lovelace through the internet; brings Gordon Moore, Jack Kilby, and others to life |

### 🌐 Articles & Interactive Resources

| Resource | URL | What It Covers |
|----------|-----|----------------|
| Nand to Tetris (free course) | https://www.nand2tetris.org | Build a computer from logic gates to a high-level language — the most hands-on complement to this session |
| "How Microchips Are Made" — Intel | https://www.intel.com/content/www/us/en/history/museum-transistor-to-transformation.html | Visual history of transistor manufacturing and Moore's Law |
| Visual Transistor Count History — Our World in Data | https://ourworldindata.org/moores-law | Interactive chart of transistor count per chip from 1970 to now |
| CPU Simulator — Visual 6502 | http://www.visual6502.org/JSSim/index.html | Interactive simulation of a real 6502 CPU — watch registers and logic gates change in real time |
| NVIDIA H100 Architecture White Paper | https://resources.nvidia.com/en-us-tensor-core | Official deep-dive on how modern GPU cores are organised; shows exactly why AI training needs thousands of them |

### 🔗 People to Look Up

- **Gordon Moore** — Co-founder of Intel; his 1965 paper predicting exponential transistor growth became "Moore's Law" and shaped the entire semiconductor industry.
- **Jack Kilby** — Texas Instruments engineer who invented the integrated circuit in 1958; shared the 2000 Nobel Prize in Physics for it.
- **John von Neumann** — Mathematician who formalised the stored-program computer architecture (fetch-decode-execute) that every modern CPU still follows.
- **Grace Hopper** — US Navy admiral and computer scientist; created the first compiler and championed the idea that programs could be written in human-readable language, not binary.
- **Jensen Huang** — CEO and co-founder of NVIDIA; made the strategic bet that GPUs would power AI, turning a gaming chip company into the world's most valuable semiconductor firm.
- **Sophie Wilson** — Designed the ARM instruction set (the ISA inside every smartphone); the 32-bit ARM instruction shown in this lesson is her architecture.
