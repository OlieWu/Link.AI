// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: process.env.REACT_APP_FIREBASE_API_KEY,
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
