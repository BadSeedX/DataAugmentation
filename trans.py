# ----------------------------------------------------
#                       26*45*9
#           将数据集中的图片进行基础数据增强操作
#   调整后要保存增强后的图像到save文件夹，并将图片的路径，
#   图片中的目标框写入txt文件中
# ----------------------------------------------------


import torch
import random
import os
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
    def lightingNoise(self, img, swap = (1, 0, 2)):
        # perms = ((0, 2, 1), (1, 0, 2),(1, 2, 0), (2, 0, 1), (2, 1, 0))
        # swap = perms[random.randint(0, len(perms) - 1)]
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


def write_(path, str_):
    f = open("E:/DataAugmentation/data/" + "txt/" + path.split('.')[0].split('_')[0] + ".txt")
    file = open("dataset2.txt", "a+")
    file.write("./data/dataset/" + path.split('.')[0] + str_)
    contents = f.readlines()
    for content in contents:
        file.write(" ")
        for c in content.split(' ')[1:]:
            file.write(str(int(float(c))) + ",")
        file.write("1")
    file.write("\n")
    file.close()
    f.close()


if __name__ == "__main__":

    #rawImage = Image.open("E:/DataAugmentation/data/rawImages/227.jpg")

    trans = trans()
    dir_ = "E:/DataAugmentation/data/temp/mixup_imgs/"
    paths = os.listdir(dir_)
    for path in paths:
        origin = Image.open(dir_ + path)

        trans.adjustContrast(origin).save("E:/DataAugmentation/data/save/" + path.split('.')[0] + "_01.jpg")
        str_ = "_01.jpg"
        write_(path, str_)
        trans.adjustBrightness(origin).save("E:/DataAugmentation/data/save/" + path.split('.')[0] + "_02.jpg")
        str_ = "_02.jpg"
        write_(path, str_)
        trans.adjustSaturation(origin).save("E:/DataAugmentation/data/save/" + path.split('.')[0] + "_03.jpg")
        str_ = "_03.jpg"
        write_(path, str_)
        trans.adjustGamma(origin).save("E:/DataAugmentation/data/save/" + path.split('.')[0] + "_04.jpg")
        str_ = "_04.jpg"
        write_(path, str_)
        trans.adjustHue(origin).save("E:/DataAugmentation/data/save/" + path.split('.')[0] + "_05.jpg")
        str_ = "_05.jpg"
        write_(path, str_)
        trans.lightingNoise(origin).save("E:/DataAugmentation/data/save/" + path.split('.')[0] + "_06.jpg")
        str_ = "_06.jpg"
        write_(path, str_)
        trans.lightingNoise(origin, (2, 1, 0)).save("E:/DataAugmentation/data/save/" + path.split('.')[0] + "_07.jpg")
        str_ = "_07.jpg"
        write_(path, str_)
        trans.lightingNoise(origin, (0, 2, 1)).save("E:/DataAugmentation/data/save/" + path.split('.')[0] + "_08.jpg")
        str_ = "_08.jpg"
        write_(path, str_)





    """
    testImage = trans.rotate(rawImage)
    plt.figure("test")
    plt.imshow(testImage)
    plt.show()
    """