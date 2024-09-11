import React, { useState, useEffect } from 'react';

const UserCounts = () => {
    const [dataikan, setDataikan] = useState([]);
    const [selectedYear, setYear] = useState('2017');
    const [selectedProvince, setProvince] = useState('Bali');

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5000/data-ikan-berdasarkan-metode');
                const data = await response.json();
                setDataikan(data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    const uniqueProvince = [...new Set(dataikan.map(item => item.province))];
    const uniqueYear = [...new Set(dataikan.map(item => item.year))];

    const dataFinal = dataikan
        .filter(item => item.year === selectedYear && item.province === selectedProvince)
        .map(item => ({
            method: item.method,
            total: parseFloat(item.value)
        }));

    const highest = dataFinal.length > 0
        ? Math.max(...dataFinal.map(item => item.total).filter(value => !isNaN(value)))
        : 0; // Handle empty dataFinal

    const formatNumber = (number) => {
        return number.toLocaleString(); // Formats number with commas
    };
    return (
        <div className="w-full bg-white mt-[2vw] pt-[2vw] pb-[5vw] px-[3vw] relative">
            <div className="w-full flex justify-between mb-[3vw]">
                <div>
                    <h1 className="text-[1.4vw]">Nilai Produksi Budidaya (Rp) Berdasarkan Metode Penangkapan</h1>
                </div>
                <div className="flex items-center justify-center pr-[2vw]">
                    <select
                        name="year"
                        id="year"
                        className="text-[1vw] mt-[0.3vw] outline-none pr-[1vw] mr-[2vw]"
                        value={selectedYear}
                        onChange={(e) => setYear(e.target.value)}
                    >
                        {uniqueYear.map((item, index) => (
                            <option
                                value={item}
                                key={index}
                                className={`mr-[1.5vw] cursor-pointer duration-300 ease-in-out ${item !== selectedYear ? 'text-[#acacac]' : 'text-black'}`}
                            >
                                {item}
                            </option>
                        ))}
                    </select>
                    <select
                        name="province"
                        id="province"
                        className="text-[1vw] mt-[0.3vw] outline-none"
                        value={selectedProvince}
                        onChange={(e) => setProvince(e.target.value)}
                    >
                        {uniqueProvince.map((item, index) => (
                            <option
                                value={item}
                                key={index}
                                className={`mr-[1.5vw] cursor-pointer duration-300 ease-in-out ${item !== selectedProvince ? 'text-[#acacac]' : 'text-black'}`}
                            >
                                {item}
                            </option>
                        ))}
                    </select>
                </div>
            </div>
            {/* Bar Charts */}
            <div className="h-[20vw] w-full mt-[1vw] px-[0.2vw] pb-[2vw] relative">
                {/* SIDEBAR */}
                {[highest * 0.25, highest * 0.50, highest * 0.75, highest].map((value, index) => (
                    <div key={index} className="w-full flex h-[25%] items-center justify-center">
                        <p className="w-[1vw] text-center text-[0.9vw]">Rp. {value !== null ? formatNumber(value) : ''}</p>
                        <div className="h-[0.05vw] ml-[7vw] w-full bg-[#373737] opacity-25"></div>
                    </div>
                ))}
                {/* CHARTS */}
                <div className="w-[90%] h-full top-0 absolute flex items-end justify-end ml-[7vw] pr-[2.4vw] mt-[3vw]">
                    <div className="overflow-x-scroll w-full">
                        <div className="w-[210vw] h-[14.5vw] mb-[1vw] pl-[2vw] flex items-end">
                            {dataFinal.map((item, index) => (
                                <div key={index} className="w-[4vw] mr-[5.5vw] h-full flex items-end">
                                    <div className={`w-[2vw] duration-2s ease bg-red-400`} style={{ height: `${(item.total / highest) * 100}%` }}></div>
                                </div>
                            ))}
                        </div>
                        <div className="w-[210vw] pl-[2vw] flex pt-[1vw] items-end border-t-[0.1vw] border-[#909090]">
                            {dataFinal.map((item, index) => (
                                <div className="h-[100%] text-center w-[4vw] text-[0.9vw] mr-[5.5vw]" key={index}>
                                    {item.method}
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default UserCounts;
