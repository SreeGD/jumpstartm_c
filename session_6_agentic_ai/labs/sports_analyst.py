# Lab — Sports Analyst AI Agent
# Session 6: Agentic AI
#
# Prerequisites: pip install anthropic
# Get an API key: https://console.anthropic.com
# Set environment variable: export ANTHROPIC_API_KEY=your_key_here
#
# Run: python sports_analyst.py

import anthropic
import os

# ─────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────

client = anthropic.Anthropic()
# Note: Anthropic() automatically reads ANTHROPIC_API_KEY from environment


# ─────────────────────────────────────────
# PART 1: Simple One-Shot Analysis
# Ask once, get an answer
# ─────────────────────────────────────────

def analyse_player(player_name: str) -> str:
    """Ask the AI to analyse a player"""
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=400,
        system="""You are a sharp, opinionated football and basketball analyst.
        When asked about a player, give exactly 3 things:
        1. Their biggest strength (with a specific stat or moment)
        2. Their biggest weakness (be honest)
        3. One bold, controversial opinion about them
        Be concise. Be specific. No waffle.""",
        messages=[
            {"role": "user", "content": f"Analyse {player_name}"}
        ]
    )
    return response.content[0].text


print("=== One-Shot Player Analysis ===")
print(analyse_player("Vinícius Jr"))
print("\n" + "─"*50 + "\n")
print(analyse_player("Luka Doncic"))


# ─────────────────────────────────────────
# PART 2: Change the Persona
# Same model, different system prompt = different voice
# ─────────────────────────────────────────

def analyse_with_persona(player_name: str, persona: str) -> str:
    """Same question, different analyst persona"""
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=300,
        system=persona,
        messages=[
            {"role": "user", "content": f"Give me your take on {player_name}"}
        ]
    )
    return response.content[0].text


personas = {
    "Harsh Critic": "You are an extremely harsh football critic. You see through hype. Nothing impresses you. Be blunt.",
    "Fanboy": "You are an enormous fan of this player. You see only the positive. Use lots of emojis. Be enthusiastic.",
    "Tactical Coach": "You are a tactical analyst. You think only in systems, formations, and positional roles. Use technical terms.",
}

player = "Jude Bellingham"
print(f"\n=== Same player ({player}), different analyst ===\n")

for persona_name, persona_prompt in personas.items():
    print(f"🎭 {persona_name}:")
    print(analyse_with_persona(player, persona_prompt))
    print()


# ─────────────────────────────────────────
# PART 3: Multi-Turn Conversation (Memory)
# The agent remembers the whole conversation
# ─────────────────────────────────────────

def chat_with_analyst():
    """
    An interactive sports analyst.
    Type your questions, type 'quit' to exit.
    The analyst remembers everything in the conversation.
    """
    print("\n=== Sports Analyst Chat ===")
    print("Ask anything about football or basketball.")
    print("The analyst remembers your previous questions.")
    print("Type 'quit' to exit.\n")

    conversation_history = []  # This IS the agent's memory

    system = """You are a world-class sports analyst with deep knowledge of
    football and basketball. You are direct, insightful, and occasionally
    controversial. Reference specific games, stats, and moments.
    Keep answers under 150 words unless asked for more detail."""

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Analyst: See you at the next match. ⚽🏀")
            break
        if not user_input:
            continue

        # Add the user's message to conversation history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Call the API with the full conversation history
        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=300,
            system=system,
            messages=conversation_history  # Send ALL previous messages
        )

        analyst_reply = response.content[0].text

        # Add the analyst's reply to history too (for next turn's context)
        conversation_history.append({
            "role": "assistant",
            "content": analyst_reply
        })

        print(f"\nAnalyst: {analyst_reply}\n")


# ─────────────────────────────────────────
# RUN THE INTERACTIVE CHAT
# ─────────────────────────────────────────

# Uncomment to run the chat:
# chat_with_analyst()

# Or run a scripted demo:
print("\n=== Scripted Multi-Turn Demo ===")
print("Showing how the agent remembers context...\n")

history = []
system = "You are a concise sports analyst. Reference prior context in your answers."

questions = [
    "Analyse Pedri's season",
    "Compare him to Iniesta at the same age",  # 'him' = Pedri — agent must remember
    "What position would best suit his style?",  # 'his' = Pedri — still remembers
]

for q in questions:
    print(f"User: {q}")
    history.append({"role": "user", "content": q})

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=200,
        system=system,
        messages=history
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    print(f"Analyst: {reply}\n")


# ─────────────────────────────────────────
# CHALLENGE
# ─────────────────────────────────────────
# 1. Add a "debate mode" — give two players, analyst argues for one
#
# 2. Add a "predict the score" feature — give a match (e.g., "Man City vs Arsenal"),
#    analyst gives a reasoned prediction
#
# 3. Connect to your Session 4 stats data — feed the analyst actual numbers
#    from your top_scorers.py and ask it to explain what the data means
