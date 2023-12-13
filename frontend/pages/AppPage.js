import { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const AppPage = () => {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async () => {
    if (!text) return;
    setIsLoading(true);
    try {
      const response = await axios.post('/api/summarize', { text });
      setSummary(response.data.summary);
    } catch (error) {
      setSummary('Network error. Please try again.');
    }
    setIsLoading(false);
  };

  const onDrop = useCallback((acceptedFiles) => {
    const reader = new FileReader();
    reader.onload = (event) => {
      setText(event.target.result);
    };
    acceptedFiles.forEach(file => reader.readAsText(file));
  }, []);

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div className="min-h-screen bg-gradient-to-r from-blue-500 to-teal-400 flex flex-col items-center justify-center">
      <div className="bg-white p-8 rounded-xl shadow-lg max-w-2xl w-full">
        <h2 className="text-3xl font-bold text-gray-800 mb-6 text-center">
          Insert your text or upload a document
        </h2>
        
        <textarea
          className="w-full p-4 text-gray-800 mb-6 rounded border-2 border-gray-300 focus:border-blue-500 transition duration-300"
          placeholder="Paste your text here..."
          rows="6"
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></textarea>
        
        <div className="flex justify-center">
          <button
            onClick={handleSubmit}
            className="py-2 px-4 bg-gradient-to-r from-green-400 to-blue-500 text-white rounded shadow-lg transition duration-300 hover:bg-gradient-to-l"
            disabled={isLoading}
          >
            {isLoading ? 'Loading...' : 'Submit'}
          </button>
        </div>

        {summary && (
          <div className={`mt-4 p-4 rounded ${summary.startsWith('Network error') ? 'bg-red-100' : 'bg-gray-100'}`}>
            <h3 className="font-semibold text-center text-gray-800">Summary:</h3>
            <p className="text-black">{summary}</p>
          </div>
        )}
        

        <div {...getRootProps()} className="flex flex-col items-center justify-center p-6 border-2 border-gray-300 border-dashed rounded mt-6">
          <input {...getInputProps()} />
          <p className="mb-3 font-semibold text-gray-800">Drag and drop a file here, or click to select a file</p>
        </div>
      </div>
    </div>
  );
};

export default AppPage;