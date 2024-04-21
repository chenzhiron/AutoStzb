import datetime
from io import BytesIO
from PIL import Image
import numpy as np
def calculate_max_timestamp(time_list):
    try:
        timestamp_list = []
        status = 0
        for times in time_list:
            try:
                dt = datetime.datetime.strptime(times, '%H:%M:%S')
                timestamp = dt.hour * 3600 + dt.minute * 60 + dt.second
                timestamp_list.append(timestamp)
            except Exception as e:
                status = 1
                timestamp_list.append(0)

        if sum(timestamp_list) == 0 and status == 0:
            return None
        return max(timestamp_list)
    except Exception as e:
        return None


def img_bytes_like(img):
     # 将NumPy数组转换为PIL图像对象
    img_pil = Image.fromarray(img)

    # 转换图像为RGB模式
    rgb_img = img_pil.convert("RGB")
    
    # 创建一个BytesIO对象来保存图像数据
    with BytesIO() as f:
        # 保存图像为JPEG格式
        rgb_img.save(f, format='JPEG')
        return f.getvalue()