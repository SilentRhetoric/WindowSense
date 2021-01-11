## Configuring the Python Environment

This program was written and tested on Python 3.7 to ensure compatibility with 
Raspberry Pi OS, which officially supports Python 3.7 as of this writing.

### Packages

The following Python packages, which are not included in the Python standard 
library, will need to be installed via pip or another package manager:
- requests  
- dotenv  
- pyowm  
- schedule
- sense_hat

### Environment Variables


#### OpenWeatherMap API
Calling the OpenWeatherMap API requires an API key obtainable for free once you create an account.  The Python script has been written to get the API key, along with the latitude & longitude to use for the weather forecast, from a separate .env file that is not part of the Github repository.  The code itself does not contain these values to protect the privacy of anyone who shares the code.  

Create your own .env file with three key=value pairs that looks like this:

`API_KEY=reallylongstringofnumbersandletters`  
`LATITUDE=00.00`  
`LONGITUDE=00.00`

#### Google Services API

