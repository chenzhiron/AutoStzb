import time
import numpy as np
from modules.ocr.main import ocr_format_val
from modules.utils import reg_card
from modules.devices.main import Devices
from modules.taskfn.tasks_utils import battle_time

def role_lists(img, filtered_lines):
		state = False
		resarr = []
		end_time = 0
		for v in filtered_lines:
			current = []

			isnpc = ocr_format_val(np.array(img.crop([1084,  v[1] + 195, 1152, v[1] + 195 + 100])))
			if isnpc == '守军':
				continue

			# 名字
			r = ocr_format_val(np.array(img.crop([1084, v[1] + 195, 1308, v[1] + 195 + 100]))) or \
				ocr_format_val(np.array(img.crop([1084, v[1] + 195 - 70,1308, v[1] + 195])))
			current.append(r)

			# 武将名字
			offset_top = 195 + 139 - 19
			offset_bottom = 195 + 261
			
			leftv = ocr_format_val(np.array(img.crop([1084, v[1] + offset_top, 1127, v[1] + offset_bottom]))) or \
				ocr_format_val(np.array(img.crop([1084, v[1] + offset_top - 70 ,1127, v[1] + 261+139])))
			current.append(leftv)

			centerv = ocr_format_val(np.array(img.crop([1319, v[1] + offset_top, 1365, v[1] + offset_bottom]))) or \
				ocr_format_val(np.array(img.crop([1319, v[1] + offset_top - 70 ,1365, v[1] + 261+139])))
			current.append(centerv)

			rightv = ocr_format_val(np.array(img.crop([1547, v[1] + offset_top, 1594, v[1] + offset_bottom]))) or \
				  ocr_format_val(np.array(img.crop([1547, v[1] + offset_top - 70 ,1594, v[1] + 261+139])))
			current.append(rightv)
			
			end_time = battle_time(img, v[1])
			print('current', current)

			resarr.append(current)
		return (state,resarr, end_time)

def loopinfo2(d,img):
		r, filtered_lines = reg_card(img)
		if r != 0:
			d.swipe(950, 218 + int(r), 950, 218)
			return (True,[])
		state, resarr, end_time = role_lists(img, filtered_lines)
		return (state,resarr, end_time)

def siege_main2(d, end_time):
	rr = []
	while True:
		swipe_state, r2, battle_end_time = loopinfo2(d, d.screenshot())
		if swipe_state:
			time.sleep(0.5)
			continue

		if end_time > battle_end_time and battle_end_time != 0:
			break
		for v in r2:
			rr.append(v)
		d.swipe(950,965,950, 225)
		time.sleep(0.5)


if __name__ == '__main__':
	d = Devices('127.0.0.1:16384')
	siege_main2(d)
