# Lab — Caesar Cipher
# Session 2: Maths for Computing
#
# Concepts: ASCII values, modular arithmetic, loops, strings
#
# Instructions for Teacher:
#   Build Part 1 live. Let Student predict outputs.
#   Part 2 is the challenge — let him try it first.
#
# Instructions for Student:
#   Run each part. Understand what % (modulo) is doing.
#   Can you break the cipher without the key?

# ─────────────────────────────────────────
# BACKGROUND: ASCII and ord()
# ─────────────────────────────────────────
# Every character has a numeric code (ASCII)
# ord('A') = 65, ord('B') = 66, ... ord('Z') = 90
# chr(65) = 'A', chr(66) = 'B', etc.

print("=== ASCII Values ===")
print(f"ord('A') = {ord('A')}")
print(f"ord('Z') = {ord('Z')}")
print(f"chr(65)  = {chr(65)}")
print(f"chr(77)  = {chr(77)}")  # What letter is this?


# ─────────────────────────────────────────
# PART 1: Caesar Cipher
# Shift every letter by 'shift' positions
# ─────────────────────────────────────────

def encrypt(text, shift):
    """Encrypt a message by shifting each letter"""
    result = ""
    for char in text.upper():
        if char.isalpha():
            # Shift the letter, wrap around using modulo
            # (ord(char) - 65) converts A→0, B→1, ... Z→25
            # + shift moves it forward
            # % 26 wraps around (Z+1 → A)
            # + 65 converts back to ASCII
            shifted = (ord(char) - 65 + shift) % 26 + 65
            result += chr(shifted)
        else:
            result += char  # Keep spaces and punctuation
    return result

def decrypt(text, shift):
    """Decrypt by shifting backwards"""
    return encrypt(text, -shift)


# Test it
message = "MESSI IS GOAT"
shift = 3

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print(f"\n=== Caesar Cipher ===")
print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

# Send Teacher an encrypted message!
secret = encrypt("ADVAITH WILL ACE NITW", 7)
print(f"\nSecret message for Teacher: {secret}")
print("(Teacher decrypts it using shift=7)")


# ─────────────────────────────────────────
# PART 2: Frequency Analysis — Breaking the Cipher
# ─────────────────────────────────────────
# In English, 'E' is the most common letter (~13%)
# If you have a long encrypted message, the most
# common letter in the cipher is probably 'E'
# That tells you the shift!

def frequency_analysis(text):
    """Count how often each letter appears"""
    counts = {}
    for char in text.upper():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    # Sort by frequency, most common first
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)

# Encrypt a long text (use a sports quote)
long_text = """
THE BEST PLAYERS IN THE WORLD DONT WAIT FOR THE BALL THEY GO AND GET IT.
GREAT TEAMS MOVE THE BALL QUICKLY AND FIND THE OPEN PLAYER.
IN BASKETBALL THE BEST OFFENSE IS MOVING WITHOUT THE BALL.
"""

encrypted_long = encrypt(long_text, 11)
print("\n=== Frequency Analysis ===")
print(f"Encrypted text:\n{encrypted_long[:60]}...")

freq = frequency_analysis(encrypted_long)
print(f"\nMost common letters: {freq[:5]}")
most_common = freq[0][0]
# If 'E' is most common in English, and 'X' is most common here,
# then shift = ord('X') - ord('E') = 19
guessed_shift = (ord(most_common) - ord('E')) % 26
print(f"\nMost common letter in cipher: {most_common}")
print(f"Guessed shift: {guessed_shift}")
print(f"Decrypted guess:\n{decrypt(encrypted_long, guessed_shift)[:100]}")


# ─────────────────────────────────────────
# CHALLENGE for Student
# ─────────────────────────────────────────

# 1. Send Teacher an encrypted message using any shift you choose
#    (don't tell Teacher the shift — see if he can crack it)

# 2. Try encrypting "ABCDEFGHIJKLMNOPQRSTUVWXYZ" with shift=13
#    This special cipher is called ROT13 — why is it special?

# 3. What's the maximum number of shifts you'd need to try
#    to brute-force any Caesar cipher? Is this secure?
