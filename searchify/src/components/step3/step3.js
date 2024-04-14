import React, { useState, useEffect } from 'react';
import step3 from '../../icons/step3.svg';
import './step3.css';

const Step3 = ({handleMood, handleMusicTypes, handleSpecialRequirements}) => {
  const [mood, setMood] = useState('');
  const [musicTypes, setMusicTypes] = useState('');
  const [specialRequirements, setSpecialRequirements] = useState('');

  return (
    <>
      <div className="step">
        <h2>Step 3</h2>
        <img className='stepviz' src={step3} alt='step3' />
      </div>
      <form className="step3">
        <label>
          I’m in a mood of
          <textarea
            value={mood}
            onChange={(e) => {
              console.log(e.target.value);
              setMood(e.target.value);
              handleMood(e.target.value);
            }}
            placeholder="Describe your mood"
          />
        </label>
        <label>
          I like these music types
          <textarea
            value={musicTypes}
            onChange={(e) => {
              setMusicTypes(e.target.value);
              handleMusicTypes(e.target.value);
            }}
            placeholder="Enter music types"
          />
        </label>
        <label>
          Any special requirements go here
          <textarea
            value={specialRequirements}
            onChange={(e) => {
              setSpecialRequirements(e.target.value);
              handleSpecialRequirements(e.target.value);
            }}
            placeholder="Any special requirements"
          />
        </label>
      </form>
    </>
  );
}

export default Step3;