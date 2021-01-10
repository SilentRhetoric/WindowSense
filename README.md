# WindowSense
 


"""
The WindowSense program creates a graphical display to indicate if the
outside temperature will be comfortable if you open your windows for 
fresh air.  You can set your preferred inside temperature comfort range 
with min and max temperature values.  The program gets hourly local 
temperature forecasts for the next 8 hours and graphs them relative to 
your specified inside comfort range.  You can then see at a glance when 
it will be good to open or close your windows to maintain a comfortable 
temperature inside your home.

When outside temps are forecasted to be within your comfort range, the 
screen will display a green square, either "high" on row 4 if the outside
temperature will be nearer the high end of your comfort range or "low" on row 5
if the outside temperature will be nearer the low end of your comfort range.

When outside temperatures will be beyond your comfort range, the screen will
display additional squares above or below your green comfort range to indicate
that the forecast expects hotter temperatures, in progressively redder squares,
or colder temperatures, in progressive bluer squares, above or below your green
comfort range, respectively.

The temperature bands represented by the display rows are set dynamically to
half of the difference between your inside comfort range low and high settings.
For example, a comfort range of 65-75 will yield screen pixels that each
represent five-degree temperature differences above or below the average, 70,
of your comfort range.

The forecasts are updated hourly and the screen refreshed so that the graph
always shows you the next eight hours of expected temperatures relative to your
comfort range.
"""

 """
        This function uses the PyOWM library's one_call module to call
        the Open Weather Map API for a OneCall report that contains
        various current and forecast data.  The call requests forecast
        data on an hourly basis and specifically gets the regular
        forecast temperatures from the temperature section (as opposed
        to the "feels like" temperature).

        Finally, the function calls another function draw_graph and
        passes the list of hourly forecast temperatures to it so that
        the screen graph can be drawn based on the .
        """


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

