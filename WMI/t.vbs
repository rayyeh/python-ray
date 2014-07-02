On Error Resume Next

strComputer = "192.168.7.44"

Function IsAlive2(strComputer)
'***************************
'Declaration: function isAlive(strComputer)
'Purpose: Sends ICMP packet to remote machine
'Return value: BOOL true if machine is alive, else BOOL false
'***************************
	WScript.Echo  "It is isAlive Function" & strComputer
	isAlive = False
	Set objLocalWMI = GetObject("winmgmts:\\.\root\cimv2")
	SET ping = objLocalWMI.ExecQuery("select * from Win32_PingStatus where Address = '" & strComputer & "'")
	
	For Each png in ping
		WScript.Echo  "ping xx" & strComputer
		isAlive = False
		If png.StatusCode = 0 then 
			isAlive = True
			WScript.Echo "IP Addr is OK"
		Else
			WScript.Echo "IP Addr can not ping "
		End If
	NEXT			
	Set ping = Nothing
End Function

If IsAlive2(strComputer).isAlive  = True  Then
	WScript.Echo "Call IsAlive2 successfull!"
End If

Function IsAlive(strTarget)
	' Create a object reference to WMI on the local system
	Set objLocalWMI = GetObject("winmgmts:\\.\root\cimv2")
	
	' The neat little WMI ping statement
	Set colPingStatus = objLocalWMI.ExecQuery ("Select * from Win32_PingStatus Where Address = '" & strTarget & "'")	
	
	' The command above returns a collection, even tho we only have a single object we care about, we need to get refernces
	' to the object, and not the collection to do stuff

	For Each objPingStatus in colPingStatus
		' If the ping rturned 0 Then it's successful and we contine to check
		If objPingStatus.StatusCode = 0 Then
			' If the Constant value for PING_ONLY is set to TRUE, then it will skip running the WMI Check
			' This is a little less accurate in my experience, but can speed up queries to lots of systems
			' if the target list is valid (and just some systems may be powered off.)
			If NOT PING_ONLY Then
				' We need to turn off the VBScript behavior of stopping when it encounters an error
				' This is called Error Trapping, VBScript will ignore errors and continue onto the next line
				On Error Resume Next
				' We now just try to create a refernce to the remote systems WMI, if it's not responding or
				' we don't have priviledges on the remote system, then VBScript will throw an error, but continue on
				' since we stated On Error Resume Next
				Set objWMIService = GetObject("winmgmts:\\" & strTarget & "\root\cimv2")
				' Now we check if VBScript did throw an error, if the last statement was successful, then the
				' Number property of the Err object will be 0, othterwise it's a numerical reference to an error

				If Err.number <> 0 Then
					' return a descriptive Error, along with the error number, to be reported
					' In this case, the PING was successful, but we couldn't connect to it
					IsAlive = "WMI Failed to connect, error " & Err.Number
					WScript.Echo IsAlive
					' Tidy up by destroying the objects created
					Set objWMIService = Nothing
					Set objLocalWMI = Nothing
					Exit Function
				Else
					' If we make it then the Ping was Successful, and WMI connect was successful, so return OK
					IsAlive = "OK" 
					WScript.Echo IsAlive
				' End If Err.number <> 0
				End If
				' This statement turns the Error Trapping off, so VBScript will stop if it encounters an error again
				On Error Goto 0
			Else
				' We Pinged OK and PING_ONLY was set TRUE, so we return OK here
				IsAlive = "OK"
				WScript.Echo IsAlive				
			' End If NOT PING_ONLY
			End If
		Else
			' The Ping Check failed, and we didn't bother doing the WMI check, so we just return a status of Could not be pinged
			IsAlive = "Could not be pinged"
			WScript.Echo IsAlive
		' End If objPingStatus.StatusCode = 0
		End If

	' Loop back to the next object in the colPingStatus colletion (even though there shouldn't be any other objects.)
	Next
	' Tidy up by destroying the objects
	Set objWMIService = Nothing
	Set objLocalWMI = Nothing
	Set colPingStatus = Nothing
End Function
