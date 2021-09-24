import os
import cv2
from math import ceil

def crop(img_folder_path, txt_folder_path, save_folder_path):
    img_paths = os.listdir(img_folder_path)
    file_paths = os.listdir(txt_folder_path)
    for img_path in img_paths:
        img_path = img_folder_path + img_path
        img = cv2.imread(img_path)
        txt_path = txt_folder_path + img_path.split('/')[-1].split('.')[0] + ".txt"
        txt = open(txt_path, "r")
        if img is not None:
            height, width, channel = img.shape
            contents = txt.readlines()
            for idx, content in enumerate(contents):
                cls, x1, y1, x2, y2 = content.split()
                x1, y1, x2, y2 = int(float(x1)), int(float(y1)), ceil(float(x2)), ceil(float(y2))
                crop_img = img[y1:y2, x1:x2]
                save_path = save_folder_path + img_path.split('/')[-1].split('.')[0] + "_" + str(idx) + ".jpg"
                cv2.imwrite(save_path, crop_img)
        txt.close()

if __name__ == "__main__":
    img_folder_path = "E:/DataAugmentation/data/rawImages/"
    txt_folder_path = "E:/DataAugmentation/data/txt/"
    save_folder_path = "E:/DataAugmentation/data/cropImages/"
    crop(img_folder_path, txt_folder_path, save_folder_path)

