import re

def reg_address(coordinates):
	result = []
	for coord in coordinates:
			# 使用正则表达式去掉头尾括号
			coord = re.sub(r'^（|）$', '', coord)
			# 使用正则表达式分割字符串
			x, y = re.split(r'\W+', coord)
			# 转换为整数并添加到结果数组
			result.append([int(x), int(y)])

	return result
