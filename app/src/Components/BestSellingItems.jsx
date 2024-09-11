import React, { useState, useEffect } from 'react';

const BestSellingItems = () => {
    const [sellingItems, setSellingItems] = useState([]);
    const [selectedPlace, setSelectedPlace] = useState('Aceh'); // Add state for selected place

    // Fetch data from the Flask endpoint
    useEffect(() => {
        const fetchSellingItems = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5000/data-ikan-berdasarkan-jenis-ikan-tangkap-laut');
                const data = await response.json();
                setSellingItems(data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchSellingItems();
    }, []);

    // Get unique provinces
    const uniqueProvinces = Array.from(new Set(sellingItems.map(item => item.province_name)));

    // Process the fetched data
    const filteredItems = sellingItems
        .filter(item => item.province_name === selectedPlace && item.jenis_ikan !== "" && item.total_value > 0)
        .map(item => ({
            nama: item.jenis_ikan,
            jumlah: item.total_value
        }));

    // Sort items by total value in descending order
    const sortedItems = filteredItems.sort((a, b) => b.jumlah - a.jumlah);

    // Get the top 10 items
    const top5Items = sortedItems.slice(0, 5);

    // Handle place selection
    const handlePlaceClick = (place) => {
        setSelectedPlace(place);
    };

    return (
        <div className="w-[60%] bg-white p-[2.5vw]">
            <div className="flex items-center justify-between">
                <div>
                    <h1 className="text-[1.2vw]">Jenis Tangkapan Terbanyak</h1>
                    <p className="text-[0.7vw]">(2020)</p>
                </div>

                <div className="flex w-[17vw] overflow-scroll mr-[2vw] items-center mt-[1vw]">
                    {uniqueProvinces.map((item, index) => (
                        <button
                            key={index}
                            className={`mr-[1.5vw] text-[0.8vw] cursor-pointer duration-300 ease-in-out ${item === selectedPlace ? 'text-black' : 'text-[#acacac]'}`}
                            onClick={() => handlePlaceClick(item)}
                        >
                            {item}
                        </button>
                    ))}
                </div>
            </div>

            <div className="mr-[2vw] mt-[1vw]">
                {top5Items.map((item, index) => (
                    <div className="w-full py-[0.9vw] bg-[#5299f5] rounded-[0.3vw] mb-[0.3vw]" key={index}>
                        <p className="text-[0.9vw] text-white px-[2vw] flex">
                            <span className="w-[40%]">{index + 1}. {item.nama}</span>
                            <span className="w-[10%]">|</span>
                            <span className="w-[20%]">Total: Rp.{item.jumlah.toLocaleString()}</span>
                            {/* Assuming avg_quantity is not provided, you may need to calculate it if needed */}
                        </p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default BestSellingItems;
