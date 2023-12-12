from flask import Flask, request, jsonify  
from transformers import pipeline  # Importing the pipeline function from HuggingFace Transformers

app = Flask(__name__)  # Creating an instance of the Flask class. This instance is our WSGI application.

# Initialize the HuggingFace summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Route for summarizing text
@app.route('/summarize', methods=['POST'])
def summarize_text():
    # Extract text from the incoming JSON request
    data = request.get_json()
    text = data['text']

    # Generate the summary
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

    # Return the summary as a JSON response
    return jsonify(summary=summary)

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="API is up and running")  

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True) 
