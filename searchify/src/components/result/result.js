import React, { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import SongsList from '../songList/songList';
import { useLocation } from 'react-router-dom';
import './result.css';

const Result = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const recommendations = new URLSearchParams(location.search).get('recommendations');
    console.log(recommendations);

    const backSearch = () => {
        // Perform search here
        // Redirect to home page
        navigate("/");
    };


    return (
        <div>
            <h1>Da Da, here it is</h1>
            <SongsList recommendations={recommendations} />
            <div className="back-container">
                <button className="textbutton" onClick={backSearch}>Back</button>
            </div>
        </div>
    );
}

export default Result;