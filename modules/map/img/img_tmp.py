import os
import numpy as np
from PIL import Image

# 创建一个字典来保存灰度图像数据
gray_images = {}


def init_img_tmp():
    # 获取当前目录下所有图片文件
    image_files = [f for f in os.listdir('.') if
                   os.path.isfile(f) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # 遍历每个图片文件
    for file in image_files:
        # 获取图片名字（没有后缀名）
        image_name = os.path.splitext(file)[0]

        # 打开图片
        image = Image.open(file)

        # 将图片转换为灰度图像
        gray_image = image.convert("L")

        # 将灰度图像转换为灰度图像数据
        gray_image_data = np.array(gray_image)

        # 将灰度图像数据添加到字典中
        gray_images[image_name] = gray_image_data

    # 打印灰度图像数据字典
    print(gray_images)


init_img_tmp()
