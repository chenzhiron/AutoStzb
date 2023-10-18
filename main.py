import sys

import io
import os

from device.main_device import connect_device

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)

# from dispatcher.main import start_scheduler


if __name__ == '__main__':
    device = connect_device()





    # # 征兵模块 start
    # # 点击势力
    # ocr_txt = ocr_txt_verify((295, 575, 340, 650))
    # result = crop_string(ocr_txt, 2)[0]
    # if result == '势力':
    #     device.click(335, 600)
    # time.sleep(1)
    # # 点击要征兵的队伍
    # ocr_txt = ocr_txt_verify((100, 0, 200, 60))
    # result = crop_string(ocr_txt, 2)[0]
    # print(result)
    # if result == '势力':
    #     # 需要计算各队伍坐标
    #     device.click(100, 260)
    # time.sleep(1)
    # # 点击进入征兵页面
    # ocr_txt = ocr_txt_verify((575, 470, 705, 520))
    # result = crop_string(ocr_txt, 2)[0]
    # if result == '证兵':
    #     device.click(600, 500)
    # # elif result == '证兵中':
    # #     print('证兵中')
    # # 拖动征兵进度条
    # time.sleep(1)
    # ocr_txt = ocr_txt_verify((1000, 630, 1130, 670))
    # result = crop_string(ocr_txt, 4)[0]
    # print(result)
    # if result == '确认证兵':
    #     device.swipe(410, 435, 850, 435)
    #     device.swipe(410, 545, 850, 435)
    #     device.swipe(410, 650, 850, 435)
    # time.sleep(1)
    # # 计算征兵时间
    # ocr_txt = ocr_txt_verify((760, 385, 848, 635))
    # result = calculate_max_timestamp(ocr_txt)
    # print(result)
    # # 点击确认征兵
    # device.click(1050, 650)
    # time.sleep(1)
    # # 再次确认
    # device.click(780, 470)
    # time.sleep(1)
    # device.click(1130, 80)
    # time.sleep(1)
    # device.click(1150, 40)
    # # 征兵模块 end

    # 标记地图模块 start
    # ocr_txt = ocr_txt_verify((965, 100, 1060, 140))
    # # 如果没有点击则点击
    # if ocr_txt == None:
    #     device.click(1220, 85)
    # time.sleep(1)
    # # 再次点击标记
    # device.click(1010, 120)
    # time.sleep(1)
    # # 点击土地
    # device.click(1050,185)
    # time.sleep(2)
    # # 跳到土地选择
    # img_sources = device.screenshot().crop((820,250,1150,510))
    # result = ocr_default(np.array(img_sources))
    # # 选择扫荡
    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         if line[1][0] == '扫荡':
    #             first_list = line[0]
    #             center_point = [sum(coord) / len(coord) for coord in zip(*first_list)]
    #             device.click(820+center_point[0], 250+center_point[1])
    #             print(line)
    #             break
    # # ocr_txt = ocr_txt_verify((820,250,1150,510))
    # print(result)
    # time.sleep(1)
    # # 选择出征队伍，需要优化
    # device.click(555, 580)
    # time.sleep(1)
    #
    # # 预备优化
    # # ocr_txt = ocr_txt_verify((1082,640,1150,680))
    # # result = crop_string(ocr_txt, 2)[0]
    # # if result == None:
    # #     device.click(1082, 640)
    #
    # ocr_txt = ocr_txt_verify((615,520,710,555))
    # result = calculate_max_timestamp(ocr_txt)
    # time.sleep(1)
    # ocr_txt = ocr_txt_verify((1082,640,1150,680))
    # result = crop_string(ocr_txt, 2)[0]
    # print(result)
    # time.sleep(1)
    # device.click(1082, 660)
    # # 土地基于 标记模块 选择扫荡 end

    # 战报查看
    # ocr_txt = ocr_txt_verify((295, 575, 340, 650))
    # result = crop_string(ocr_txt, 2)[0]
    # if result == '势力':
    #     device.click(110,540)
    #     time.sleep(1)
    #     ocr_txt = ocr_txt_verify((195, 0, 300, 65))
    #     result = crop_string(ocr_txt, 2)[0]
    #     print(result)
    #     if result == '战报':
    #         device.click(600,270)
    #         time.sleep(1)
    #         ocr_txt = ocr_txt_verify((100, 0, 300, 65))
    #         result = crop_string(ocr_txt, 4)[0]
    #         if result == '战报详情':
    #             # 胜利/失败/平局
    #             ocr_txt = ocr_txt_verify((580, 90, 690, 150))
    #             result = crop_string(ocr_txt, 2)[0]
    #             print(result)
    #             #我方兵力
    #             ocr_txt = ocr_txt_verify((0, 100, 160, 145))[0]
    #             print(ocr_txt)
    #             #敌方兵力
    #             ocr_txt = ocr_txt_verify((1120,100, 1280, 145))[0]
    #             print(ocr_txt)
    #             time.sleep(1)
    #             device.click(1150, 40)
    #             time.sleep(1)
    #             device.click(1150, 40)
    #         print(result)
