import cv2
import numpy as np
import time 
from matplotlib import pyplot as plt

def get_diagram_as_image(fig_in):
    fig_in.canvas.draw()
    data = np.array(fig_in.canvas.renderer.buffer_rgba())
    data_bgr = cv2.cvtColor(data, cv2.COLOR_RGBA2BGR)

    return data_bgr

def do_brightness_contrast():
    global brightness, contrast, new_image

    print('======================')
    print('Brightness:', brightness)
    print('Contrast:', contrast)

    factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
    print('Factor:', factor)

    start_time = time.perf_counter()

    # Using OpenCV LUT
    x = np.arange(0, 256, 1)
    lut = np.uint8(np.clip(brightness + factor * (np.float32(x) - 128.0) + 128, 0, 255))
    new_image = cv2.LUT(im, lut)
    end_time = time.perf_counter()

    print((end_time - start_time) * 1000.0, 'ms')

    ax.clear()
    x = np.arange(0, 256, 1)
    ax.plot(x, x, 'g--', label='Original', linewidth=2)
    ax.plot(x, lut, 'r-', label='Brightness/contrast mapping', linewidth=2)
    plt.legend()

    lut_im = get_diagram_as_image(fig)
    cv2.imshow('LUT', lut_im)

    cv2.imshow('original', im)
    cv2.imshow('modified', new_image)

def on_trackbar_brightness(br):
    global brightness
    brightness = br - 255
    do_brightness_contrast()


def on_trackbar_contrast(cntr):
    global contrast
    contrast = cntr - 255
    do_brightness_contrast()

if __name__ == "__main__":
    fname = 'homework/lowlight-street-4.JPG'
    #fname = 'homework/lowlight-street-2.JPG'
    im = cv2.imread(fname)

    new_image = im.copy()

    fig = plt.figure(figsize=(4, 4), dpi=100)
    ax = fig.add_subplot(111)
    plt.xlabel('Eredeti intenzitásérték')
    plt.ylabel('Pont operáció eredménye')
    plt.xlim([0, 255])
    plt.ylim([0, 255])
    plt.tight_layout()
    
    brightness = 0
    contrast = 0
    
    cv2.imshow('original', im)
    cv2.imshow('modified', im)

    cv2.createTrackbar('Brightness', 'modified', 255, 511, on_trackbar_brightness)
    cv2.createTrackbar('Contrast', 'modified', 255, 511, on_trackbar_contrast)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

