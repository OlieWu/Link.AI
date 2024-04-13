import React, { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";


const Result = () => {
    const navigate = useNavigate();
    const backSearch = () => {
        // Perform search here
        // Redirect to home page
        navigate("/");
    };
    return (
        <div>
            <h1>Result</h1>
            <button onClick={backSearch}>Back to Search</button>
        </div>
    );
}

export default Result;