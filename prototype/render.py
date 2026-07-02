"""Terminal text rendering: paragraph wrapping, rules, and menus."""

import shutil
import textwrap

WIDTH = min(shutil.get_terminal_size((80, 24)).columns, 76)


def say(text: str) -> None:
    """Print text wrapped to terminal width, preserving paragraph breaks."""
    for para in text.strip().split("\n\n"):
        print(textwrap.fill(" ".join(para.split()), WIDTH))
        print()


def rule(label: str = "") -> None:
    if label:
        pad = WIDTH - len(label) - 4
        print(f"── {label} " + "─" * max(pad, 0))
    else:
        print("─" * WIDTH)
    print()


def ask(prompt: str, options: list) -> int:
    """Show a numbered menu of labels, return the chosen index."""
    print(prompt)
    for i, label in enumerate(options, 1):
        print(f"  {i}. {label}")
    print()
    while True:
        try:
            raw = input("> ").strip()
        except EOFError:
            print("\n(input ended — closing here)")
            raise SystemExit(0)
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            print()
            return int(raw) - 1
        print(f"Pick a number between 1 and {len(options)}.")
