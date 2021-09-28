# ---------------------------------------------------------
#  每进行一种trans中的操作，就要把新生成图片的检测框信息写清楚
# ---------------------------------------------------------


import torchvision.transforms.functional as TF
from PIL import Image


# trans.flip

path = "./data/rawImages/227.jpg"
img = Image.open(path)
file = open("./data/txt/227.txt")
contents = file.readlines()

halfw = img.width // 2
x1 = contents[0].split(' ')[1]
x2 = contents[0].split(' ')[3]

if contents[0].split(' ')[1] < halfw:
    new_x2 = img.width - x1
    new_x1 = img.width - x2

# new_x1, y1, new_x2, y2

# print(contents[0].split(' '))
# print(img.height, img.width)