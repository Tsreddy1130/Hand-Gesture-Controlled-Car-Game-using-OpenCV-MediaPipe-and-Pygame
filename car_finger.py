import cv2
import mediapipe as mp
import pygame
import sys

# MediaPipe setup
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Pygame setup
pygame.init()

# Constants for the screen size (increase the arena size)
SCREEN_WIDTH = 800  # Increased width
SCREEN_HEIGHT = 600  # Increased height

# Colors
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

# Load the car image and resize it (reduce the size of the car)
car_img = pygame.image.load('car.png')  # Replace 'car.png' with your car image file path
car_img = pygame.transform.scale(car_img, (50, 30))  # Resize the car image
car_rect = car_img.get_rect()

# Set initial position of the car
car_rect.centerx = SCREEN_WIDTH // 2
car_rect.centery = SCREEN_HEIGHT // 2

# Variables for car movement
car_speed = 5

# For webcam input:
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Initially set finger count to 0 for each cap
        fingerCount = 0

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:
                # Get hand index to check label (left or right)
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label

                # Set variable to keep landmarks positions (x and y)
                handLandmarks = []

                # Fill list with x and y positions of each landmark
                for landmarks in hand_landmarks.landmark:
                    handLandmarks.append([landmarks.x, landmarks.y])

                # Test conditions for each finger: Count is increased if finger is considered raised.
                # Thumb: TIP x position must be greater or lower than IP x position, depending on hand label.
                if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                    fingerCount += 1
                elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                    fingerCount += 1

                # Other fingers: TIP y position must be lower than PIP y position, as image origin is in the upper left corner.
                if handLandmarks[8][1] < handLandmarks[6][1]:  # Index finger
                    fingerCount += 1
                if handLandmarks[12][1] < handLandmarks[10][1]:  # Middle finger
                    fingerCount += 1
                if handLandmarks[16][1] < handLandmarks[14][1]:  # Ring finger
                    fingerCount += 1
                if handLandmarks[20][1] < handLandmarks[18][1]:  # Pinky
                    fingerCount += 1

                # Draw hand landmarks 
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        # Display finger count on the image (for debugging purposes)
        cv2.putText(image, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)

        # Display image
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

        # Pygame part to handle car movement based on finger count
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update car position based on finger count
        if fingerCount == 1:
            car_rect.y -= car_speed  # Move forward
        elif fingerCount == 2:
            car_rect.y += car_speed  # Move backward
        elif fingerCount == 3:
            car_rect.x -= car_speed  # Move left
        elif fingerCount == 4:
            car_rect.x += car_speed  # Move right
        elif fingerCount == 5:
            pass  # Stop (no movement)

        # Boundary checking (optional)
        if car_rect.left < 0:
            car_rect.left = 0
        elif car_rect.right > SCREEN_WIDTH:
            car_rect.right = SCREEN_WIDTH
        if car_rect.top < 0:
            car_rect.top = 0
        elif car_rect.bottom > SCREEN_HEIGHT:
            car_rect.bottom = SCREEN_HEIGHT

        # Fill the screen with white color
        screen.fill(WHITE)

        # Draw the car on the screen
        screen.blit(car_img, car_rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

cap.release()
cv2.destroyAllWindows()
