# ============================================================
#   CodeAlpha Python Internship | Task 4: Chatbot
#   NeoBot — Rule-Based Chatbot Mini Project
#   Run: python chatbot.py
#   Requirements: pip install colorama
# ============================================================

import time
import random
from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)  # Initialize colorama for Windows support

# ── COLOR SHORTCUTS ──────────────────────────────────────────
C  = Fore.CYAN
G  = Fore.GREEN
Y  = Fore.YELLOW
R  = Fore.RED
M  = Fore.MAGENTA
W  = Fore.WHITE
D  = Fore.WHITE + Style.DIM
B  = Style.BRIGHT
RS = Style.RESET_ALL

# ── KNOWLEDGE BASE ───────────────────────────────────────────
# Each key = list of trigger words, value = list of replies (random pick)

RESPONSES = {
    # Greetings
    ("hello", "hi", "hey", "hii", "helo", "sup", "yo"): [
        "Hey there! 👋 Great to see you. What's on your mind?",
        "Hello! NeoBot online and ready. How can I help?",
        "Hi! Hope you're having a great day 😊"
    ],

    # How are you
    ("how are you", "how r u", "how are u", "hows you", "how do you do"): [
        "I'm just a bot, but I'm feeling great! 🤖 How about you?",
        "Running at full power! Thanks for asking 😄 And you?",
        "All systems operational! What can I do for you today?"
    ],

    # User is fine
    ("i'm fine", "im fine", "i am fine", "good", "great", "i'm good", "im good", "doing well"): [
        "Awesome! 😊 Glad to hear that.",
        "That's great! Let's have a good chat then.",
        "Nice! So what are we talking about today?"
    ],

    # Name
    ("what is your name", "who are you", "your name", "what's your name", "whats your name"): [
        "I'm NeoBot 🤖 — built by a CodeAlpha intern using Python!",
        "Call me NeoBot! Your friendly Python-powered chatbot.",
        "NeoBot at your service! Crafted with Python 🐍"
    ],

    # What can you do
    ("what can you do", "help", "commands", "options", "what do you know"): [
        None  # Handled specially below with a formatted menu
    ],

    # Python
    ("python", "coding", "programming", "code", "learn python"): [
        "Python is awesome! 🐍 Start with basics: variables, loops, functions — then move to libraries like NumPy and Pandas.",
        "For Python beginners: try freeCodeCamp or W3Schools. Practice daily on HackerRank!",
        "Python tip: Use list comprehensions instead of loops for cleaner code. E.g., [x*2 for x in range(10)]"
    ],

    # Jokes
    ("joke", "tell me a joke", "make me laugh", "funny"): [
        "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
        "I told my computer I needed a break. Now it won't stop sending me KitKat ads. 🍫",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings. 😂",
        "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?' 😄"
    ],

    # Fun facts
    ("fact", "fun fact", "tell me a fact", "interesting", "did you know"): [
        "Fun fact: Python was named after Monty Python, not the snake! 🎭",
        "Did you know? The first computer bug was an actual bug — a moth found in a Harvard computer in 1947! 🦋",
        "Fun fact: There are more possible games of chess than atoms in the observable universe! ♟️",
        "Did you know? The average person spends 6 months of their lifetime waiting for red lights. 🚦"
    ],

    # Time
    ("time", "what time is it", "current time", "what's the time"): [
        None  # Handled specially below
    ],

    # Date
    ("date", "what's today", "today's date", "what day is it"): [
        None  # Handled specially below
    ],

    # Thanks
    ("thanks", "thank you", "thx", "ty", "thank u"): [
        "You're welcome! 😊 Anything else I can help with?",
        "Anytime! That's what I'm here for 🤖",
        "Happy to help! Let me know if you need anything else."
    ],

    # Bye
    ("bye", "goodbye", "exit", "quit", "see you", "cya", "good night", "goodnight"): [
        None  # Handled specially — also exits the loop
    ],

    # Age / about bot
    ("how old are you", "when were you made", "your age"): [
        "I was just born recently as a CodeAlpha intern project! 🐣 Young but smart.",
        "I'm brand new — fresh out of Python code! 😄"
    ],

    # Weather (can't really know, joke response)
    ("weather", "temperature", "rain", "sunny"): [
        "I wish I could check the weather, but I'm stuck inside this terminal! 😄 Try weather.com!",
        "No sensors here! But I hope it's sunny wherever you are ☀️"
    ],

    # Internship
    ("internship", "codealpha", "project", "task"): [
        "This chatbot is Task 4 of the CodeAlpha Python Internship 🎓 Hope it gets full marks!",
        "CodeAlpha internship projects are a great way to build your Python portfolio 💼",
        "NeoBot was built as a mini project for CodeAlpha Task 4 — Rule-Based Chatbot 🤖"
    ],

    # Creator
    ("who made you", "who created you", "your creator", "who built you"): [
        "I was built by a passionate CodeAlpha Python intern! 👨‍💻",
        "A talented CodeAlpha intern created me using Python 🐍"
    ],
}

# ── HELPER FUNCTIONS ─────────────────────────────────────────

