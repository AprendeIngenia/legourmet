import numpy as np
import mediapipe as mp
import cv2
from typing import Tuple, Any


class FaceDetect:
    def __init__(self):
        # mediapipe
        self.object_detect_mp = mp.solutions.face_detection
        self.face_detector_mp = self.object_detect_mp.FaceDetection(min_detection_confidence=0.7, model_selection=0)
        self.bbox: list = []
        self.face_points: list = []

    def check_face_detect(self, face_image: np.ndarray) -> Tuple[bool, Any]:
        rgb_image = face_image.copy()
        rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)

        faces_info = self.face_detector_mp.process(rgb_image)
        if faces_info.detections is None:
            return False, faces_info
        else:
            return True, faces_info

    def count_faces(self, faces: Any) -> int:
        return len(faces.detections)

    def main(self, faces_images: np.ndarray) -> int:
        check_faces, faces_info = self.check_face_detect(faces_images)
        if check_faces is False:
            return 0
        else:
            return self.count_faces(faces_info)



