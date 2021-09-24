import torch
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms.functional as TF

class trans:
    def __init__(self):
        pass

    # 调整对比度
    def adjustContrast(self, img, contrast_factor = 2):
        return TF.adjust_contrast(img, contrast_factor)

    # 调整图像亮度
    def adjustBrightness(self, img, brightness_factor = 2):
        return TF.adjust_brightness(img, brightness_factor)

    # 调整图像饱和度
    def adjustSaturation(self, img, saturation_factor = 2):
        return TF.adjust_saturation(img, saturation_factor)

    # 调整图片色相
    def adjustHue(self, img, hue_factor=0.1):
        return TF.adjust_hue(img, hue_factor)

    # gamma校正
    def adjustGamma(self, img, gamma=2):
        return TF.adjust_gamma(img, gamma)

    # 随机交换图片颜色通道
    def lightingNoise(self, img):
        perms = ((0, 2, 1), (1, 0, 2),(1, 2, 0), (2, 0, 1), (2, 1, 0))
        swap = perms[random.randint(0, len(perms) - 1)]
        img = TF.to_tensor(img)
        img = img[swap, :, :]
        return TF.to_pil_image(img)

    # 水平(竖直)翻转
    # TODO 图片翻转，对应的boxes也要翻转
    def flip(self, img, flip = "h"):
        if flip == "h":
            return TF.hflip(img)
        elif flip == "v":
            return TF.vflip(img)

    # 图片旋转
    # TODO 图片旋转，对应的boxes也要旋转
    def rotate(self, img, angle = 10):
        return img.rotate(angle, expand=True)

if __name__ == "__main__":

    rawImage = Image.open("E:/DataAugmentation/data/rawImages/227.jpg")

    trans = trans()
    testImage = trans.rotate(rawImage)
    plt.figure("test")
    plt.imshow(testImage)
    plt.show()