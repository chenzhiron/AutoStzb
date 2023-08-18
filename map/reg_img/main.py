from PIL import Image

def convert_to_grayscale(image_path):
    image = Image.open(image_path)

    # 将图像转换为灰度
    gray_image = image.convert('L')

    gray_image.save(image_path)
    # 返回灰度图像
    return gray_image

# 调用函数并保存灰度图像
# gray_image = convert_to_grayscale('path/to/your/image.jpg')
# gray_image.save('path/to/save/gray_image.jpg')