## auto_stzb
* 地图土地识别 × (目前依赖于标记)

## 开始
    模拟器支持：目前仅支持 夜神模拟器，分辨率要求1280*720,夜神模拟器默认开启adb链接，其他模拟器自行测试
    仅支持一台模拟器，多开需要自行修改端口（不同模拟器端口不同，自行查阅官方文档），修改文件 start.py 和 config/const.py，
    双击 start.bat
    顺利的话 能看到窗口最后出现
    Use http://192.168.1.25:18878/ to access the application
    其中 192.168.1.25 是本地ip，18878 是端口
    打开浏览器访问上述ip


## electron
    目前基于electron 启动后无法解决内存泄露

## 模拟器要求
* 分辨率 1280* 720
* 模拟器版本 安卓10以下 
* 后续补充........


## 安装依赖包出现
    import paddle
    ModuleNotFoundError: No module named 'paddle'

    执行
    python -m pip install paddlepaddle==2.5.1 -i https://pypi.tuna.tsinghua.edu.cn/simple

## pyminitouch 使用问题
1. 端口占用： 修改 config/const.py 配置文件中的 operate_change_port 
2. 后续补充.....