# --------------------------------------------
#   将给定文件夹的图片路径，检测框写入txt文件
# --------------------------------------------

import os

# 原始图片信息txt路径
txt_dir = "./data/txt/"
# 需要转换的图片文件夹
img_dir = "./data/temp/mixup_imgs/"

# 从img_dir中得到所有图片名
img_paths = os.listdir(img_dir)

# 遍历所有要转换的图片并写入dataset
for img_path in img_paths:
    # 单个图片完整路径
    # path = img_dir + img_path

    # 创建dataset txt文件并打开
    dataset_txt = "dataset2.txt"
    dataset_txt = open(dataset_txt, "a+")
    # 写入图片路径(根据不同的项目要改写)
    dataset_txt.write("./data/dataset/" + img_path)

    # 打开图片对应的txt文件(注意路径改写)并读取
    f = open(txt_dir + img_path.split('.')[0].split('_')[0] + ".txt")
    contents = f.readlines()
    for content in contents:
        dataset_txt.write(" ")
        for c in content.split(' ')[1:]:
            dataset_txt.write(str(int(float(c))) + ",")
        dataset_txt.write("1")
    dataset_txt.write("\n")
    dataset_txt.close()
    f.close()





"""
dir_ = "./data/"
paths = os.listdir(dir_ + "txt")
for path in paths:

    f = open(dir_ + "txt/" + path)
    file = open("dataset.txt", "a+")
    img_path = dir_ + "dataset/" + path.split('.')[0] + ".jpg"
    file.write(img_path)

    contents = f.readlines()
    for content in contents:
        file.write(" ")
        for c in content.split(' ')[1:]:
            file.write(str(int(float(c))) + ",")
        file.write("1")
    file.write("\n")
    file.close()
    f.close()
"""



