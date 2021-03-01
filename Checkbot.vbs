Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "PATH_TO_START.BAT" & Chr(34), 0
Set WshShell = Nothing