import subprocess

adb_path = '.\\device\\adb\\adb.exe'
devices_serial = '127.0.0.1:62001'
framework = 'x86'
minitouch_path = r'.\\device\\libs\\{}\\minitouch'.format(framework)
automation_path = r'.\\device\\DroidCast-debug-1.1.1.apk'

def run_adb_command(command):
    try:
        result = subprocess.check_output(
            f"{adb_path} -s{devices_serial} {command}", shell=True, stderr=subprocess.STDOUT
        )
        return result.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print(e)
        return e.output.decode('utf-8').strip()


if __name__ == '__main__':
    # 示例：执行 adb 命令获取设备列表
    devices_serial = run_adb_command('devices').split()[-2]
    print(devices_serial)
    framework = run_adb_command('shell getprop ro.product.cpu.abi')
    print(framework)
    execute_minitouch = run_adb_command('push ' + minitouch_path + ' /data/local/tmp/')
    print(execute_minitouch)
    # 执行 cd /data/local/tmp 命令
    run_adb_command("shell cd /data/local/tmp/")
    # 执行 chmod 777 minitouch 命令
    run_adb_command("shell chmod 777 /data/local/tmp/minitouch")
    run_adb_command('install' + ' ' + automation_path)