"""
    Tracker performance visualizer.

    Author: Orens Xhagolli (oxx6096@cs.rit.edu)
    Fall, 2018

    Acknowledgements: Thanks to Dr. Satya Mallick from learnopencv.com
"""

import cv2
import sys
import time


def main():
    if len(sys.argv) != 3:
        raise AssertionError("Usage: python speed_compare.py tracker_type number_seconds")

    # Create the tracker
    tracker = getattr(cv2, "Tracker{}_create".format(sys.argv[1]))()

    # Create the video channel
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        raise AssertionError("Could not open video feed!")

    # Select ROI in the video
    _, _ = video.read()
    time.sleep(2)  # Allows for laptop cameras to light up
    ok, frame = video.read()

    bbox = cv2.selectROI("Select ROI to track", frame)
    cv2.destroyAllWindows()  # Clear screen

    if not tracker.init(frame, bbox):
        raise AssertionError("Could not initialize tracker!")

    run_sum = []
    clock = time.time() + 10
    while time.time() < clock:
        ok, frame = video.read()

        # Time the tracker speed in fps
        timer = cv2.getTickCount()
        ok, bbox = tracker.update(frame)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        run_sum.append(fps)

        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        cv2.putText(frame, type(tracker).__name__, (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        cv2.imshow("Tracking ...", frame)
        cv2.waitKey(1)

    print("Average fps for " + type(tracker).__name__ + " is " + str(sum(run_sum) / len(run_sum)))


if __name__ == "__main__":
    main()
