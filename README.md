# NLPaper

## Overview
NLPaper is a FullStack application designed to interact with documents using natural language processing. It allows users to perform various tasks like summarizing documents, extracting text, and more.

### Backend (Python/Flask)
Located in the `backend` directory, the backend API is built with Flask and utilizes the HuggingFace Transformers library for NLP tasks.

#### Main Features
- **Text Summarization**: Summarizes text using the HuggingFace summarizer model.
- **Text Extraction**: Extracts text from PDF and DOCX files for processing.
- **File Upload**: Handles PDF and DOCX file uploads and processes them accordingly.

#### Challenges Faced
- Handling file uploads and text extraction in different formats (PDF, DOCX).
- Implementing effective text summarization with character limitations.
- Ensuring seamless integration between the front-end and back-end.

#### Future Improvements
- Expand the range of document formats supported.
- Implement additional NLP functionalities like topic identification and question answering.
- Optimize the text processing for larger documents.

### Frontend (React/Next.js)
The front end, found in the `frontend` directory, is developed with Next.js and React.

#### Key Functionalities
- **Interactive UI**: A user-friendly interface for interacting with the NLP functionalities.
- **File Drag and Drop**: Users can upload documents via drag and drop.
- **Text Input**: Users can input text directly for summarization.

#### Challenges Faced
- Ensuring responsiveness and intuitive UX design.
- Efficiently managing state and API requests in React.
- Implementing the drag and drop feature for file uploads.

#### Future Improvements
- Enhance the UI/UX design for better user engagement.
- Include real-time text analysis features.
- Implement more interactive elements like visualizations of text analysis.

### API Endpoints
- `/summarize`: POST endpoint for text summarization.
- `/upload`: POST endpoint for uploading and processing PDF/DOCX files.
- `/health`: GET endpoint for API health check.

---

## Setup and Installation
1. **Backend Setup**: Navigate to the `backend` directory and install dependencies.
2. **Frontend Setup**: In the `frontend` directory, install necessary packages and start the Next.js server.

## Testing
- `test_api.py`: Contains tests for the backend API functionalities.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/anth-riv/NLPaper/issues) if you want to contribute.