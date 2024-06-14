import cv2
import numpy as np
from frame_process.people_detection.main import PeopleDetector


class PeopleProcessing:
    def __init__(self):
        self.people_processor = PeopleDetector()

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)

    def main(self):
        while True:
            ret, frame = self.cap.read()
            people_count = self.people_processor.main(frame)
            cv2.imshow('people detect', frame)
            t = cv2.waitKey(1)
            if t == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()
