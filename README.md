# Text Analyzer CLI

A lightweight Python command-line application for analyzing text and extracting useful statistics.

## Features

- Character counting
- Word counting
- Line counting
- Sentence counting
- Longest word detection
- Direct text input through command-line arguments
- Read text from UTF-8 files
- JSON output support
- Interactive input mode
- Input validation and error handling
- Persian sentence punctuation support

## Requirements

- Python 3.10 or newer
- No external dependencies required

## Project Structure

```text
text-analyzer-cli/
├── src/
│   └── analyzer.py
├── tests/
│   └── test_analyzer.py
├── .gitignore
├── LICENSE
└── README.md
```

## Usage

### Interactive Mode

Run the application without arguments:

```bash
python src/analyzer.py
```

### Analyze Direct Text

```bash
python src/analyzer.py --text "Python is powerful and interesting."
```

### Analyze a Text File

```bash
python src/analyzer.py --file sample.txt
```

Files must use UTF-8 encoding.

### JSON Output

```bash
python src/analyzer.py --text "Python is powerful." --json
```

Example output:

```json
{
    "characters": 19,
    "words": 3,
    "lines": 1,
    "sentences": 1,
    "longest_word": "powerful"
}
```

### Command-Line Help

```bash
python src/analyzer.py --help
```

## Running Tests

The project uses Python's built-in `unittest` framework.

```bash
python -m unittest discover -s tests -v
```

## Technologies

- Python
- argparse
- JSON
- pathlib
- unittest

## License

This project is licensed under the MIT License. See the LICENSE file for details.