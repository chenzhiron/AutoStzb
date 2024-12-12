@echo off

chcp 65001

:: 设置 Git 可执行文件路径和项目相关参数
set GIT_PATH=.\toolkit\gitbash\cmd\git.exe
set REPO_URL=https://github.com/chenzhiron/AutoStzb.git
set LOCAL_DIR=%CD%

"%GIT_PATH%" remote add origin "%REPO_URL%"
"%GIT_PATH%" pull --depth=1 origin main

pause
