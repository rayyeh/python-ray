'' from IP to get machine name
'' Usage cmd > cscript wmi8.vbs >> w8.txt

'On Error Resume Next
Const wbemFlagReturnImmediately = &h10
Const wbemFlagForwardOnly = &h20

'出現輸入目標電腦IP位?的訊息視窗
strSubnetPrefix  =InputBox("請輸入起始IP前三段,如 192.168.7. ,最後一碼要包含.", "訊息")
intBeginSubnet =InputBox("請輸入起始IP","訊息")
intEndSubnet =InputBox("請輸入結束IP位址","訊息")

'在D磁碟機建立GroupMember.txt文字檔
FilePath =InputBox("請輸入產生的檔名與路徑","訊息")
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

