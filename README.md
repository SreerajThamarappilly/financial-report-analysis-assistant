# financial-report-analysis-assistant

The Financial Report Analysis Assistant is a fintech application that leverages state-of-the-art NLP techniques and Large Language Models (LLMs) like OpenAI, along with frameworks such as LangChain and LlamaIndex, to analyze financial documents. It extracts key financial metrics, generates summaries, and allows users to interactively query the content for deeper insights. It streamlines the process of extracting key information and gaining insights from complex financial texts.

## Features

- **Document Ingestion**: Upload and process financial reports in PDF or DOCX format.
- **Key Metric Extraction**: Automatically extract important financial metrics like revenue, profit, expenses, etc.
- **Summarization**: Generate concise summaries of financial reports using LLMs.
- **Interactive Querying**: Ask questions about the financial reports and receive detailed answers.
- **Web Interface**: User-friendly web application built with Streamlit for easy interaction.
- **Scalability**: Designed to handle multiple documents and user queries efficiently.

## Technologies and Concepts Used

- **Python 3.11**
- **Large Language Models (LLMs)**:
    - **OpenAI**: For generating summaries and answering queries.
    - **LangChain**: Framework for building applications powered by LLMs.
    - **LlamaIndex (GPT Index)**: Efficient indexing and querying over documents.
- **Natural Language Processing (NLP)**:
    - **spaCy**: For entity recognition and custom financial metric extraction.
    - **PyPDF2 and pdfminer.six**: For extracting text from PDF documents.
    - **python-docx**: For extracting text from DOCX files.
- **Streamlit**: For building the web application interface.

## Directory Structure

```bash
financial_report_analysis_assistant/
├── README.md
├── requirements.txt
├── .env
├── app.py
├── utils/
│   ├── __init__.py
│   ├── document_processor.py
│   ├── metric_extractor.py
│   ├── summarizer.py
│   └── query_engine.py
├── data/
│   ├── documents/sample_report.txt
│   ├── index.json
├── templates/
│   └── index.html
├── static/
│   └── css/styles.css
```

- **README.md**: Project documentation.
- **requirements.txt**: Python dependencies.
- **.env**: Environment variables (e.g., API keys).
- **app.py**: Main application script.
- **utils/**: Directory containing utility modules.
- **document_processor.py**: Handles document ingestion and text extraction.
- **metric_extractor.py**: Extracts financial metrics from the text.
- **summarizer.py**: Generates summaries using LLMs.
- **query_engine.py**: Handles user queries over the indexed documents.
- **data/**: Stores documents and index files.
- **templates/**: Contains templates for the web interface.

## Environment Variables

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Run the Application

```bash
streamlit run app.py
```

## Testing the Application

1. Open your web browser and navigate to http://localhost:8501
2. Upload a financial report in PDF or DOCX format.
3. View extracted financial metrics and generated summaries.
4. Interact with the assistant by asking questions about the report content.

## License

*This project is licensed under the MIT License.*
