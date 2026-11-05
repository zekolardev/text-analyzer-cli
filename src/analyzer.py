
import argparse
import json
import re
import sys
from pathlib import Path


def analyze_text(text):
    """Analyze text and return useful statistics."""

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    words = re.findall(r"\b[\w']+\b", text, re.UNICODE)
    sentences = re.findall(r"[.!?؟]+", text)
    lines = text.splitlines()

    longest_word = max(words, key=len, default="")

    return {
        "characters": len(text),
        "words": len(words),
        "lines": len(lines),
        "sentences": len(sentences),
        "longest_word": longest_word,
    }


def display_results(result):
    """Display analysis results in a readable format."""

    print("\n--- Analysis Results ---")

    for key, value in result.items():
        label = key.replace("_", " ").title()
        print(f"{label}: {value}")


def create_parser():
    """Create and configure command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Analyze text and extract useful statistics."
    )

    input_group = parser.add_mutually_exclusive_group()

    input_group.add_argument(
        "-t",
        "--text",
        help="Text to analyze directly."
    )

    input_group.add_argument(
        "-f",
        "--file",
        help="Path to a UTF-8 text file."
    )

    parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        help="Display results in JSON format."
    )

    return parser


def main(argv=None):
    """Run the Text Analyzer CLI."""

    parser = create_parser()
    args = parser.parse_args(argv)

    if args.text is not None:
        text = args.text

    elif args.file is not None:
        try:
            text = Path(args.file).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            print(f"Error: Could not read file: {error}", file=sys.stderr)
            return 1

    else:
        print("=" * 30)
        print("       TEXT ANALYZER CLI")
        print("=" * 30)

        try:
            text = input("\nEnter your text:\n")
        except EOFError:
            print("\nError: No input received.", file=sys.stderr)
            return 1

    if not text.strip():
        print("\nError: Text cannot be empty.", file=sys.stderr)
        return 1

    result = analyze_text(text)

    if args.json:
        print(json.dumps(result, indent=4, ensure_ascii=False))
    else:
        display_results(result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
