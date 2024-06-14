import cv2
import math
import numpy as np
from ultralytics import YOLO
from frame_process.people_detection.models.config import (people_detect_model, people_detect_classes, people_color)
from typing import List, Any, Tuple


class PeopleDetector:
    def __init__(self):
        self.model = YOLO(people_detect_model)
        self.classes = people_detect_classes
        self.color = people_color

    def check_people(self, people_frame: np.ndarray) -> Tuple[bool, Any]:
        detect = False
        results = self.model(people_frame, stream=False, conf=0.80)
        for res in results:
            boxes = res.boxes
            for box in boxes:
                cls = int(box.cls[0])
                cls = self.classes[cls]
                if cls in self.color:
                    detect = True
        if detect is False:
            return False, results
        else:
            return True, results

    def extract_detection_info(self, people_image: np.ndarray, detect_info: Any) -> Tuple[list, int, float]:
        height, width, _ = people_image.shape
        bbox: List = []
        cls: int = 0
        conf: float = 0.0
        people_count: int = 0

        for res in detect_info:
            boxes = res.boxes
            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                x1 = max(0, x1)
                y1 = max(0, y1)
                x2 = min(width, x2)
                y2 = min(height, y2)
                bbox = [x1, y1, x2, y2]

                cls = int(box.cls[0])
                conf = math.ceil(box.conf[0])
                people_count = len(boxes)
        return bbox, people_count, conf

    def main(self, people_frame: np.ndarray):
        check_people, info_people = self.check_people(people_frame)
        if check_people:
            people_bbox, people_count, conf = self.extract_detection_info(people_frame, info_people)
            return people_count
        else:
            return 0



