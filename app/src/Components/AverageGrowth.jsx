import React, { useEffect, useState } from 'react';

const AverageGrowth = () => {
    const [data, setData] = useState([]);
    const [selectedDate, setSelectedDate] = useState('2018');
    const [selectedPlace, setSelectedPlace] = useState('Aceh');

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5000/data-ikan-berdasarkan-wilayah');
                const result = await response.json();
                setData(result);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    const uniqueYears = Array.from(new Set(data.map(item => item.Year)));
    const uniqueProvinces = Array.from(new Set(data.map(item => item.province_name)));

    // Process data to get usergrowth based on unique years and provinces
    const usergrowth = data
        .filter(item => item.Year === selectedDate && item.province_name === selectedPlace && item.category_name !== "Jumlah")
        .map(item => ({
            jumlah: item.total_value,
            category: item.category_name
        }));

    const highest = Math.max(...usergrowth.map(item => parseFloat(item.jumlah)));

    const totalJumlah = data
        .filter(item => item.Year === selectedDate && item.province_name === selectedPlace && item.category_name === "Jumlah")
        .map(item => ({
            jumlah: item.total_value
        }));
    return (
        <div className="w-full bg-white mt-[2vw] py-[2vw] rounded-sm px-[3vw] flex justify-between">
            <div className="flex justify-between mb-[3vw]">
                <div>
                    <h1 className="text-[1.4vw] w-[18vw]">Jumlah Ikan (Berdasarkan Perairan Laut & Umum)</h1>
                    <select
                        name="date"
                        id="date"
                        className="outline-none text-[0.9vw] mt-[1vw] bg-white"
                        value={selectedDate}
                        onChange={(e) => setSelectedDate(e.target.value)}
                    >
                        {uniqueYears.map((item, index) => (
                            <option value={item} key={index}>{item}</option>
                        ))}
                    </select>
                    <br />
                    <select
                        name="places"
                        id="places"
                        className="outline-none text-[0.9vw] mt-[1vw] bg-white"
                        value={selectedPlace}
                        onChange={(e) => setSelectedPlace(e.target.value)}
                    >
                        {uniqueProvinces.map((item, index) => (
                            <option value={item} key={index}>{item}</option>
                        ))}
                    </select>
                    <div className="mt-[3vw] flex items-center justify-start">
                        <div className="w-[0.6vw] h-[0.6vw] bg-blue-400 mr-[0.3vw]"></div>
                        <p className="text-[0.8vw] mr-[1vw]">Laut</p>
                        <div className="w-[0.6vw] h-[0.6vw] bg-red-400 mr-[0.3vw]"></div>
                        <p className="text-[0.8vw] mr-[1vw]">Umum</p>
                    </div>
                </div>
            </div>

            {/* Charts */}
            <div className="w-[35vw] h-full flex flex-col ml-[-7vw] mt-[2vw] relative">
                <div className="w-full h-[10vw] flex justify-between">
                    <div className="w-[20%] flex items-start justify-center flex-col">
                        <div className="w-[0.1vw] bg-black h-full opacity-25"></div>
                        <p className="text-[0.8vw] w-full h-[2vw] mt-[1vw] border-t-[0.1vw] border-black pt-[1vw]">0</p>
                    </div>
                    {[highest / 4, (highest / 4) * 2, (highest / 4) * 3, highest].map((item, index) => (
                        <div className={`w-[20%] flex items-start justify-center flex-col`} key={index}>
                            <div className="w-[0.1vw] bg-black h-full opacity-25"></div>
                            <p className="text-[0.8vw] w-full h-[2vw] mt-[1vw] ml-[-1.5vw] border-t-[0.1vw] border-black pt-[1vw]">{Math.ceil(item)}</p>
                        </div>
                    ))}
                </div>
                <div className="w-[80%] h-full absolute left-0 top-0 flex justify-center flex-col ">
                    {usergrowth.map((item, index) => (
                        <div key={index} className={`${item.category === 'Perairan Umum Daratan' ? 'bg-red-400 mb-[3vw]' : 'bg-blue-400 mb-[1vw]'} h-[2vw] ${item.jumlah < 0 ? "hidden" : ""}`} style={{ width: `${item.jumlah / highest * 100}%` }}></div>
                    ))}
                </div>
            </div>

            <div className="flex items-center justify-center flex-col mt-[-3vw]">
                <p className="flex text-[2vw] items-center">
                    {totalJumlah.map((item, index) => (
                        Math.ceil(item.jumlah)
                    ))}
                </p>
                <p className="text-[1vw] text-center">Total
                    <br />
                    <span className='text-[0.6vw]'>(From Both)</span>
                </p>
            </div>
        </div>
    );
};

export default AverageGrowth;
