import time
import numpy as np
from modules.devices.main import Devices
from modules.ocr.main import ocr_format_ranking, ocr_format_val, ocrnotdet
from modules.utils import export_excel


class Ranking():
    def __init__(self, d):
        self.d = d
        self.result = []
        self.top = 259
        self.offset_y = 905
        self.ordinal_offsety = 5

    def execute(self):
        while True:
            orid = self.d.screenshot()
            namespic = orid.crop([400, 257, 615, 905])
            names = ocr_format_ranking(np.array(namespic))
            print(names)
            if names == None:
                continue

            for k, v in enumerate(names):
                # names[2] = ocrnotdet()
                n = orid.crop([115,v[0] + 257 - self.ordinal_offsety,190,v[1] + 257 + self.ordinal_offsety])
                ordinal = ocr_format_val(np.array(n))
                names[k].append(ordinal)

            if names[-1][3] == '300':
                break

            r2_l = len(self.result)
            d_l = len(names)
            if len(self.result) >= d_l:
                t = 0
                for k_r, v_r in enumerate(names):
                    if self.result[-(d_l - k_r)][2] == v_r[2]:
                        t += 1
                print(r2_l, t)
                if t == d_l:
                    break

            self.offset_y = names[-1][1] + self.top
            for v in names:
                self.result.append(v)
            self.d.drag(960,self.offset_y, 960, self.top, 1.5)
            time.sleep(1)
        print(self.result)

        self.exportdata()

    def exportdata(self):
        a_r = []
        a_r.append(['排名', '姓名'])
        for k, v in enumerate(self.result):
            if v[3] == None:
                v[3] = k + 1
            a_r.append([v[3], v[2]])
        export_excel(a_r, '排行数据')

if __name__ == '__main__':
  d = Devices('127.0.0.1:16384')
  Ranking(d).execute()
