'' from IP to get machine name
'' Usage cmd > cscript wmi8.vbs >> w8.txt

'On Error Resume Next
Const wbemFlagReturnImmediately = &h10
Const wbemFlagForwardOnly = &h20

'�X�{��J�ؼйq��IP��?���T������
strSubnetPrefix  =InputBox("�п�J�_�lIP�e�T�q,�p 192.168.7. ,�̫�@�X�n�]�t.", "�T��")
intBeginSubnet =InputBox("�п�J�_�lIP","�T��")
intEndSubnet =InputBox("�п�J����IP��}","�T��")

'�bD�Ϻо��إ�GroupMember.txt��r��
FilePath =InputBox("�п�J���ͪ��ɦW�P���|","�T��")
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objTextFile = objFSO.CreateTextFile( FilePath , True)

Function ListUsers(strComputer)	
	Set objWMIService = GetObject("winmgmts:" _ 
		& "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
	Set colItems = objWMIService.ExecQuery _ 
		("Select * from Win32_UserAccount Where LocalAccount = True") 
 
	For Each objItem in colItems 
		objTextFile.writeline "Computer: " & strComputer & ";" &_	
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

For i = intBeginSubnet To intEndSubnet
	strComputer = strSubnetPrefix & i
	set objIPStatus=GetObject("winmgmts:").ExecQuery("Select * From WIN32_PingStatus where address='" & strComputer & "'" )
	For Each objItem in objIPStatus
		If objItem.statuscode=0 Then
		Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\CIMV2")
		Set colItems = objWMIService.ExecQuery("SELECT * FROM Win32_ComputerSystem", "WQL", wbemFlagReturnImmediately + wbemFlagForwardOnly)
		For Each objName In colItems
			WScript.Echo "Name: " & objName.Name
			ListUsers(objName.Name)	
		Next
		End If
	Next
Next 

