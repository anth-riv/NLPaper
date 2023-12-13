
const AppPage = () => {
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
        ></textarea>
        
        <div className="my-6 border-b-2 border-gray-200"></div>
        
        <div className="flex flex-col items-center justify-center p-6 border-2 border-gray-300 border-dashed rounded">
          <p className="mb-3 font-semibold text-gray-800">Drag and drop a file here</p>
          <p className="text-gray-600">or</p>
          <button className="mt-3 py-2 px-4 bg-gradient-to-r from-green-400 to-blue-500 text-white rounded shadow-lg transition duration-300 hover:bg-gradient-to-l">
            Select a file
          </button>
        </div>
      </div>
    </div>
  );
};

export default AppPage;