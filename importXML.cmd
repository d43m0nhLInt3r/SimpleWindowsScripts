::Version 2.2.26082020
@echo off
echo "\\\---BGInfo Installer---///"
if "%i%"=="install" ( 
echo "---copy files---"
xcopy /s BGInfo\ "C:\Program Files (x86)\BGInfo\"
schtasks.exe /create /tn BGInfo /XML "C:\Program Files (x86)\BGInfo\bginfo.xml"
) ELSE (
echo "---Manually Installation selected---"
schtasks.exe /create /tn BGinfo /XML C:\path\to\bginfo.xml
)
pause
