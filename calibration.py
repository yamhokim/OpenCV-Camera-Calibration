# Implementing a camera calibration function utilizing Zhang's method

# Reference Links:
# https://www.youtube.com/watch?v=3h7wgR5fYik&t=38s&ab_channel=NicolaiNielsen 
# https://www.youtube.com/watch?v=_-BTKiamRTg&list=PLkmvobsnE0GEo-D7DLnrYS1K4OemycX6k&index=77&ab_channel=NicolaiNielsen 
# https://www.youtube.com/watch?v=JHeNger8B2E&t=374s&ab_channel=AiPhile
# https://www.youtube.com/watch?v=-9He7Nu3u8s&ab_channel=CyrillStachniss 
# https://medium.com/analytics-vidhya/camera-calibration-with-opencv-f324679c6eb7 

# Demo Code for Reusing Camera Matrices on videos
#import cv2

# Assuming you have already obtained the camera matrix
"""
camera_matrix = ...

# Save the camera matrix to a file
fs = cv2.FileStorage("camera_matrix.yml", cv2.FILE_STORAGE_WRITE)
fs.write("camera_matrix", camera_matrix)
fs.release()
"""

"""
import cv2

# Load the camera matrix from the file
fs = cv2.FileStorage("camera_matrix.yml", cv2.FILE_STORAGE_READ)
camera_matrix = fs.getNode("camera_matrix").mat()
fs.release()

import cv2
import numpy as np

# Load the camera matrix
fs = cv2.FileStorage("camera_matrix.yml", cv2.FILE_STORAGE_READ)
camera_matrix = fs.getNode("camera_matrix").mat()
fs.release()
"""

"""
# Open the video file
video = cv2.VideoCapture("your_video.mp4")

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Apply camera matrix to the frame
    undistorted_frame = cv2.undistort(frame, camera_matrix, np.zeros(5))

    # Display the undistorted frame or perform other operations

    cv2.imshow("Undistorted Frame", undistorted_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
"""
