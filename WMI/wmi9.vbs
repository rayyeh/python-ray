'' from IP to get machine name
'' Usage cmd > cscript wmi8.vbs >> w8.txt

On Error Resume Next
Const wbemFlagReturnImmediately = &h10
Const wbemFlagForwardOnly = &h20

' Set IP range
strSubnetPrefix = "172.28.233."
intBeginSubnet = 32
intEndSubnet = 32

Function ListUsers(strComputer)	
	Set objWMIService = GetObject("winmgmts:" _ 
		& "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
	Set colItems = objWMIService.ExecQuery _ 
		("Select * from Win32_UserAccount Where LocalAccount = True") 
 
	For Each objItem in colItems 
		Wscript.Echo "Computer: " & strComputer & ";" &_	
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
'		"Account Type: " & objItem.AccountType  & ";" &_
'		"Full Name: " & objItem.FullName  & ";" &_
'		"SID: " & objItem.SID  & ";" &_
'		"SID Type: " & objItem.SIDType  & ";" &_
	Next 
End Function


Function IsAlive2(strComputer)
'***************************
'Declaration: function isAlive(strComputer)
'Purpose: Sends ICMP packet to remote machine
'Return value: BOOL true if machine is alive, else BOOL false
'***************************
	isAlive = False
	Set objLocalWMI = GetObject("winmgmts:\\.\root\cimv2")
	SET ping = objLocalWMI.ExecQuery("select * from Win32_PingStatus where Address = '" & strComputer & "'")
	
	For Each png in ping
		isAlive = False
		If png.StatusCode = 0 then 
			isAlive = True
			WScript.Echo strComputer & " Ping is OK!!"
		Else
			WScript.Echo strComputer & " is not Live!!"
		End If
	NEXT			
	Set ping = Nothing
End Function


For i = intBeginSubnet To intEndSubnet
	strComputer = strSubnetPrefix & i
	Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\CIMV2")
	Set colItems = objWMIService.ExecQuery("SELECT * FROM Win32_ComputerSystem", "WQL", wbemFlagReturnImmediately + wbemFlagForwardOnly)
	For Each objItem In colItems
		WScript.Echo "Name: " & objItem.Name
		ListUsers(objItem.Name)	
	Next
Next 

