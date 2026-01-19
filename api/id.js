const fetch = require('node-fetch');

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }
  
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'POST method required' });
  }
  
  try {
    const { value } = req.body;
    
    if (!value || value.length !== 13 || !/^\d+$/.test(value)) {
      return res.status(400).json({ error: 'Invalid ID card number' });
    }
    
    const url = `https://apitu.psnw.xyz/index.php?type=idcard&value=${value}&mode=sff`;
    const response = await fetch(url);
    
    if (!response.ok) {
      throw new Error(`API returned ${response.status}`);
    }
    
    const data = await response.json();
    
    return res.status(200).json(data);
    
  } catch (error) {
    console.error('Error:', error);
    return res.status(500).json({ 
      error: 'API call failed',
      details: error.message 
    });
  }
};