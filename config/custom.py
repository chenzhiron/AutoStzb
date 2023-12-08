class CustomConfig:
    def __init__(self, time_sleep):
        self.time_sleep = time_sleep

    #     self.operate_url = '127.0.0.1'
    #     # 模拟器端口
    #     self.operate_port = 62001
    # 
    #     # 模拟器点击方案 端口
    #     self.operate_change_port = 60000
    # 
    #     # 模拟器截图方案 url 链接模拟器并映射端口
    #     self.automation_serial = self.operate_url + ':' + str(self.operate_port)
    #     self.automation_port = 53520
    # 
    #     # 链接成功后访问该网址拿到截图
    #     self.screenshot_url = 'http://127.0.0.1:' + str(self.automation_port) + '/screenshot'
    # 
    #     # web页面port
    #     self.web_port = 18878
    # 
    # def changeUrl(self, url):
    #     self.operate_url = url
    #     from device.AutoMation import init
    #     init(self.operate_url)

    def changeTimesleep(self, time_sleep):
        try:
            if float(time_sleep) <= 0:
                time_sleep = 1
            self.time_sleep = float(time_sleep)
        except:
            self.time_sleep = float(time_sleep)
        from device.AutoMation import change_automation_timeSleep
        change_automation_timeSleep(self.time_sleep)
        print(self.time_sleep)

    def getTimesleep(self):
        return self.time_sleep


customConfig = CustomConfig(1.0)
