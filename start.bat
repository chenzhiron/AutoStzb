@echo off

chcp 65001

set SCRIPT_PATH=%~dp0
set PATH=%PATH%;%SCRIPT_PATH%toolkit\Scripts

%SCRIPT_PATH%toolkit\python.exe %SCRIPT_PATH%toolkit\get_pip.py
%SCRIPT_PATH%\toolkit\Scripts\pip.exe install %SCRIPT_PATH%\toolkit\future-0.18.3-py3-none-any.whl

%SCRIPT_PATH%toolkit\python.exe %SCRIPT_PATH%toolkit\Scripts\pip.exe install --no-warn-script-location -r %SCRIPT_PATH%requirements.txt

%SCRIPT_PATH%toolkit\python.exe %SCRIPT_PATH%main.py

pause