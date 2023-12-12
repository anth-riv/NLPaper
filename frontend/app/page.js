
export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-r from-blue-500 to-teal-400 flex items-center justify-center">
      <div className="bg-white p-8 rounded-xl shadow-lg max-w-md">
        <h1 className="text-4xl font-bold text-gray-800 mb-6">
          Welcome to <span className="bg-clip-text text-transparent bg-gradient-to-r from-green-400 to-blue-500">NLPaper</span>
        </h1>
        <p className="text-gray-600 mb-6">
          A modern FullStack application for interacting with your documents using natural language.
        </p>
        <div className="flex justify-center">
          <button className="py-2 px-4 bg-gradient-to-r from-green-400 to-blue-500 text-white rounded hover:shadow-md transition duration-300">
            Start Now
          </button>
        </div>
      </div>
    </div>
  );
}
