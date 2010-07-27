Option Explicit
WScript.Echo "Machine Type : " & getComputerType(".")
WScript.Echo "Computer Name : " & getComputerInfo("computer")
WScript.Echo "Logged on Uesr : " & getComputerInfo("user")
WScript.Echo "User Domain : " & getComputerInfo("domain")
WScript.Echo "Computer Account in AD: " & isComputerAccountExists(getComputerInfo("computer"))

Function getComputerType(host)
	Dim wmi, network, system, item, temp
	Set wmi = GetObject("winmgmts:{impersonationlevel=impersonate}!\\" & host & "\root\cimv2")
	Set system = wmi.ExecQuery("SELECT * FROM Win32_ComputerSystem")
	For Each item In system
		temp = item.SystemType
	Next
	getComputerType = temp
End Function

Function getComputerInfo(info)
	Dim network
	Set network = CreateObject("WScript.Network")
	Select Case LCase(info)
	  Case "computer"
	    getComputerInfo = network.ComputerName
          Case "user"
            getComputerInfo = network.UserName
          Case "domain"
            getComputerInfo = network.UserDomain
        End Select
End Function

Function isComputerAccountExists(host)
	Dim conn, cmd , rs
	Set conn = CreateObject("ADODB.Connection")
	Set cmd = CreateObject("ADODB.Command")
	conn.provider = "adsdsoobject"
	conn.open "active directory provider"
	cmd.activeconnection = conn
	cmd.commandtext = "<LDAP://" & GetObject("LDAP://rootdse").Get("defaultnamingcontext") & ">;(&(objectcategory=computer)(objectclass=computer)(cn=" & host & "));cn;subtree"
	Set rs = cmd.Execute
	If rs.recordcount = 0 Then
	isComputerAccountExists = False
	Else
		isComputerAccountExists = True
	End If
End Function
