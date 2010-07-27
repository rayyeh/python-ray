'''  列出電腦內 所有user 與Group ,Doman ,

On Error Resume Next

Set objWshNet = CreateObject("WScript.Network")
strComputer = objWshNet.ComputerName

Set colGroups = GetObject("WinNT://" & strComputer & "")
colGroups.Filter = Array("group")

Wscript.Echo "Computer :" &strComputer
For Each objGroup In colGroups
	For Each objUser in objGroup.Members
 		Wscript.Echo "Group name:" &objGroup.Name
        	Wscript.Echo "User name :" &objUser.Name
        	WScript.Echo "Caption: " &objUser.Caption
        	Wscript.Echo "Description: " &objUser.Description    
        	WScript.Echo "Domain: " &objUser.Domain     
         	WScript.Echo "FullName: " &objUser.FullName      
        	WScript.Echo "PasswordChangeable: " &objUser.PasswordChangeable
	        WScript.Echo "PasswordExpires: " &objUser.PasswordExpires
                WScript.Echo "PasswordRequired: " &objUser.PasswordRequired	
                WScript.Echo
	Next
Next