#https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=de
#https://www.google.com/intl/de/chrome/thank-you.html?standalone=1&statcb=0&installdataindex=empty&defaultbrowser=0#
#https://downloads.jam-software.de/treesize_free/TreeSizeFreeSetup.exe
#https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
#http://download.pdfforge.org/download/pdfcreator/PDFCreator-stable?download
#https://download.teamviewer.com/download/TeamViewer_Setup.exe
#https://downloads.malwarebytes.com/file/adwcleaner
#https://www.elby.ch/download/SetupVCD.exe
#http://www.audacityorg.de/download/audacity.exe
#https://github.com/Open-Shell/Open-Shell-Menu/releases
#https://keepass.info/download.html
#https://www.videolan.org/vlc/download-windows.html
#https://www.java.com/de/download/win10.jsp


import os
import urllib.request
from datetime import datetime
import webbrowser

#Websites where you can download the latest stable software
aUrls = [
    "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=de",
 "https://www.google.com/intl/de/chrome/thank-you.html?standalone=1&statcb=0&installdataindex=empty&defaultbrowser=0#",
  "https://downloads.jam-software.de/treesize_free/TreeSizeFreeSetup.exe",
  "https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html",
  "http://download.pdfforge.org/download/pdfcreator/PDFCreator-stable?download",
  "https://download.teamviewer.com/download/TeamViewer_Setup.exe",
  "https://downloads.malwarebytes.com/file/adwcleaner",
  "https://www.elby.ch/download/SetupVCD.exe",
  "http://www.audacityorg.de/download/audacity.exe"
  ]

#How to name the downloaded file, Backslash needed
aExe = ["\Firefox.exe", "\Chrome.exe", "\TreeSize.exe", "\Putty.exe", "\PDFCreator.exe", "\Teamviewer.exe", "\ADWCleaner.exe", "\VirtualCloneDrive.exe", "\Audacity.exe"]

#Websites where you only can download specific versions
urls = [
    "https://github.com/Open-Shell/Open-Shell-Menu/releases",
 "https://keepass.info/download.html",
  "https://www.videolan.org/vlc/download-windows.html",
  "https://www.java.com/de/download/win10.jsp"
  ]


dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")
os.makedirs(timestampStr)


#Loop for latest Software
for num, name in enumerate(aUrls, start=0):
    urllib.request.urlretrieve (name, timestampStr + aExe[num])

#Loop to open URLs
for x in urls:
    webbrowser.open(x)
