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
      WScript.Echo "AccountType: " & objItem.AccountType
      WScript.Echo "Caption: " & objItem.Caption
      WScript.Echo "Description: " & objItem.Description
      WScript.Echo "Disabled: " & objItem.Disabled
      WScript.Echo "Domain: " & objItem.Domain
      WScript.Echo "FullName: " & objItem.FullName
'     WScript.Echo "InstallDate: " & WMIDateStringToDate(objItem.InstallDate)
      WScript.Echo "LocalAccount: " & objItem.LocalAccount
      WScript.Echo "Lockout: " & objItem.Lockout
      WScript.Echo "Name: " & objItem.Name
      WScript.Echo "PasswordChangeable: " & objItem.PasswordChangeable
      WScript.Echo "PasswordExpires: " & objItem.PasswordExpires
      WScript.Echo "PasswordRequired: " & objItem.PasswordRequired
      WScript.Echo "SID: " & objItem.SID
      WScript.Echo "SIDType: " & objItem.SIDType
      WScript.Echo "Status: " & objItem.Status
      WScript.Echo
   Next
Next


Function WMIDateStringToDate(dtmDate)
WScript.Echo dtm: 
	WMIDateStringToDate = CDate(Mid(dtmDate, 5, 2) & "/" & _
	Mid(dtmDate, 7, 2) & "/" & Left(dtmDate, 4) _
	& " " & Mid (dtmDate, 9, 2) & ":" & Mid(dtmDate, 11, 2) & ":" & Mid(dtmDate,13, 2))
End Function