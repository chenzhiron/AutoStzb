from PIL import Image
from path.img import path


def fill_image(image_path):
    image = Image.open(image_path)
    width, height = image.size

    # 创建一个与原始图像相同大小的新图像
    filled_image = Image.new('RGB', (width, height), 'black')

    # 计算中心点的位置
    center_x = width // 2
    center_y = height // 2

    # 获取中心100*100的矩形区域
    left = center_x - 50
    top = center_y - 50
    right = center_x + 50
    bottom = center_y + 50

    # 将中心矩形区域从原始图像复制到新图像
    filled_image.paste(image.crop((left, top, right, bottom)), (left, top))

    # 返回填充后的图像
    return filled_image


if __name__ == '__main__':
    # 调用函数并保存填充后的图像
    filled_image = fill_image(path)
    filled_image.save(path)