def typewrite(text, delay=0.012):
    """Print text with a typewriter effect."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()


def thinking_animation():
    """Show a 'thinking...' animation."""
    print(D + "  NeoBot is thinking", end='', flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(D + ".", end='', flush=True)
    print(RS)
    time.sleep(0.2)


def print_header():
    """Print the app header."""
    print()
    print(C + B + "  ╔══════════════════════════════════════════╗")
    print(C + B + "  ║                                          ║")
    print(C + B + "  ║   🤖  N E O B O T  —  AI  C H A T B O T ║")
    print(C + B + "  ║       CodeAlpha Python Internship         ║")
    print(C + B + "  ║              Task  04                     ║")
    print(C + B + "  ╚══════════════════════════════════════════╝")
    print()
    print(D + "  " + "─" * 46)
    print(D + f"  Session started: {datetime.now().strftime('%d %b %Y  %I:%M %p')}")
    print(D + "  " + "─" * 46)
    print()


def print_help_menu():
    """Print the help/commands menu."""
    print()
    print(Y + B + "  ┌─────────────────────────────────────┐")
    print(Y + B + "  │         WHAT I CAN DO 📋             │")
    print(Y + B + "  ├─────────────────────────────────────┤")
    topics = [
        ("👋 Greetings",     "hello, hi, hey"),
        ("😄 Mood check",    "how are you"),
        ("🤖 About me",      "who are you, your name"),
        ("🐍 Python help",   "python, coding, learn"),
        ("😂 Jokes",         "tell me a joke"),
        ("💡 Fun facts",     "fun fact, did you know"),
        ("🕐 Time / Date",   "time, date"),
        ("🌤  Weather",      "weather"),
        ("🎓 Internship",    "codealpha, project"),
        ("👋 Exit",          "bye, quit, exit"),
    ]
    for icon_label, example in topics:
        print(Y + f"  │  {icon_label:<18}" + W + f"  → {example:<18}" + Y + "│")
    print(Y + B + "  └─────────────────────────────────────┘")
    print()


def format_bot_reply(text):
    """Print a formatted bot reply."""
    print()
    print(C + "  ┌─ " + B + "NEOBOT" + RS + C + " ─────────────────────────────")
    # Typewrite the reply with indent
    lines = text.split('\n')
    for line in lines:
        print(C + "  │ " + RS + W + "  " + line)
    print(C + "  └──────────────────────────────────────")
    print()


def format_user_input():
    """Format the user input prompt."""
    t = datetime.now().strftime('%H:%M')
    return G + B + f"\n  YOU [{t}] " + RS + G + "❯ " + RS


def get_response(user_input):
    """Match user input to a response."""
    text = user_input.lower().strip()

    # ── Special cases ──

    # Help menu
    if any(w in text for w in ("help", "what can you do", "commands", "options")):
        print_help_menu()
        return None

    # Time
    if any(w in text for w in ("time", "what time")):
        now = datetime.now().strftime("%I:%M %p")
        return f"Current time is ⏰ {now}"

    # Date
    if any(w in text for w in ("date", "today", "what day")):
        today = datetime.now().strftime("%A, %d %B %Y")
        return f"Today is 📅 {today}"

    # Bye / Exit
    if any(w in text for w in ("bye", "goodbye", "exit", "quit", "see you", "cya", "good night", "goodnight")):
        farewell = random.choice([
            "Goodbye! It was great chatting with you 👋",
            "See you later! Keep coding 🐍✨",
            "Bye! Come back anytime 😊"
        ])
        format_bot_reply(farewell)
        print(D + "  Session ended. Have a great day!\n")
        return "EXIT"

    # ── Match against knowledge base ──
    for triggers, replies in RESPONSES.items():
        if any(trigger in text for trigger in triggers):
            if replies[0] is None:
                continue  # already handled above
            return random.choice(replies)

    # ── Fallback ──
    fallbacks = [
        "Hmm, I'm not sure about that 🤔 Try asking something else, or type 'help'.",
        "I didn't catch that! 😅 Type 'help' to see what I can do.",
        "Interesting question! But I don't have an answer for that yet 🤖",
        "I'm still learning! Try rephrasing or type 'help' for options.",
    ]
    return random.choice(fallbacks)


# ── MAIN LOOP ────────────────────────────────────────────────

def run():
    print_header()

    # Welcome message
    thinking_animation()
    format_bot_reply(
        "Hey! 👋 I'm NeoBot — your Python-powered chatbot.\n"
        "  I can chat, crack jokes, share facts, and more!\n"
        "  Type 'help' to see what I can do. Type 'bye' to exit."
    )

    while True:
        try:
            user_msg = input(format_user_input()).strip()
        except (KeyboardInterrupt, EOFError):
            print()
            format_bot_reply("Caught a KeyboardInterrupt! Goodbye 👋")
            break

        if not user_msg:
            print(D + "  (Type something or 'help' for options)")
            continue

        thinking_animation()
        response = get_response(user_msg)

        if response == "EXIT":
            break
        elif response is not None:
            format_bot_reply(response)


if __name__ == "__main__":
    run()
