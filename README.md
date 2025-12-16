# csv-profiler

A simple Python tool to profile CSV files (missing values, column types, basic stats) and generate a quick summary report.

## Features
- Detect column dtypes
- Missing values summary
- Basic numeric statistics
- Example scripts included

## Requirements
- Python 3.9+
- pandas

Install dependencies:
```bash
pip install -r requirements.txt
```

Usage

Option 1: Run as a module (recommended)
```bash
python -m csv_profiler path/to/file.csv
```

Option 2: Run a script (if you have a main script in the package)
```bash
python src/csv_profiler/main.py path/to/file.csv
```

## Example
python -m csv_profiler examples/sample.csv

## Project Structure

src/csv_profiler/ - main package code

examples/ - sample files / usage examples
