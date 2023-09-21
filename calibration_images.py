import cv2
import os

chessboardDimensions = (9, 6)

n = 0   # image counter

image_directory_path = "calibration images"
# Check if the directory already exists, if not, create it

check_directory = os.path.isdir(image_directory_path)

if check_directory == False:
    os.makedirs(image_directory_path)
    print(f"The directory '{image_directory_path}' has been created")
else:
    print(f"The directory '{image_directory_path}' already exists")

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def detect_checker_board(image, grayImage, criteria, boardDimensions):
    ret, corners  = cv2.findChessboardCorners(grayImage, boardDimensions)
    if ret == True:
        corners1 = cv2.cornerSubPix(grayImage, corners, (3, 3), (-1, -1), criteria)
        image = cv2.drawChessboardCorners(image, boardDimensions, corners1, ret)

    return image, ret

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    copyFrame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    image, board_detected = detect_checker_board(frame, gray, criteria, chessboardDimensions)

    cv2.putText(frame, f"saved image: {n}", (30, 40), cv2.FONT_HERSHEY_PLAIN, 1.4, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("frame", frame)
    cv2.imshow("copyFrame", copyFrame)

    if cv2.waitKey(1) == ord('q'):
        break
    if cv2.waitKey(1) == ord('s') and board_detected == True:
        cv2.imwrite(f"{image_directory_path}/image{n}.png", copyFrame)

        print(f"saved image {n}")
        n += 1

cap.release()
cv2.destroyAllWindows()

print(f"Total Saved Images: {n}")
