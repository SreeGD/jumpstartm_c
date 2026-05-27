# Session 2 — Assignment

---

## Task 1 — Binary Arithmetic by Hand

Convert **without a calculator**:

| Decimal | Binary |
|---------|--------|
| 19      | ?      |
| 37      | ?      |
| 128     | ?      |

| Binary   | Decimal |
|----------|---------|
| 10111    | ?       |
| 110010   | ?       |
| 1000000  | ?       |

**Bonus:** Add two binary numbers by hand: `1011 + 1101 = ?`  
*(Hint: same as decimal addition, but carry happens at 2 not 10)*

---

## Task 2 — Extend the Caesar Cipher

Open `labs/caesar_cipher.py` and answer the challenge questions:

1. Encrypt "ABCDEFGHIJKLMNOPQRSTUVWXYZ" with shift 13.  
   What do you notice? Why is ROT13 special?

2. What is the maximum number of unique Caesar cipher shifts?  
   Is this a secure encryption method? Why or why not?

3. Write a **brute force cracker** — try all possible shifts and print each decryption:
```python
def brute_force(ciphertext):
    for shift in range(26):
        print(f"Shift {shift:2d}: {decrypt(ciphertext, shift)}")
```
Use it on: `"ZNNNY ZF THBG"` — what's the message?

---

## Task 3 — Passing Network Experiment

Open `labs/passing_network.py`. Make these changes:

1. **Remove Xavi** from the passes list (delete all his entries).  
   Re-run. Who becomes most central now?  
   What does this tell you about team tactics?

2. **Add a new player** of your choice (any position) with at least 3 pass connections.  
   Re-run. Did centrality change?

3. Write 3 sentences: what does "centrality" tell a football manager that goals and assists don't?

---

## Task 4 — Big-O in Real Life

For each algorithm below, state whether it's O(1), O(log n), O(n), or O(n²):

1. Looking up a player's stat by their shirt number in an array (direct index lookup)
2. Searching for a player by name in an **unsorted** list of 10,000 players
3. Searching for a player by name in a **sorted** list using binary search
4. Comparing every player in a squad against every other player (all pairs)
5. Finding the highest scorer — scanning through a list once

---

## Bring to Next Session

- Binary arithmetic answers
- Brute-force cracker code (what was the hidden message?)
- Passing network experiment results + your 3 sentences
- Big-O answers
