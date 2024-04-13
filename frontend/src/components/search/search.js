import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";
import Step1 from '../step1/step1';
import Step2 from '../step2/step2';
import Step3 from '../step3/step3';

const Search = () => {
    const [step, setStep] = useState(1);
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
    return (
        <div>
            <h1>Customize your playlist</h1>
            <h2>Step {step}</h2>
            {renderStep()}
            <button onClick={handlePrev} disabled={step === 1}>Previous</button>
            <button onClick={handleNext} disabled={step === 3}>Next</button>
        </div>
    );
}

export default Search;