// pages/api/summarize.js
export default async function handler(req, res) {
  console.log("Requête reçue :", req.body);
  const url = 'http://localhost:8000/summarize';

  try {
    console.log("Envoi à Flask :", req.body);
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
    console.log("Réponse de Flask :", data);
    res.status(200).json(data);
  } catch (error) {
    console.error("Erreur lors de la requête à Flask :", error);
    res.status(500).json({ message: 'Erreur de serveur interne', details: error.message });
  }
}

  