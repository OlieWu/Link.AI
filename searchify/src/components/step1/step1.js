import React, { useState, useEffect } from 'react';
import step1 from '../../icons/step1.svg';
import spotify from '../../icons/spotify.svg';
import './step1.css';

const Step1 = () => {
  const handleLogin = async () => {
    // make a call to /login
    try {
      const response = await fetch("http://localhost:5000/login");
      console.log("hello");
      if (!response.ok) {
        console.log("status", response);
        // TODO: display error
        throw "Error";
      }

      // TODO: call redirect here
      const data = await response.json();
      console.log("url", data["url"]);
      // navigate(data["url"]);
      window.open(data["url"], "_blank");
      // window.location.href = newLocation;
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
      <div>
          <div className="step">
              <h2>Step 1</h2>
              <img className='stepviz' src={step1} alt='step1' />

          </div>
          <div className='spotify_login'>
              <img src={spotify} />
              <button className="textbutton" onClick={handleLogin}>Login</button>
          </div>
      </div>
  );
}

export default Step1;