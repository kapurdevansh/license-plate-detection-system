# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:10:12 2024

@author: devansh
"""
import cv2
from datetime import datetime
import threading

class CameraCapture(threading.Thread):
    def __init__(self):
        super().__init__()
        self.output_path = None
        self.filename = None
        self.capture = cv2.VideoCapture(0)
        self.stopped = False

    def run(self):
        while not self.stopped:
            ret, frame = self.capture.read()
            cv2.imshow('Camera Feed', frame)

            # Break the loop and capture snapshot when 's' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('s'):
                self.capture_snapshot(frame)
                break

            # Break the loop when 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.capture.release()
        cv2.destroyAllWindows()

    def capture_snapshot(self, frame):
        # Generate a timestamp-based filename
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.filename = f'car_{timestamp}.jpg'

        # Save the snapshot as an image file
        self.output_path = 'E:/IPBA/byop/license_plate_detection/input/'  # specify your desired output directory
        filepath = self.output_path + self.filename
        cv2.imwrite(filepath, frame)
        print(f"Snapshot captured and saved as {filepath}")

    def stop(self):
        self.stopped = True

def main():
    camera = CameraCapture()
    camera.start()
    camera.join()

    # Access the captured snapshot filename and output path
    output_path = camera.output_path
    filename = camera.filename
    return output_path, filename

if __name__ == "__main__":
    main()



