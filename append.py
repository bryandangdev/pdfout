from PyPDF2 import PdfReader, PdfWriter
import argparse
import os

def append_pdfs(input_pdfs, output_pdf):
    """Append multiple PDFs into one file in the order provided."""
    writer = PdfWriter()

    for pdf_path in input_pdfs:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"Created combined PDF: {output_pdf}")


def main():
    parser = argparse.ArgumentParser(
        description="Append multiple PDF files into one PDF in the order provided.",
        epilog="Example usage: python append.py file1.pdf file2.pdf file3.pdf -o combined.pdf"
    )
    
    parser.add_argument(
        "input_pdfs",
        nargs="+", # nargs means one or more arguments
        help="Input PDF file paths (at least two)"
    )

    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output PDF file path"
    )

    args = parser.parse_args()
    append_pdfs(args.input_pdfs, args.output)


if __name__ == "__main__":
    main()
