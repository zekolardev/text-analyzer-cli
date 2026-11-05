
import io
import json
import tempfile
import unittest

from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from unittest.mock import patch

from src.analyzer import analyze_text, main


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

    def test_persian_question_mark(self):
        result = analyze_text("سلام. حالت چطوره؟")
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


class TestTextAnalyzerCLI(unittest.TestCase):

    def test_text_argument(self):
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main(["--text", "Hello world."])

        self.assertEqual(exit_code, 0)
        self.assertIn("Words: 2", output.getvalue())

    def test_json_output(self):
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main(["--text", "Hello world.", "--json"])

        result = json.loads(output.getvalue())

        self.assertEqual(exit_code, 0)
        self.assertEqual(result["words"], 2)
        self.assertEqual(result["sentences"], 1)

    def test_file_input(self):
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "sample.txt"
            file_path.write_text("Python is powerful.", encoding="utf-8")

            with redirect_stdout(output):
                exit_code = main(["--file", str(file_path)])

        self.assertEqual(exit_code, 0)
        self.assertIn("Words: 3", output.getvalue())

    def test_missing_file(self):
        error_output = io.StringIO()

        with redirect_stderr(error_output):
            exit_code = main(["--file", "missing_file.txt"])

        self.assertEqual(exit_code, 1)
        self.assertIn("Could not read file", error_output.getvalue())

    def test_empty_text_argument(self):
        error_output = io.StringIO()

        with redirect_stderr(error_output):
            exit_code = main(["--text", "   "])

        self.assertEqual(exit_code, 1)
        self.assertIn("cannot be empty", error_output.getvalue())

    def test_interactive_input(self):
        output = io.StringIO()

        with patch("builtins.input", return_value="Python is great"):
            with redirect_stdout(output):
                exit_code = main([])

        self.assertEqual(exit_code, 0)
        self.assertIn("Words: 3", output.getvalue())


if __name__ == "__main__":
    unittest.main()
