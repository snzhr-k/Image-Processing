import cv2
import numpy as np

im = cv2.imread('car.JPG',cv2.IMREAD_COLOR)

bounds_lower = np.array([120, 0, 0])
bounds_upper = np.array([255, 130, 100])
res = cv2.imRange(im, bounds_lower, bounds_upper)
