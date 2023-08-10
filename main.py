from device.main import connect_device
from ocr.main import ocr_txt_click, ocr_txt
from path.img import path


if __name__ == '__main__':
    d = connect_device()
    d.screenshot().save(path)
    # while 1:
    #     result = orc_txt_click(path,'开始游戏')
    #     if result:
    #         break
    # print(result)
    result = ocr_txt(path)
    print(result)