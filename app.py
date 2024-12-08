# app.py

import streamlit as st
from utils.document_processor import process_document
from utils.metric_extractor import extract_metrics
from utils.summarizer import generate_summary
from utils.query_engine import build_index, query_index
import os

def main():
    st.title("Financial Report Analysis Assistant")

    # Upload Document
    st.header("Upload Financial Report")
    uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])
    if uploaded_file is not None:
        document_text = process_document(uploaded_file)
        st.success("Document processed successfully.")

        # Extract Financial Metrics
        metrics = extract_metrics(document_text)
        st.subheader("Extracted Financial Metrics")
        st.write(metrics)

        # Generate Summary
        if st.button("Generate Summary"):
            summary = generate_summary(document_text)
            st.subheader("Summary")
            st.write(summary)

        # Save Document Text
        os.makedirs('data/documents', exist_ok=True)
        with open(f"data/documents/{uploaded_file.name}.txt", 'w', encoding='utf-8') as f:
            f.write(document_text)

        # Build Index
        if st.button("Build Index for Querying"):
            build_index('data/documents')
            st.success("Index built successfully.")

        # Query Interface
        query = st.text_input("Ask a question about the report:")
        if query:
            response = query_index(query)
            st.subheader("Answer")
            st.write(response)

if __name__ == "__main__":
    main()
