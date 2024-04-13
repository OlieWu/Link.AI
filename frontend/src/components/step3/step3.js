import React, { useState, useEffect } from 'react';

const Step3 = () => {
    const [mood, setMood] = useState('');
    const [musicTypes, setMusicTypes] = useState('');
    const [specialRequirements, setSpecialRequirements] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        // Process the data here or pass it to parent component
        console.log({ mood, musicTypes, specialRequirements });
        // Call onNext to proceed to the next step
        onNext();
    };

    return (
        <form className="step3" onSubmit={handleSubmit}>
          <h1>Customize your playlist</h1>
          <h2>Step 3</h2>
          <label>
            I’m in a mood of
            <textarea 
              value={mood}
              onChange={(e) => setMood(e.target.value)}
              placeholder="Describe your mood"
            />
          </label>
          <label>
            I like these music types
            <textarea 
              value={musicTypes}
              onChange={(e) => setMusicTypes(e.target.value)}
              placeholder="Enter music types"
            />
          </label>
          <label>
            Any special requirements go here
            <textarea 
              value={specialRequirements}
              onChange={(e) => setSpecialRequirements(e.target.value)}
              placeholder="Any special requirements"
            />
          </label>
        </form>
    );
}

export default Step3;