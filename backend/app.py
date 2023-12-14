from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS
import fitz  # PyMuPDF
import docx
import os

app = Flask(__name__)
# Enables CORS for all domains and allows credentials (cookies, headers) for cross-origin requests.
CORS(app, supports_credentials=True)

# Initialize the HuggingFace summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_text_from_pdf(file_storage):
    """
    Extract text from a PDF file.
    This function first saves the uploaded file to a temporary path, 
    opens it for reading, and then deletes the temporary file.
    """
    temp_path = "tempfile.pdf"
    file_storage.save(temp_path)

    doc = fitz.open(temp_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    # Delete the temporary file after use
    os.remove(temp_path)
    return text

def extract_text_from_docx(file_storage):
    """
    Extract text from a DOCX file.
    Similar to the PDF extraction, this function first saves the uploaded file 
    to a temporary path, opens it for reading, and then deletes the temporary file.
    """
    temp_path = "tempfile.docx"
    file_storage.save(temp_path)

    doc = docx.Document(temp_path)
    fullText = [para.text for para in doc.paragraphs]
    
    os.remove(temp_path)
    return '\n'.join(fullText)

@app.route('/summarize', methods=['POST'])
def summarize_text():
    """
    Summarize the provided text using the HuggingFace summarizer model.
    The function receives JSON data, extracts the text, and uses the summarizer
    to generate a summarized version of the input text.
    """
    try:
        data = request.get_json()
        summary = summarizer(data['text'], max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        return jsonify(summary=summary)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/upload', methods=['POST'])
def handle_upload():
    """
    Handle file upload for PDF and DOCX files.
    Depending on the file's content type, the function routes the file to the
    appropriate text extraction method (PDF or DOCX).
    """
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file provided"}), 400

    if file.content_type == 'application/pdf':
        text = extract_text_from_pdf(file)
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        text = extract_text_from_docx(file)
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    return jsonify({"text": text})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="API is running")

if __name__ == '__main__':
    app.run(port=8000, debug=True)