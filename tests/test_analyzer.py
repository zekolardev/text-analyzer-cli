
import unittest

from src.analyzer import analyze_text


class TestTextAnalyzer(unittest.TestCase):

    def test_word_count(self):
        result = analyze_text("Python is powerful")
        self.assertEqual(result["words"], 3)

    def test_character_count(self):
        result = analyze_text("Hello")
        self.assertEqual(result["characters"], 5)

    def test_line_count(self):
        result = analyze_text("First line\nSecond line")
        self.assertEqual(result["lines"], 2)

    def test_sentence_count(self):
        result = analyze_text("Hello. How are you?")
        self.assertEqual(result["sentences"], 2)

    def test_longest_word(self):
        result = analyze_text("I love programming")
        self.assertEqual(result["longest_word"], "programming")

    def test_empty_text(self):
        result = analyze_text("")
        self.assertEqual(result["words"], 0)
        self.assertEqual(result["longest_word"], "")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            analyze_text(123)


if __name__ == "__main__":
    unittest.main()
