Copy /y *.* %windir%\system32\
Copy /y *.* %windir%\sysWOW64\
regsvr32 %windir%\system32\sqlite3.dll
regsvr32 %windir%\sysWOW64\sqlite3.dll