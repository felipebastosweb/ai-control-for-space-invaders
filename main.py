
# OpenCV integration with Space Invaders
# Modified by Felipe Bastos <felipebastosweb@gmail.com

import time
import pyautogui
from vision import DetectHumanMovement

moving = DetectHumanMovement()

while True:
    moving.capture_gray_image()
    faces = moving.detect_faces()
    fists = moving.detect_fists()
    for face in faces:
        orientation = moving.face_laterality_orientation(face)
        if orientation < 0:
            pyautogui.press("left")
        if orientation > 0:
            pyautogui.press("right")
    if moving.fist_check():
        pyautogui.click()
    time.sleep(1)
