// This is an EXAMPLE of what you would add to your index.html's JavaScript

const crop = 'Tomatoes';
const market = 'Pune';

fetch(`http://localhost:5000/api/forecast?crop=${crop}&market=${market}`)
  .then(response => response.json())
  .then(data => {
    console.log(data.insight); // "AI predicts a demand peak..."
    // Now, use this 'data' to update your chart and insight text on the webpage
  });