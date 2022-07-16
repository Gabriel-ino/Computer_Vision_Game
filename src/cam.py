import cv2
from hand_tracker import HandTracker


class Cam:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.frame = None
        self.hand_tracker = HandTracker()

    def recording(self):
        check, self.frame = self.cam.read()
        self.frame = cv2.flip(self.frame, 1)
        self.hand_tracker.tracking(self.frame)
        key = cv2.waitKey(0)

    def convert_frame(self):
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame, (720, 480))







