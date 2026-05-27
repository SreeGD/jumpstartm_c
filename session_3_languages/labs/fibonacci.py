# Lab — Fibonacci in Python
# Session 3: Introduction to Programming Languages
#
# Student types this himself — his first standalone Python file.
# Teacher reads each line and explains it before Student types it.
#
# Run with: python fibonacci.py

# ─────────────────────────────────────────
# PART 1: Simple version — using a loop
# ─────────────────────────────────────────

def fibonacci_loop(n):
    """Return the first n Fibonacci numbers"""
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence[:n]

print("=== Fibonacci (loop) ===")
print(fibonacci_loop(10))
# → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ─────────────────────────────────────────
# PART 2: Recursive version
# A function that calls itself — like mathematical induction
# f(n) = f(n-1) + f(n-2)
# ─────────────────────────────────────────

def fibonacci_recursive(n):
    """Return the nth Fibonacci number (recursive)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print("\n=== Fibonacci (recursive) ===")
for i in range(10):
    print(f"f({i}) = {fibonacci_recursive(i)}")


# ─────────────────────────────────────────
# PART 3: The Golden Ratio connection
# Each Fibonacci number divided by the previous → approaches φ (phi)
# φ ≈ 1.618... — the golden ratio, appears everywhere in nature
# ─────────────────────────────────────────

sequence = fibonacci_loop(20)

print("\n=== The Golden Ratio ===")
print("Ratio of consecutive Fibonacci numbers:")
for i in range(1, len(sequence)):
    if sequence[i-1] != 0:
        ratio = sequence[i] / sequence[i-1]
        print(f"f({i})/f({i-1}) = {sequence[i]}/{sequence[i-1]} = {ratio:.6f}")

print(f"\nThe Golden Ratio φ ≈ 1.618033988...")
print("It appears in art, architecture, and nature.")


# ─────────────────────────────────────────
# SPORTS CONNECTION
# The Fibonacci sequence appears in basketball shot selection
# and optimal passing angles in football — here's a fun connection
# ─────────────────────────────────────────

print("\n=== Sports Connection ===")
print("Fibonacci numbers as squad numbers:")
fib_squad = [f for f in fibonacci_loop(15) if 1 <= f <= 99]
print(f"Valid squad numbers: {fib_squad}")
print("(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)")


# ─────────────────────────────────────────
# CHALLENGE
# ─────────────────────────────────────────

# 1. How many steps does fibonacci_recursive(30) take?
#    How does this compare to fibonacci_loop(30)?
#    Which is more efficient? What's the Big-O of each?
#    (This connects back to Session 2!)

# 2. Modify fibonacci_loop to also print each number
#    as we go, with a note if it's prime

# 3. Find the first Fibonacci number greater than 1,000,000
#    How many numbers in the sequence until we get there?
