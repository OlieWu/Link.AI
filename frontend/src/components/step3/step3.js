import React, { useState, useEffect } from 'react';
import step3 from '../../icons/step3.svg';
import './step3.css';

const Step3 = () => {
  const [mood, setMood] = useState('');
  const [musicTypes, setMusicTypes] = useState('');
  const [specialRequirements, setSpecialRequirements] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault(); // TODO: figure out if this is an issue
    // Process the data here or pass it to parent component
    console.log({ mood, musicTypes, specialRequirements });

    // Send request to endpoint in backend
    try {
      data = {
        "mood": mood,
        "musicTypes": musicTypes,
        "specialRequirements": specialRequirements
      }
      const response = await fetch("/recommendations", {
        method: 'POST', // Specify POST method
        headers: { 'Content-Type': 'application/json' }, // Set content type
        body: JSON.stringify(data), // Stringify data object
      });

      if (!response.ok) {
        throw new Error(`Error fetching data: ${response.status}`);
      }
      const songs = await response.json();
      // TODO: we need to go to SongList and pass in this information here
      // setData(fetchedData);
    } catch (error) {
        setError(error.message);
    } finally {
        setIsLoading(false);
    }
    // Parce data to Gemini
  };

  return (
    <>
      <div className="step">
        <h2>Step 3</h2>
        <img className='stepviz' src={step3} alt='step3' />
      </div>
      <form className="step3" onSubmit={handleSubmit}>
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
    </>
  );
}

export default Step3;