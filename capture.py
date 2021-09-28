import cv2

def capture():
    video = cv2.VideoCapture("E:/DataAugmentation/data/video/test.avi")
    idx = 0
    time = 0
    freq = 1000
    if video.isOpened():
        rval, frame = video.read()
    else:
        rval = False
    while rval:
        rval, frame = video.read()
        if(time % freq == 0):
            cv2.imwrite("E:/DataAugmentation/data/temp/capture_imgs/" + str(idx) + ".jpg", frame)
            idx += 1
        time += 1
        cv2.waitKey(1)
    video.release()

if __name__ == "__main__":
    capture()
