# Hand-Gesture-Controlled-Car-Game-using-OpenCV-MediaPipe-and-Pygame
##Introduction:
This project demonstrates how to control a virtual car in a Pygame environment using hand gestures captured from a webcam. The car's movement is controlled by detecting the number of raised fingers using MediaPipe's hand-tracking capabilities. The project uses OpenCV to capture the webcam feed, MediaPipe for hand detection and finger counting, and Pygame to create a simple game environment.

##Features
Hand Gesture Recognition: Detects and counts the number of raised fingers.
Car Movement: Controls the car's movement (up, down, left, right) based on the number of fingers detected.
Interactive Game Environment: A simple car game using Pygame where the car's movement is controlled in real-time.
Requirements
Before you begin, ensure you have the following installed:

###Python 3.6+  
###OpenCV (cv2)  
###MediaPipe  
###Pygame  



You can install the required packages using pip:

bash
`````pip install opencv-python mediapipe pygame`````


#How It Works
##Capture Webcam Input: The script captures video from your webcam using OpenCV.
##Detect Hand Gestures: MediaPipe processes the video feed to detect hand landmarks and count the number of raised fingers.
##Control Car Movement: The car’s movement on the screen is controlled based on the finger count detected by MediaPipe.
##Render with Pygame: The car and game environment are displayed using Pygame.
**
Add Your Car Image**:Place your car image (car.png) in the project directory. Make sure the image is named car.png or update the file name in the script accordingly.
