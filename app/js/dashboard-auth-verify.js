document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the unique key from sessionStorage
    const uniqueKey = sessionStorage.getItem('unique_key');

    if (uniqueKey) {
        // Create a FormData object
        const formData = new FormData();
        formData.append('unique_key', uniqueKey);

        // Verify the unique key with the server
        fetch('http://127.0.0.1:5000/verify_key', {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (!data.valid) {
                window.location.href = 'pages/samples/login.html';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred: ' + error.message);
            window.location.href = 'pages/samples/login.html';
        });
    } else {
        // Redirect to login page if no unique key is found
        window.location.href = 'pages/samples/login.html';
    }
});