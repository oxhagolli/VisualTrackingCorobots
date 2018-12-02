#!/usr/bin/env python

"""
    Visual Tracker for the Kinect

    Author: Orens Xhagolli (oxx6096@cs.rit.edu)
    Fall, 2018
"""

import rospy
import cv2

from sensor_msgs.msg import Image as KinectImage
from cv_bridge import CvBridge


class Robot:

    def __init__(self, tracker):
        self.bridge = CvBridge()  # OpenCV API
        self.image = None  # Start with no image
        self.tracker = tracker # tacker OBJECT
        self.tracker_success = False # tacker read flag set to False
        self.tracker_bbox = None # No initial bounding box
        self.tracker_init = False

    def image_update(self, raw_image):
        self.image = self.bridge.imgmsg_to_cv2(raw_image, "passthrough")

    def tracker_update(self):
        self.tracker_success, self.tracker_bbox = self.tracker.update(self.image)

    def visualize(self):
        """
            This section of code is based off of Satya Mallick's implementation from learnopencv.com - Changes have been made appropriately.
        """
        if self.tracker_success:
            p1 = (int(self.tracker_bbox[0]), int(self.tracker_bbox[1]))
            p2 = (int(self.tracker_bbox[0] + self.tracker_bbox[2]), int(self.tracker_bbox[1] + self.tracker_bbox[3]))
            cv2.rectangle(self.image, p1, p2, (255, 0, 0), 2, 1)
        else:
            cv2.putText(self.image, "Tracking failure!", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        if self.image is not None:
            cv2.putText(self.image, "Tracking ...", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
            cv2.imshow("Tracking ...", self.image)
            cv2.waitKey(1)
        else:
            rospy.loginfo("Nothing to visualize!")

    def orchestrator(self, raw_image):
        self.image_update(raw_image)
        if self.tracker_init:
            self.tracker_update()
            self.visualize()

    def selectROI(self, raw_image):
        self.image_update(raw_image)
        if not self.tracker_init:
            self.tracker_bbox = cv2.selectROI(self.image, False)
            self.tracker_success = self.tracker.init(self.image, self.tracker_bbox)
            self.tracker_init = True


def main():
    # Initialize node
    rospy.init_node("oxx6096_tracker", anonymous=False)

    tracker = cv2.TrackerMedianFlow_create() # create a tracker object
    robot = Robot(tracker) # create the robot object

    rospy.Subscriber("/camera/rgb/image_raw", KinectImage, robot.orchestrator, queue_size=1)
    rospy.Subscriber("/camera/rgb/image_raw", KinectImage, robot.selectROI, queue_size=1)

    while not rospy.is_shutdown():
        rospy.spin()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo("Thank you for using the tracker! Exiting ...")
