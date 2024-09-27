@echo off
rem Run the command and capture the output
set OUTPUT=
for /f "tokens=*" %%i in ('"C:\Program Files\Docker\Docker\resources\bin\docker" run -d --env-file .env -p 5000:5000 flask_app') do set OUTPUT=%%i

rem Write the captured output to a file
echo docker kill %OUTPUT% > docker_kill.bat

pause