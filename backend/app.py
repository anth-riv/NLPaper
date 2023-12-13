from flask import Flask, request, jsonify
from transformers import pipeline  # Importing pipeline function from HuggingFace Transformers

app = Flask(__name__)

# Initializing HuggingFace summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Route for summarizing text
@app.route('/summarize', methods=['POST'])
def summarize_text():
    try:
        data = request.get_json()
        print("Data received:", data)  # Printing received data

        # Generating the summary
        summary = summarizer(data['text'], max_length=130, min_length=30, do_sample=False)[0]['summary_text']

        # Returning the summary as a JSON response
        return jsonify(summary=summary)
    except Exception as e:
        print("Error:", e)  # Printing the error
        return jsonify({"error": str(e)}), 500

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="API is running")

# Running the Flask app
if __name__ == '__main__':
    app.run(port=8000, debug=True)