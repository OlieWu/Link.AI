// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: process.env.REACT_APP_FIREBASE_API_KEY,
  authDomain: "searchify-cbc7b.firebaseapp.com",
  projectId: "searchify-cbc7b",
  storageBucket: "searchify-cbc7b.appspot.com",
  messagingSenderId: "984307538973",
  appId: "1:984307538973:web:1770814d6849f0a3883af4",
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
