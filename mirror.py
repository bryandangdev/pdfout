from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import argparse
import os

def create_mirror(input_pdf):
    """For each page in the input PDF, add a horizontally flipped copy."""
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        # Add original page
        writer.add_page(page)

        # Add flipped copy
        mirrored = page.mediabox
        mirrored_page = page
        mirrored_page.rotate(0)  # ensures we can apply the matrix
        mirrored_page.add_transformation([ -1, 0, 0, 1, float(mirrored.width), 0 ]) # mirror horizontally
        writer.add_page(mirrored_page)

    # Generate output filename
    base, ext = os.path.splitext(input_pdf)
    output_pdf = f"{base}-flipped{ext}"
    
    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"Created: {output_pdf}")


def main():
    parser = argparse.ArgumentParser(
        description="Insert a mirrored copy of each page in the PDF following the original. " 
                    "If the input contains {a,b}, the output will be {a,a',b,b'}, where x' is the mirror.",
        epilog="Example usage: python mirror_pages.py input.pdf"
    )
    
    parser.add_argument(
      "input_pdf",
      help="Input PDF file path"
    )

    args = parser.parse_args()
    create_mirror(args.input_pdf)


if __name__ == "__main__":
    main()
