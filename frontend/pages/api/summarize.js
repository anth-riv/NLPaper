// pages/api/summarize.js
export default async function handler(req, res) {
  console.log("Request received :", req.body);
  const url = 'http://localhost:8000/summarize';

  try {
    console.log("Send to Flask :", req.body);
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(req.body),
    });

    if (!response.ok) {
      throw new Error(`HTTP status ${response.status}`);
    }

    const data = await response.json();
    console.log("Flask's response:", data);
    res.status(200).json(data);
  } catch (error) {
    console.error("Error during request to Flask :", error);
    res.status(500).json({ message: 'Internal server error', details: error.message });
  }
}