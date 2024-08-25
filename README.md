![Screenshot (11)](https://github.com/user-attachments/assets/99315806-7013-4cba-b21f-4b5d82dac992)# Hand-Gesture-Controlled-Car-Game-using-OpenCV-MediaPipe-and-Pygame
## Introduction:
This project demonstrates how to control a virtual car in a Pygame environment using hand gestures captured from a webcam. The car's movement is controlled by detecting the number of raised fingers using MediaPipe's hand-tracking capabilities. The project uses OpenCV to capture the webcam feed, MediaPipe for hand detection and finger counting, and Pygame to create a simple game environment.

## Features
Hand Gesture Recognition: Detects and counts the number of raised fingers.
Car Movement: Controls the car's movement (up, down, left, right) based on the number of fingers detected.
Interactive Game Environment: A simple car game using Pygame where the car's movement is controlled in real-time.
Requirements
Before you begin, ensure you have the following installed:

### Python 3.6+  
### OpenCV (cv2)  
### MediaPipe  
### Pygame  



You can install the required packages using pip:

bash
`````pip install opencv-python mediapipe pygame`````


# How It Works
##  -Capture Webcam Input: ## The script captures video from your webcam using OpenCV.
##  -Detect Hand Gestures: ## MediaPipe processes the video feed to detect hand landmarks and count the number of raised fingers.
##  -Control Car Movement: ##The car’s movement on the screen is controlled based on the finger count detected by MediaPipe.
##  -Render with Pygame: ## The car and game environment are displayed using Pygame.
**Add Your Car Image**:Place your car image (car.png) in the project directory. Make sure the image is named car.png or update the file name in the script accordingly.

## usage:
 you can either download the python file or simply clone the reposirity:
1. **Clone the Repository** ```git clone https://github.com/yourusername/hand-gesture-car-game.git```
2. **Navigate to the Project Directory** ```cd hand-gesture-car-game```
3. **Add Your Car Image**:Place your car image (car.png) in the project directory. Make sure the image is named car.png or update the file name in the script accordingly.
4. **Run the Script**:```python main.py```

## outputs:
    if fingerCount == 1:--> move forward
    if fingerCount == 2:-->move backward
    if fingerCount == 3:-->move left
    if fingerCount == 4:-->move right
    if fingerCount == 5:-->stop
![Screenshot (3)](https://github.com/user-attachments/assets/9376a89e-ef4f-431b-9d4f-1974ccf65078)![Screenshot (16)](https://github.com/user-attachments/assets/4cf0d241-7372-4717-8ebd-59719383da39)
![Screenshot (9)](https://github.com/user-attachments/assets/a05df287-7669-45e2-a21f-68f268f6737a)![Screenshot (11)](https://github.com/user-attachments/assets/047c9da4-0a8a-49c6-bb81-e72595610769)






