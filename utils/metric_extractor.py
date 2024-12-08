# utils/metric_extractor.py

import spacy

nlp = spacy.load("en_core_web_sm")

def extract_metrics(text):
    """
    Extracts key financial metrics from the text.

    Args:
        text (str): Input text.

    Returns:
        dict: Dictionary of extracted financial metrics.
    """
    doc = nlp(text)
    metrics = {}

    # Custom logic to extract financial metrics
    # This is a simplified example; in practice, you may need more advanced techniques
    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()
        if "revenue" in line_lower:
            metrics['Revenue'] = line.strip()
        elif "profit" in line_lower:
            metrics['Profit'] = line.strip()
        elif "expenses" in line_lower:
            metrics['Expenses'] = line.strip()
        elif "net income" in line_lower:
            metrics['Net Income'] = line.strip()
    return metrics
