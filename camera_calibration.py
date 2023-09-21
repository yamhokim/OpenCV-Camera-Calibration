import cv2
import os
import numpy as np

chessboardDimensions = (9, 6)

square_size = 14    # may need to change this later

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

calibration_data_path = "../calib_data"
check_directory = os.path.isdir(calibration_data_path)

if not check_directory:
    os.makedirs(calibration_data_path)
    print(f"The directory '{calibration_data_path}' has been created")
else:
    print(f"The directory '{calibration_data_path}' already exists")

obj_3d = np.zeros((chessboardDimensions[0] * chessboardDimensions[1], 3), np.float32)

obj_3d[:, :2] = np.mgrid[0 : chessboardDimensions[0], 0 : chessboardDimensions[1]].T.reshape(-1,2)
obj_3d *= square_size
print(obj_3d)


obj_points_3d = []
img_points_2d = []

image_dir_path = "calibration images"

files = os.listdir(image_dir_path)
for file in files:
    print(file)
    imagePath = os.path.join(image_dir_path, file)

    image = cv2.imread(imagePath)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(image, chessboardDimensions, None)
    if ret == True:
        obj_points_3d.append(obj_3d)
        corners2 = cv2.cornerSubPix(grayscale, corners, (3,3), (-1, -1), criteria)
        img_points_2d.append(corners2)

        img = cv2.drawChessboardCorners(image, chessboardDimensions, corners2, ret)

cv2.destroyAllWindows()
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points_3d, img_points_2d, grayscale.shape[::-1], None, None)
print("calibrated")

np.savez(f"{calibration_data_path}/MultiMatrix", camMatrix=mtx, distCoef=dist, rVector=rvecs, tVector=tvecs)


# Double checking that the data was saved properly
data = np.load(f"{calibration_data_path}/MultiMatrix.npz")

camMatrix = data["camMatrix"]
distCof = data["distCoef"]
rVector = data["rVector"]
tVector = data["tVector"]

