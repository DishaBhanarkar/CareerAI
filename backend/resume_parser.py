import pdfplumber


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF resume.
    """

    extracted_text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                extracted_text += text + "\n"

    return extracted_text


if __name__ == "__main__":

    pdf_path = "resume.pdf"

    text = extract_text_from_pdf(pdf_path)

    print("\n--- EXTRACTED RESUME TEXT ---\n")

    print(text)