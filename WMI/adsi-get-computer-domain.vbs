On Error Resume Next

Const ADS_SCOPE_SUBTREE = 2

Set objConnection = CreateObject("ADODB.Connection")
Set objCommand =   CreateObject("ADODB.Command")
objConnection.Provider = "ADsDSOObject"
objConnection.Open "Active Directory Provider"
Set objCommand.ActiveConnection = objConnection

objCommand.Properties("Page Size") = 1000
objCommand.Properties("Searchscope") = ADS_SCOPE_SUBTREE 

objCommand.CommandText = _
    "SELECT CN FROM 'LDAP://dc=UITC,dc=com' WHERE objectCategory='computer'"  
Set objRecordSet = objCommand.Execute

objRecordSet.MoveFirst

Do Until objRecordSet.EOF
    strComputer = objRecordSet.Fields("Name").Value

    ' =====================================================================
    ' Insert your code here
    ' =====================================================================

    Set objComputer = GetObject("WinNT://" & strComputer & "")
    objComputer.Filter = Array("User")
    For Each objUser in objComputer
        Wscript.Echo objUser.Name
    Next

    ' =====================================================================
    ' End
    ' =====================================================================

    objRecordSet.MoveNext
Loop
