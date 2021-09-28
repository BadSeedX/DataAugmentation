# -------------------------------
#   将输入的两张图片进行mixup混合
# -------------------------------



import cv2
import os

def mixup(dir1,dir2):

    dir1_img_paths = os.listdir(dir1)
    dir2_img_paths = os.listdir(dir2)
    save_path = "./data/temp/mixup_imgs/"

    for dir1_img_path_ in dir1_img_paths:
        dir1_img_path = dir1 + dir1_img_path_
        for dir2_img_path_ in dir2_img_paths:
            dir2_img_path = dir2 + dir2_img_path_
            dir1_img = cv2.imread(dir1_img_path)
            dir2_img = cv2.imread(dir2_img_path)
            # mix_img_height = max(dir1_img.shape[1], dir2_img.shape[2])
            # mix_img_width = max(dir1_img.shape[2], dir2_img.shape[2])
            lambd = 0.5
            mix_img = dir1_img * lambd + dir2_img * (1. - lambd)
            save = save_path + dir1_img_path_.split('.')[0] + "_" + dir2_img_path_.split('.')[0] + ".jpg"
            cv2.imwrite(save, mix_img)
    """
    pos_img = cv2.imread(pos)
    neg_img = cv2.imread(neg)
    mix_img_height = max(pos_img.shape[1], neg_img.shape[2])
    mix_img_width = max(pos_img.shape[2], neg_img.shape[2])
    mix_img_shape = (3, mix_img_height, mix_img_width)
    lambd = 0.5
    print(pos_img)
    mix_img = pos_img*lambd + neg_img * (1. - lambd)
    cv2.imshow('mix_img', mix_img)
    cv2.waitKey(0)
    """

if __name__ == "__main__":
    dir1 = "./data/rawImages/"
    dir2 = "./data/temp/capture_imgs/"
    mixup(dir1, dir2)
