// API Gateway endpoint URL
const apiUrl = 'https://your-api-gateway-url.amazonaws.com/visitor-count';

// Fetch visitor count from the API
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    document.getElementById('visitor-count').textContent = data.count;
  })
  .catch(error => {
    console.error('Error fetching visitor count:', error);
    document.getElementById('visitor-count').textContent = 'Error';
  });