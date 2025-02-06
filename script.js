document.getElementById('startAgent').addEventListener('click', function() {
    fetch('/start-agent', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('AI Agent started successfully!');
            fetchLog();
        } else {
            alert('Failed to start AI Agent.');
        }
    });
});

function fetchLog() {
    fetch('/get-log')
    .then(response => response.json())
    .then(data => {
        const logDiv = document.getElementById('log');
        logDiv.innerHTML = '';
        data.log.forEach(entry => {
            logDiv.innerHTML += `<p>${entry}</p>`;
        });
    });
}

// Fetch log every 5 seconds
setInterval(fetchLog, 5000);
