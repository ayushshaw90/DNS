
import { useState } from 'react';
import Details from '../../Components/Details/index'
import Prediction from '../../Components/Prediction/index'
export default function Index(){

    const [showDetail, setShowDetail] = useState(false);
    const [predict, setPredict] = useState(false);

    const handleClick = () => {
        setPredict(false);
      setShowDetail(!showDetail);
    };
    const handle = () => {
        setShowDetail(false);
        setPredict(!predict);
    };

    return(
        <>
        <div className='flex flex-col  pr-8 pt-4 gap-12  '>
        <h1 className='text-white text-xl pl-48 font-semibold'>Domain Details</h1>
        <div className="flex flex-wrap justify-evenly items-center">
        <div className="flex gap-3">
        <label className="text-white text-lg"> Domain Name: </label>
        <input type="text" className="text-black p-1 shadow-md shadow-black rounded-md " placeholder="Enter Domain Name"/>
        </div>
        
        <button onClick={handleClick} className="p-3 shadow-black shadow-lg rounded-md text-white text-lg bg-[url('https://res.cloudinary.com/ddtzbznea/image/upload/v1702463464/background-card-reports_hwlwq5.png')] hover:shadow-white">Domain Details</button>
        
        
        <button onClick={handle} className="p-3 rounded-md shadow-lg shadow-black bg-[url('https://res.cloudinary.com/ddtzbznea/image/upload/v1702463464/background-card-reports_hwlwq5.png')] text-white text-lg hover:shadow-white ">Predict</button>
        </div>
        {showDetail&& <Details/> }
        {predict && <Prediction/>}

        </div>
        
        </>
    )
}