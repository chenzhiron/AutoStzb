# encoding:utf-8
import requests
from path.img import path
import base64
from PIL import Image

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id= &client_secret= '
host_ocr = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token='

access_token = ''
if __name__ == '__main__':
    # response = requests.get(host)
    # if response:
    #     access_token = response.json()['session_key']
    #     print(access_token)
    headers = {'content-type': 'application/x-www-form-urlencoded', 'Access': 'application/json'}
    img_data = base64.b64encode(Image.open(path).tobytes())
    params = {"image": img_data}
    img_text = requests.post(host_ocr + access_token, data=img_data, headers=headers)
    if img_text:
        print(img_text.json())
