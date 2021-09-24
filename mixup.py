import cv2

def mixup(pos,neg):
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

if __name__ == "__main__":
    mixup("E:/DataAugmentation/data/rawImages/001.jpg","E:/DataAugmentation/data/rawImages/002.jpg")
