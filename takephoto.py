import os
import time

import cv2
import imageio


def TakePhoto():
    save_path = "./photo/"
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    try:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        # 添加水印
        x, y, d = frame.shape
        x -= 200
        y -= 180
        cv2.putText(img=frame, text='http://zkeeer.space',
                    org=(x, y), fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                    fontScale=1, color=(255, 255, 255))
        # 保存图片
        img_name = "{}pic_{}.png".format(save_path, int(time.time()))
        cv2.imwrite(img_name, frame)
        return img_name
    except BaseException as e:
        return ""


def TakeGIF(seconds=5):
    img_list = []
    frame_rate = 10
    tmp_path = "./tmp/"
    save_path = "./photo/"

    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    try:
        cap = cv2.VideoCapture(0)

        for index in range(0, int(seconds * frame_rate)):
            # 获取图片
            ret, frame = cap.read()
            # 添加水印
            x, y, d = frame.shape
            x -= 200
            y -= 180
            cv2.putText(img=frame, text='http://zkeeer.space',
                        org=(x, y), fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                        fontScale=1, color=(255, 255, 255))
            # 压缩
            x, y, d = frame.shape
            frame = cv2.resize(frame, (y // 2, x // 2))

            # 保存图片
            cv2.imwrite("{}{}.png".format(tmp_path, index), frame)
            img_list.append(imageio.imread("{}{}.png".format(tmp_path, index)))
            os.remove("{}{}.png".format(tmp_path, index))
            time.sleep(1 / frame_rate)

        # 保存gif
        img_name = "{}gif_{}.gif".format(save_path, int(time.time()))
        imageio.mimsave(img_name, img_list)
        return img_name
    except BaseException as e:
        return ""


if __name__ == '__main__':
    TakeGIF(5)
