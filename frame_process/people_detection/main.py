from typing import List, Tuple

import cv2
import numpy as np
from ultralytics import YOLO

from frame_process.people_detection.models.config import people_color, people_detect_classes, people_detect_model


class PeopleDetector:
    def __init__(self):
        self.model = YOLO(people_detect_model)
        self.classes = people_detect_classes
        self.people_class_id = 0
        self.people_label = "person"
        self.people_color = people_color[self.people_label]

    def check_people(self, people_frame: np.ndarray) -> Tuple[bool, List]:
        results = self.model(people_frame, stream=False, conf=0.60)
        detect_boxes = [box for res in results for box in res.boxes if int(box.cls[0]) == self.people_class_id]
        return bool(detect_boxes), detect_boxes

    def draw_detections_boxes(self, people_frame: np.ndarray, info_people: List):
        for box in info_people:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            color = self.people_color
            conf = float(box.conf[0])
            cv2.rectangle(people_frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(people_frame, f"{self.people_label} {conf:.4f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    def main(self, people_frame: np.ndarray, draw_detections: bool = True) -> int:
        check_people, info_people = self.check_people(people_frame)
        if check_people:
            if draw_detections:
                self.draw_detections_boxes(people_frame, info_people)
            return len(info_people)
        else:
            return 0
