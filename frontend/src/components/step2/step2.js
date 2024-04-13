import React, { useState, useEffect } from 'react';
import step2 from '../../icons/step2.svg';
const Step2 = () => {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = () => {
        // You would handle the file upload here, possibly sending it to a backend server
        console.log('File to upload:', selectedFile);
        // Reset the selected file
        setSelectedFile(null);
    };
    return (
        <div>
            <div className="step">
                <h2>Step 2</h2>
                <img className='stepviz' src={step2} alt='step2' />
            </div>
            <div className="status">
                <p>Right now I’m</p>
            </div>
            <div className="upload-area">
                <input type="file" onChange={handleFileChange} accept="image/*,video/*" />
                {selectedFile && (
                    <button onClick={handleUpload}>
                        Upload {selectedFile.name}
                    </button>
                )}
            </div>
        </div>
    );
}

export default Step2;