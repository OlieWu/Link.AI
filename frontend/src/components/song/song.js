import React, { useState, useEffect } from 'react';
import "./song.css";
import play from '../../icons/play.svg';

const Song = ({ image, name, artist }) => {
    return (
        <div className="item-container">
            <div className="image-container">
                <img src={image} alt={name} />
            </div>
            <div className="text-container">
                <h2>{name}</h2>
                <p>{artist}</p>
            </div>
            <button className="play-button">
                <img src={play} alt='play'/>
            </button>
        </div>

    );
}

export default Song;