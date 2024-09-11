import React from 'react';

const BestSellingItems = () => {
    // Hardcoded values for month and best-selling items
    const month = 'March 2023';

    const bestSellingItems = [
        { items: 'Item 1', total_quantity: 1000, avg_quantity: 200, dates: 'March 2023' },
        { items: 'Item 2', total_quantity: 800, avg_quantity: 160, dates: 'March 2023' },
        { items: 'Item 3', total_quantity: 600, avg_quantity: 120, dates: 'March 2023' },
        { items: 'Item 4', total_quantity: 400, avg_quantity: 80, dates: 'March 2023' },
        { items: 'Item 5', total_quantity: 200, avg_quantity: 40, dates: 'March 2023' },
    ];

    const months = [
        'January 2023', 'February 2023', 'March 2023', 'April 2023', 'May 2023', 'June 2023',
        'July 2023', 'August 2023', 'September 2023', 'October 2023', 'November 2023', 'December 2023'
    ];

    // No need for updateMonth function since the month is static

    // Sort the best-selling items array based on total_quantity in descending order
    const sortedItems = bestSellingItems.sort((a, b) => {
        return parseInt(b.total_quantity, 10) - parseInt(a.total_quantity, 10);
    });

    // Get the top 5 items (though already static, retaining the logic for clarity)
    const top5Items = sortedItems.slice(0, 5);
    return (
        <div className="w-[60%] bg-white p-[2.5vw]">
            <div className="flex items-center justify-between">
                <div className="">
                    <h1 className="text-[1.2vw]">Best Selling Items</h1>
                    <p className="text-[0.7vw]">(All Places)</p>
                </div>

                <div className="flex w-[17vw] overflow-scroll mr-[2vw] items-center mt-[1vw]">
                    {months.map((item, index) => (
                        <button
                            key={index}
                            className={`mr-[1.5vw] text-[0.8vw] cursor-pointer duration-300 ease-in-out ${item !== month ? 'text-[#acacac]' : 'text-black'}`}
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
                            <span className="w-[40%]">{index + 1}. {item.items}</span>
                            <span className="w-[10%]">|</span>
                            <span className="w-[20%]">Total: {item.total_quantity}</span>
                            <span className="w-[10%]">|</span>
                            <span className="w-[20%]">Average: {item.avg_quantity}</span>
                        </p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default BestSellingItems;
