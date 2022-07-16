import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.finger_x_coordinate = None
        self.finger_y_coordinate = None

    def tracking(self, img):
        results = self.hands.process(img)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 8:
                        cv2.circle(img, (cx, cy), 25, (255,0,255), cv2.FILLED)
                        self.finger_x_coordinate = cx
                        self.finger_y_coordinate = cy
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)




