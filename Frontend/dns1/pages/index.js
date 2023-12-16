import Image from 'next/image'
import Link from 'next/link'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowRight } from '@fortawesome/free-solid-svg-icons';
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
  return (

    <div>
       {isLoading ? (
        <Loading />
      ) : (
    
          <div className='flex flex-col pl-48 pr-8 pt-4 gap-12  '>
            <h1 className='text-white text-xl font-semibold'>Dashboard</h1>
            <div className='grid grid-cols-3 gap-8 overflow-hidden'> 
              <div className=" text-white shadow-lg shadow-black  h-[24rem] bg-cover bg-no-repeat rounded-lg bg-[url('https://res.cloudinary.com/ddtzbznea/image/upload/v1702465492/cardimgfree_wr2cmr.png')]">
                <h1> Welcome! </h1>
                <h1>To website name</h1>
              </div>
              <div className=" yo rounded-lg  shadow-lg shadow-black"> 
              <div className='pt-2'>
                <h1 className='text-center text-white'>Blacklisted Domains</h1>
                </div>
              </div>
              <div className=" yo rounded-lg h-[24rem] shadow-lg shadow-black"> 
              <div className='pt-2'>
                <h1 className='text-center text-white'>Whitelisted Domains</h1>
                </div>
              </div>
              </div>
              <div className="yo rounded-lg  shadow-lg shadow-black"> 
              <div className='pt-2'>
                <h1 className='text-center text-white border-b'>Blacklisted Domains</h1>
                <div className='flex pt-2 justify-around text-white'>
                   <h1>Domain Name</h1>
                   <h1>No. of Requests</h1>
                   <h1>No.of Subdomains</h1>
                </div>
                </div>
              </div>
            
          </div>
      )}
    </div>
  )
}
