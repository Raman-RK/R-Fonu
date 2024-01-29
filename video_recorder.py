# video_recorder.py
import sys

import cv2
import numpy as np
import pyautogui
from pyautogui import screenshot

output_path = "output_video.avi"

screen_size = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_path, fourcc, 20.0, (screen_size.width, screen_size.height))

try:
    while True:
        img = screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
except KeyboardInterrupt:
    out.release()
