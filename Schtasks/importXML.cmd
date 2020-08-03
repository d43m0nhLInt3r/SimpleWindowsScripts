set /P i=Enter a new Task Name: 
set /P p=Enter the full path to the xml file: 
schtasks.exe /create /tn %i% /XML %p%
