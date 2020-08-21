pause
REM @echo off
echo "\\\---Installer---///"
cd ..
pause
SET i=install
echo "---checking if files exists...---"
pause
IF EXIST 'files\' (
pause
	IF EXIST 'files\Data1' (
        	IF EXIST 'files\Data2' (
pause
			echo "---copy files...---"
        		xcopy /s "X:\files" C:\ 
pause
			echo "---Installation started...---"
			cd /d C:\Data1 && installSoftware.cmd & Win10.reg\HideFolderReg.cmd & BGInfo\importXML.cmd & BGInfo\bginfox64.cmd & echo "---Completed---" && pause && del "C:\Install.cmd"
  		) ELSE (
			echo "---ERROR - Directory \files\Data2 not found---" && pause
    		) ELSE (
			echo "---ERROR - Directory \files\Data1 not found---" && pause
    		) ELSE (
			echo "---ERROR - Directory \files\ not found---" && pause
)

