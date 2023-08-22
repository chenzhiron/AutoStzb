from PIL import Image

def img_join():
			# 读取图片
	image1 = Image.open('image1.jpg')
	image2 = Image.open('image2.jpg')


	# 获取图片宽度和高度
	width = max(image1.width, image2.width)
	height = image1.height + image2.height


	# 创建一个新的空白图片
	result_image = Image.new('RGB', (width, height))

	# 将第一张图片粘贴到上半部分
	result_image.paste(image1, (0, 0))

	# 将第二张图片粘贴到下半部分
	result_image.paste(image2, (0, image1.height))

	# 保存拼接后的图片
	result_image.save('result.jpg')
