#!/usr/local/bin/python -u

import subprocess
import argparse
import os
import time

adb_command = ''
res = os.environ['PATH'].split(';')
adb_path = os.path.normpath('toolkit\\adb\\adb.exe')
for v in res:
    if adb_path in os.path.normpath(v):
        print(v,'result')
        adb_command = [os.path.normpath(v)]
        break
    else:
        adb_command = ['adb']

def run_adb(device_serial, args, pipe_output=True):
    args = adb_command + ['-s', device_serial] + args
    print('args', args)
    output = None
    if pipe_output:
        output = subprocess.PIPE

    process = subprocess.Popen([str(arg) for arg in args], stdout=output, encoding='utf-8')
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr


def locate_apk_path(simulator):
    return_code, output, _ = run_adb(simulator,["shell", "pm", "path", "ink.mol.droidcast_raw"])
    if return_code or output == "":
       return_code2 =  run_adb(simulator,['install', './toolkit/adb/DroidCast_raw-release-1.1.apk'])
       print(return_code2)
    time.sleep(1)
    return_code, output, _ = run_adb(simulator,["shell", "pm", "path", "ink.mol.droidcast_raw"])
    prefix = "package:"
    postfix = ".apk"
    begin_index = output.index(prefix, 0)
    end_index = output.rfind(postfix)

    return "CLASSPATH=" + output[begin_index + len(prefix):(end_index + len(postfix))].strip()



# def identify_device(simulator):
#     return_code, output, _ = run_adb(["devices"])
#     if return_code:
#         raise RuntimeError("Fail to find devices")
#     else:
#         print(output)
#         device_serial_no = args_in.device_serial
#         devices_info = str(output)
#         device_count = devices_info.count('device') - 1

#         if device_count < 1:
#             raise RuntimeError("Fail to find devices")

#         if device_count > 1 and not device_serial_no:
#             raise RuntimeError("Please specify the serial number of target device you want to use ('-s serial_number').")


def automate(simulator):
    try:
        print('start screenshot server')
        print(">>> adb connect %s" % simulator)
        
        return_code, _, _ = run_adb(simulator, ['connect', simulator])
        print(return_code, _, _)
        # identify_device(simulator)
        class_path = locate_apk_path(simulator)

        return_code, _, _ = run_adb(simulator, ["forward", "tcp:53516", "tcp:53516"])
        print(">>> adb forward tcp:53516", return_code)

        arguments = ["shell", class_path, "app_process", "/", "ink.mol.droidcast_raw.Main", "--port=53516"]
        run_adb(simulator, arguments, pipe_output=False)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    automate('127.0.0.1:62025')
