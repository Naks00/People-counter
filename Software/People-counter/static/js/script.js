// Function to update the count
async function updateCount() {
    try {
      const response = await fetch('/count');
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const data = await response.json();
      document.getElementById('count').innerText = data.count;
    } catch (error) {
      console.error('Error updating count:', error);
      document.getElementById('count').innerText = 'Error';
    }
  }
  
  // Function to reset the counter
  async function resetCounter() {
    try {
      const response = await fetch('/reset', { method: 'POST' });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const data = await response.json();
      alert(data.message);
      await updateCount(); // Refresh the count
    } catch (error) {
      console.error('Error resetting counter:', error);
      alert('Error resetting counter.');
    }
  }
  async function fetchDailyCounts() {
    try {
        const response = await fetch("/daily_counts");
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const dailyCounts = await response.json();
        displayDailyCounts(dailyCounts);
    } catch (error) {
        console.error("Error fetching daily counts:", error);
    }
}

function displayDailyCounts(dailyCounts) {
    const ctx = document.getElementById('dailyCountsChart').getContext('2d');

    // Extract dates and counts from the dailyCounts data
    const dates = dailyCounts.map(day => day.date);
    const counts = dailyCounts.map(day => day.count);

    // Create the chart
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: dates,
            datasets: [{
                label: 'Pedestrians per Day',
                data: counts,
                backgroundColor: 'rgba(236, 29, 36, 0.45)',
                borderColor: 'rgb(0, 0, 0)',
                borderWidth: 3
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Pedestrians'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Date'
                    }
                }
            }
        }
    });
}

// Call this function when the page loads to fetch and display the data
fetchDailyCounts();

  
  // Event listener for the reset button
  document.getElementById('reset-button').addEventListener('click', resetCounter);
  
  // Update the count every 2 seconds
  setInterval(updateCount, 2000);
  
  // Initial count update
  updateCount();
  