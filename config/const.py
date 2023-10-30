TIMESLEEP = 1

# 模拟器url 链接
operate_url = '127.0.0.1'

# 模拟器端口
operate_port = 62001


# 模拟器点击方案 端口
operate_change_port = {5025, 5026, 5027, 5028, 5029, 5030, 5031, 5032, 5033, 5034, 5035, 5036, 5037, 5038, 5039, 5040}

# 模拟器截图方案 url
# 链接模拟器并映射端口
auto_mation = {
    'device_serial': operate_url + ':' + str(operate_port),
    'port': 53520
}
# 链接成功后访问该网址拿到截图
screenshot_url = 'http://' + operate_url + ':' + str(auto_mation['port']) + '/screenshot'

# web页面port
web_port = 18878
