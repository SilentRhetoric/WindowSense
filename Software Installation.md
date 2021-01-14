# Configuring the Python Environment

This program was written and tested on Python 3.7 to ensure compatibility with 
Raspberry Pi OS, which officially supports Python 3.7 as of this writing.

## Packages

The following Python packages, which are not included in the Python standard 
library, will need to be installed via pip or another package manager:
- requests  
- dotenv  
- pyowm  
- schedule
- sense_hat


## Environment Variables for Personal Accounts
The script requires you to have two accounts, OpenWeatherMap and Google Device Acccess, in order to call these APIs.  The credentials for each are saved in .env files which are not part of this repo for privacy and security--you need to create your own to get the script running. 

### OpenWeatherMap API
Calling the OpenWeatherMap API requires an API key obtainable for free once you create an account. 
The Python script has been written to get the API key, along with the latitude & longitude 
to use for the weather forecast, from a separate .env file that is not part of the Github repository. 
The code itself does not contain these values to protect the privacy of anyone who shares the code.  

Create your own .env file named `owm_config.env` with three key=value pairs that looks like this:

`API_KEY=reallylongstringofnumbersandletters`  
`LATITUDE=00.00`  
`LONGITUDE=00.00`


### Google Services API

You can sign up for a Google Device Access account for five dollars to create a project. 
Separately, you need to create an OAuth 2.0 Client ID for your Google account through the Google Cloud Platform Console. 
As this process is quite involved, I have linked to some helpful resources for these processes in the [Learning Resources.md](LearningResources.md) file in this repo. 
Again, the code does not contain any of these values for security purposes.  Once you have these IDs, tokens, etc. do not share them with anyone!  


Create a second .env file named `google_auth.env` with the following key=value pairs:


`PROJECT_ID=`  
`CLIENT_ID=`  
`CLIENT_SECRET=`  
`REDIRECT_URI=`  
`TOKEN_TYPE=`  
`ACCESS_TOKEN=`  
`REFRESH_TOKEN=`


### Finally 
Save both files in the /home/pi directory on the Pi or wherever you clone the repo into.  The script will pick these up automatically when it runs.