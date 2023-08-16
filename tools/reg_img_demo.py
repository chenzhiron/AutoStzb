
from path.img import path
from PIL import Image

def fill_non_white(image):
    # 将图片转换为RGBA模式，以便处理透明度
    image = image.convert("RGBA")

    # 获取图片的宽度和高度
    width, height = image.size

    # 创建一个新的空白图片，尺寸与原图片相同
    new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # 遍历每个像素点
    for x in range(width):
        for y in range(height):
            # 获取当前像素点的颜色值
            r, g, b, a = image.getpixel((x, y))

            # 检查是否为白色（RGB值全为255）
            if r == 255 and g == 255 and b == 255:
                # 将白色像素点复制到新图片中
                new_image.putpixel((x, y), (r, g, b, a))
            else:
                # 将非白色像素点填充为黑色（不透明）
                new_image.putpixel((x, y), (0, 0, 0, 255))

    # 转换为RGB模式
    new_image = new_image.convert("RGB")

    return new_image


if __name__ == '__main__':

    # 打开原图片
    image = Image.open(path)

    # 调用函数进行处理
    new_image = fill_non_white(image)

    # 保存新图片为JPEG格式
    new_image.save(path)
