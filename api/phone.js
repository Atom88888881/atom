const fetch = require('node-fetch');

module.exports = async (req, res) => {
  // ✅ ตั้งค่า CORS ให้รองรับ
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  // ✅ จัดการ OPTIONS request (สำหรับ CORS preflight)
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }
  
  // ✅ อนุญาตเฉพาะ POST
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'POST method required' });
  }
  
  try {
    // ✅ รับข้อมูลจาก request body
    const { phone } = req.body;
    
    // ✅ ตรวจสอบเบอร์โทรศัพท์
    if (!phone || phone.length !== 10 || !/^\d+$/.test(phone)) {
      return res.status(400).json({ error: 'Invalid phone number' });
    }
    
    // ✅ เรียก API ภายนอก
    const url = `https://apitu.psnw.xyz/index.php?type=phone&value=${phone}&mode=sff`;
    const response = await fetch(url);
    
    if (!response.ok) {
      throw new Error(`API returned ${response.status}`);
    }
    
    const data = await response.json();
    
    // ✅ ส่งผลลัพธ์กลับ
    return res.status(200).json(data);
    
  } catch (error) {
    console.error('Error:', error);
    return res.status(500).json({ 
      error: 'API call failed',
      details: error.message 
    });
  }
};