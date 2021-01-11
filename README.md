# WindowSense
"Someone ought to open up a window!"

Get a sense of when to open your windows for fresh air with WindowSense.
Set your thermostat for comfort and save money on heating and cooling by 
letting in the breeze at the best times.  

WindowSense integrates the temperature forecast with your Nest thermostat
comfort settings to visualize when the outside air will be just right to
throw open the windows for fresh air that won't make your home too hot or cold.

The RGB LED matrix display uses a rainbow of colors to signal what's happening
with the temperature over the next eight hours so you can plan ahead and 
maximize your home's comfort and efficiency.

## The inspiration

There's something special about air that's just the right temperature such that
you can't feel it at all.  Last fall, when the days were still warm and the 
nights were getting cold, my wife and I were trying to open the windows as much as possible
for fresh air. However, as the resident steward of the thermostat, 
I also wanted to make sure we were not letting in hot late-afternoon air that 
would kick on our air conditioning or leaving the windows open too long and 
allowing the house to get too cold from the chilly, nighttime air.  Depending 
on the day, there was sometimes just a narrow window of opportunity to let in 
fresh air that would feel just right--not too hot or too cold.  And so the idea
was born to create a smart device to tell us when it would be comfortable--and efficient--
to throw open the windows for a cross-breeze.

## The WindowSense display



## How it works

WindowSense runs on a Raspberry Pi  and helps your keep your home fresh through a few functions:

1. Reading your Nest thermostat's heat & cool setpoints via Google's smart device access API
2. Getting the weather forecast from OpenWeatherMap's API using the pyowm library 
3. Dynamically calculating and drawing a graph that relates the outside temps to
your personal comfort settings
4. Providing temp & humidity readouts, setpoint readouts, brightness adjustments, and 
a way to safely shut down the Raspberry Pi.

## What's in this repo

This repository includes the Python script which runs WindowSense, as well as some additional resources, including:

1. "Raspberry Pi Setup" - Guidance for how to set up a fresh Raspberry Pi
2. "Software Installation" - Instructions on how to set up the software and get the script running
3. "Hardware Assembly" - Information on the hardware and 3D-printed case
4. "Learning Resources" - Supplemental learning resources for those interested in learning more about 
the technologies used to create WindowSense

## Thanks and acknowledgments

I want to extend many thanks to the Raspberry Pi Foundation and the countless makers and teachers
who comprise the incredible community around these devices that inspired and helped me to create this project.

Not long after COVID began to reshape our lives I found myself with lots of time at home 
and an itch to start a new indoor hobby.  Intrigued by a tech article about someone's 
Raspberry Pi project, I went down the rabbit hole and soon had one of my own.  Aside from
one semester of C++ in college 15 years ago, however, I had minimal experience with computer programming, 
so I set out learn on my own.  

I have been continually amazed at the quantity and quality 
of materials which have been created by this generous community to help people like me 
learn about computer hardware, coding, and myriad real-world project applications.  In addition
to my gratitude here and some small monetary donations to nonprofits, I also 
want to give back to this community by paying forward some of the help
I have received.  For that reason, I have enriched this repo with a variety of
resources that I found valuable on my learning journey and which I hope
will enable and inspire others to become makers of their ideas.






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

This function uses the PyOWM library's one_call module to call
the Open Weather Map API for a OneCall report that contains
various current and forecast data.  The call requests forecast
data on an hourly basis and specifically gets the regular
forecast temperatures from the temperature section (as opposed
to the "feels like" temperature).

Finally, the function calls another function draw_graph and
passes the list of hourly forecast temperatures to it so that
the screen graph can be drawn based on the
