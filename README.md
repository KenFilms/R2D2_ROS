# R2D2 ROS Work-in-Progress

## What to expect here?
This is a documentation of my Star Wars R2D2 project for now. I will add the code of this project as soon, I have it working. Currently, as you can see below, I'm getting the hardware all wired up with controllers, actuators and sensors.

## Introduction
As a Star Wars Tech nerd, I need my own R2D2. This is a long lasting dream come true. After purchasing a used DeAgostini R2D2 in roughly 1:2 scale off EBay for a very good price, I played around with it for some time. Aaand I got bored of the limited functionality. There is so much more potential in the quite nice overall build quality and hardware of the robot. So I decided to give it a try and extend the capabilities to make R2D2 actually a bit more of a robot with some intelligence. Thus making this toy not only more fun to interact with, but also more useful.

![Alt R2D2_front](images/R2D2_overview.jpg?raw=true "R2D2_overview")

Here is a list of planned features for the heavily modefied robot (hardware and software):
* SLAM navigation using the lidar sensor
* Offline speech recognition (speech-to-text) of a library of known commands (around 100 commands) - https://github.com/julius-speech/julius 
* Speech generation (text-to-speech) for answering questions and providing status information.
* Natural Language Processing and probably a chat bot framework. 
* Face Detection utilizing openCV http://wiki.ros.org/vision_opencv 

## Replacing original controller board
According to "kombat" on the Desgostini R2D2 forum, he stated that main controller seems to be Orange Pi Zero Plus 2 H5 (https://forum.deagostini.co.uk/?g=posts&t=30073). It has a H5 Quad-core Cortex-A53 with around 1,3GHz. and 512MB DDR2 RAM (sared with GPU) and all bunch of nice features, such as WiFi, camera-support, HDMI etc. Unfortunately, the system seems to be closed, so we cannot just flash new software unto the device. So one way of replacing it, would be just to purchase an "open" Orange Pi Zero, but I wanted to have a more powerful main controller with higher CPU frequency and more customizable, such as adding M2 SSD storage. So I decided for an "old" Intel NUC MYHE Kit, which I had bought a few years ago and it was lying around in my drawer...probably for that reason. Now, with more power coms not only more responsibility ;) but also considerably bigger dimensions and also higher energy consumption. While the Orangi Pi is only about 48mm x 46mm and relatuvey flat, the stripped Intel NUC.

![Alt electronic_control_scheme](images/R2D2_electronics.jpg?raw=true "R2D2_electronics")

## Additional hardware
* Intel 5th Gen NUC Core i5-5300U, NUC5I5MYHE. This replaces the Orangpi Pi Zero.
* RESP MIC 2.0 ReSpeaker Mic Array v2.0. This microphone array will be able to record voices more clearly than a single microphone which came as part of the orginal SeAgostini kit. Additionally, we can get the direction of sound probably by beam forming. https://www.reichelt.de/de/de/respeaker-mic-array-v2-0-resp-mic-2-0-p248721.html?r=1 
* Modified YLidar X4 https://www.ydlidar.com/products/view/5.html. For perfoming SLAM, it's the easiest to get this job done by using a Lidar sensor. I was giving it quite a thought how to get it mounted onto the robot without manipulating the overall R2D2 harmonic design too much. At the same time, I wanted to get a range covering angle which is big enough to get reasonably enough data for SLAM. Especially considering that we'd like only use the lidar signals withut odometry e.g. potentionally from encoders in the wheels of the robot. Without disassembling the wheel motors, I don't actually know if there are any encoders inside or if it's just open loop control of stepper motors. Even if there would be encoders, we'd to wire it up from the hardware controller board all the way up to the head which is rotating. So, the best would be to only use the lidar for SLAM. Finally, I mounted it onto the lower front. It looks a bit weird, admittedly. https://automaticaddison.com/how-to-build-an-indoor-map-using-ros-and-lidar-based-slam/ . As you can see on the photos, I modified the YLidar X4 so that the motor is mounted onto the same side as the laser to achieve a flatter oervall design. Also I painted the orginally blue and black pastic white to match the designand black to prevent laser reflections. 
* Modified Genius 120 Degree Ultra Wide Angle Full HD. I stripped the plastic cover and cut down the unnecessary audio recording part of the PCB. This had to be done to fir the limited dimensions for mounting it behind the "eye" of R2D2.
* Two micro servos to move two of the opposing blue head plates.
* One Time-of_Flight sensor for obstacles at lower heights than the Lidar can capture. This will be mounted into the front foot. 
* more stuff, like USB contollers, wiring, screws, aluminium mounting plates, servos for the opening cooling windows in the head. cpu fan for cooling the main CPU, USB to TTL conversion board, etc. 

![Alt R2D2_front](images/R2D2_front.jpg?raw=true "R2D2_front")
![Alt R2D2_front](images/R2D2_details.jpg?raw=true "R2D2_details")
![Alt R2D2_front](images/R2D2_lidar.jpg?raw=true "R2D2_lidar")

## Reverse engineered communication between ROS and hardware controller
"Dald DDe" on YouTube did some amazing reverse engineering work on the signals being send from the Orange Pi main controller boaard to the hardware controllers. 
He created a list of commands accepted by the hardware controller: https://pastebin.com/ij5brpVd by uart sniffing. The code for UART sniffing and also a video explaining the wiring can be found here: https://pastebin.com/MRx4fzs5. https://www.youtube.com/watch?v=fD6QIEKGQrY&t=0s 

## Energy supply
This is a whole big topic. I had previously build a smaller R2D2 using a raspberry Pi and found out it's crucial to sperate the supply for the controller baords and motors because large fluctuations in the supply voltage created by the motors cannot be handled well by controller boards. The original power supply of DeAgostini was designed quite well incorporating the principle of separated power supplies However, due to changing to the intel NUC, I needed a bigger battery overall, being able to supply 19V and quite a few Amps when running energy-intensive computations being at full speed with the motors. So I decided for the Laptop Portable Power Bank 5V 12V 16V 19V 30000mAh. Unfortunately, this power bank does not fit into the torso qithout modification. So either I solder around with LiPo batteries, which only experts should so. Or I have to fit it into a sort of small "backpack" for R2.
