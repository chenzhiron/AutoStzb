
import numpy as np
from ..ocr.main import ocr_format_val
from ..utils import find_multiple_templates, pil_to_cv2, export_excel
from ..devices.main import Devices
from .tasks_utils import BaseTypeImg, battle_time

class FlipLists(BaseTypeImg):
	def __init__(self, d, end_time):
		BaseTypeImg.__init__(self)
		self.d = d
		self.custom_end_time = end_time
		self.result = []
		self.screenshot = None
		self.filtered_lines = []
		self.end_time = 0
		self.offset_y = 965

	def role_lists(self):
		resarr = []
		for v in self.filtered_lines:
			current = [0] * 3
			state = ocr_format_val(np.array(self.screenshot.crop([815, v + 270 + 195, 1066,  v + 195 + 300])))
			print('land state: ',state)
			if state == '成功占领':
				m_name = ocr_format_val(np.array(self.screenshot.crop([563, v + 195, 800, v + 195 + 100])))
				current[0] = m_name
				print('prent name: ',m_name)
				# 添加土地标志判断是否是土地还是要塞
				island = ocr_format_val(np.array(self.screenshot.crop([810, v + 195, 1060, v + 195 + 100])))
				if island is not None and '土地' in island:
					current[1] = 1
				else:
					current[2] = 1
						# 战报时间
				self.end_time = battle_time(self.screenshot, v)
			else:
				continue
			resarr.append(current)
		return resarr
	
	def loopinfo(self):
		self.offset_y = 0
		main_img = pil_to_cv2(self.screenshot.crop([40, 185, 122, 740]))
		lines = find_multiple_templates(main_img, self.attack_template_img)
		print('lines:', lines)
		r_lines = []
		for v in lines:
			if v > 620:
				self.offset_y = int(v)
				break
			else:
				r_lines.append(v)

		self.offset_y = int(lines[-1] + 360 + 195)

		self.filtered_lines = r_lines	
		print('filtered_lines: ', self.filtered_lines)
		if len(self.filtered_lines) > 0:
			resarr = self.role_lists()
			return resarr
		else:
			return []
	
	def execute(self):
		while True:
			self.screenshot = self.d.screenshot()
			r2 = self.loopinfo()
			print('r2 info_end_time: ', r2, self.end_time)
			if self.end_time is not None and \
					self.end_time != 0 and self.custom_end_time > self.end_time:
				break

			for v in r2:
				self.result.append(v)
			print('self.offset_y', self.offset_y)
			self.d.swipe(950, self.offset_y , 950, 225)
			
		data_map = {}
		for v in self.result:
			if data_map.get(v[0]):
				c = data_map[v[0]]
				c[1] += v[1]
				c[2] += v[2]
			else:
				data_map[v[0]] = v

		print(data_map)
		a_r = []
		a_r.append(['姓名', '翻地', '拆除'])
		for key, value in data_map.items():
			a_r.append(value)

		export_excel(a_r, '翻地拆除数据')

if __name__ == '__main__':
	d = Devices('127.0.0.1:16384')
	flip = FlipLists(d,1731232800)
	flip.execte()
