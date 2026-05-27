# Lab 2 — The Guessing Game
# Session 4: Loops, Conditionals, User Input
#
# Concepts: while loops, if/elif/else, input(), random, functions
# Run: python lab2_guessing_game.py

import random

# ─────────────────────────────────────────
# PART 1: Basic Guessing Game
# ─────────────────────────────────────────

def play_game(max_number=100):
    """
    The computer picks a secret number.
    Player has to guess it.
    """
    secret = random.randint(1, max_number)
    attempts = 0
    max_attempts = 10

    print(f"\n=== Guess the Number! (1 to {max_number}) ===")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        # Get player's guess
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Please enter a number!")
            continue

        attempts += 1

        # Check the guess
        if guess < secret:
            print("Too low! 📉")
        elif guess > secret:
            print("Too high! 📈")
        else:
            print(f"\n🎉 Correct! The number was {secret}.")
            print(f"You got it in {attempts} attempt(s)!")
            return attempts

    print(f"\n💀 Game over! The number was {secret}.")
    return attempts


# ─────────────────────────────────────────
# PART 2: Binary Search Strategy
# Always guess the MIDDLE of the remaining range
# This is O(log n) — guaranteed to find any number
# in at most log₂(n) guesses
# ─────────────────────────────────────────

def binary_search_strategy(secret, max_number=100):
    """
    Demonstrate that binary search always wins.
    Teacher runs this, Student watches the strategy.
    """
    low = 1
    high = max_number
    attempts = 0

    print(f"\n=== Binary Search Demo (secret = {secret}) ===")
    print(f"Always guess the middle of the remaining range.\n")

    while low <= high:
        mid = (low + high) // 2
        attempts += 1
        print(f"Attempt {attempts}: Range [{low}, {high}] → Guess {mid}")

        if mid == secret:
            print(f"\n✅ Found {secret} in {attempts} attempts!")
            print(f"log₂({max_number}) ≈ {__import__('math').log2(max_number):.1f}")
            print("Binary search needs at most ⌈log₂(n)⌉ guesses.")
            return attempts
        elif mid < secret:
            low = mid + 1
            print(f"   Too low — eliminate lower half")
        else:
            high = mid - 1
            print(f"   Too high — eliminate upper half")

    return attempts


# ─────────────────────────────────────────
# PART 3: Play the game!
# Then watch the optimal strategy
# ─────────────────────────────────────────

print("First, YOU play:")
play_game(100)

secret = random.randint(1, 100)
print(f"\nNow watch the optimal strategy (secret is {secret}):")
binary_search_strategy(secret, 100)

print("\n" + "="*50)
print("KEY INSIGHT:")
print(f"1,000 numbers → at most {__import__('math').ceil(__import__('math').log2(1000))} guesses")
print(f"1,000,000 numbers → at most {__import__('math').ceil(__import__('math').log2(1000000))} guesses")
print(f"1,000,000,000 numbers → at most {__import__('math').ceil(__import__('math').log2(1000000000))} guesses")
print("\nThat's O(log n). Doubling the input adds just ONE more guess.")
print("This is why sorted data + binary search is so powerful.")


# ─────────────────────────────────────────
# CHALLENGE
# ─────────────────────────────────────────
# 1. Change the game to 1–1000. How many guesses does binary search need?
# 2. Add a "hard mode" where the secret number changes if you're close!
#    (Each time you guess within 10, the secret moves by a random amount)
# 3. Track all of a player's guesses and tell them their average attempts
#    over 5 games. Are they improving?
