from PIL import Image, ImageDraw


def fill_image(image_path, fill_area):
    image = Image.open(image_path)
    width, height = image.size

    # 创建一个与原始图像相同大小的新图像
    filled_image = Image.new('RGB', (width, height), 'black')

    # 将原始图像复制到新图像
    filled_image.paste(image, (0, 0))

    # 创建一个绘图对象
    draw = ImageDraw.Draw(filled_image)

    # 在填充区域外部绘制黑色矩形
    draw.rectangle([0, 0, width, fill_area[1]], fill='black')  # 上部分
    draw.rectangle([0, fill_area[3], width, height], fill='black')  # 下部分
    draw.rectangle([0, fill_area[1], fill_area[0], fill_area[3]], fill='black')  # 左部分
    draw.rectangle([fill_area[2], fill_area[1], width, fill_area[3]], fill='black')  # 右部分

    filled_image.save(image_path)


def convert_non_white_to_black(image_path):
    # 打开图片
    image = Image.open(image_path)

    # 获取图片尺寸
    width, height = image.size

    # 遍历每个像素点
    for x in range(width):
        for y in range(height):
            # 获取当前像素点的颜色
            pixel = image.getpixel((x, y))

            # 检查当前像素点的颜色是否为白色
            if pixel != (255, 255, 255):
                # 将非白色像素点涂成黑色
                image.putpixel((x, y), (0, 0, 0))

    # 保存修改后的图片
    image.save(image_path)
