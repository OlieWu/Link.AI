import React, { useState, useEffect } from 'react';
import Song from '../song/song';
import change from '../../icons/change.svg';

const SongsList = () => {
    const [songs, setSongs] = useState([]);

    // Fetch songs from an backend

    return (
        <div>
            <button className='iconbutton'>
                <img src={change} alt='change' />
            </button>
            {songs.map(song => (
                <Song key={song.name} name={song.name} artist={song.artist} />
            ))}
        </div>
    );
}

export default SongsList;
