import {
  getDownloadURL,
  getStorage,
  ref,
  uploadBytesResumable,
} from "firebase/storage";
import { app } from "../../firebase";
import React, { useState } from "react";
import upload from "../../icons/upload.svg";
import "./step2.css";

const Step2 = () => {
  const [uploading, setUploading] = useState(false);
  const [uploadedImages, setUploadedImages] = useState([]);
  const [imageUploadError, setImageUploadError] = useState("");

  const handleFileChange = async (event) => {
    const files = Array.from(event.target.files);
    if (!files.length) {
      setImageUploadError("Please select a file to upload.");
      return;
    }
    setUploading(true);
    setImageUploadError("");

    try {
      const urls = await Promise.all(files.map((file) => storeImage(file)));
      console.log("Uploaded URLs:", urls);
      setUploadedImages(urls); // Store the URLs of uploaded images
    } catch (error) {
      setImageUploadError("Image upload failed: " + error.message);
    } finally {
      setUploading(false); // Ensure we turn off the uploading state
    }
  };

  const storeImage = async (file) => {
    const storage = getStorage(app);
    const fileName = new Date().getTime() + "-" + file.name;
    const storageRef = ref(storage, fileName);
    const uploadTask = uploadBytesResumable(storageRef, file);

    return new Promise((resolve, reject) => {
      uploadTask.on(
        "state_changed",
        (snapshot) => {
          const progress =
            (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
          console.log(`Upload is ${progress}% done`);
        },
        reject, // Directly pass error to reject the promise
        () => {
          getDownloadURL(uploadTask.snapshot.ref).then(resolve).catch(reject);
        }
      );
    });
  };

  return (
    <div>
      <h2>Step 2 - Upload Images</h2>
      <div className="upload-area">
        <input
          type="file"
          onChange={handleFileChange}
          accept="image/*"
          multiple
        />

        {uploadedImages.map((url, index) => (
          <img key={index} src={url} alt="Uploaded" className="upload" />
        ))}
      </div>
      {uploading && <p>Loading...</p>}
      {imageUploadError && (
        <p className="text-red-700 text-sm">{imageUploadError}</p>
      )}
    </div>
  );
};

export default Step2;
