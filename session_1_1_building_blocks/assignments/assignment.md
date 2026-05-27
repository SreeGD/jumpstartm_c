# Session 1.1 — Assignment

---

## Task 1 — Extend the Lab

Open `labs/logic_gates.py` and add two new gates:

**NAND gate** (NOT AND — outputs 0 only when BOTH inputs are 1):
```
NAND(0,0) → 1
NAND(1,0) → 1
NAND(1,1) → 0   ← only case that's 0
```

**NOR gate** (NOT OR — outputs 1 only when BOTH inputs are 0):
```
NOR(0,0) → 1   ← only case that's 1
NOR(1,0) → 0
NOR(1,1) → 0
```

Print their truth tables like Part 2 in the lab.

---

## Task 2 — Binary Conversion

Convert these numbers **without a calculator**:

| Decimal | Binary |
|---------|--------|
| 7       | ?      |
| 13      | ?      |
| 25      | ?      |

And convert these binary numbers to decimal:

| Binary  | Decimal |
|---------|---------|
| 1010    | ?       |
| 11001   | ?       |
| 100000  | ?       |

*Hint: Binary is base-2. Each position is a power of 2: 1, 2, 4, 8, 16, 32...*

---

## Task 3 — Research

Answer in 3–5 sentences:

1. **What is Moore's Law ending?** What physical limit are we hitting that stops transistors from getting smaller?

2. **What is a quantum computer?** How is it fundamentally different from a transistor-based computer?

3. **Why is NVIDIA worth $3 trillion?** Connect your answer to what you learned about GPUs in this session.

---

## Task 4 — Think

Sree described a CPU as LeBron James and a GPU as a soccer team.

Write your own analogy for CPU vs GPU using basketball or soccer.  
Be specific — describe a real game situation that maps to how they work differently.

---

## Bring to Next Session

- Extended `logic_gates.py` with NAND and NOR
- Binary conversion answers
- Your CPU vs GPU analogy
