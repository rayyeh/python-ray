' ====================================
' == List computer user id  
' ========================================

Const wbemFlagReturnImmediately = &h10
Const wbemFlagForwardOnly = &h20

arrComputers = Array("UT09002311")
For Each strComputer In arrComputers
   WScript.Echo
   WScript.Echo "=========================================="
   WScript.Echo "Computer: " & strComputer
   WScript.Echo "=========================================="

   Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\CIMV2")
   Set colItems = objWMIService.ExecQuery("SELECT * FROM Win32_UserAccount", "WQL", _
                                          wbemFlagReturnImmediately + wbemFlagForwardOnly)

   For Each objItem In colItems
      WScript.Echo "AccountType: " & objItem.AccountType & ";" &_
      "Caption: " & objItem.Caption & ";" &_
      "Description: " & objItem.Description & ";" &_
      "Disabled: " & objItem.Disabled & ";" &_
      "Domain: " & objItem.Domain  & ";" &_
      "LocalAccount: " & objItem.LocalAccount & ";" &_
      "Lockout: " & objItem.Lockout & ";" &_
      "Name: " & objItem.Name & ";" &_
      "PasswordChangeable: " & objItem.PasswordChangeable & ";" &_
      "PasswordExpires: " & objItem.PasswordExpires & ";" &_
      "PasswordRequired: " & objItem.PasswordRequired & ";" &_
      "Status: " & objItem.Status

'      WScript.Echo "SID: " & objItem.SID
'      WScript.Echo "SIDType: " & objItem.SIDType
'      WScript.Echo "FullName: " & objItem.FullName 
'      WScript.Echo "InstallDate: " & WMIDateStringToDate(objItem.InstallDate)
'      WScript.Echo
   Next
Next


Function WMIDateStringToDate(dtmDate)
WScript.Echo dtm: 
	WMIDateStringToDate = CDate(Mid(dtmDate, 5, 2) & "/" & _
	Mid(dtmDate, 7, 2) & "/" & Left(dtmDate, 4) _
	& " " & Mid (dtmDate, 9, 2) & ":" & Mid(dtmDate, 11, 2) & ":" & Mid(dtmDate,13, 2))
End Function