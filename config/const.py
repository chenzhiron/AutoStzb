TIMESLEEP = 1

# 模拟器url 链接
operate_url = '127.0.0.1'

# 模拟器端口
operate_port = 62001


# 模拟器点击方案 端口
operate_change_port = {16001, 16002, 16003, 16004, 16005, 16006, 5009, 5008, 5007, 5006, 5005, 5004, 5003, 5002, 5001,
                       5000, 5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017, 5018, 5019, 5020, 5021, 5022, 5023, 5024}

# 模拟器截图方案 url
# 链接模拟器并映射端口
auto_mation = {
    'device_serial': operate_url + ':' + str(operate_port),
    'port': 53520
}
# 链接成功后访问该网址拿到截图
screenshot_url = 'http://' + operate_url + ':' + str(auto_mation['port']) + '/screenshot'

# web操作url
web_host = 'http://127.0.0.1'
web_port = 18878
