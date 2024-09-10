function handleLogin(event) {
    event.preventDefault();  // Prevent the default form submission

    // Get form data
    const username = document.getElementById('exampleInputEmail').value;
    const password = document.getElementById('exampleInputPassword').value;

    // Create a FormData object to send the data
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    // Send a POST request to the login API
    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.unique_key) {
            // Store the unique key in sessionStorage
            sessionStorage.setItem('unique_key', data.unique_key);

            // Redirect to the dashboard
            window.location.href = '../../index.html';
        } else {
            alert(data.error || 'Unknown error occurred');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred: ' + error.message);
    });
}
