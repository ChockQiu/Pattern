@echo off
pyinstaller --distpath .\build --log-level WARN -Fy pattern.py -i favicon.ico
echo Build Finish.