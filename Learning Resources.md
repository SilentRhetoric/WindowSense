# Learning Resources

I want to share a variety of resources that I have used as a novice 
maker to learn various skills I used to create this project.  I enjoy collecting 
bookmarks and hope that these links can help others find quality resources on 
their journey as a maker.

## Backstory

Not long after COVID began to reshape our lives I found myself with lots of time at home 
and an itch to start a new indoor hobby.  Intrigued by a tech article about someone's 
Raspberry Pi project, I went down the rabbit hole and soon bought one of my own.  Aside from
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


## Raspberry Pi

Lots of valuable information is available in the [Raspberry Pi documentation portal](https://www.raspberrypi.org/documentation/).

For real-time help, I have chatted with the knowledgeable folks on the [Raspberry Pie Discord](https://discord.gg/HYpS9NC) server.

### Raspberry Pi Zero WH

This project uses a [Raspberry Pi Zero WH](https://www.raspberrypi.org/products/raspberry-pi-zero-w/), which is a tiny computer that has
fourty GPIO conections, integrated WifI and Bluetooth (the "W") and pre-soldered headers 
on those GPIO so HATs (hardware attached on top) can be connected without needing to 
solder anything.  You could also use a regular W and solder on a header.  Although the SenseHAT is often
shown on top of a full-sized Raspberry Pi 3 or 4, that much computing power is overkill for this
project, so I used a Zero.  This also allows the WindowSense case to be just slightly larger than the SenseHAT, itself.

### Sense HAT
The [Raspberry Pi Sense HAT ](https://www.raspberrypi.org/products/sense-hat/) is a special hat that 
incorporate a collection of sensors, a 5-way joystick button, and an 8x8 RGB LED matrix as a way to learn how to do a variety of 
physical computing things with a Raspberry Pi.  This project utilizes the display and the joystick for interactive elements.

There is an [introductory walkthrough to the Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) which I found very helpful.
The [API guide for the Sense HAT](https://pythonhosted.org/sense-hat/api/) explains how to interact with it, and the full [source code for the SenseHat](https://github.com/astro-pi/python-sense-hat) is also available on Github.

### Raspberry Pi OS
The Pi runs a modified version of Linux called [Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit) 
which can be configured like a desktop or a pared-down operating system with only a command line interface.
While developing the project, I used the desktop interface and then transitioned to the "Lite" OS 
for the permanent installation for a more efficient and reliable device.

I used the [Pi Terminal documentation](https://www.raspberrypi.org/documentation/usage/terminal/) 
for the terminal, or command line interface, to learn this method of 
interacting with a computer when working on the Lite OS.

## 3D Printing & Design
Around the same time I began tinkering with my first Raspberry Pi I also decided 
to learn 3D printing!  This is another incredible community with lots of help
and open-source models available.

### Prusa
Many of the printing enthusiasts at [Reddit's r/3Dprinting forum](https://www.reddit.com/r/3Dprinting/)
recommend the Prusa i3 line of printers as a mid-range model that reliably produces great FFF-style prints, is open source, 
and is surrounded by an enthusiastic community.  I bought the [Prusa i3 MK3S kit](https://shop.prusa3d.com/en/3d-printers/180-original-prusa-i3-mk3s-kit.html)
and assembled it myself to learn how 3D printers work.  They have their own community [Prusa Printers](https://www.prusaprinters.org) that includes a forum, model sharing, 
and other resources.  There is even a Discord server [prusa3d](https://discord.gg/cjk3FuJ) where I 
have received much help from experienced printers.

### Fusion 360
Based on recommendations and having grown frustrated with using [TinkerCAD](https://www.tinkercad.com) 
in a browser to design 3D models, I decided to take the plunge into Autodesk's desktop design app [Fusion 360](https://www.autodesk.com/products/fusion-360/overview).
It it a powerful app with a steep learning curve, but I found [Paul McWhorter's YouTube series](https://www.youtube.com/watch?v=y5tp4QXciK4) extremely helpful as an introduction
to the interface and the basics of parametric design.  The WindowSense case design has undergone about a hundred versions
from concept to the final model.  Over a dozen iterations were printed and tested to dial in the fit, function, and finish.

### Thingiverse
One could not mention 3D printing without mentioning [Thingiverse](https://www.thingiverse.com), which is the biggest and most well-known
site for sharing 3D models.  It is a trove of interesting models, from the functional to the artistic, and 
a great place to get inspired by what is possible to create through 3D printing.

## Python


### PyCharm
I have used a variety of Python IDEs while learning the language and developing WindowSense, but [PyCharm](https://www.jetbrains.com/pycharm/)
is the best by far.  This is a sophisticated tool for professional developers, but I found it to
be very well designed and helpful in debugging, linting, and refactoring my code.  There was a bit of learning curve, but 

#### Codecademy

#### ReadTheDocs

### Google Device Access

### OpenWeatherMap

[OpenWeatherMap Guide](https://openweathermap.org/guide)
[OpenWeatherMap OneCall API](https://openweathermap.org/api/one-call-api)

#### PyOWM

[PyOWM Documentation](https://buildmedia.readthedocs.org/media/pdf/pyowm/latest/pyowm.pdf)

## Colaboration

### Git

### Markdown
Several of the files in this repository are written in the beginner-friendly 
Markdown language using the helpful syntax guide at 
[MarkdownGuide.org](https://www.markdownguide.org/basic-syntax/).  
This simple language allows Github and other programs to generate attractive 
HTML from a syntax that is also readable as a plain text file.

### Discord
