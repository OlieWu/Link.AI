import React, { useState, useEffect } from 'react';
import change from '../../icons/change.svg';
import Song from '../song/song';
import './songList.css';

const SongsList = () => {
    // const [songs, setSongs] = useState([]);

    // Fetch songs from an backend
    const songs = [
        {
            name: 'Song 1',
            artist: 'Artist 1',
            cover: 'https://media.pitchfork.com/photos/5f9c62a0cc786205a9c32981/1:1/w_1024%2Cc_limit/ariana_grande_positions_album_art.jpg'
        },
        {
            name: 'Song 2',
            artist: 'Artist 2',
            cover: 'https://media.pitchfork.com/photos/5f9c62a0cc786205a9c32981/1:1/w_1024%2Cc_limit/ariana_grande_positions_album_art.jpg'
        },
        {
            name: 'Song 3',
            artist: 'Artist 3',
            cover: 'https://media.pitchfork.com/photos/5f9c62a0cc786205a9c32981/1:1/w_1024%2Cc_limit/ariana_grande_positions_album_art.jpg'
        },
        {
            name: 'Song 4',
            artist: 'Artist 4',
            cover: 'https://media.pitchfork.com/photos/5f9c62a0cc786205a9c32981/1:1/w_1024%2Cc_limit/ariana_grande_positions_album_art.jpg'
        },
        {
            name: 'Song 5',
            artist: 'Artist 5',
            cover: 'https://media.pitchfork.com/photos/5f9c62a0cc786205a9c32981/1:1/w_1024%2Cc_limit/ariana_grande_positions_album_art.jpg'
        }
    ];
    return (
        <div className='container'>
            <div className="change-container">
                <button className='change, iconbutton'>
                    <img src={change} alt='change' />
                </button>
            </div>
            {/* TODO: in the react code, make sure to extract the track */}
            {songs.map(song => (
                <Song key={song.name} image={song.cover} name={song.name} artist={song.artist} />
            ))}
        </div>
    );
}

export default SongsList;
