# Lab — Logic Gates in Python
# Session 1.1: Building Blocks
#
# Instructions for Sree:
#   Type this live. Explain each line as you go.
#   Let Advaith predict the output before running each section.
#
# Instructions for Advaith:
#   Run each section. Try changing the inputs.
#   Can you predict the output before running?

# ─────────────────────────────────────────
# PART 1: The Three Basic Gates
# ─────────────────────────────────────────

def AND(a, b):
    """Both inputs must be 1 for output to be 1"""
    return a and b

def OR(a, b):
    """At least one input must be 1 for output to be 1"""
    return a or b

def NOT(a):
    """Flips the input: 0 becomes 1, 1 becomes 0"""
    return not a


# Test them — predict the output before running!
print("=== AND Gate ===")
print(AND(1, 1))   # → True
print(AND(1, 0))   # → False
print(AND(0, 0))   # → False

print("\n=== OR Gate ===")
print(OR(1, 0))    # → True
print(OR(0, 0))    # → False

print("\n=== NOT Gate ===")
print(NOT(1))      # → False
print(NOT(0))      # → True


# ─────────────────────────────────────────
# PART 2: Truth Tables
# Print ALL combinations for AND and OR
# ─────────────────────────────────────────

print("\n=== AND Truth Table ===")
print("A | B | A AND B")
print("--|---|--------")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} | {b} | {int(AND(a, b))}")

print("\n=== OR Truth Table ===")
print("A | B | A OR B")
print("--|---|-------")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} | {b} | {int(OR(a, b))}")


# ─────────────────────────────────────────
# PART 3: Combine Gates — Build XOR
# XOR = "one OR the other but NOT both"
# This is used in encryption and binary addition
# ─────────────────────────────────────────

def XOR(a, b):
    """True when inputs are DIFFERENT"""
    return OR(AND(a, NOT(b)), AND(NOT(a), b))

print("\n=== XOR Gate ===")
print("A | B | A XOR B")
print("--|---|--------")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} | {b} | {int(XOR(a, b))}")

# Notice: XOR(1,1) = 0. Different from OR.
# Sree: "XOR is the key gate in binary addition."


# ─────────────────────────────────────────
# CHALLENGE: Can Advaith extend this?
# ─────────────────────────────────────────

# Try building NAND (NOT AND) — used in actual chip design
# def NAND(a, b):
#     return NOT(AND(a, b))

# Try building NOR (NOT OR)
# def NOR(a, b):
#     return NOT(OR(a, b))
