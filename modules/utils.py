from datetime import datetime

import cv2
from matplotlib import pyplot as plt
import numpy as np
from openpyxl import Workbook
import os
from datetime import datetime

def formatDate(date_str):
	try:
		# 格式化字符串，插入空格
		formatted_date_str = date_str[:10] + " " + date_str[10:]
		# 解析为 datetime 对象
		date_time_obj = datetime.strptime(formatted_date_str, "%Y/%m/%d %H:%M:%S")
		# 将 datetime 对象转换为时间戳
		timestamp = date_time_obj.timestamp()
		return timestamp
	except:
		return None

def format_date_strptime(date_str):
	# 将字符串解析为 datetime 对象
	dt = datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")

	# 转换为时间戳
	timestamp = int(dt.timestamp())

	return timestamp

def get_formatted_time():
		# 获取当前时间
		now = datetime.now()
		
		return now.timestamp()

def canny_lines(img, area=[140, 195, 1660, 965],threshold_p=200,minLineLength_p=1000, maxLineGap_p=10, offset=100):
	# 裁剪并转为灰度
	cropped_img = np.array(img.crop(area).convert('L'))
	# Canny 边缘检测
	edges = cv2.Canny(cropped_img, 100, 200)
	lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=threshold_p, minLineLength=minLineLength_p, maxLineGap=maxLineGap_p)
		 
	# # 创建彩色图像以绘制线条
	# line_img = cv2.cvtColor(cropped_img, cv2.COLOR_GRAY2BGR)
	
	# # 检测到线条时，绘制每条线
	# if lines is not None:
	# 		for line in lines:
	# 				x1, y1, x2, y2 = line[0]
	# 				cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 绘制为绿色线条，宽度为 2
	
	# plt.imshow(line_img)
	# plt.title("Detected Lines on Image")
	# plt.axis('off')
	# plt.show()

	try:
		lines = lines.squeeze()
		sorted_lines = lines[np.argsort(lines[:, 1])]
		print('sorted_lines: ', sorted_lines)
		filtered_lines = [sorted_lines[0]]  # 保留第一个线条
		# 遍历排序后的线条，过滤掉相邻线条之间 y 值差距小于 100 的线条
		for i in range(1, len(sorted_lines)):
			if sorted_lines[i][1] - sorted_lines[i-1][1] >= offset:
				filtered_lines.append(sorted_lines[i])
			
		filtered_lines = np.array(filtered_lines)
	except Exception as e:
		filtered_lines = []
		print("canny_lines_error: ", e)
	print('canny_lines_origin: ', filtered_lines)
	return filtered_lines

def filter_record(v):
	offset_y = 0
	filter_lines = []
	for i in range(len(v)):
			if v[i][1] > 600:
				continue

			if i == len(v) - 1:
				filter_lines.append(v[i])
				break
			if v[i+1][1] - v[i][1] > 280:
					filter_lines.append(v[i])
			else:
				if i == 0:
					offset_y = v[i+1][1]
					break
				offset_y = v[i][1]
				break
	print('filter_lines', filter_lines)
	print('offset_y', offset_y)
	return (np.array(filter_lines), int(offset_y))
				

def reg_one_line(v):
	print(v[1])
	if v[1] > 95 and v[1] < 113:
		return 0
	if v[1] > 40:
		return v[1]
	else :
		return 0
	

def reg_card(img):
	filtered_lines = canny_lines(img)
	r = reg_one_line(filtered_lines[0])
	return r, filtered_lines

def export_excel(data, filename):
	# 创建一个新的工作簿
	wb = Workbook()
	ws = wb.active
	for v in data:
		# 插入数据
		ws.append(v)
	# 保存 Excel 文件
	wb.save(filename+'.xlsx')

def save_error(d):
	
	# 获取当前项目路径
	current_path = os.getcwd()

	# 设置 error 文件夹路径
	error_folder_path = os.path.join(current_path, "error")

	# 创建 error 文件夹，如果不存在
	if not os.path.exists(error_folder_path):
			os.mkdir(error_folder_path)

	# 设置当前日期的文件夹路径
	date_folder_name = datetime.now().strftime("%Y-%m-%d")
	date_folder_path = os.path.join(error_folder_path, date_folder_name)

	# 创建日期文件夹，如果不存在
	if not os.path.exists(date_folder_path):
			os.mkdir(date_folder_path)
	img_path = os.path.join(date_folder_path, str(get_formatted_time())+'.png')
	d.screenshot().save(img_path)

def find_multiple_templates(main_img, template, threshold=0.8, method=cv2.TM_CCOEFF_NORMED, offset_y = 200):
		
		# 获取模板图像的尺寸
		h, w = template.shape[:2]
		
		# 使用模板匹配
		result = cv2.matchTemplate(main_img, template, method)
		
		# 根据阈值找到符合条件的所有匹配点
		if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
				match_locations = np.where(result <= threshold)  # 对于 TM_SQDIFF，值越小匹配度越高
		else:
				match_locations = np.where(result >= threshold)
	
		filtered_y_positions = []
		for pt in zip(*match_locations[::-1]):  # 使用[::-1] 交换坐标顺序
				y = pt[1]
				
				# 如果过滤列表为空，直接添加第一个匹配点
				if not filtered_y_positions:
						filtered_y_positions.append(y)
				else:
						# 只添加与最后一个 y 坐标距离超过 min_distance 的 y 坐标
						if abs(y - filtered_y_positions[-1]) >= offset_y:
								filtered_y_positions.append(y)
		return filtered_y_positions  # 返回 y 坐标列表
		
		# # 在主图像上绘制匹配矩形框
		# matched_img = main_img.copy()
		# for pt in zip(*match_locations[::-1]):  # 使用[::-1] 交换坐标顺序
		#     top_left = pt
		#     bottom_right = (top_left[0] + w, top_left[1] + h)
		#     cv2.rectangle(matched_img, top_left, bottom_right, (0, 255, 0), 2)
		
		# # 显示结果
		# plt.figure(figsize=(10, 5))
		# plt.imshow(cv2.cvtColor(matched_img, cv2.COLOR_BGR2RGB))
		# plt.title('Multiple Matched Regions')
		# plt.axis('off')
		# plt.show()
		
		# return match_locations

def pil_to_cv2(pil_img):
		# 将 PIL 图像转换为 RGB 模式（如果不是 RGB 模式）
		pil_img = pil_img.convert("RGB")
		# 转换为 numpy 数组
		cv_img = np.array(pil_img)
		# 将颜色通道从 RGB 转为 BGR 以适配 OpenCV
		cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
		return cv_img
