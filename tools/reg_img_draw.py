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
    draw.rectangle([0, 0,width, fill_area[1]], fill='black')  # 上部分
    draw.rectangle([0, fill_area[3], width, height], fill='black')  # 下部分
    draw.rectangle([0, fill_area[1], fill_area[0], fill_area[3]], fill='black')  # 左部分
    draw.rectangle([fill_area[2], fill_area[1], width, fill_area[3]], fill='black')  # 右部分

    filled_image.save(image_path)