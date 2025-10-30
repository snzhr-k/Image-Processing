import cv2


def mouse_click(event, x, y, flags, param):
    # Taking global a variable
    global im_gray_bgr, im_gray_bgr_orig

    # More mouse events:
    # https://docs.opencv.org/4.12.0/d0/d90/group__highgui__window__flags.html#ga927593befdddc7e7013602bca9b079b0
    if event == cv2.EVENT_MOUSEMOVE:
        im_gray_bgr = im_gray_bgr_orig.copy()
        # If the image has 3 indexable dimensions
        if im_gray_bgr.ndim == 3:
            im_gray_bgr[:, x] = [0, 255, 255]
            im_gray_bgr[y, :] = [0, 255, 255]

        # If we change the contents of the image matrix, it must be redisplayed
        cv2.imshow('im', im_gray_bgr)


# im = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
im_gray = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)
im_gray_bgr = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2BGR)
im_gray_bgr_orig = im_gray_bgr.copy()

print('Indexable dimensions of the image:', im_gray_bgr.ndim)
print('Image shape:', im_gray_bgr.shape)
print('Image pixel type:', im_gray_bgr.dtype)

cv2.imshow('im', im_gray_bgr)
# Set mouse callback function for the window
cv2.setMouseCallback('im', mouse_click)
# Exit to keypress
cv2.waitKey(0)

cv2.destroyAllWindows()
