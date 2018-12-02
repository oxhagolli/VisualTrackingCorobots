"""
    Tracker performance visualizer.

    Author: Orens Xhagolli (oxx6096@cs.rit.edu)
    Fall, 2018

    Acknowledgements: Thanks to Dr. Satya Mallick from learnopencv.com for great examples!
"""

import cv2
import sys
import os
import re


def main():
    if len(sys.argv) != 3:
        raise AssertionError("Usage: python hierarchy_compare.py tracker_type tests_path")

    # Create the tracker
    tracker = getattr(cv2, "Tracker{}_create".format(sys.argv[1]))()

    # Read the test directory. Assumes the test follow the format used in the paper
    path = sys.argv[2]
    if path[-1] != "/":
        path += "/"
    files = os.listdir(path)
    sorted_files = sorted(files, key=lambda filename: int(re.findall(r'\d+', filename)[0]))

    # Select the ROI in the test
    frame = cv2.imread(path + sorted_files.pop(0), 0)
    bbox = cv2.selectROI("Select ROI to track", frame)
    cv2.destroyAllWindows()  # Clear screen

    if not tracker.init(frame, bbox):
        raise AssertionError("Could not initialize tracker!")

    while len(sorted_files) > 0:
        frame = cv2.imread(path + sorted_files.pop(0), 0)
        ok, bbox = tracker.update(frame)

        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        cv2.putText(frame, type(tracker).__name__, (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        cv2.imshow("Tracking ...", frame)
        cv2.waitKey(33)  # Assumes ~30fps


if __name__ == "__main__":
    main()
