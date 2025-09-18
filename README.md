# PDF Utilities
Simple Python scripts for PDF processing. Mainly used for my own TTRPG sessions.
- `mirror.py` -- Duplicates each pagee and adds a horizontal flip.
- `append.py` -- Appends multiple PDFs in ordere.

## Requirements
- Python 3.7+
- PyPDF2 (do `pip install PyPDF2` if you don't have it)

## Usage
Mirror:
```
python mirror.py input.pdf
# output: input-flipped.pdf
```

Append:
```
python append.pdf file1.pdf file2.pdf -o combined.pdf
# output: combined.pdf
```