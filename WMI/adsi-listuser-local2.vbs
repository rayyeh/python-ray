On Error Resume Next

Const ForReading = 1


strComputer = "UT09002311"
strTestString = "/" & strComputer & "/"

Set colGroups = GetObject("WinNT://" & strComputer & "/Administrators")

For Each objUser In colGroups.Members
    If InStr(objUser.AdsPath, strTestString) Then
        Wscript.Echo "Local user: " & objUser.Name
    Else
        Wscript.Echo "Domain user: " & objUser.Name
    End If
Next

       
    ' =====================================================================
    ' Insert your code here
    ' =====================================================================
strComputer = "."
Set objNetwork = CreateObject("WScript.Network")
Set objNewtork.Filter= Array("group")
Wscript.Echo "Machine name:" &objNetwork.ComputerName    
    
For Each objGroup In objNewtork.group	    	
        Wscript.Echo "Group name:" &objGroup.Name 
    	For Each objUser in objGroup.Members
    		Wscript.Echo "======================================" 
    	        Wscript.Echo "Group name:" &objGroup.Name
        	Wscript.Echo "User name :" &objUser.Name
        	WScript.Echo "Caption: " & objUser.Caption
        	Wscript.Echo "Description: " &objUser.Description    
        	WScript.Echo "Domain: " & objUser.Domain     
        	WScript.Echo "FullName: " & objUser.FullName      
        	WScript.Echo "PasswordChangeable: " & objUser.PasswordChangeable
                WScript.Echo "PasswordExpires: " & objUser.PasswordExpires
                WScript.Echo "PasswordRequired: " & objUser.PasswordRequired	         
    	Next
Next
    ' =====================================================================
    ' End
    ' =====================================================================
    
