import React, { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import SongsList from '../songList/songList';

const Result = () => {
    const navigate = useNavigate();
    const backSearch = () => {
        // Perform search here
        // Redirect to home page
        navigate("/");
    };
    return (
        <div>
            <h1>Da Da, here it is</h1>
            <SongsList />
            <button className="textbutton" onClick={backSearch}>Back</button>
        </div>
    );
}

export default Result;