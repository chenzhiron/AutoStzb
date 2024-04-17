@echo off

chcp 65001

set "SCRIPT_PATH=%~dp0"
set "PATH=%PATH%;%SCRIPT_PATH%toolkit\Scripts;%SCRIPT_PATH%;"

set "MIRROR_URL=https://pypi.tuna.tsinghua.edu.cn/simple"

"%SCRIPT_PATH%\toolkit\python.exe" "%SCRIPT_PATH%\toolkit\get_pip.py" --index-url="%MIRROR_URL%"
"%SCRIPT_PATH%\toolkit\python.exe" "%SCRIPT_PATH%\toolkit\Scripts\pip.exe" install "%SCRIPT_PATH%\toolkit\future-0.18.3-py3-none-any.whl"
"%SCRIPT_PATH%\toolkit\python.exe" "%SCRIPT_PATH%\toolkit\Scripts\pip.exe" install --index-url="%MIRROR_URL%" -r "%SCRIPT_PATH%\requirements.txt"
"%SCRIPT_PATH%\toolkit\python.exe" "%SCRIPT_PATH%\start.py"

pause
