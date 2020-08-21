::Version 2.1.19082020
@echo off
echo "\\\---BGInfo Installer---///"
if "%i%"=="install" ( 
echo "---Install Option selected---"
echo "---copy Files---"
xcopy /s BGInfo\ "C:\Program Files (x86)\BGInfo\"
echo "---Entry added...---"
schtasks.exe /create /tn BGInfo /XML "C:\Program Files (x86)\BGInfo\bginfo.xml"
) ELSE (
echo "---Manuell Installation selected---"
IF EXIST "bginfo.xml" (
echo "---Entry added...---"
schtasks.exe /create /tn BGInfo /XML bginfo.xml
) ELSE ( 
echo "---Error - File not found---"
)
)
pause
