
import { useState } from 'react';
// import Details from '../../Components/Details/index'
// import Prediction from '../../Components/Prediction/index'
export default function Index(){
    const [inputData, setInputData] = useState('');
    const [response, setResponse] = useState(null);
  
    const handleInputChange = (e) => {
      setInputData(e.target.value);
    };
  
 

  const sendDataToServer = async () => {
    const url = 'http://4.240.110.164:5000/getdetails';

    try {
      // Define the data you want to send in the POST request
      const data = {
        domain_name: inputData,
      };

    //   Send the POST request
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      // Parse the JSON response
      const responseData = await response.json();
      console.log(responseData);
      // Update the state with the response data
      setResponse(responseData);

      
      console.log(responseData);
    } catch (error) {
      console.error('Error sending POST request:', error);
    }
  };
  return(
        <>
        <div className='flex flex-col  gap-12  '>
        <h1 className='text-white text-xl font-semibold'>Domain Details</h1>
        <div className="flex flex-wrap justify-evenly items-center">
        <div className="flex gap-3">
        <label className="text-white text-lg"> Domain Name: </label>
        <input type="text" value={inputData} onChange={handleInputChange} className="text-black p-1 shadow-md shadow-black rounded-md " placeholder="Enter Domain Name"/>
        </div>
        
        <button onClick={sendDataToServer}  className="p-3 shadow-black shadow-lg rounded-md text-white text-lg bg-[url('https://res.cloudinary.com/ddtzbznea/image/upload/v1702463464/background-card-reports_hwlwq5.png')] hover:shadow-white">Domain Details</button>
        
        
        <button  className="p-3 rounded-md shadow-lg shadow-black bg-[url('https://res.cloudinary.com/ddtzbznea/image/upload/v1702463464/background-card-reports_hwlwq5.png')] text-white text-lg hover:shadow-white ">Predict</button>
        </div>

        {response && (
        <div>
          <h2 className='text-xl text-white'>Response from Server:</h2>
          {/* <pre className='text-white'>{JSON.stringify(response, null, 2)}</pre> */}
          {/* <h2>{response.A}</h2> */}
          <h1 className='text-white text-xl text-center pb-2'>Domain Name: {response.domain_name}</h1>
          <div className='grid grid-cols-2  gap-4'>
          <div className='yo p-3 text-white rounded-lg shadow-lg shadow-black'>
            
          <h2 className='text-xl font-semibold'>Type A</h2>  <br></br>
          {response.A && response.A.length > 0 ? (
            <div>
          {response.A.map((entry) => (
            <div key={entry?.ip_address}>
              <p>ASN Date: {entry?.asn_date}</p>
              <p>Country Code: {entry?.country_code}</p>
              <p>IP Address: {entry?.ip_address}</p>
              <p>Last Updated: {entry?.last_updated}</p>
              <p>Registration Timestamp: {entry?.reg_timestamp}</p>
              
            </div>
          ))}
          </div>):(<p>No data available for Type A.</p>)}
          </div>
          <div className='yo p-3 text-white rounded-lg shadow-lg shadow-black'>
          <h2 className='text-xl font-semibold'>Type AAAA </h2><br></br>
      {response.AAAA && response.AAAA.length > 0 ? (
        <div>
          {response.AAAA.map((entry) => (
            <div key={entry?.ip_address}>
              <p>ASN Date: {entry?.asn_date}</p>
              <p>Country Code: {entry?.country_code}</p>
              <p>IP Address: {entry?.ip_address}</p>
              <p>Last Updated: {entry?.last_updated}</p>
              <p>Registration Timestamp: {entry?.reg_timestamp}</p>
              
            </div>
          ))}
        </div>
      ) : (
        <p>No data available for Type AAAA (IPv6).</p>
      )}
      </div>
      <div className='yo p-3 text-white rounded-lg shadow-lg shadow-black'>
      <h2 className='text-xl font-semibold'>Type MX</h2><br></br>
      {response.MX && response.MX.length > 0 ? (
        <div>
          {response.MX.map((entry, index) => (
            <div key={index}>
              <p>MX Record: {entry}</p>
              
            </div>
          ))}
        </div>
      ) : (
        <p>No data available for Type MX.</p>
      )}
      </div>
      <div className='yo p-3 text-white rounded-lg shadow-lg shadow-black'>
      <h2 className='text-xl font-semibold'>Type NS</h2><br></br>
      {response.NS && response.NS.length > 0 ? (
        <div>
          {response.NS.map((entry, index) => (
            <div key={index}>
              <p>NS Record: {entry}</p>
              
            </div>
          ))}
        </div>
      ) : (
        <p>No data available for Type NS.</p>
      )}
      </div>
      <div className='yo p-3 text-white rounded-lg shadow-lg shadow-black'>
      <h2 className='text-xl font-semibold'>Type SOA</h2><br></br>
      {response.SOA && response.SOA.length > 0 ? (
        <div>
          {response.SOA.map((entry, index) => (
            <div key={index}>
              <p>SOA Record: {entry}</p>
              
            </div>
          ))}
        </div>
      ) : (
        <p>No data available for Type SOA.</p>
      )}
      </div>
      <div className='yo p-3 text-white rounded-lg shadow-lg shadow-black'>
      <h2 className='text-xl font-semibold'>Type TXT</h2><br></br>
      {response.TXT && response.TXT.length > 0 ? (
        <div>
          {response.TXT.map((entry, index) => (
            <div key={index}>
              <p>TXT Record: {entry}</p>
              
            </div>
          ))}
        </div>
      ) : (
        <p>No data available for Type TXT.</p>
      )}
      </div>
      <div className='yo p-3 text-white rounded-lg shadow-lg shadow-black'>
      <h2 className='text-xl font-semibold'>Type CNAME</h2><br></br>
      {response.CNAME && response.CNAME.length > 0 ? (
        <div>
         
              <p>CNAME Record: {response.CNAME}</p>
              <hr />
            
        </div>
      ) : (
        <p>No data available for Type CNAME.</p>
      )}
      </div>
      <div className='yo p-3 text-white rounded-lg shadow-lg shadow-black'>
 <h2 className='text-xl font-semibold'>Type SRV</h2><br></br>
{response.SRV && response.SRV.length > 0 ? (
        <div>
          {response.SRV.map((entry,index) => (
            <div key={index}>
              <p>Priority: {entry?.priority}</p>
              <p>Weight: {entry?.weight}</p>
              <p>Port: {entry?.port}</p>
              <p>Target: {entry?.target}</p>
              
              
            </div>
          ))}
        </div>
      ) : (
        <p>No data available for Type SRV.</p>
      )}
      </div>
      <div className='yo p-3 text-white rounded-lg shadow-lg shadow-black'>
    <h2 className='text-xl font-semibold'>Type PTR</h2><br></br>
      {response.PTR && response.PTR.length > 0 ? (
        <div>
         
              <p>PTR Record: {response.PTR}</p>
              
            
        </div>
      ) : (
        <p>No data available for Type PTR.</p>
      )}

        </div>
        </div>
        </div>
      )}
       

        </div>
        
        </>
    )
}