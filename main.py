from device.main import connect_device
from ocr.main import orc_txt, orc_test
from path.img import path


if __name__ == '__main__':
    d = connect_device()
    d.screenshot().save(path)
    # result = orc_txt(path, '开始游戏')
    # while 1:
    #     result = orc_txt(path,'开始游戏')
    #     if result:
    #         break
    # print(result)
    result = orc_test(path)
    print(result)