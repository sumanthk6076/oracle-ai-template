import sys
import time
import os

# ANSI color codes
RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
MAGENTA= "\033[95m"
BLUE   = "\033[94m"
WHITE  = "\033[97m"
DIM    = "\033[2m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typewrite(text, delay=0.03, color=""):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def progress_bar(label, duration=1.2, width=30):
    print(f"  {CYAN}{label}{RESET}")
    sys.stdout.write("  [")
    for i in range(width):
        time.sleep(duration / width)
        filled = GREEN + "█" + RESET
        sys.stdout.write(filled)
        sys.stdout.flush()
    sys.stdout.write(f"] {GREEN}Done!{RESET}\n\n")
    sys.stdout.flush()

def banner():
    lines = [
        "  ╔══════════════════════════════════════════╗",
        "  ║                                          ║",
        "  ║    🚀  JUST GETTING STARTED  🚀          ║",
        "  ║                                          ║",
        "  ╚══════════════════════════════════════════╝",
    ]
    for line in lines:
        print(CYAN + BOLD + line + RESET)
        time.sleep(0.07)

def checklist():
    steps = [
        ("Set up your environment",  GREEN),
        ("Write your first script",  GREEN),
        ("Run & test your code",     GREEN),
        ("Level up your skills",     YELLOW),
        ("Build something amazing!", MAGENTA),
    ]
    print(BOLD + WHITE + "\n  Your Journey:\n" + RESET)
    for i, (step, color) in enumerate(steps, 1):
        time.sleep(0.3)
        print(f"  {color}{'✔' if i <= 3 else '○'}  {i}. {step}{RESET}")
    print()

def sparkle_line():
    chars = ["✦", "✧", "★", "✦", "✧", "✶", "✦", "✧", "★", "✦"]
    colors = [CYAN, YELLOW, MAGENTA, GREEN, BLUE, WHITE]
    line = ""
    for i, ch in enumerate(chars):
        line += colors[i % len(colors)] + ch + " "
    print("  " + line + RESET)

def main():
    clear()
    print()
    banner()
    print()
    sparkle_line()
    print()

    typewrite("  Welcome aboard! Let's build something great.", delay=0.04, color=WHITE + BOLD)
    print()

    steps = [
        "Loading your tools   ",
        "Warming up Python    ",
        "Unlocking creativity ",
    ]
    for step in steps:
        progress_bar(step, duration=0.8)

    checklist()

    sparkle_line()
    print()
    typewrite("  You're all set. The only way is forward. 💡", delay=0.04, color=YELLOW + BOLD)
    print()

if __name__ == "__main__":
    main()
