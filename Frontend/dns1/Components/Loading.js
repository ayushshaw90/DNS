// components/Loading.js

import React from 'react';

const Loading = () => {
  return (
    <div className="fixed top-0 left-0 w-screen h-screen flex flex-col items-center gap-3 justify-center bg-gray-800 opacity-75">
      <div className="loader ease-linear rounded-full border-8 border-t-8 border-gray-200 h-24 w-24"></div>
      <h1 className=' text-xl text-[#60b6f0]'>Loading...</h1>
    </div>
  );
};

export default Loading;
