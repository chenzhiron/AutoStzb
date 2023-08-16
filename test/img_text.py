from path.img import path
from ocr.main import ocr_txt

if __name__ == '__main__':
    res = ocr_txt(path)
    print(res)