import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom'; // Assuming you are using react-router for navigation
import { BestSellingItems, AverageGrowth, ItemTrends, UserCounts } from './Components';

const Dashboard = (props) => {
    const username = sessionStorage.getItem('username');
    const navigate = useNavigate();

    useEffect(() => {
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
                        navigate('/'); // Redirect to login if the key is invalid
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred: ' + error.message);
                    navigate('/'); // Redirect to login on error
                });
        } else {
            // Redirect to login page if no unique key is found
            navigate('/');
        }
    }, [navigate]); // The effect will run once when the component mounts

    return (
        <div className="flex w-full">
            {/* Sidebar */}
            <div className="w-[19vw] h-[100vh] fixed bg-white top-0 z-[1] flex flex-col items-center border-r-[0.1vw] border-[#dfdfdf]">
                <div className="w-full h-[8vw] mb-[2vw] flex items-center justify-center">
                    <img src="/public/fav.png" className="w-[3vw] mr-[1vw]" alt="Logo" />
                    <h1 className="text-[2vw]">Silain</h1>
                </div>
                {/* Nav */}
                <a href="/dashboard" className="flex items-center pl-[2vw] mb-[1.5vw] bg-[#F5F5F7] w-[80%] h-[3.5vw] rounded-[0.5vw]">
                    <img src="../public/dashboard-active.svg" className="w-[1.5vw] mr-[1.5vw]" alt="Dashboard Icon" />
                    <p className="text-third text-[1vw]">Dashboard</p>
                </a>
                <a href="/" className="flex items-center pl-[2vw] mb-[1.5vw] w-[80%] h-[3.5vw] rounded-[0.5vw] hover:bg-[#F5F5F7] duration-[0.6s] ease">
                    <img src="../public/user.svg" className="w-[1.5vw] mr-[1.5vw]" alt="Logout Icon" />
                    <p className="text-[1vw] text-[#8E92BC]">Logout</p>
                </a>
            </div>

            <div className="ml-[19vw] pb-[5vw] bg-[#f4f4f4] px-[3vw] w-full relative overflow-hidden">
                <div className="w-full flex items-center justify-between mt-[3vw]">
                    <p className="text-third text-[1.6vw] leading-[2vw]">
                        Hi {username}!
                        <br />
                        <span className="text-[#828282] text-[1vw]">Let’s see what’s up today!</span>
                    </p>
                    <img src="../public/profil-dummy.png" className="w-[3.5vw]" alt="Profile" />
                </div>
                {/* <General averageRating={props.averageRating} averageIncomeStart={props.averageIncomeStart} averageGrowth={props.averageGrowth} percentageDifference={props.percentageDifference} /> */}
                {/* <AverageGrowth usergrowth={props.usergrowth} /> */}
                <AverageGrowth />

                <div className="flex w-full mt-[2vw]">
                    <ItemTrends />

                    <BestSellingItems />
                </div>
                <UserCounts />
            </div>
        </div >
    );
};

export default Dashboard;
