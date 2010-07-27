On Error Resume Next

Const ForReading = 1


       
    ' =====================================================================
    ' Insert your code here
    ' =====================================================================
strComputer = "UT09002311"
Set objComputer = GetObject("WinNT://" & strComputer & "")
Set objComputer.Filter = Array("group")
Wscript.Echo "Machine name:" &strComputer    
    
For Each objGroup In objComputer	    	 
    	For Each objUser in objGroup.Members
    		Wscript.Echo "======================================" 
    	        Wscript.Echo "Group name:" &objGroup.Name
        	Wscript.Echo "User name :" &objUser.Name
        	Wscript.Echo "ADs path:" &objUser.AdsPath
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
    
