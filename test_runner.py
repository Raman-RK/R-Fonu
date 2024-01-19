# test_runner.py
import os
import pytest
import subprocess
import cv2
import numpy as np
from selenium import webdriver
from mss import mss
from PIL import Image


@pytest.fixture(scope="session")
def setup(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def capture_screen_video(output_path):
    mon = {'left': 0, 'top': 0, 'width': 800, 'height': 600}  # Adjust the values based on your screen resolution

    with mss() as sct:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")  # Alternative codec
        out = cv2.VideoWriter(output_path, fourcc, 20.0, (mon['width'], mon['height']))

        while True:
            screenShot = sct.grab(mon)
            img = Image.frombytes('RGB', (screenShot.width, screenShot.height), screenShot.rgb)
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            out.write(frame)

            cv2.imshow('test', frame)
            if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
                break

        out.release()
        cv2.destroyAllWindows()


def test_run():
    test_signin_path = os.path.join(os.path.dirname(__file__), 'testCases/test_signin.py')
    test_teams_path = os.path.join(os.path.dirname(__file__), 'testCases/test_teams.py')
    test_phone_path = os.path.join(os.path.dirname(__file__), 'testCases/test_phone.py')
    allure_results_path = os.path.join(os.path.dirname(__file__), 'allure-results')

    # Start recording video in the background
    video_output_path = os.path.join(os.path.dirname(__file__), 'fonu', 'video', 'test_run_video.avi')
    video_process = subprocess.Popen(['python', 'video_recorder.py', video_output_path])

    # Run the tests
    pytest.main(['-q', '--alluredir', allure_results_path, test_signin_path, test_teams_path, test_phone_path])

    # Stop recording video
    video_process.terminate()


if __name__ == "__main__":
    test_run()
