import cv2
import numpy as np

def paste(pic_path):
    img = cv2.imread(pic_path)
    dst = cv2.imread("E:/DataAugmentation/data/rawImages/002.jpg")
    mask = 255 * np.ones(img.shape, img.dtype)
    center = (100, 100)
    output = cv2.seamlessClone(img, dst, mask, center, cv2.MIXED_CLONE)

    cv2.imencode('.jpg', output)[1].tofile(r'E:/DataAugmentation/data/saveImages/001.jpg')
    cv2.imshow('output', output)
    cv2.waitKey(0)

if __name__ == "__main__":
    paste("E:/DataAugmentation/data/cropImages/002.jpg")