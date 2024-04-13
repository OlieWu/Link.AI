import React, { useState, useEffect } from 'react';
import Song from '../song/song';

const SongsList = () => {
    const [songs, setSongs] = useState([]);

    // Fetch songs from an backend

    return (
        <div>
            {songs.map(song => (
                <Song key={song.name} name={song.name} artist={song.artist} />
            ))}
        </div>
    );
}

export default SongsList;
