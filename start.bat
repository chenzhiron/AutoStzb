@echo off


chcp 65001

.\toolkit\python.exe .\toolkit\get-pip.py

.\toolkit\python.exe .\toolkit\Scripts\pip.exe install -r .\requirements.txt

.\toolkit\python.exe .\start.py

.\toolkit\python.exe .\main.py

pause
