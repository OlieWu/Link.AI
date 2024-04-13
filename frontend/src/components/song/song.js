import React, { useState, useEffect } from 'react';

const Song = ({ image, name, artist }) => {
    return (
        <div>
            <img src={image} alt={name} />
            <h3>{name}</h3>
            <p>{artist}</p>
            <button>Play</button>
        </div>
    );
}

export default Song;