import cv2 as cv
import numpy as np

from modules.map.img.init import gray_images


def matchTemplate_img(img, template, threshold=0.8):
    img = img.convert('L')
    template = gray_images[template]
    res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
    w, h = template.shape[::-1]
    loc = np.where(res >= threshold)
    loc_array = []
    base_pt = None
    for pt in zip(*loc[::-1]):
        if base_pt is None:
            base_pt = pt
            tmp = (pt[0], pt[1], pt[0] + w, pt[1] + h)
            loc_array.append(tmp)
            # 在这里处理第一个匹配坐标
            continue
            # 检查当前匹配坐标与第一个匹配坐标的偏移量
        dx = pt[0] - base_pt[0]
        dy = pt[1] - base_pt[1]
        # 检查偏移量是否大于正负5距离
        if abs(dx) > 5 or abs(dy) > 5:
            tmp = (pt[0], pt[1], pt[0] + w, pt[1] + h)
            loc_array.append(tmp)
    print(loc_array)
    return loc_array

# if __name__ == '__main__':
#     matchTemplate_img()
