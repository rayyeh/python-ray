'' List Local User Accounts Using WMI

On Error Resume Next 
 
arrComputers = Array("UT09002311","UT09500411")
For Each strComputer In arrComputers
	
	Set objWMIService = GetObject("winmgmts:" _ 
		& "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
	Set colItems = objWMIService.ExecQuery _ 
		("Select * from Win32_UserAccount Where LocalAccount = True") 
 
	For Each objItem in colItems 
		Wscript.Echo "Computer: " & strComputer & ";" &_	
		"Account Type: " & objItem.AccountType  & ";" &_
		"Caption: " & objItem.Caption  & ";" &_
		"Description: " & objItem.Description  & ";" &_
		"Disabled: " & objItem.Disabled  & ";" &_
		"Domain: " & objItem.Domain  & ";" &_
		"Local Account: " & objItem.LocalAccount  & ";" &_
		"Lockout: " & objItem.Lockout  & ";" &_
		"Name: " & objItem.Name  & ";" &_
		"Password Changeable: " & objItem.PasswordChangeable  & ";" &_
		"Password Expires: " & objItem.PasswordExpires  & ";" &_
		"Password Required: " & objItem.PasswordRequired  & ";" &_
		"Status: " & objItem.Status  
'		"Full Name: " & objItem.FullName  & ";" &_
'		"SID: " & objItem.SID  & ";" &_
'		"SID Type: " & objItem.SIDType  & ";" &_
	Next 
Next