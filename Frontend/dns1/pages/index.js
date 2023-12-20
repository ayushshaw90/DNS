import Image from 'next/image'

import React, { useState, useEffect } from 'react';
import Loading from '../components/Loading';

export default function Index() {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    
    const fakeAsyncOperation = () => {
      setTimeout(() => {
        setIsLoading(false);
      }, 2000);
    };

    fakeAsyncOperation();
  }, []);
  const data=[
    {
      name:'adblock.gjtech.net',
      white:'google.com'
    },
    {
      name:'spam404bl.com',
      white:'youtube.com'
    },
    {
      name:'hufilter.hu',
      white:'facebook.com'
    },
    {
      name:'fredfiber.no',
      white:'twitter.com'
    },
    {
      name:'securemecca.com',
      white:'googleadservices.com'
    },
    {
      name:'vin-plastiks.com',
      white:'instagram.com'
    },
    {
      name:'juvander.net',
      white:'github.com'
    },
    {
      name:'allblock.net',
      white:'microsoft.com'
    },
    {
      name:'acclaimsports.com',
      white:'apple.com'
    },

  ];
  return (

    <div>
       {isLoading ? (
        <Loading />
      ) : (
    
          <div className='flex flex-col gap-12  '>
            {/* <h1 className='text-white text-xl font-semibold'>Dashboard</h1> */}
            <h1 className='text-white text-xl font-semibold border border-gray-1000 rounded-md text-center'>Dashboard</h1>
            <div className='grid  grid-cols-3 gap-8 overflow-hidden'> 
              {/* <div className=" text-white shadow-lg shadow-black  h-[24rem] bg-cover bg-no-repeat rounded-lg bg-[url('https://res.cloudinary.com/ddtzbznea/image/upload/v1702465492/cardimgfree_wr2cmr.png')]">
                <h1> Welcome! </h1>
                <h1>To website name</h1>
              </div> */}
              <div className="text-white shadow-lg shadow-black bg-cover bg-no-repeat rounded-lg bg-[url('https://res.cloudinary.com/ddtzbznea/image/upload/v1702465492/cardimgfree_wr2cmr.png')] flex flex-col justify-center items-center p-4 md:p-8 lg:p-12">
                <h1 className="text-center text-lg md:text-2xl lg:text-3xl xl:text-4xl 2xl:text-5xl font-bold mb-2"> Welcome to </h1>
                <h1 className="text-center text-xl md:text-3xl lg:text-4xl xl:text-5xl 2xl:text-6xl font-bold mb-4">SecureShield</h1>
                <p className="text-center text-base md:text-lg lg:text-xl xl:text-2xl 2xl:text-3xl">
                  <i>Navigate safely, </i><i>Navigate securely.</i>
                </p>
              </div>

              <div className=" yo rounded-lg  shadow-lg shadow-black"> 
              <div className='pt-2'>
                <h1 className='text-center text-white pb-2 text-lg'>Blacklisted Domains</h1>
                {data.map((d, index) => (
                  <div key={index}>
                    <h1 className='text-white pt-1 text-center'>{d.name}</h1>

                    </div>
                ))}
                </div>
              </div>
              <div className=" yo rounded-lg h-[24rem] shadow-lg shadow-black"> 
              <div className='pt-2'>
                <h1 className='text-center text-white text-lg'>Whitelisted Domains</h1>
                {data.map((d, index) => (
                  <div key={index}>
                    <h1 className='text-white pt-1 text-center'>{d.white}</h1>

                    </div>
                ))}
                </div>
              </div>
              </div>
              {/* <div className="yo rounded-lg  shadow-lg shadow-black"> 
              <div className='pt-2'>
                <h1 className='text-center text-white border-b'>Blacklisted Domains</h1>
                <div className='flex pt-2 justify-around text-white'>
                   <h1>Domain Name</h1>
                   <h1>No. of Requests</h1>
                   <h1>No.of Subdomains</h1>
                </div>
                </div>
              </div> */}
            
          </div>
      )}
    </div>
  )
}
