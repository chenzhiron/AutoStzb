import os
import subprocess

current_dir = os.getcwd()
exe_path = os.path.join(current_dir, 'web', 'web_stzb', 'web_stzb.exe')

print(exe_path)


def run_electron(url, process_id):
    try:
        subprocess.Popen(f'"{exe_path}" -p{url} -s{process_id}',
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        # os.system(f'"{exe_path}" -p{url} -s{process_id}')
    except Exception as e:
        print('run electron error: ', e)


if __name__ == '__main__':
    run_electron('http://127.0.0.1:18878', 7224)