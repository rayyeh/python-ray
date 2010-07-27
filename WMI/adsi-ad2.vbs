'' 列出本機的LDAP  資訊

On Error Resume Next

Set objSysInfo = CreateObject("ADSystemInfo")
Set objNetwork = CreateObject("Wscript.Network")

strUserPath = "LDAP://" & objSysInfo.UserName
Set objUser = GetObject(strUserPath)

For Each strGroup in objUser.MemberOf
    strGroupPath = "LDAP://" & strGroup
    Wscript.Echo "strGroupPath :" &strGroupPath
    Set objGroup = GetObject(strGroupPath)
    Wscript.Echo "CN Name:" &objGroup.CN
Next
