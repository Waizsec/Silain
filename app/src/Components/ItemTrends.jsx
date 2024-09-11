import React, { useState, useEffect } from 'react';
import { PieChart, Pie, Cell, Legend, ResponsiveContainer } from 'recharts';

const ItemTrends = () => {
    const [sellingItems, setSellingItems] = useState([]);
    const [selectedYear, setSelectedYear] = useState('2018'); // Replace with your default year
    const [selectedProvince, setSelectedProvince] = useState('Aceh'); // Replace with your default province

    useEffect(() => {
        const fetchSellingItems = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5000/data-ikan-berdasarkan-medan');
                const data = await response.json();
                setSellingItems(data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchSellingItems();
    }, []);

    const uniqueYears = Array.from(new Set(sellingItems.map(item => item.Year)));
    const uniqueProvinces = Array.from(new Set(sellingItems.map(item => item.province_name)));

    // Filter, sort, and process the data
    const filteredItems = sellingItems
        .filter(item => item.Year === selectedYear && item.province_name === selectedProvince && item.total_value !== "-")
        .map(item => ({
            location: item.location_name,
            total: parseFloat(item.total_value) // Convert total_value to number
        }));

    const data = filteredItems.map(item => ({
        name: item.location,
        value: parseInt(item.total, 10),
    }));

    const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#FDFAS3', '#AF19E0'];

    return (
        <div className="w-[40%] bg-white px-[3vw] py-[2.5vw] mr-[1vw]">
            <div className="flex items-center justify-between">
                <div>
                    <h1 className="text-[1.2vw]">Jumlah Ikan (Berdasarkan Medan)</h1>
                </div>

                <div className="flex flex-col">
                    <select
                        name="province"
                        id="province"
                        className="text-[1vw] mt-[0.3vw] outline-none"
                        value={selectedProvince}
                        onChange={(e) => setSelectedProvince(e.target.value)}
                    >
                        {uniqueProvinces.map((item, index) => (
                            <option
                                value={item}
                                key={index}
                                className={`mr-[1.5vw] cursor-pointer duration-300 ease-in-out ${item !== selectedProvince ? 'text-[#acacac]' : 'text-black'}`}
                            >
                                {item}
                            </option>
                        ))}
                    </select>
                    <select
                        name="year"
                        id="year"
                        className="text-[1vw] mt-[0.3vw] outline-none"
                        value={selectedYear}
                        onChange={(e) => setSelectedYear(e.target.value)}
                    >
                        {uniqueYears.map((item, index) => (
                            <option
                                value={item}
                                key={index}
                                className={`mr-[1.5vw] cursor-pointer duration-300 ease-in-out ${item !== selectedYear ? 'text-[#acacac]' : 'text-black'}`}
                            >
                                {item}
                            </option>
                        ))}
                    </select>
                </div>
            </div>

            <ResponsiveContainer width="100%" height={400}>
                <PieChart>
                    <Pie
                        data={data}
                        dataKey="value"
                        cx="50%"
                        cy="50%"
                        outerRadius={80}
                        fill="#8884d8"
                        label
                    >
                        {data.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                        ))}
                    </Pie>
                    <Legend />
                </PieChart>
            </ResponsiveContainer>
        </div>
    );
};

export default ItemTrends;
