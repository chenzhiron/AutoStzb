TIMESLEEP = 1

# 模拟器url 链接
operate_url = '127.0.0.1'

# 模拟器端口
operate_port = 62001


# 模拟器点击方案 端口
operate_change_port = {5041, 5042, 5043, 5044, 5045, 5046, 5047, 5048, 5049}

# 模拟器截图方案 url 链接模拟器并映射端口
auto_mation = {
    'device_serial': operate_url + ':' + str(operate_port),
    'port': 53520
}
# 链接成功后访问该网址拿到截图
screenshot_url = 'http://' + operate_url + ':' + str(auto_mation['port']) + '/screenshot'

# web页面port
web_port = 18878
