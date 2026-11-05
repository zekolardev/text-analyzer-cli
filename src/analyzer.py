
import re


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


def main():
    print("=" * 30)
    print("       TEXT ANALYZER CLI")
    print("=" * 30)

    text = input("\nEnter your text:\n")

    if not text.strip():
        print("\nError: Text cannot be empty.")
        return

    result = analyze_text(text)

    print("\n--- Analysis Results ---")

    for key, value in result.items():
        label = key.replace("_", " ").title()
        print(f"{label}: {value}")


if __name__ == "__main__":
    main()
