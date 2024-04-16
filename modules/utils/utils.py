import datetime
from io import BytesIO
from PIL import Image

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

def img_bytes_like(v):
   # 将NumPy数组转换为PIL Image对象
    img = Image.fromarray(v)

    # 将图像编码为JPEG格式的bytes-like object
    with BytesIO() as f:
        img.save(f, format='JPEG')
        img_bytes = f.getvalue()
    return img_bytes
