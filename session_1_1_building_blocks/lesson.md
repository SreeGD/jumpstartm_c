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
