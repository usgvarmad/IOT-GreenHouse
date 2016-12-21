Barn Owl
============

**University of Pennsylvania, ESE 519: Real Time and Embedded Systems**

* Grayson Honan, Uzval Dontiboyina, Nikheel Vishwas Savant
* [Blog](https://devpost.com/software/barn-owl)

### DESCRIPTION AND GOALS
Our goal with Barn Owl is to automate a micro-farm using the existing greenhouse outside of the Skirkanich building. Several plants will be cared for automatically in the greenhouse using various sensors (temperature/humidity, lighting, soil moisture) to monitor conditions. Watering intervals, fans, and lighting will be adjusted by our system to provide optimal growing conditions. A front-end interface will be used to monitor the greenhouse and provide manual control. The front-end interface will also allow users to specify which plants are being grown in order to better tailor the conditions to the needs of a certain plant species.

### VIDEOS
* [Barn Owl - Sensor Demo](https://www.youtube.com/watch?v=tP8d-07KyO8)
* [Barn Owl - Camera Slider Demo](https://www.youtube.com/watch?v=YH9azuOEQMQ)
* [Barn Owl - App Demo](https://www.youtube.com/watch?v=E3g4D_ApXCE)

### REPORT
Please see the file BarnOwlFinalReport.pdf

### BUILD INSTRUCTIONS
To use the scripts in the "code" folder, follow these steps:

1. Flash Photon.ino in the Photon folder. Necessary libraries are in the Libraries folder. Be sure to update the server IP.
2. Run server.py, stackSERVER.py, and GUI.py on a host PC. All CSV files in the Plant Profiles folder need to be in the same directory as GUI.py.
3. All Rapsberry PI code can be run from anywhere on a PI. Be sure to update the host IP in the send.py script.
