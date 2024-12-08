# utils/document_processor.py

import PyPDF2
from pdfminer.high_level import extract_text
import docx2txt
import chardet

def process_document(uploaded_file):
    """
    Processes the uploaded document and extracts text.

    Args:
        uploaded_file (UploadedFile): The uploaded file object.

    Returns:
        str: Extracted text from the document.
    """
    if uploaded_file.type == "application/pdf":
        # Use pdfminer for better PDF text extraction
        text = extract_text(uploaded_file)
        return text
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        # Use docx2txt for DOCX files
        text = docx2txt.process(uploaded_file)
        return text
    else:
        raise ValueError("Unsupported file type.")
