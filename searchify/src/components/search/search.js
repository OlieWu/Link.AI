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

    const [mood, setMood] = useState('');
    const [musicTypes, setMusicTypes] = useState('');
    const [specialRequirements, setSpecialRequirements] = useState('');

    const handleMood = (data) => {
        setMood(data);
    }

    const handleMusicTypes = (data) => {
        setMusicTypes(data);
    }

    const handleSpecialRequirements = (data) => {
        setSpecialRequirements(data);
    }
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
                return <Step3 
                    handleMood={handleMood}
                    handleMusicTypes={handleMusicTypes}
                    handleSpecialRequirements={handleSpecialRequirements}
                />;
            default:
                return <Step1 />;
        }
    };
    // const performSearch = () => {
    //     // Perform search here
    //     // Redirect to result page
    //     navigate("/result");
    // };

    const performSearch = async (event) => {
        event.preventDefault(); // TODO: figure out if this is an issue
        // Process the data here or pass it to parent component
        console.log({ mood, musicTypes, specialRequirements });
        console.log("this guy is called");
    
        // Send request to endpoint in backend
        try {
          const data = {
            "mood": mood,
            "musicTypes": musicTypes,
            "specialRequirements": specialRequirements
          }
          
          const response = await fetch("http://localhost:5000/recommendations", {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
          });
    
          if (!response.ok) {
            throw new Error(`Error fetching data: ${response.status}`);
          }
          console.log(response);
          
          // TODO: we need to go to SongList and pass in this information here
          // setData(fetchedData);
          // we should be redirected by flask
    
        } catch (error) {
            console.error(error.message);
        } finally {
          console.log("hello");
            // setIsLoading(false);
        }
        // Parce data to Gemini
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