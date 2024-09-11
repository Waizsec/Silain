import { useState } from 'react';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (event) => {
    event.preventDefault();  // Prevent the default form submission

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
          throw new Error('response');
        }
        return response.json();
      })
      .then(data => {
        if (data.unique_key && data.username) {
          // Store the unique key and username in sessionStorage
          sessionStorage.setItem('unique_key', data.unique_key);
          sessionStorage.setItem('username', username);

          // Redirect to the dashboard
          window.location.href = '/dashboard';
        } else {
          alert(data.error || 'Unknown error occurred');
        }
      })
      .catch(error => {
        console.error('Error:', error);
        alert('An error occurred: ' + error.message);
      });
  };

  return (
    <>
      <div className="flex w-full h-[57vw] overflow-hidden">
        <form onSubmit={handleLogin} className="w-[50vw] h-screen flex flex-col justify-center px-[15vw]">
          <h2 className="text-[1.8vw] font-semibold text-[#2B3674]">Sign In</h2>
          <p className="text-[0.9vw] text-[#A3AED0] mt-[0.4vw] mb-[2vw]">
            Please Enter Your Username and Password
          </p>
          <label htmlFor="username" className="text-biru text-[0.9vw]">
            Username*
          </label>
          <input
            type="text"
            id="exampleInputEmail"
            name="username"
            className="w-full h-[3vw] border-[0.1vw] border-[#d0d0d0] placeholder:text-[0.9vw] pl-[1vw] mt-[1vw] mb-[1vw] rounded-[1vw] text-[0.9vw] outline-none"
            placeholder="Ex: KelompokD"
            value={username}
            onChange={(e) => setUsername(e.target.value)}  // Bind input to state
            required
          />
          <label htmlFor="password" className="text-biru text-[0.9vw]">
            Password*
          </label>
          <input
            type="password"
            id="exampleInputPassword"
            name="password"
            className="w-full h-[3vw] border-[0.1vw] border-[#d0d0d0] placeholder:text-[0.9vw] pl-[1vw] mt-[1vw] rounded-[1vw] text-[0.9vw] outline-none"
            placeholder="******"
            value={password}
            onChange={(e) => setPassword(e.target.value)}  // Bind input to state
            required
          />
          <input type="submit" value="Sign In" className="text-[0.9vw] bg-[#5e75f4] text-white mt-[2vw] w-full h-[3vw] rounded-[1vw] cursor-pointer hover:bg-[#8192f4] duration-[0.6s] ease-in-out" />
        </form>

        {/* Right Background */}
        <div className="w-[50vw] overflow-hidden bg-auth rounded-bl-[10vw] items-center justify-center">
          <div className="w-full h-full flex items-center justify-center">
            <img src="/fav.png" className='w-[6vw] mr-[2vw]' />
            <h1 className="text-[6vw] text-white font-semibold">
              Silain
            </h1>
          </div>

        </div>
      </div>
    </>
  );
}

export default App;
