import numpy as np

from modules.devices.main import Devices
from modules.ocr.main import ocr_format_val
from modules.utils import export_excel, find_multiple_templates, pil_to_cv2
from modules.taskfn.tasks_utils import BaseTypeImg, battle_time


class SiegeBattles(BaseTypeImg):
	def __init__(self, d, end_time):
		BaseTypeImg.__init__(self)
		self.d = d
		self.custom_end_time = end_time
		self.end_time = end_time
		self.result = []
		self.offset_y = 965
		self.screenshot = None
		self.filtered_lines = []

	def siege_battles(self):
		resarr = []
		for v in self.filtered_lines:
			current = []
			# 名字
			r = ocr_format_val(np.array(self.screenshot.crop([568,v + 195, 820, v + 195 + 70]))) or \
				ocr_format_val(np.array(self.screenshot.crop([568,v + 195 - 70,820, v + 195])))
			current.append(r)

			print('name:',r)

			# 战报时间
			times = battle_time(self.screenshot, v)
			self.end_time = times
			print('end_time:', times)
			current.append(times)
			# 单次战斗数量
			battles = ocr_format_val(np.array(self.screenshot.crop([1770, v + 195 + 130, 1830,  v + 195 + 200]))) or \
				ocr_format_val(np.array(self.screenshot.crop([1770, v + 195 + 70, 1830,  v + 195 + 130])))
			try:
				if battles == None:
					battles = 1
				else:
					battles = int(battles) + 1
			except ValueError:
				battles = 1
			current.append(battles)

			print('battles:',battles)
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
			resarr = self.siege_battles()
			return resarr
		else:
			return []
		
	def execute(self):
		while True:
			self.screenshot = self.d.screenshot()
			r2 = self.loopinfo()
			print('r2:', r2)
			if self.end_time is not None and \
					self.end_time != 0 and self.custom_end_time > int(self.end_time):
				break
			
			r2_l = len(r2)
			if len(self.result) >= r2_l:
				t = 0
				for k_r,v_r in enumerate(r2):
					if self.result[-(k_r+1)][0] == v_r[0] and \
						self.result[-(k_r+1)][1] == v_r[1] and \
						self.result[-(k_r+1)][2] == v_r[2]:
						t += 1
				if t == r2_l:
					break
			for v in r2:
					self.result.append(v)
			print('self.offset_y', self.offset_y)
			self.d.swipe(950, self.offset_y , 950, 225)
		print(self.result)

		data_map = {}
		for v in self.result:
			if data_map.get(v[0]):
				c = data_map[v[0]]
				c[1] = v[1]
				c[2] += v[2]
			else:
				data_map[v[0]] = v

		print(data_map)
		a_r = []
		a_r.append(['姓名', '最后一次行动的时间戳(可忽略)','出击次数'])
		for key, value in data_map.items():
			a_r.append(value,value)

		export_excel(a_r, '攻城数据')

if __name__ == '__main__':
	d = Devices('127.0.0.1:16384')
	SiegeBattles(d, 1731232800).execute()
