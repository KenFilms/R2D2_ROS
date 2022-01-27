# R2D2 ROS Work-in-Progress
After purchasing a used DeAgostini R2D2 off EBay for a good price, and playing around, I got a bit bored of the limited functionality. There is so much more potential in the quite nice overall hardware of the robot. So I decided to give it a atry and extend the capabilities to make R2D2 actually a bit more of a robot with some intelligence. Thus making this toy not only more fun to interact with, but also more useful.\



![Alt R2D2_front](images/R2D2_overview.jpg?raw=true "R2D2_overview")

Here is a list of planned features for the heavily modefied robot (hardware and software):
* SLAM navigation using the lidar sensor
* Offline speech recognition (speech-to-text) of a library of known commands (around 100 commands) - https://github.com/julius-speech/julius 
* Speech generation (text-to-speech) for answering questions and providing status information.
* Natural Language Processing and probably a chat bot framework. 
* Face Detection utilizing openCV http://wiki.ros.org/vision_opencv 

## Modifications to original hardware

## Additional hardware
* Intel 5th Gen NUC Core i5-5300U, NUC5I5MYHE. This replaces the 
https://www.ydlidar.com/products/view/5.html 

![Alt R2D2_front](images/R2D2_front.jpg?raw=true "R2D2_front")
![Alt R2D2_front](images/R2D2_details.jpg?raw=true "R2D2_details")

## Lidar Modifications

![Alt R2D2_front](images/R2D2_lidar.jpg?raw=true "R2D2_lidar")

## Reverse engineered communication between ROS and hardware controller

He managed to reverse engineer the commands to be accepted by the hardware controller: https://pastebin.com/ij5brpVd by uart sniffing. The code for UART sniffing and also a video explaining the wiring can be found here: https://pastebin.com/MRx4fzs5. https://www.youtube.com/watch?v=fD6QIEKGQrY&t=0s 
