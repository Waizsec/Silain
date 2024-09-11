import React from 'react';
import { LineUserCounts } from '.';

const UserCounts = (props) => {
    const date = 'December 2023'; // Static date
    const highestUser = 3000; // Static highest user count
    const totalusers = 10000; // Static total users

    const totaluser = [
        { region: 'Region1', total: 1200, type: 'individual' },
        { region: 'Region2', total: 800, type: 'company' },
        { region: 'Region3', total: 500, type: 'individual' },
        { region: 'Region4', total: 300, type: 'company' },
    ]; // Static user data

    const uniqueRegions = [...new Set(totaluser.map(item => item.region))];

    function formatNumber(value) {
        if (Number.isInteger(value)) {
            return value.toFixed(0);
        } else {
            return value.toFixed(2);
        }
    }

    const formattedValues = [
        formatNumber(highestUser),
        formatNumber(highestUser * 0.75),
        formatNumber(highestUser * 0.50),
        formatNumber(highestUser * 0.25),
        null
    ];

    return (
        <>
            <div className="w-full bg-white mt-[2vw] pt-[2vw] pb-[5vw] px-[3vw] relative">
                <div className="w-full flex justify-between mb-[3vw]">
                    <div>
                        <h1 className="text-[1.4vw]">New Users Registered</h1>
                        <select name="date" id="date" className="outline-none text-[0.9vw] mt-[1vw]" value={date} disabled>
                            <option value={date}>{date}</option>
                        </select>
                    </div>
                    <div className="flex items-center justify-center pr-[2vw]">
                        <img src="/image/icons/customer.svg" className="w-[4vw]" alt="" />
                        <p className="ml-[2vw] text-[0.8vw] text-[#A3AED0]">
                            Total Users
                            <br />
                            <span className="text-[1.5vw] text-[#2B3674]">
                                {totalusers}
                            </span>
                        </p>
                    </div>
                </div>
                {/* Bar Charts */}
                <div className="h-[20vw] w-full mt-[1vw] px-[0.2vw] pb-[2vw] relative">
                    {/* SIDEBAR */}
                    {formattedValues.map((value, index) => (
                        <div key={index} className="w-full flex h-[20%] items-center justify-center">
                            <p className="w-[1vw] text-center text-[0.9vw]">{value !== null ? value : ''}</p>
                            <div className="h-[0.05vw] ml-[1vw] w-full bg-[#373737] opacity-25"></div>
                        </div>
                    ))}
                    {/* Tag */}
                    <div className="absolute top-0 right-0 flex items-center justify-center">
                        <div className="w-[0.6vw] h-[0.6vw] bg-blue-400 mr-[0.3vw]"></div>
                        <p className="text-[0.8vw] mr-[1vw]">Individual</p>
                        <div className="w-[0.6vw] h-[0.6vw] bg-red-400 mr-[0.3vw]"></div>
                        <p className="text-[0.8vw] mr-[1vw]">Company</p>
                    </div>
                    {/* CHARTS */}
                    <div className="w-full h-full top-0 absolute flex items-end justify-end ml-[2vw] pr-[2.4vw] mt-[0.4vw]">
                        <div className="overflow-x-scroll w-full">
                            <div className="w-[210vw] h-[14.5vw] mb-[1vw] pl-[2vw] flex items-end">
                                {uniqueRegions.map((region, outerIndex) => (
                                    <div key={outerIndex} className="w-[4vw] mr-[5.5vw] h-full flex items-end">
                                        {totaluser
                                            .filter(item => item.region === region)
                                            .map((item, innerIndex) => (
                                                <div key={innerIndex} className={`w-[2vw] duration-2s ease ${item.type === 'company' ? 'bg-red-400' : 'bg-biru'}`} style={{ height: `${(item.total / highestUser) * 100}%` }}></div>
                                            ))}
                                    </div>
                                ))}
                            </div>
                            <div className="w-[210vw] pl-[2vw] flex pt-[1vw] items-end border-t-[0.1vw] border-[#909090]">
                                {uniqueRegions.map((region, outerIndex) => (
                                    <div className="h-[100%] text-center w-[4vw] text-[0.9vw] mr-[5.5vw]" key={outerIndex}>
                                        {region}
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default UserCounts;
