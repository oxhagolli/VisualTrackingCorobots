# Visual Tracking for Corobots
This project contains supporting code and files for my Master's project at the Rochester Institute of Technology.
The goal of this project is to provide a good framework of comparing different Visual Tracking algorithms and
an implementation for making OpenCV tracking compatible with the Robot Operating System (ROS). My adviser is 
[Dr. Zachary Butler](https://cs.rit.edu/~zjb/).

# Requirements
This project requires OpenCV and/or ROS to properly run. Please follow up-to-date guides to install each library 
properly. Usually a `requirements.txt` file can't achieve the desired goal properly since these are really large 
libraries.

Additionally, you might need to download pre-trained models to run GOTURN.

# Usage
## Hierarchy of Tracking Comparison
To run the hierarchical tests, follow the order described in the paper. The usage for `hierarchy_compare.py` is as 
follows:
```
python hierarchy_compare.py tracker_type tests_path
```

For example, if we were to run a MedianFlow tracker on the crowded environment test, it would look like this:
```
python hierarchy_compare.py MedianFlow tests/crowded
```

## Speed Comparison
To run the speed tests, simply pick a tracker and the time that you would like to let it run for. The longer, 
the more reliable your statistics will be. Avoid drifting scenarios during runtime to get an accurate read.
The usage for `speed_compare.py` is as follows:
```
python speed_compare.py tracker_type number_seconds
``` 

For example, if we were to run the AdaBoost tracker, over the course of 1 minute, we would do the following:
```
python speed_compare.py Boosting 60
```

## ROS Tracker

Please follow the documentation on the ROS website to properly run the `tracker.py` file. This is simply a 
ROS-compatible implementation of the tracking API.

### Please note that capitalization matters during usage. Use proper case.

### All code should be compatible with the latest OpenCV. Refer to documentation for proper tracker_type names.

# Acknowledgements

## Adviser
Thank you Dr. Zachary Butler for advising my Master's project.

## Code Resources
Thank you to Dr. Satya Mallick for his tutorials on learnopencv.com.
I reused a lot of the code from the tutorial on tracking on writing the comparison algorithms.

## Video
Thank you to Omkar Kakade (ork1257@cs.rit.edu), Christian Brady (chb9645@cs.rit.edu),
Akshay Sharma (acs1246@cs.rit.edu), Aniruddha Shukla (ags4602@cs.rit.edu) and Gokul Chandraketu (gg6796@cs.rit.edu)
for helping create the test videos.

# Errata
For any errors or concerns with the code or the paper, please reach out to Orens Xhagolli (oxx6096@cs.rit.edu).
Please feel free to use github issues or any other github functionality if you would like to contribute. 
All contributions are welcome.

# License
This project is under the MIT License. For any questions related to licensing please reach out to 
Orens Xhagolli (oxx6096@cs.rit.edu)