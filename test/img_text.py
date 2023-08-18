from cnocr import CnOcr

ocr = CnOcr(rec_model_name='ch_PP-OCRv3')
if __name__ == '__main__':
    from path.img import path
    result = ocr.ocr(path)
    print(result)

# 从左往右点，如果能进入下一个页面，则正式执行，如果没有，则放弃，按照坐标来