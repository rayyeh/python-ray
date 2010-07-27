''' List Administrator information

On Error Resume Next

strComputer = "UT09002311"
strTestString = "/" & strComputer & "/"

Set colGroups = GetObject("WinNT://" & strComputer & "/Administrators")

For Each objUser In colGroups.Members
    If InStr(objUser.AdsPath, strTestString) Then
        Wscript.Echo "Local user: " & objUser.Name
        Wscript.Echo "ADs path:" &objUser.AdsPath
    Else
        Wscript.Echo "Domain user: " & objUser.Name
    End If
Next
