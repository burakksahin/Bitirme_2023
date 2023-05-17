import cv2
import time

from playsound import playsound
import numpy as np
from drowsy_detection import VideoFrameHandler
from drowsy_detection import plot_text


def main():
    frame_count = 0

    # Initialize the VideoFrameHandler object
    frame_handler = VideoFrameHandler()

    # Set the thresholds for the drowsiness detection algorithm
    thresholds: dict = {"WAIT_TIME": 2.5, "EAR_THRESH": 0.14}

    # Set up the camera capture object
    cap = cv2.VideoCapture(0)

    # Loop through the frames from the camera
    while True:
        frame_count += 1
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was successfully read
        if not ret:
            print("Error reading frame from camera")
            break

        # Process the frame using the VideoFrameHandler object
        processed_frame, play_alarm = frame_handler.process(frame, thresholds)

       

        # Display the processed frame on the console
        print(processed_frame.shape)
        print(f"Alarm should be played: {play_alarm}")
        
        # play sound if alarm is on
        if play_alarm and frame_count % 0.5 == 0:
            playsound('alert.wav', block=True)


        cv2.imshow("frame", processed_frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
