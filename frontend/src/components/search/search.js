import React, { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import Step1 from '../step1/step1';
import Step2 from '../step2/step2';
import Step3 from '../step3/step3';
import prev from '../../icons/prev.svg';
import next from '../../icons/next.svg';
import './search.css';

const Search = () => {
    const [step, setStep] = useState(1);
    const navigate = useNavigate();

    const handleNext = () => {
        setStep(step + 1);
    };

    const handlePrev = () => {
        setStep(step - 1);
    };

    const renderStep = () => {
        switch (step) {
            case 1:
                return <Step1 />;
            case 2:
                return <Step2 />;
            case 3:
                return <Step3 />;
            default:
                return <Step1 />;
        }
    };
    const performSearch = () => {
        // Perform search here
        // Redirect to result page
        navigate("/result");
    };
    return (
        <div>
            <h1>Customize your playlist</h1>
            {renderStep()}
            <div className="button-container">
                <button className="iconbutton" onClick={handlePrev}>
            {step !== 1 && (
                    <img src={prev} alt='prev' />
                
            )}
            </button>

            <button className="iconbutton" onClick={handleNext}>
            {step !== 3 && (
                    <img src={next} alt='next' />
                
            )}
            </button>
            
            {step === 3 && (
                <button className="textbutton" onClick={performSearch} disabled={step !== 3}>Search</button>
            )}
            </div>
        </div>
    );
}

export default Search;