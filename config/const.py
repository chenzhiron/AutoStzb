# 模拟器url 链接
operate_url = '127.0.0.1'

# 模拟器端口
operate_port = 62001


# 模拟器点击方案 端口
operate_change_port = 60000

# 模拟器截图方案 url 链接模拟器并映射端口
automation_serial = operate_url + ':' + str(operate_port)
automation_port = 53520


# 链接成功后访问该网址拿到截图
screenshot_url = 'http://127.0.0.1:' + str(automation_port) + '/screenshot'

# web页面port
web_port = 18878
