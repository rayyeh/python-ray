On Error Resume Next

Set objNetwork = CreateObject("Wscript.Network")
strLocalComputer = objNetwork.ComputerName

'If strComputer = "" Then
'    Wscript.Quit
'End If

' =====================================================================
' Insert your code here
' =====================================================================
Set strComputer = "UT09002311"
Wscript.Echo "Computer name:" &strComputer
Set objWMIService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")

Set colInstalledPrinters =  objWMIService.ExecQuery _
    ("Select * from Win32_Printer")

For Each objPrinter in colInstalledPrinters
    Wscript.Echo "Name: " & objPrinter.Name
    Wscript.Echo "Location: " & objPrinter.Location
    Wscript.Echo "Default: " & objPrinter.Default
Next

' =====================================================================
' End
' =====================================================================
