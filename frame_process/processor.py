import cv2
import threading
from frame_process.people_detection.main import PeopleDetector


class PeopleProcessing:
    def __init__(self):
        self.thread = None
        self.people_processor = PeopleDetector()

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)

        self.people_count = 0
        self.running = False
        self.lock = threading.Lock()

    def start_processing(self):
        self.running = True
        self.thread = threading.Thread(target=self.process)
        self.thread.start()

    def stop_processing(self):
        self.running = False
        self.thread.join()
        self.cap.release()
        cv2.destroyAllWindows()

    def process(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Could not read frame.")
                continue
            people_count = self.people_processor.main(frame)
            with self.lock:
                self.people_count = people_count
            #cv2.imshow('people detect', frame)
            if cv2.waitKey(1) == 27:
                self.stop_processing()
                break

    def get_people_count(self):
        with self.lock:
            return self.people_count
