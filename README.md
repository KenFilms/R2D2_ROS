# R2D2 ROS Work-in-Progress
My 1:2 scale R2D2 project. I'm modifying hardware and software of the De Agostini R2D2 to work with ROS. Functionalities include SLAM via Lidar, offline voice commands using julius, face recognition using a fullHD camera. This is a work-in-progress.

![Alt R2D2_front](images/R2D2_overview.jpg?raw=true "R2D2_overview")

## Planned Features
* SLAM navigation using the lidar sensor
* Speech recognition (speech-to-text) of a library of known commands (around 100 commands) - https://github.com/julius-speech/julius 
* Speech generation (text-to-speech) for answering questions and providing status information.
* Natural Language Processing and probably a chat bot framework. 

## Modifications to original hardware
The original 
Intel 5th Gen NUC Core i5-5300U, NUC5I5MYHE
https://www.ydlidar.com/products/view/5.html 

![Alt R2D2_front](images/R2D2_front.jpg?raw=true "R2D2_front")
![Alt R2D2_front](images/R2D2_details.jpg?raw=true "R2D2_details")

## Lidar Modifications

![Alt R2D2_front](images/R2D2_lidar.jpg?raw=true "R2D2_lidar")

## Reverse engineered communication between ROS and hardware controller

He managed to reverse engineer the commands to be accepted by the hardware controller: https://pastebin.com/ij5brpVd by uart sniffing. The code for UART sniffing and also a video explaining the wiring can be found here: https://pastebin.com/MRx4fzs5. https://www.youtube.com/watch?v=fD6QIEKGQrY&t=0s 
