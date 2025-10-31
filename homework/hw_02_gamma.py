import cv2
import numpy as np

def on_trackbar(pos):
    global img_1
    # map [0..80] to gamma ~ (0.2 .. 5.0) with 40 ≈ 1.0
    gamma = (pos / 10.0) - 3
    if gamma < 1:
        gamma = -1.0 / (gamma - 2.0)

    lut = create_gamma_lut(gamma)
    apply_lut(img_1, lut, f"γ = {gamma:0.2f}")

def create_gamma_lut(gamma):
    lut = np.arange(256, dtype=np.float32) / 255.0
    lut = np.power(lut, gamma)
    return np.uint8(lut * 255.0)

def apply_lut(image, lut, label_text):
    print(label_text)
    im_lut = cv2.LUT(image, lut)         # applies to all 3 channels
    cv2.imshow('Gamma', im_lut)
    

#fname = 'homework/inside-1.JPG'
fname = 'homework/lowlight-street-1.JPG'
img_1 = cv2.imread(fname, cv2.IMREAD_COLOR)

cv2.imshow('gamma', img_1)
cv2.namedWindow('Gamma')                 # create the window first
cv2.createTrackbar('Parameter', 'Gamma', 40, 80, on_trackbar)
on_trackbar(40)                          # draw initial view

cv2.waitKey(0)
cv2.destroyAllWindows()

