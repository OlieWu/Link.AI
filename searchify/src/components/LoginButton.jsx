import * as React from 'react';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// import { faBrands, faSpotify } from '@fortawesome/free-brands-svg-icons';
// import { library } from '@fortawesome/fontawesome-svg-core'
// import { all } from '@awesome/kit-KIT_CODE/icons'

// library.add(...all);

const LoginButton = () => {
    const navigate = useNavigate();

    const handleLogin = async () => {
        // make a call to /login
        console.log("hungry");
        try {
            const response = await fetch('http://localhost:5000/login');
            console.log("hello");
            if (!response.ok) {
                console.log("status", response);
                // TODO: display error
                throw "Error";
            }

            // TODO: call redirect here
            const data = await response.json();
            console.log("url", data["url"]);
            // navigate(data["url"]);
            window.open(data["url"], '_blank')
            // window.location.href = newLocation;
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    return (
        <Stack direction="row" spacing={2}>
            <IconButton aria-label="Spotify" color="inherit">
            {/* <FontAwesomeIcon icon={["faBrands", "faSpotify"]} /> */}
            </IconButton>
            <Button onClick={handleLogin} variant="contained" color="primary" disableRipple>
                <Typography variant="body1">Log into Spotify</Typography>
            </Button>
        </Stack>
  );
}

export default LoginButton;