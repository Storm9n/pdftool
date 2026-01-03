import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def parse_page_ranges(pages_str):
    """
    Parse a string like '1,2-4' into a list of page numbers.
    :param pages_str: Comma-separated string of page ranges
    """
    pages = []
    for part in pages_str.split(","):
        if "-" in part:
            start, end = part.split("-")
            pages.extend(range(int(start), int(end) + 1))
        else:
            pages.append(int(part))
    return pages


def extract_pages(input_pdf, output_pdf, pages_str):
    """
    Docstring for extract_pages

    :param input_pdf: Path of the input PDF file
    :param output_pdf: Path of the output PDF file
    :param pages_str: Comma-separated string of page ranges
    """
    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()

    pages = parse_page_ranges(pages_str)

    for p in pages:
        writer.add_page(reader.pages[p - 1])

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"Extracted pages {pages_str} → {output_pdf}")


def main():
    """
    Main function to parse arguments and call extract_pages.
    """
    parser = argparse.ArgumentParser(description="Extract specific pages from a PDF.")

    parser.add_argument("input_pdf", type=Path, help="Path to the input PDF")

    parser.add_argument("output_pdf", type=Path, help="Path to the output PDF")

    parser.add_argument("--pages", required=True, help="Pages to extract, e.g. '1,2-4'")

    args = parser.parse_args()

    extract_pages(args.input_pdf, args.output_pdf, args.pages)


if __name__ == "__main__":
    main()
