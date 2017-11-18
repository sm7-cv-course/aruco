import cv2
import numpy as np
from cv2 import aruco

# Parameters
markers_y = 2
markers_x = 3
img_w = 297
img_h = 207

# Create image
marker_board = np.zeros((img_h, img_w))

mark_size = img_w // markers_x
step_x = img_w // markers_x
step_y = img_h // markers_y

aruco_dict = cv2.aruco.getPredefinedDictionary( aruco.DICT_5X5_250 )

img = aruco.drawMarker(aruco_dict, 2, 700)


# for i in range(1, markers_y, step_y):
#     for j in range(1, markers_x, step_x):
#         img = aruco.drawMarker(aruco_dict, 2, 70)
#         aruco.drawMarker(dict, 5, 10, img, 1)

        # cv2.drawMarker(dict, (j, i), (255, 255, 255),
        #                markerType=cv2.MARKER_SQUARE,
        #                markerSize=mark_size)
                       # thickness=2, line_type=8)



cv2.imwrite("aruco.png", img)
# cv2.imwrite("aruco.png", marker_board)
